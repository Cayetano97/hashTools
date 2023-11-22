from tkinter import Tk, Label, Entry, Button, messagebox, OptionMenu, StringVar, ttk
from tkinter.filedialog import askopenfilename
import hashlib
import pyperclip

hash_functions = {
    "MD5": hashlib.md5,
    "SHA-1": hashlib.sha1,
    "SHA-256": hashlib.sha256,
    "SHA-384": hashlib.sha384,
    "SHA-512": hashlib.sha512,
    "BLAKE2b": hashlib.blake2b,
    "BLAKE2s": hashlib.blake2s,
}

# Window
window = Tk()
window.title("Hash Tools")
window.geometry("400x250")

# Global variables
hash_function_var = StringVar()
hash_entry = None
hash_result_label = None

tab = ttk.Notebook(window)

# Functions


def create_tab(text, content):
    tab_frame = ttk.Frame(tab)
    tab.add(tab_frame, text=text)
    content(tab_frame)


def hashChecker():
    selected_function = hash_function_var.get()
    provided_hash = hash_entry.get().lower()

    Tk().withdraw()
    file_route = askopenfilename()

    if provided_hash != "":
        with open(file_route, "rb") as file_to_read:
            file_readed = file_to_read.read()

        if selected_function in hash_functions:
            readable_hash = hash_functions[selected_function](
                file_readed).hexdigest()
    else:
        messagebox.showerror(
            "Hash_Checker", "You must enter a hash before selecting a file")
        return

    if provided_hash == readable_hash:
        messagebox.showinfo("Hash_Checker", "Hashes match")
    else:
        messagebox.showerror("Hash_Checker", "Hashes don't match")


def hashGenerator():
    selected_function = hash_function_var.get()

    Tk().withdraw()
    file_route = askopenfilename()

    with open(file_route, "rb") as file_to_read:
        file_readed = file_to_read.read()

    if selected_function in hash_functions:
        readable_hash = hash_functions[selected_function](
            file_readed).hexdigest()

    hash_result_label['text'] = readable_hash

 # Copy hash to clipboard


def copyHash():
    hash_to_copy = hash_result_label['text']
    pyperclip.copy(hash_to_copy)

# Tab content


def tab_content_1(frame):
    global hash_entry

    hash_label = Label(frame, text="Select the hash function:")
    hash_label.pack(pady=5)

    hash_function_var.set(list(hash_functions.keys())[0])
    hash_function_menu = OptionMenu(
        frame, hash_function_var, *hash_functions.keys())
    hash_function_menu.pack()

    hash_label = Label(frame, text="Enter the hash provided to check:")
    hash_label.pack()

    hash_entry = Entry(frame)
    hash_entry.pack(pady=5)

    hash_label = Label(frame, text="Now, select the file to check:")
    hash_label.pack(pady=5)

    seleccionar_archivo_button = Button(
        frame, text="Select file to check hash", command=hashChecker)
    seleccionar_archivo_button.pack()


def tab_content_2(frame):
    global hash_result_label

    hash_label = Label(frame, text="Select the hash function:")
    hash_label.pack(pady=5)

    hash_function_var.set(list(hash_functions.keys())[0])
    hash_function_menu = OptionMenu(
        frame, hash_function_var, *hash_functions.keys())
    hash_function_menu.pack()

    seleccionar_archivo_button = Button(
        frame, text="Select file to generate hash", command=hashGenerator)
    seleccionar_archivo_button.pack(pady=5)

    hash_result_label = Label(frame, text="")
    hash_result_label.pack(pady=5)

    copy_button = Button(frame, text="Copy Hash", command=copyHash)
    copy_button.pack(pady=5)


create_tab("Check Hash", tab_content_1)
create_tab("Generate Hash", tab_content_2)

tab.pack(expand=1, fill="both")
window.mainloop()
