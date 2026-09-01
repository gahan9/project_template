import os
import math
import cv2
import numpy as np
import shutil

SRC_DIR = r"C:\Projects\_creative\kadence_ukulele_workshop"
OUT_FILE = os.path.join(SRC_DIR, "kadence_ukulele_workshop_cinematic_reel.mp4")
BRAIN_COPY = r"C:\Users\gahan\.gemini\antigravity-ide\brain\8a12cb96-3ed8-467e-a40a-e34fd33cc79a\kadence_ukulele_workshop_cinematic_reel.mp4"

WIDTH = 1080
HEIGHT = 1920
FPS = 30

def create_vignette(w, h, strength=0.35):
    x = np.linspace(-1, 1, w, dtype=np.float32)
    y = np.linspace(-1, 1, h, dtype=np.float32)
    xx, yy = np.meshgrid(x, y)
    radius = np.sqrt(xx**2 + yy**2)
    vignette = np.clip(1.0 - (radius * strength), 0.0, 1.0)
    return np.dstack([vignette, vignette, vignette])

VIGNETTE_MASK = create_vignette(WIDTH, HEIGHT, 0.38)

def apply_cinematic_grade(frame):
    img_f = frame.astype(np.float32) / 255.0
    img_f = 0.5 * (1 + np.sin(np.pi * (img_f - 0.5)))
    b, g, r = cv2.split(img_f)
    r = np.clip(r * 1.06, 0.0, 1.0)
    b = np.clip(b * 0.94 + 0.02 * (1.0 - r), 0.0, 1.0)
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
    blur_amount = int(abs(math.sin(progress * math.pi)) * 40)
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

def overlay_modern_badge(frame, line1="KADENCE UKULELE WORKSHOP", line2="FROM ZERO TO STAGE IN 60 MINS", alpha=0.90):
    h, w = frame.shape[:2]
    overlay = frame.copy()
    box_w = int(w * 0.88)
    box_h = 120
    box_x = (w - box_w) // 2
    box_y = h - 240
    
    cv2.rectangle(overlay, (box_x, box_y), (box_x + box_w, box_y + box_h), (12, 12, 16), -1)
    cv2.rectangle(overlay, (box_x, box_y), (box_x + 8, box_y + box_h), (50, 195, 255), -1)
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
    
    cv2.putText(frame, line1, (box_x + 28, box_y + 44), cv2.FONT_HERSHEY_DUPLEX, 0.68, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, line2, (box_x + 28, box_y + 86), cv2.FONT_HERSHEY_SIMPLEX, 0.62, (70, 205, 255), 2, cv2.LINE_AA)
    return frame

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

