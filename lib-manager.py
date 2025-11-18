import tkinter as tk
from tkinter import messagebox

file_path = r"e:\python\libs.csv"
libs = []

# Load libs from file
try:
    with open(file_path, "r") as database:
        for line in database:
            if line.strip():
                libs.append(line.strip())
except FileNotFoundError:
    pass


def show_libs():
    listbox.delete(0, tk.END)
    for lib in libs:
        listbox.insert(tk.END, lib)


def add_lib():
    lib_name = entry.get().strip()
    if lib_name:
        libs.append(lib_name)
        entry.delete(0, tk.END)
        show_libs()
        save_libs()
    else:
        messagebox.showwarning("Warning", "Please enter a lib name.")


def delete_lib():
    if libs:
        selection = listbox.curselection()
        if selection:
            idx = selection[0]
            del libs[idx]
            show_libs()
            save_libs()
        else:
            messagebox.showwarning("Warning", "Please select a lib to delete.")
    else:
        messagebox.showwarning("Warning", "No libs to delete.")


def save_libs():
    with open(file_path, "w") as cnf:
        for lib in libs:
            cnf.write(lib + "\n")


def quit_app():
    save_libs()
    root.quit()


# Create main window
root = tk.Tk()
root.title("Libs Manager")

# Listbox for showing libs
listbox = tk.Listbox(root, height=10, width=50)
listbox.pack(pady=10)

# Entry for adding lib
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

show_btn = tk.Button(button_frame, text="Show Libs", command=show_libs)
show_btn.pack(side=tk.LEFT, padx=5)

add_btn = tk.Button(button_frame, text="Add Lib", command=add_lib)
add_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Lib", command=delete_lib)
delete_btn.pack(side=tk.LEFT, padx=5)

quit_btn = tk.Button(button_frame, text="Quit", command=quit_app)
quit_btn.pack(side=tk.LEFT, padx=5)

# Initial show
show_libs()

root.mainloop()
