import os
import math
import cv2
import numpy as np
import shutil
from PIL import Image, ImageDraw, ImageFont

SRC_DIR = r"C:\Projects\_creative\kadence_ukulele_workshop"
OUT_FILE = os.path.join(SRC_DIR, "kadence_ukulele_brand_cinematic_reel.mp4")
BRAIN_COPY = r"C:\Users\gahan\.gemini\antigravity-ide\brain\8a12cb96-3ed8-467e-a40a-e34fd33cc79a\kadence_ukulele_brand_cinematic_reel.mp4"
LOGO_PATH = os.path.join(SRC_DIR, "kadence_logo.png")

WIDTH = 1080
HEIGHT = 1920
FPS = 30

FONT_PATH_BOLD = r"C:\Windows\Fonts\segoeuib.ttf"
FONT_PATH_MAIN = r"C:\Windows\Fonts\arialbd.ttf"
FONT_PATH_TAG = r"C:\Windows\Fonts\trebucbd.ttf"

def create_vignette(w, h, strength=0.36):
    x = np.linspace(-1, 1, w, dtype=np.float32)
    y = np.linspace(-1, 1, h, dtype=np.float32)
    xx, yy = np.meshgrid(x, y)
    radius = np.sqrt(xx**2 + yy**2)
    vignette = np.clip(1.0 - (radius * strength), 0.0, 1.0)
    return np.dstack([vignette, vignette, vignette])

VIGNETTE_MASK = create_vignette(WIDTH, HEIGHT, 0.36)

def apply_cinematic_grade(frame):
    """Rich Kodak 250D warm amber & teal color grading."""
    img_f = frame.astype(np.float32) / 255.0
    img_f = 0.5 * (1 + np.sin(np.pi * (img_f - 0.5)))
    b, g, r = cv2.split(img_f)
    r = np.clip(r * 1.07, 0.0, 1.0)
    b = np.clip(b * 0.93 + 0.02 * (1.0 - r), 0.0, 1.0)
    g = np.clip(g * 1.01, 0.0, 1.0)
    graded = cv2.merge([b, g, r]) * VIGNETTE_MASK
    return np.clip(graded * 255.0, 0, 255).astype(np.uint8)

def apply_light_leak(frame, intensity=0.5, pos_x=0.2, pos_y=0.1, color=(40, 140, 255)):
    if intensity <= 0.01:
        return frame
    h, w = frame.shape[:2]
    leak = np.zeros((h, w, 3), dtype=np.float32)
    cx, cy = int(w * pos_x), int(h * pos_y)
    axis_x = int(w * 0.7 * intensity)
    axis_y = int(h * 0.4 * intensity)
    cv2.ellipse(leak, (cx, cy), (axis_x, axis_y), 35, 0, 360, (color[0]/255.0, color[1]/255.0, color[2]/255.0), -1)
    leak = cv2.GaussianBlur(leak, (101, 101), 0)
    frame_f = frame.astype(np.float32) / 255.0
    screen = 1.0 - (1.0 - frame_f) * (1.0 - leak * intensity)
    return np.clip(screen * 255.0, 0, 255).astype(np.uint8)

def apply_whip_blur(frame, progress=0.5):
    blur_amount = int(abs(math.sin(progress * math.pi)) * 42)
    if blur_amount < 3:
        return frame
    if blur_amount % 2 == 0:
        blur_amount += 1
    kernel = np.zeros((blur_amount, blur_amount))
    kernel[int((blur_amount - 1)/2), :] = np.ones(blur_amount)
    kernel /= blur_amount
    return cv2.filter2D(frame, -1, kernel)

def apply_flash_transition(frame, progress):
    flash_val = math.sin(progress * math.pi) * 140
    if flash_val <= 2:
        return frame
    return np.clip(frame.astype(np.float32) + flash_val, 0, 255).astype(np.uint8)