def render_reel():
    print("Blazing fast sequential reel assembly...")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(OUT_FILE, fourcc, float(FPS), (WIDTH, HEIGHT))
    
    # 1. SCENE 1: OPENING DIVE (65 frames)
    print("1/6: Stage Dive...")
    img_stage = cv2.imread(os.path.join(SRC_DIR, "IMG_20260830_185046.jpg"))
    for i in range(65):
        t = i / 65.0
        zoom = 1.0 + 0.42 * (t ** 1.8)
        pan_y = -0.15 * (t ** 1.5)
        frame = crop_and_fit(img_stage, zoom=zoom, pan_y=pan_y)
        frame = apply_cinematic_grade(frame)
        leak = math.exp(-((t - 0.25) ** 2) / 0.04) * 0.75
        frame = apply_light_leak(frame, intensity=leak, pos_x=0.15 + 0.3*t, pos_y=0.1)
        if i >= 55:
            trans_t = (i - 55) / 10.0
            frame = apply_whip_blur(frame, progress=trans_t)
            frame = apply_flash_transition(frame, progress=trans_t * 0.5)
        frame = overlay_modern_badge(frame, "KADENCE EXPERIENCE", "POV: YOUR FIRST UKULELE WORKSHOP")
        out.write(frame)

    # 2. SCENE 2: AISLE GLIDE SLOW-MO (85 frames)
    print("2/6: Aisle Glide...")
    f_aisle = read_sequential_frames(os.path.join(SRC_DIR, "VID_20260830_184806_HSR_120.mp4"), 120, step=2)
    for i in range(85):
        t = i / 85.0
        raw_f = f_aisle[min(len(f_aisle)-1, i)]
        frame = crop_and_fit(raw_f, zoom=1.05 + 0.06 * math.sin(t * math.pi))
        frame = apply_cinematic_grade(frame)
        if i >= 75:
            frame = apply_whip_blur(frame, progress=(i - 75) / 10.0)
        frame = overlay_modern_badge(frame, "INSTANT VIBES", "LEARN CHORDS IN UNDER 60 MINS")
        out.write(frame)

    # 3. SCENE 3: TRIPLE COLOR MATCH-CUT (90 frames)
    print("3/6: Match-Cut...")
    f_yellow = read_sequential_frames(os.path.join(SRC_DIR, "VID_20260830_185115_HSR_120.mp4"), 35, step=3)
    f_blue = read_sequential_frames(os.path.join(SRC_DIR, "VID_20260830_185704.mp4"), 35, step=1)
    f_pink = read_sequential_frames(os.path.join(SRC_DIR, "VID_20260830_185725.mp4"), 35, step=1)

    # Yellow
    for i in range(30):
        frame = crop_and_fit(f_yellow[min(len(f_yellow)-1, i)], zoom=1.08, pan_y=-0.05)
        frame = apply_cinematic_grade(frame)
        if i >= 24:
            frame = apply_flash_transition(frame, progress=(i - 24) / 6.0)
        frame = overlay_modern_badge(frame, "FIND YOUR COLOR", "SUNSHINE YELLOW UKULELE")
        out.write(frame)

    # Sky Blue
    for i in range(30):
        frame = crop_and_fit(f_blue[min(len(f_blue)-1, i)], zoom=1.08, pan_y=-0.05)
        frame = apply_cinematic_grade(frame)
        if i < 5:
            frame = apply_flash_transition(frame, progress=1.0 - (i / 5.0))
        if i >= 24:
            frame = apply_flash_transition(frame, progress=(i - 24) / 6.0)
        frame = overlay_modern_badge(frame, "FIND YOUR COLOR", "ELECTRIC CYAN BLUE UKULELE")
        out.write(frame)

    # Coral Pink Pineapple
    for i in range(30):
        frame = crop_and_fit(f_pink[min(len(f_pink)-1, i)], zoom=1.08, pan_y=-0.05)
        frame = apply_cinematic_grade(frame)
        if i < 5:
            frame = apply_flash_transition(frame, progress=1.0 - (i / 5.0))
        if i >= 24:
            frame = apply_whip_blur(frame, progress=(i - 24) / 6.0)
        frame = overlay_modern_badge(frame, "FIND YOUR COLOR", "CORAL PINK PINEAPPLE UKE")
        out.write(frame)

    # 4. SCENE 4: HERO STAGE STRUM (80 frames)
    print("4/6: Stage Strum...")
    f_hero = read_sequential_frames(os.path.join(SRC_DIR, "VID_20260830_185757.mp4"), 85, step=1)
    for i in range(80):
        t = i / 80.0
        frame = crop_and_fit(f_hero[min(len(f_hero)-1, i)], zoom=1.02 + 0.05 * t)
        frame = apply_cinematic_grade(frame)
        flare = 0.35 + 0.25 * math.sin(t * 8.0)
        frame = apply_light_leak(frame, intensity=flare, pos_x=0.5, pos_y=0.05, color=(100, 200, 255))
        if i >= 70:
            frame = apply_whip_blur(frame, progress=(i - 70) / 10.0)
        frame = overlay_modern_badge(frame, "STAGE READY", "PERFORMING WITH PURE JOY")
        out.write(frame)

    # 5. SCENE 5: WELL PLAYED BADGE MICRO-MOMENT (70 frames)
    print("5/6: Badge...")
    img_badge = cv2.imread(os.path.join(SRC_DIR, "IMG_20260830_185049.jpg"))
    for i in range(70):
        t = i / 70.0
        zoom = 1.35 - 0.25 * (t ** 0.8)
        pan_y = 0.15 - 0.22 * (t ** 1.2)
        frame = crop_and_fit(img_badge, zoom=zoom, pan_y=pan_y)
        frame = apply_cinematic_grade(frame)
        frame = apply_light_leak(frame, intensity=0.35 * math.sin(t * math.pi), pos_x=0.8, pos_y=0.2)
        if i >= 60:
            frame = apply_flash_transition(frame, progress=(i - 60) / 10.0)
        frame = overlay_modern_badge(frame, "UNLEASH YOUR BUCKET LIST", "WELL PLAYED! 🎶✨")
        out.write(frame)

    # 6. SCENE 6: GROUP VICTORY & INFINITY LOOP (70 frames)
    print("6/6: Victory & Loop...")
    img_group = cv2.imread(os.path.join(SRC_DIR, "IMG_20260830_184848.jpg"))
    for i in range(70):
        t = i / 70.0
        zoom = 1.15 - 0.12 * t
        frame = crop_and_fit(img_group, zoom=zoom, pan_y=-0.05)
        frame = apply_cinematic_grade(frame)
        if i >= 55:
            loop_t = (i - 55) / 15.0
            frame = apply_whip_blur(frame, progress=loop_t)
            frame = apply_light_leak(frame, intensity=loop_t * 0.9, pos_x=0.2, pos_y=0.1)
        frame = overlay_modern_badge(frame, "JOIN THE TRIBE", "BOOK YOUR WEEKEND SEAT 🎸")
        out.write(frame)

    out.release()
    print(f"Reel successfully rendered: {OUT_FILE}")
    try:
        shutil.copyfile(OUT_FILE, BRAIN_COPY)
        print(f"Copied to brain artifacts: {BRAIN_COPY}")
    except Exception as e:
        print(f"Brain copy note: {e}")

if __name__ == "__main__":
    render_reel()
