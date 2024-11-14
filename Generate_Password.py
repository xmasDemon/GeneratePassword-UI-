import tkinter as tk
from tkinter import messagebox
import random
import string


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор паролей")

        self.length_label = tk.Label(root, text="Длина пароля:")
        self.length_label.pack()

        self.length_entry = tk.Entry(root)
        self.length_entry.pack()

        self.lowercase_var = tk.BooleanVar()
        self.lowercase_check = tk.Checkbutton(root, text="Включить алфавит нижнего регистра [a-z]",
                                              variable=self.lowercase_var)
        self.lowercase_check.pack()

        self.digits_var = tk.BooleanVar()
        self.digits_check = tk.Checkbutton(root, text="Включить цифры [0-9]", variable=self.digits_var)
        self.digits_check.pack()

        self.special_var = tk.BooleanVar()
        self.special_check = tk.Checkbutton(root, text="Включить спецсимволы [! @ # $ %]", variable=self.special_var)
        self.special_check.pack()

        self.generate_button = tk.Button(root, text="Сгенерировать пароль", command=self.generate_password)
        self.generate_button.pack()

        self.result_label = tk.Label(root, text="", font=('Helvetica', 14))
        self.result_label.pack(pady=10)

    def generate_password(self):
        length = self.length_entry.get()

        if not length.isdigit() or int(length) <= 0:
            messagebox.showerror("Ошибка", "Введите корректную длину пароля.")
            return

        length = int(length)
        characters = ""

        if self.lowercase_var.get():
            characters += string.ascii_lowercase
        if self.digits_var.get():
            characters += string.digits
        if self.special_var.get():
            characters += "!@#$%"

        if not characters:
            messagebox.showerror("Ошибка", "Выберите хотя бы один тип символов для генерации пароля.")
            return

        password = ""
        while True:
            password = ''.join(random.choice(characters) for _ in range(length))

            if not self.special_var.get() or any(char in "!@#$%" for char in password):
                break

        self.result_label.config(text=f"Сгенерированный пароль: {password}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
