# Font Merger

هذا المشروع يدمج الخط العربي مع الخط الإنجليزي في ملف واحد ويوفر معاينة عالية الجودة للخط المدمج.  
واجهة التطبيق تعتمد على Kivy ويمكن بناء التطبيق للأندرويد باستخدام Buildozer.

## طريقة الاستخدام
- اختر ملفي الخط العربي والإنجليزي من الواجهة
- اضغط زر "دمج الخطوط ومعاينة"
- سيتم حفظ الخط المدمج وصورة معاينة في مجلد output

## المتطلبات
- Python 3.7+
- Kivy
- fontTools
- Pillow
- arabic_reshaper
- python-bidi
- colorama
- rich
- harfbuzz أو uharfbuzz

## البناء للأندرويد
تأكد من إعداد buildozer ثم نفذ:
```
buildozer -v android debug
```