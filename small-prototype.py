import tkinter as tk
from tkinter import ttk
import sqlite3
import tkinter.messagebox as messagebox

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("800x500")

        self.book_id = tk.StringVar()
        self.book_title = tk.StringVar()
        self.author = tk.StringVar()
        self.isbn = tk.StringVar()

        # Create a database connection
        self.conn = sqlite3.connect("library.db")
        self.cursor = self.conn.cursor()

        self.create_table()

        # Create and layout the widgets
        self.lbl_title = ttk.Label(root, text="Library Management System", font=("Arial", 20))
        self.lbl_title.pack(pady=20)

        self.lbl_book_id = ttk.Label(root, text="Book ID:")
        self.lbl_book_id.pack()
        self.ent_book_id = ttk.Entry(root, textvariable=self.book_id)
        self.ent_book_id.pack()

        self.lbl_book_title = ttk.Label(root, text="Book Title:")
        self.lbl_book_title.pack()
        self.ent_book_title = ttk.Entry(root, textvariable=self.book_title)
        self.ent_book_title.pack()

        self.lbl_author = ttk.Label(root, text="Author:")
        self.lbl_author.pack()
        self.ent_author = ttk.Entry(root, textvariable=self.author)
        self.ent_author.pack()

        self.lbl_isbn = ttk.Label(root, text="ISBN:")
        self.lbl_isbn.pack()
        self.ent_isbn = ttk.Entry(root, textvariable=self.isbn)
        self.ent_isbn.pack()

        self.btn_add = ttk.Button(root, text="Add Book", command=self.add_book)
        self.btn_add.pack(pady=10)

        self.btn_view = ttk.Button(root, text="View Books", command=self.view_books)
        self.btn_view.pack(pady=10)

        self.btn_delete = ttk.Button(root, text="Delete Book", command=self.delete_book)
        self.btn_delete.pack(pady=10)

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, isbn TEXT)")

    def add_book(self):
        book_id = self.book_id.get()
        book_title = self.book_title.get()
        author = self.author.get()
        isbn = self.isbn.get()

        if not book_id or not book_title or not author or not isbn:
            messagebox.showwarning("Incomplete Input", "Please fill in all fields.")
            return

        self.cursor.execute("INSERT INTO books (id, title, author, isbn) VALUES (?, ?, ?, ?)", (book_id, book_title, author, isbn))
        self.conn.commit()
        messagebox.showinfo("Success", "Book added successfully.")
        self.clear_fields()

    def view_books(self):
        self.cursor.execute("SELECT * FROM books")
        books = self.cursor.fetchall()

        if not books:
            messagebox.showinfo("No Books", "No books found in the library.")
            return

        view_window = tk.Toplevel(self.root)
        view_window.title("View Books")
        view_window.geometry("500x300")

        tree = ttk.Treeview(view_window, columns=("ID", "Title", "Author", "ISBN"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Title", text="Title")
        tree.heading("Author", text="Author")
        tree.heading("ISBN", text="ISBN")
        tree.pack(fill=tk.BOTH, expand=True)

        for book in books:
            tree.insert("", "end", values=book)

    def delete_book(self):
        book_id = self.book_id.get()

        if not book_id:
            messagebox.showwarning("Incomplete Input", "Please enter the ID of the book to delete.")
            return

        self.cursor.execute("DELETE FROM books WHERE id=?", (book_id,))
        self.conn.commit()
        messagebox.showinfo("Success", "Book deleted successfully.")
        self.clear_fields()

    def clear_fields(self):
        self.book_id.set("")
        self.book_title.set("")
        self.author.set("")
        self.isbn.set("")

if __name__ == "__main__":
    root = tk.Tk()
    library_system = LibraryManagementSystem(root)
    root.mainloop()