def crop_and_fit(img, target_w=WIDTH, target_h=HEIGHT, zoom=1.0, pan_x=0.0, pan_y=0.0):
    ih, iw = img.shape[:2]
    target_aspect = target_w / target_h
    img_aspect = iw / ih

    if img_aspect > target_aspect:
        crop_h = ih
        crop_w = int(ih * target_aspect)
    else:
        crop_w = iw
        crop_h = int(iw / target_aspect)

    crop_w = max(10, int(crop_w / zoom))
    crop_h = max(10, int(crop_h / zoom))

    center_x = int(iw / 2 + (iw - crop_w) * 0.5 * pan_x)
    center_y = int(ih / 2 + (ih - crop_h) * 0.5 * pan_y)

    x1 = max(0, min(iw - crop_w, center_x - crop_w // 2))
    y1 = max(0, min(ih - crop_h, center_y - crop_h // 2))
    x2 = min(iw, x1 + crop_w)
    y2 = min(ih, y1 + crop_h)

    cropped = img[y1:y2, x1:x2]
    return cv2.resize(cropped, (target_w, target_h), interpolation=cv2.INTER_LINEAR)

def render_dynamic_caption(frame, tag="KADENCE UKULELE", title="FEEL THE STRUM", anim_progress=1.0, accent_color=(255, 195, 40)):
    """
    Renders high-contrast, large, kinetic animated captions:
    - Smooth slide-up + pop-in spring transition
    - Vibrant pill badge with neon glow accent
    - Bold, ultra-readable typography with soft drop shadows
    """
    # Convert OpenCV BGR frame to PIL RGB
    img_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil, "RGBA")
    
    # Kinetic animation curve (ease-out bounce)
    ease = 1.0 - math.pow(1.0 - min(1.0, max(0.0, anim_progress)), 3)
    
    # Dimensions & Positioning
    card_w = 940
    card_h = 175
    card_x = (WIDTH - card_w) // 2
    
    # Animate slide up from bottom
    target_y = HEIGHT - 330
    start_y = HEIGHT - 220
    card_y = int(start_y + (target_y - start_y) * ease)
    alpha = int(245 * ease)
    
    # Semi-transparent dark frosted backdrop
    draw.rounded_rectangle(
        [card_x, card_y, card_x + card_w, card_y + card_h],
        radius=24,
        fill=(12, 14, 18, alpha),
        outline=(255, 255, 255, int(45 * ease)),
        width=2
    )
    
    # Left accent vertical glow bar
    draw.rounded_rectangle(
        [card_x + 12, card_y + 16, card_x + 22, card_y + card_h - 16],
        radius=4,
        fill=(accent_color[0], accent_color[1], accent_color[2], int(255 * ease))
    )
    
    # Category Tag Pill
    tag_font = ImageFont.truetype(FONT_PATH_TAG, 30)
    tag_w = int(draw.textlength(tag, font=tag_font)) + 32
    tag_h = 42
    tag_x = card_x + 40
    tag_y = card_y + 24
    
    draw.rounded_rectangle(
        [tag_x, tag_y, tag_x + tag_w, tag_y + tag_h],
        radius=12,
        fill=(accent_color[0], accent_color[1], accent_color[2], int(240 * ease))
    )
    draw.text((tag_x + 16, tag_y + 4), tag, font=tag_font, fill=(10, 10, 15, int(255 * ease)))
    
    # Main Headline (Large, Bold, Clean)
    title_font = ImageFont.truetype(FONT_PATH_BOLD, 48)
    title_x = card_x + 40
    title_y = card_y + 80
    
    # Text drop shadow + sharp white main
    draw.text((title_x + 2, title_y + 2), title, font=title_font, fill=(0, 0, 0, int(190 * ease)))
    draw.text((title_x, title_y), title, font=title_font, fill=(255, 255, 255, int(255 * ease)))
    
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

def read_sequential_frames(video_path, count, step=1):
    cap = cv2.VideoCapture(video_path)
    frames = []
    i = 0
    while len(frames) < count:
        ret, f = cap.read()
        if not ret:
            break
        if i % step == 0:
            if f.shape[0] > 1920:
                scale = 1920 / f.shape[0]
                f = cv2.resize(f, (int(f.shape[1] * scale), 1920), interpolation=cv2.INTER_LINEAR)
            frames.append(f)
        i += 1
    cap.release()
    return frames

def render_brand_end_slide(frame_bg, anim_progress=1.0):
    """
    Renders dedicated Brand Promotion End Slide with the official Kadence Logo:
    - Official Logo centered with smooth scale & ambient pulse
    - Main Tagline: "Kadence — Let's music"
    - Subtitle: "Ukuleles • Guitars • Community • kadence.in"
    """
    ease = 1.0 - math.pow(1.0 - min(1.0, max(0.0, anim_progress)), 3)
    
    # Darken background with deep moody stage atmosphere
    bg = cv2.addWeighted(frame_bg, 0.18, np.zeros_like(frame_bg), 0.82, 0)
    
    # Warm golden/cyan ambient halo behind logo
    h, w = bg.shape[:2]
    cx, cy = w // 2, int(h * 0.40)
    leak = np.zeros((h, w, 3), dtype=np.float32)
    cv2.ellipse(leak, (cx, cy), (int(w * 0.45 * ease), int(h * 0.16 * ease)), 0, 0, 360, (0.15, 0.55, 0.95), -1)
    leak = cv2.GaussianBlur(leak, (101, 101), 0)
    bg_f = bg.astype(np.float32) / 255.0
    screen = 1.0 - (1.0 - bg_f) * (1.0 - leak * 0.75)
    bg = np.clip(screen * 255.0, 0, 255).astype(np.uint8)
    
    # PIL Drawing
    img_pil = Image.fromarray(cv2.cvtColor(bg, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil, "RGBA")
    
    # Load and scale Logo
    if os.path.exists(LOGO_PATH):
        logo_img = Image.open(LOGO_PATH).convert("RGBA")
        logo_scale = 1.30 * (0.88 + 0.12 * ease)
        target_logo_w = int(logo_img.width * logo_scale)
        target_logo_h = int(logo_img.height * logo_scale)
        logo_resized = logo_img.resize((target_logo_w, target_logo_h), Image.LANCZOS)
        
        alpha_factor = ease
        r, g, b, a = logo_resized.split()
        a = a.point(lambda p: int(p * alpha_factor))
        logo_faded = Image.merge("RGBA", (r, g, b, a))
        
        logo_x = (WIDTH - target_logo_w) // 2
        logo_y = int(HEIGHT * 0.38 - target_logo_h // 2)
        img_pil.paste(logo_faded, (logo_x, logo_y), logo_faded)
    
    # Tagline: "Kadence — Let's music"
    tagline_font = ImageFont.truetype(FONT_PATH_BOLD, 54)
    tagline_text = "Kadence - Let's music"
    tagline_w = draw.textlength(tagline_text, font=tagline_font)
    tagline_x = (WIDTH - tagline_w) // 2
    tagline_y = int(HEIGHT * 0.50 + (1.0 - ease) * 35)
    
    draw.text((tagline_x + 2, tagline_y + 2), tagline_text, font=tagline_font, fill=(0, 0, 0, int(220 * ease)))
    draw.text((tagline_x, tagline_y), tagline_text, font=tagline_font, fill=(255, 210, 55, int(255 * ease)))
    
    # Secondary Line: "Premium Ukuleles • Guitars • Experience"
    sub_font = ImageFont.truetype(FONT_PATH_TAG, 34)
    sub_text = "Premium Ukuleles  *  Guitars  *  Workshops"
    sub_w = draw.textlength(sub_text, font=sub_font)
    sub_x = (WIDTH - sub_w) // 2
    sub_y = tagline_y + 80
    draw.text((sub_x, sub_y), sub_text, font=sub_font, fill=(225, 235, 245, int(235 * ease)))
    
    # Call to action badge
    cta_font = ImageFont.truetype(FONT_PATH_BOLD, 32)
    cta_text = "EXPLORE AT KADENCE.IN"
    cta_w = draw.textlength(cta_text, font=cta_font) + 48
    cta_h = 58
    cta_x = (WIDTH - cta_w) // 2
    cta_y = sub_y + 80
    
    draw.rounded_rectangle(
        [cta_x, cta_y, cta_x + cta_w, cta_y + cta_h],
        radius=20,
        fill=(255, 255, 255, int(240 * ease))
    )
    draw.text((cta_x + 24, cta_y + 10), cta_text, font=cta_font, fill=(15, 18, 24, int(255 * ease)))
    
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

def render_reel():
    print("Starting Brand Promotion Reel Assembly (Polished V2)...")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(OUT_FILE, fourcc, float(FPS), (WIDTH, HEIGHT))
    
    # 1. SCENE 1: CINEMATIC STAGE DIVE (65 frames)
    print("1/7: Stage Ignition & Dive...")
    img_stage = cv2.imread(os.path.join(SRC_DIR, "IMG_20260830_185046.jpg"))
    for i in range(65):
        t = i / 65.0
        zoom = 1.0 + 0.42 * (t ** 1.8)
        pan_y = -0.15 * (t ** 1.5)
        frame = crop_and_fit(img_stage, zoom=zoom, pan_y=pan_y)
        frame = apply_cinematic_grade(frame)
        leak = math.exp(-((t - 0.25) ** 2) / 0.04) * 0.75
        frame = apply_light_leak(frame, intensity=leak, pos_x=0.15 + 0.3*t, pos_y=0.1)
        
        cap_progress = min(1.0, max(0.0, (i - 5) / 18.0))
        frame = render_dynamic_caption(frame, tag="KADENCE MUSIC", title="UNLEASH YOUR SOUND", anim_progress=cap_progress, accent_color=(255, 195, 40))
        
        if i >= 55:
            trans_t = (i - 55) / 10.0
            frame = apply_whip_blur(frame, progress=trans_t)
            frame = apply_flash_transition(frame, progress=trans_t * 0.5)
        out.write(frame)

    # 2. SCENE 2: AISLE GLIDE SLOW-MO (85 frames)
    print("2/7: Aisle Glide Slow-Mo...")
    f_aisle = read_sequential_frames(os.path.join(SRC_DIR, "VID_20260830_184806_HSR_120.mp4"), 120, step=2)
    for i in range(85):
        t = i / 85.0
        raw_f = f_aisle[min(len(f_aisle)-1, i)]
        frame = crop_and_fit(raw_f, zoom=1.05 + 0.06 * math.sin(t * math.pi))
        frame = apply_cinematic_grade(frame)
        
        cap_progress = min(1.0, max(0.0, (i - 6) / 16.0))
        frame = render_dynamic_caption(frame, tag="FEEL THE STRUM", title="PURE ACOUSTIC VIBES", anim_progress=cap_progress, accent_color=(70, 215, 255))
        
        if i >= 75:
            frame = apply_whip_blur(frame, progress=(i - 75) / 10.0)
        out.write(frame)

    # 3. SCENE 3: TRIPLE COLOR MATCH-CUT (90 frames)
    print("3/7: Triple Color Match-Cut...")
    img_yellow_front = cv2.imread(os.path.join(SRC_DIR, "IMG_20260830_185056_1.jpg"))
    f_blue = read_sequential_frames(os.path.join(SRC_DIR, "VID_20260830_185704.mp4"), 35, step=1)
    f_pink = read_sequential_frames(os.path.join(SRC_DIR, "VID_20260830_185725.mp4"), 35, step=1)

    # Sunshine Yellow (frames 0-30) - Front smiling pose
    for i in range(30):
        t_y = i / 30.0
        frame = crop_and_fit(img_yellow_front, zoom=1.10 + 0.05 * t_y, pan_y=-0.05)
        frame = apply_cinematic_grade(frame)
        cap_progress = min(1.0, max(0.0, i / 10.0))
        frame = render_dynamic_caption(frame, tag="FIND YOUR COLOR", title="SUNSHINE YELLOW", anim_progress=cap_progress, accent_color=(255, 210, 30))
        if i >= 24:
            frame = apply_flash_transition(frame, progress=(i - 24) / 6.0)
        out.write(frame)

    # Sky Blue (frames 0-30)
    for i in range(30):
        frame = crop_and_fit(f_blue[min(len(f_blue)-1, i)], zoom=1.08, pan_y=-0.05)
        frame = apply_cinematic_grade(frame)
        if i < 5:
            frame = apply_flash_transition(frame, progress=1.0 - (i / 5.0))
        cap_progress = min(1.0, max(0.0, i / 10.0))
        frame = render_dynamic_caption(frame, tag="FIND YOUR COLOR", title="ELECTRIC CYAN BLUE", anim_progress=cap_progress, accent_color=(50, 210, 255))
        if i >= 24:
            frame = apply_flash_transition(frame, progress=(i - 24) / 6.0)
        out.write(frame)

    # Coral Pink Pineapple (frames 0-30)
    for i in range(30):
        frame = crop_and_fit(f_pink[min(len(f_pink)-1, i)], zoom=1.08, pan_y=-0.05)
        frame = apply_cinematic_grade(frame)
        if i < 5:
            frame = apply_flash_transition(frame, progress=1.0 - (i / 5.0))
        cap_progress = min(1.0, max(0.0, i / 10.0))
        frame = render_dynamic_caption(frame, tag="FIND YOUR COLOR", title="CORAL PINK PINEAPPLE", anim_progress=cap_progress, accent_color=(255, 95, 130))
        if i >= 24:
            frame = apply_whip_blur(frame, progress=(i - 24) / 6.0)
        out.write(frame)

    # 4. SCENE 4: HERO STAGE PERFORMANCE (75 frames)
    print("4/7: Stage Performance...")
    f_hero = read_sequential_frames(os.path.join(SRC_DIR, "VID_20260830_185757.mp4"), 80, step=1)
    for i in range(75):
        t = i / 75.0
        frame = crop_and_fit(f_hero[min(len(f_hero)-1, i)], zoom=1.02 + 0.05 * t)
        frame = apply_cinematic_grade(frame)
        flare = 0.35 + 0.25 * math.sin(t * 8.0)
        frame = apply_light_leak(frame, intensity=flare, pos_x=0.5, pos_y=0.05, color=(100, 200, 255))
        
        cap_progress = min(1.0, max(0.0, (i - 5) / 15.0))
        frame = render_dynamic_caption(frame, tag="STAGE READY", title="EVERY CHORD HITS", anim_progress=cap_progress, accent_color=(255, 180, 50))
        
        if i >= 65:
            frame = apply_whip_blur(frame, progress=(i - 65) / 10.0)
        out.write(frame)

    # 5. SCENE 5: WELL PLAYED BADGE MICRO-MOMENT (65 frames)
    print("5/7: Badge Micro-Moment...")
    img_badge = cv2.imread(os.path.join(SRC_DIR, "IMG_20260830_185049.jpg"))
    for i in range(65):
        t = i / 65.0
        zoom = 1.35 - 0.25 * (t ** 0.8)
        pan_y = 0.15 - 0.22 * (t ** 1.2)
        frame = crop_and_fit(img_badge, zoom=zoom, pan_y=pan_y)
        frame = apply_cinematic_grade(frame)
        frame = apply_light_leak(frame, intensity=0.35 * math.sin(t * math.pi), pos_x=0.8, pos_y=0.2)
        
        cap_progress = min(1.0, max(0.0, (i - 5) / 15.0))
        frame = render_dynamic_caption(frame, tag="KADENCE VIBES", title="WELL PLAYED!", anim_progress=cap_progress, accent_color=(255, 215, 60))
        
        if i >= 55:
            frame = apply_flash_transition(frame, progress=(i - 55) / 10.0)
        out.write(frame)

    # 6. SCENE 6: GROUP VICTORY CELEBRATION (65 frames)
    print("6/7: Group Celebration...")
    img_group = cv2.imread(os.path.join(SRC_DIR, "IMG_20260830_184848.jpg"))
    for i in range(65):
        t = i / 65.0
        zoom = 1.15 - 0.12 * t
        frame = crop_and_fit(img_group, zoom=zoom, pan_y=-0.05)
        frame = apply_cinematic_grade(frame)
        
        cap_progress = min(1.0, max(0.0, (i - 5) / 15.0))
        frame = render_dynamic_caption(frame, tag="JOIN THE TRIBE", title="PLAY. CONNECT. INSPIRE.", anim_progress=cap_progress, accent_color=(70, 220, 255))
        
        if i >= 52:
            trans_t = (i - 52) / 13.0
            frame = apply_whip_blur(frame, progress=trans_t)
            frame = apply_light_leak(frame, intensity=trans_t * 0.9, pos_x=0.5, pos_y=0.4, color=(100, 200, 255))
        out.write(frame)

    # 7. SCENE 7: DEDICATED BRAND PROMOTION & LOGO SLIDE (80 frames)
    print("7/7: Dedicated Brand Logo & Tagline Outro Slide...")
    for i in range(80):
        t = i / 80.0
        anim_prog = min(1.0, (i + 4) / 22.0)
        
        frame = crop_and_fit(img_stage, zoom=1.12 + 0.04 * t, pan_y=-0.1)
        frame = render_brand_end_slide(frame, anim_progress=anim_prog)
        
        leak_pulse = 0.35 + 0.2 * math.sin(t * math.pi)
        frame = apply_light_leak(frame, intensity=leak_pulse, pos_x=0.5, pos_y=0.35, color=(70, 180, 255))
        
        if i >= 68:
            loop_t = (i - 68) / 12.0
            frame = apply_whip_blur(frame, progress=loop_t)
            frame = apply_light_leak(frame, intensity=loop_t * 0.9, pos_x=0.15, pos_y=0.1)
        out.write(frame)

    out.release()
    print(f"Brand Promotion Reel successfully rendered: {OUT_FILE}")
    try:
        shutil.copyfile(OUT_FILE, BRAIN_COPY)
        print(f"Copied to brain artifacts: {BRAIN_COPY}")
    except Exception as e:
        print(f"Brain copy note: {e}")

if __name__ == "__main__":
    render_reel()

