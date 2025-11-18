import tkinter as tk
from tkinter import messagebox, ttk

file_path = r"e:\python\libs.csv"
books = []

try:
    with open(file_path, "r", encoding="utf-8") as database:
        for line in database:
            if line.strip():
                parts = line.strip().split(",")
                if len(parts) == 4:
                    books.append(parts)
except FileNotFoundError:
    pass


def show_books():
    tree.delete(*tree.get_children())
    for book in books:
        tree.insert("", tk.END, values=book)


def add_book():
    title = entry_title.get().strip()
    price = entry_price.get().strip()
    writer = entry_writer.get().strip()
    write_date = entry_write_date.get().strip()

    if not (title and price and writer and write_date):
        messagebox.showwarning("Warning", "Please fill all fields.")
        return

    books.append([title, price, writer, write_date])

    entry_title.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_writer.delete(0, tk.END)
    entry_write_date.delete(0, tk.END)

    show_books()
    save_books()


def delete_book():
    selection = tree.selection()
    if not selection:
        messagebox.showwarning("Warning", "Select an item to delete.")
        return

    index = tree.index(selection[0])
    del books[index]

    show_books()
    save_books()


def save_books():
    with open(file_path, "w", encoding="utf-8") as cnf:
        for book in books:
            cnf.write(",".join(book) + "\n")


root = tk.Tk()
root.title("Books Manager")

columns = ("title", "price", "writer", "write_date")
tree = ttk.Treeview(root, columns=columns, show="headings", height=12)
tree.heading("title", text="Book Title")
tree.heading("price", text="Book Price")
tree.heading("writer", text="Writer")
tree.heading("write_date", text="Write Date")
tree.pack(pady=10)

entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Book Title:").grid(row=0, column=0, padx=5)
entry_title = tk.Entry(entry_frame, width=25)
entry_title.grid(row=0, column=1, padx=5)

tk.Label(entry_frame, text="Book Price:").grid(row=1, column=0, padx=5)
entry_price = tk.Entry(entry_frame, width=25)
entry_price.grid(row=1, column=1, padx=5)

tk.Label(entry_frame, text="Writer:").grid(row=2, column=0, padx=5)
entry_writer = tk.Entry(entry_frame, width=25)
entry_writer.grid(row=2, column=1, padx=5)

tk.Label(entry_frame, text="Write Date:").grid(row=3, column=0, padx=5)
entry_write_date = tk.Entry(entry_frame, width=25)
entry_write_date.grid(row=3, column=1, padx=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=12)

add_btn = tk.Button(button_frame, text="Add Book", command=add_book)
add_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(button_frame, text="Delete Book", command=delete_book)
delete_btn.pack(side=tk.LEFT, padx=5)

show_books()

root.mainloop()
