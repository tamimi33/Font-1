#!/usr/bin/env python3
"""
دمج الخطوط مع معاينة عالية الجودة
Font merger with high-quality preview
"""
import os
import sys
import subprocess
import time
import traceback
import shutil
import tempfile
from fontTools.ttLib import TTFont
try:
    from fontTools.varLib.instancer import instantiateVariableFont
except Exception:
    try:
        from fontTools.varLib.mutator import instantiateVariableFont
    except Exception:
        instantiateVariableFont = None

from fontTools.merge import Merger
from fontTools.subset import main as subset_main
from PIL import Image, ImageDraw, ImageFont, features
import arabic_reshaper
from bidi.algorithm import get_display
from colorama import init as colorama_init, Fore, Style
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn
from rich.console import Console

# محاولة استيراد harfbuzz و uharfbuzz
try:
    import harfbuzz as hb
except ImportError:
    try:
        import uharfbuzz as hb
    except ImportError:
        hb = None

colorama_init(autoreset=True)

FONT_DIR = "/sdcard/fonts"
TEMP_DIR = "/sdcard/fonts/temp_processing"
EN_PREVIEW = "The quick brown fox jumps over the lazy dog. 1234567890"
AR_PREVIEW = "سمَات مجّانِية، إختر منْ بين أكثر من ١٠٠ سمة مجانية او انشئ سماتك الخاصة هُنا في هذا التطبيق النظيف الرائع، وأظهر الابداع.١٢٣٤٥٦٧٨٩٠"

def run_merge(arabic_path, english_path, output_dir):
    """
    دمج خطين عربي وإنجليزي في ملف واحد مع إخراج معاينة PNG.
    :param arabic_path: مسار الخط العربي
    :param english_path: مسار الخط الإنجليزي
    :param output_dir: مجلد الإخراج
    :return: مسار الخط المدمج + مسار صورة المعاينة
    """
    try:
        os.makedirs(output_dir, exist_ok=True)
        # دمج الخطين
        merger = Merger()
        merged = merger.merge([arabic_path, english_path])
        merged_font_path = os.path.join(output_dir, "merged_font.ttf")
        merged.save(merged_font_path)
        # معاينة الخط المدمج
        preview_text = AR_PREVIEW + "\n\n" + EN_PREVIEW
        reshaped_text = arabic_reshaper.reshape(preview_text)
        bidi_text = get_display(reshaped_text)
        img = Image.new("RGB", (1000, 250), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(merged_font_path, 48)
        draw.text((10, 50), bidi_text, font=font, fill=(0, 0, 0))
        preview_image_path = os.path.join(output_dir, "preview.png")
        img.save(preview_image_path)
        return merged_font_path, preview_image_path
    except Exception as e:
        print("خطأ أثناء الدمج أو المعاينة:", e)
        traceback.print_exc()
        return None, None

if __name__ == "__main__":
    # مثال للاستخدام
    arabic_path = "arabic.ttf"
    english_path = "english.ttf"
    output_dir = "output"
    merged_font, preview_img = run_merge(arabic_path, english_path, output_dir)
    print("Merged font saved to:", merged_font)
    print("Preview image saved to:", preview_img)