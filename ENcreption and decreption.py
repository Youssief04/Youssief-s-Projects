import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            base = ord('a')
        elif 'A' <= char <= 'Z':
            base = ord('A')
        elif '0' <= char <= '9':
            base = ord('0')
        else:
            result += char
            continue

        if mode == "encrypt":
            result += chr((ord(char) - base + shift) % 26 + base)
        elif mode == "decrypt":
            result += chr((ord(char) - base - shift) % 26 + base)

    return result

def encrypt_decrypt():
    text = input_text.get("1.0", tk.END).strip()
    shift = int(shift_value.get())
    mode = operation.get()

    output = caesar_cipher(text, shift, mode) 
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)

root = tk.Tk()
root.title("DISCRETE PROJECT")
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

input_text = tk.Text(frame, width=40, height=10)
input_text.grid(column=0, row=0, rowspan=4, padx=5, pady=5)

output_text = tk.Text(frame, width=40, height=10)
output_text.grid(column=1, row=0, rowspan=4, padx=5, pady=5)

operation = ttk.Combobox(frame, values=["encrypt", "decrypt"], state="readonly")
operation.set("encrypt")
operation.grid(column=0, row=4, padx=5, pady=5)

shift_label = ttk.Label(frame, text="Shift:")
shift_label.grid(column=1, row=4, padx=5, pady=5)

shift_value = ttk.Spinbox(frame, from_=1, to=25, width=5)
shift_value.set(3)
shift_value.grid(column=1, row=4, padx=5, pady=5)

button = ttk.Button(frame, text="Encrypt/Decrypt", command=encrypt_decrypt)
button.grid(column=0, row=5, padx=5, pady=5, sticky=tk.W)

root.mainloop()