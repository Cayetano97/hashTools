from tkinter import Tk, Label, Entry, Button, messagebox, OptionMenu, StringVar
from tkinter.filedialog import askopenfilename
import hashlib

hash_functions = ["md5", "sha1", "sha256", "sha384", "sha512"]

def hashChecker():
    selected_function = hash_function_var.get()
    provided_hash = hash_entry.get().lower()

    Tk().withdraw()
    file_route = askopenfilename()

    if provided_hash != "":
        with open(file_route, "rb") as file_to_read:
            file_readed = file_to_read.read()

        if selected_function == "md5":
            readable_hash = hashlib.md5(file_readed).hexdigest()
        elif selected_function == "sha1":
            readable_hash = hashlib.sha1(file_readed).hexdigest()
        elif selected_function == "sha256":
            readable_hash = hashlib.sha256(file_readed).hexdigest()
        elif selected_function == "sha384":
            readable_hash = hashlib.sha384(file_readed).hexdigest()
        elif selected_function == "sha512":
            readable_hash = hashlib.sha512(file_readed).hexdigest()
    else:
        messagebox.showerror("Hash_Checker", "You must enter a hash before selecting a file")
        return

    if provided_hash == readable_hash:
        messagebox.showinfo("Hash_Checker", "Hashes match")
    else:
        messagebox.showerror("Hash_Checker", "Hashes don't match")

# Window
window = Tk()
window.title("Hash Checker")
window.geometry("300x175")

hash_label = Label(window, text="Select the hash function:")
hash_label.pack()

hash_function_var = StringVar()
hash_function_var.set(hash_functions[0]) 
hash_function_menu = OptionMenu(window, hash_function_var, *hash_functions)
hash_function_menu.pack()

hash_label = Label(window, text="Enter the hash to check:")
hash_label.pack()

hash_entry = Entry(window)
hash_entry.pack(pady=5)

hash_label = Label(window, text="Now, select the file to check:")
hash_label.pack(pady=5)

seleccionar_archivo_button = Button(window, text="Select File to check hash", command=hashChecker)
seleccionar_archivo_button.pack()

window.mainloop()
