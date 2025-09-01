import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.image import Image
from font_merger import run_merge

class FontMergerApp(App):
    def build(self):
        self.arabic_font = ""
        self.english_font = ""
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text="اختر الخط العربي:"))
        self.arabic_chooser = FileChooserIconView()
        self.arabic_chooser.bind(selection=self.select_arabic)
        layout.add_widget(self.arabic_chooser)
        layout.add_widget(Label(text="اختر الخط الإنجليزي:"))
        self.english_chooser = FileChooserIconView()
        self.english_chooser.bind(selection=self.select_english)
        layout.add_widget(self.english_chooser)
        self.run_btn = Button(text="دمج الخطوط ومعاينة")
        self.run_btn.bind(on_press=self.merge_fonts)
        layout.add_widget(self.run_btn)
        self.img = Image()
        layout.add_widget(self.img)
        return layout

    def select_arabic(self, chooser, selection):
        if selection:
            self.arabic_font = selection[0]

    def select_english(self, chooser, selection):
        if selection:
            self.english_font = selection[0]

    def merge_fonts(self, instance):
        if self.arabic_font and self.english_font:
            merged_font, preview_img = run_merge(self.arabic_font, self.english_font, "output")
            if preview_img:
                self.img.source = preview_img
                self.img.reload()

if __name__ == '__main__':
    FontMergerApp().run()