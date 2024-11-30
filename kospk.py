import tkinter as tk
import re

transfer_dict = {
    "наприклад": "на-при-клад",
    "український": "укра-їнсь-кий",
    "розроблення": "роз-роб-лен-ня",
    "програми": "про-гра-ми",
    "це": "це",
    "швидко": "швид-ко",
    "лис": "лис",
    "кота": "ко-та",
    "тест": "тест",
    "один": "один",
    "привіт": "при-віт"}

def transfer_word(word):
    word = word.lower()
    if word in transfer_dict:
        return transfer_dict[word]
    else:
        vowels = "аеиіїоуюяєю"
        word = re.sub(r"([а-яіїєґ])\1+", r"\1", word) # Видаляє повторення приголосних
        parts = []
        current_part = ""
        for char in word:
            current_part += char
            if char in vowels:
                parts.append(current_part)
                current_part = ""
        if current_part:
            parts.append(current_part)
        return "-".join(parts)

def transfer_text(text):
    try:
        if not text:
            raise ValueError("Введіть текст")
        words = text.split()
        transferred_text = " ".join([transfer_word(word) for word in words])
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, transferred_text)
    except ValueError as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Помилка: {e}")
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Непередбачена помилка: {type(e).__name__} - {str(e)}")

root = tk.Tk()
root.title("Перенос слів")

input_label = tk.Label(root, text="Введіть текст:")
input_label.pack(pady=5)

input_text = tk.Text(root, height=5, width=40)
input_text.pack(pady=5)

transfer_button = tk.Button(root, text="Перенести", command=lambda: transfer_text(input_text.get("1.0", tk.END).strip()))
transfer_button.pack(pady=5)

output_label = tk.Label(root, text="Результат:")
output_label.pack(pady=5)

output_text = tk.Text(root, height=5, width=40)
output_text.pack(pady=5)

test_texts = [
    "Наприклад український текст для тестування.",
    "Ще один текст для перевірки переносу слів.  Спробуємо швидкого лиса.",
    "Це короткий тест. Один кота. Привіт!"
]

test_index = 0

def run_tests():
    global test_index
    if test_index < len(test_texts):
        text = test_texts[test_index]
        input_text.delete("1.0", tk.END)
        input_text.insert(tk.END, text)  # Вставляємо тестовий текст у поле вводу
        print(f"\n--- Тест {test_index + 1} ---")
        print(f"Текст: {text}")
        transfer_text(text)
        root.update()
        test_index += 1
    else:
        print("\nТестування завершено.")

run_tests_button = tk.Button(root, text="Запустити тести", command=run_tests)
run_tests_button.pack(pady=5)

instruction_label = tk.Label(root, text="Натисніть кнопку \"Запустити тести\", потім Enter для кожного тесту.")
instruction_label.pack(pady=5)

root.mainloop()

