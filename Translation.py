import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class RealTimeTranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Translator")
        self.root.configure(bg='#1E201E')
        self.root.geometry("600x400")
        
        # Style configuration
        style = ttk.Style()
        style.configure("TLabel", background='#3A1078', foreground='#ecf0f1', font=('Helvetica', 12))
        style.configure("TButton", background='#e74c3c', foreground='#FFA62F', font=('Helvetica', 12))
        style.configure("TCombobox", font=('Helvetica', 12))
        
        # Language selection
        self.target_lang_label = ttk.Label(root, text="Target Language:")
        self.target_lang_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.target_lang_var = tk.StringVar()
        self.target_lang_select = ttk.Combobox(root, textvariable=self.target_lang_var, values=list(LANGUAGES.values()), state="readonly", width=30)
        self.target_lang_select.grid(row=0, column=1, padx=10, pady=10, sticky="w", columnspan=2)
        self.target_lang_select.current(1)
        
        # Text entry
        self.input_label = ttk.Label(root, text="Enter Text:")
        self.input_label.grid(row=1, column=0, padx=10, pady=10, sticky="nw")
        self.input_text = tk.Text(root, height=5, width=50, font=('Helvetica', 12))
        self.input_text.grid(row=1, column=1, padx=10, pady=10)

        # Translation display
        self.output_label = ttk.Label(root, text="Translated Text:")
        self.output_label.grid(row=2, column=0, padx=10, pady=10, sticky="nw")
        self.output_text = tk.Text(root, height=5, width=50, font=('Helvetica', 12), state="disabled")
        self.output_text.grid(row=2, column=1, padx=10, pady=10)

        # Translate Button
        self.translate_button = ttk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.grid(row=3, column=1, pady=20, padx=10, sticky="w")

    def translate_text(self):
        translator = Translator()
        input_text = self.input_text.get("1.0", "end-1c")
        
        
        source_lang = 'auto'
        
        target_lang = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(self.target_lang_var.get())]
        
        
        translated_text = translator.translate(input_text, src=source_lang, dest=target_lang).text
        
        
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", translated_text)
        self.output_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = RealTimeTranslatorApp(root)
    root.mainloop()
