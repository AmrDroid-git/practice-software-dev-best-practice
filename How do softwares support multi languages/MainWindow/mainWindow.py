import tkinter as tk
import json
import os

# Load translations
def load_language(lang_code):
    with open(os.path.join("locales", f"{lang_code}.json"), "r", encoding="utf-8") as f:
        return json.load(f)

class MultiLangApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-language Example")

        # Default language
        self.current_lang = "en"
        self.translations = load_language(self.current_lang)

        # Frame for language buttons
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(pady=10)

        # Buttons for language switching
        self.btn_english = tk.Button(self.top_frame, text=self.translations["lang_english"], 
                                     command=lambda: self.switch_language("en"))
        self.btn_french = tk.Button(self.top_frame, text=self.translations["lang_french"], 
                                    command=lambda: self.switch_language("fr"))
        self.btn_arabic = tk.Button(self.top_frame, text=self.translations["lang_arabic"], 
                                    command=lambda: self.switch_language("ar"))
        self.btn_german = tk.Button(self.top_frame, text=self.translations["lang_german"], 
                            command=lambda: self.switch_language("de"))

        self.btn_english.pack(side="left", padx=5)
        self.btn_french.pack(side="left", padx=5)
        self.btn_arabic.pack(side="left", padx=5)
        self.btn_german.pack(side="left", padx=5)

        # Label
        self.label = tk.Label(self.root, text=self.translations["welcome"], font=("Arial", 18))
        self.label.pack(pady=20)

    def switch_language(self, lang_code):
        # Load new translations
        self.current_lang = lang_code
        self.translations = load_language(lang_code)

        # Update all texts
        self.btn_english.config(text=self.translations["lang_english"])
        self.btn_french.config(text=self.translations["lang_french"])
        self.btn_arabic.config(text=self.translations["lang_arabic"])
        self.btn_german.config(text=self.translations["lang_german"])
        self.label.config(text=self.translations["welcome"])

def run_app():
    root = tk.Tk()
    root.geometry("600x400")
    app = MultiLangApp(root)
    root.mainloop()
