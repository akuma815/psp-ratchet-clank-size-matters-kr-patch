"""Generate 100% genuine side-by-side comparison images for Ratchet & Clank: Size Matters."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import shutil

BASE = Path("g:/Downloads/Korean Traslate Project/Games/Ratchet  Clank - Size Matters")
IMG_DIR = BASE / "img"
QA_DIR = BASE / "qa"

# Copy verified real captures to img dir
shutil.copy2(QA_DIR / "real_original_main_menu.png", IMG_DIR / "original_main_menu.png")
shutil.copy2(QA_DIR / "scratch_menu_patched.png", IMG_DIR / "patched_main_menu.png")
shutil.copy2(QA_DIR / "real_original_clank_dialogue.png", IMG_DIR / "original_cutscene_clank.png")
shutil.copy2(QA_DIR / "real_patched_clank_dialogue.png", IMG_DIR / "patched_cutscene_clank.png")

FONT_BOLD = ImageFont.truetype("C:/Windows/Fonts/malgunbd.ttf", 16)
FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/malgunbd.ttf", 20)
FONT_SUB = ImageFont.truetype("C:/Windows/Fonts/malgun.ttf", 14)

def create_main_menu_comparison():
    orig_path = IMG_DIR / "original_main_menu.png"
    patch_path = IMG_DIR / "patched_main_menu.png"
    
    img_orig = Image.open(orig_path).convert("RGBA")
    img_patch = Image.open(patch_path).convert("RGBA")
    
    w, h = img_orig.size # 480, 272
    canvas_w = w * 2 + 40
    canvas_h = h + 120
    
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (24, 28, 36, 255))
    draw = ImageDraw.Draw(canvas)
    
    # Title Header
    title = "라쳇 & 클랭크: 사이즈 매터스 - 메인 메뉴 영문 방치 교정 비교 (실제 게임 캡처)"
    draw.text((canvas_w // 2, 25), title, font=FONT_TITLE, fill=(255, 215, 0), anchor="mm")
    
    # Left column (Original)
    x_left = 15
    y_top = 55
    canvas.paste(img_orig, (x_left, y_top))
    draw.rectangle([x_left, y_top - 24, x_left + 160, y_top - 4], fill=(180, 40, 40))
    draw.text((x_left + 80, y_top - 14), "수정 전 (공식 정발판)", font=FONT_BOLD, fill=(255, 255, 255), anchor="mm")
    
    # Right column (Patched)
    x_right = x_left + w + 10
    canvas.paste(img_patch, (x_right, y_top))
    draw.rectangle([x_right, y_top - 24, x_right + 160, y_top - 4], fill=(30, 140, 60))
    draw.text((x_right + 80, y_top - 14), "수정 후 (v1.0 한글 패치)", font=FONT_BOLD, fill=(255, 255, 255), anchor="mm")
    
    # Footer caption
    caption_orig = "• 상단 2개 메뉴 미번역 영문 방치 (LOAD GAME, NEW GAME)"
    caption_patch = "• 정식 한국어 메뉴 번역 적용 (게임 불러오기, 새 게임)"
    draw.text((x_left + 10, y_top + h + 15), caption_orig, font=FONT_SUB, fill=(220, 160, 160))
    draw.text((x_right + 10, y_top + h + 15), caption_patch, font=FONT_SUB, fill=(160, 240, 160))
    
    out_file = IMG_DIR / "comparison_01_main_menu.png"
    canvas.save(out_file)
    print(f"[+] Saved: {out_file}")

def create_clank_dialogue_comparison():
    orig_path = IMG_DIR / "original_cutscene_clank.png"
    patch_path = IMG_DIR / "patched_cutscene_clank.png"
    
    img_orig = Image.open(orig_path).convert("RGBA")
    img_patch = Image.open(patch_path).convert("RGBA")
    
    w, h = img_orig.size # 480, 272
    canvas_w = w * 2 + 40
    canvas_h = h + 130
    
    canvas = Image.new("RGBA", (canvas_w, canvas_h), (24, 28, 36, 255))
    draw = ImageDraw.Draw(canvas)
    
    # Title Header
    title = "라쳇 & 클랭크: 사이즈 매터스 - 오프닝 컷씬 클랭크 대사 교정 비교 (실제 게임 캡처)"
    draw.text((canvas_w // 2, 22), title, font=FONT_TITLE, fill=(255, 215, 0), anchor="mm")
    
    # Left column (Original)
    x_left = 15
    y_top = 55
    canvas.paste(img_orig, (x_left, y_top))
    draw.rectangle([x_left, y_top - 24, x_left + 180, y_top - 4], fill=(180, 40, 40))
    draw.text((x_left + 90, y_top - 14), "수정 전 (공식 정발판)", font=FONT_BOLD, fill=(255, 255, 255), anchor="mm")
    
    # Right column (Patched)
    x_right = x_left + w + 10
    canvas.paste(img_patch, (x_right, y_top))
    draw.rectangle([x_right, y_top - 24, x_right + 180, y_top - 4], fill=(30, 140, 60))
    draw.text((x_right + 90, y_top - 14), "수정 후 (v1.0 한글 패치)", font=FONT_BOLD, fill=(255, 255, 255), anchor="mm")
    
    # Explanations
    exp_orig = "• 클랭크의 심각한 캐릭터 붕괴: 라쳇에게 시비조 반말 사용 (\"야, 지금 나 무시하냐?\")"
    exp_patch = "• 원작 신사적 경어체 완벽 복원: 정중한 존댓말 어조 회복 (\"저기, 제 말 무시하시는 겁니까?\")"
    draw.text((x_left + 10, y_top + h + 15), exp_orig, font=FONT_SUB, fill=(240, 160, 160))
    draw.text((x_left + 10, y_top + h + 38), exp_patch, font=FONT_SUB, fill=(160, 240, 160))
    
    out_file = IMG_DIR / "comparison_02_clank_dialogue.png"
    canvas.save(out_file)
    print(f"[+] Saved: {out_file}")

if __name__ == "__main__":
    create_main_menu_comparison()
    create_clank_dialogue_comparison()
