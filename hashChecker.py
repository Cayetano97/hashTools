from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter.filedialog import askopenfilename
import hashlib

def hashChecker():
    provided_hash = hash_entry.get().lower()

    Tk().withdraw()
    file_route = askopenfilename()

    if provided_hash != "":
        with open(file_route, "rb") as file_to_read:
            file_readed = file_to_read.read()
            readable_hash = hashlib.sha256(file_readed).hexdigest()
    else:
        messagebox.showerror("Hash_Checker", "You must enter a hash before selecting a file")

    if provided_hash == readable_hash:
        messagebox.showinfo("Hash_Checker", "Hashes match")
    else:
        messagebox.showerror("Hash_Checker", "Hashes don't match")


# Window

window = Tk()
window.title("Hash_256 Checker")
window.geometry("300x125") 

hash_label = Label(window, text="Enter the hash to check:")
hash_label.pack()

hash_entry = Entry(window)
hash_entry.pack(pady=5)

hash_label = Label(window, text="Now, select the file to check:")
hash_label.pack(pady=5)

seleccionar_archivo_button = Button(window, text="Select File to check hash", command=hashChecker)
seleccionar_archivo_button.pack()

window.mainloop()
