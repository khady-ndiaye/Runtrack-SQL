import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector
import csv

def connect_db():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Papito1989*",
            database="store"
        )
        return conn
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
        return None

class StoreManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Management")
        
        self.conn = connect_db()
        if self.conn is None:
            return
        self.cursor = self.conn.cursor()

        self.create_widgets()
        self.load_products()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_widgets(self):
        self.filter_label = tk.Label(self.root, text="Filter by Category:")
        self.filter_label.grid(row=0, column=0, padx=10, pady=5)

        self.filter_combo = ttk.Combobox(self.root, state="readonly")
        self.filter_combo.grid(row=0, column=1, padx=10, pady=5)
        self.filter_combo.bind("<<ComboboxSelected>>", self.load_products)
        
        self.table = tk.Listbox(self.root, width=70, height=15)
        self.table.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.grid(row=1, column=3, sticky="ns")
        self.table.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.table.yview)
        
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=2, column=0, columnspan=3, pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Product", command=self.add_product)
        self.add_button.grid(row=0, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Product", command=self.delete_product)
        self.delete_button.grid(row=0, column=1, padx=10, pady=5)

        self.update_button = tk.Button(self.button_frame, text="Update Product", command=self.update_product)
        self.update_button.grid(row=0, column=2, padx=10, pady=5)

        self.export_button = tk.Button(self.button_frame, text="Export to CSV", command=self.export_to_csv)
        self.export_button.grid(row=0, column=3, padx=10, pady=5)

        self.load_categories()

    def load_categories(self):
        self.cursor.execute("SELECT name FROM category")
        categories = [row[0] for row in self.cursor.fetchall()]
        self.filter_combo["values"] = ["All"] + categories
        self.filter_combo.current(0)

    def load_products(self, event=None):
        self.table.delete(0, tk.END)
        selected_category = self.filter_combo.get()
        if selected_category == "All":
            query = "SELECT p.id, p.name, p.price, p.quantity, c.name FROM product p JOIN category c ON p.id_category = c.id"
            self.cursor.execute(query)
        else:
            query = "SELECT p.id, p.name, p.price, p.quantity, c.name FROM product p JOIN category c ON p.id_category = c.id WHERE c.name = %s"
            self.cursor.execute(query, (selected_category,))
        
        products = self.cursor.fetchall()
        for product in products:
            self.table.insert(tk.END, f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Quantity: {product[3]}, Category: {product[4]}")

    def export_to_csv(self):
        with open("products.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Price", "Quantity", "Category"])
            query = "SELECT p.id, p.name, p.price, p.quantity, c.name FROM product p JOIN category c ON p.id_category = c.id"
            self.cursor.execute(query)
            writer.writerows(self.cursor.fetchall())
        messagebox.showinfo("Success", "Products exported successfully")
    def add_product(self):
        def save_product():
            name = entry_name.get()
            description = entry_description.get()
            price = entry_price.get()
            quantity = entry_quantity.get()
            category = combo_category.get()

            if not name or not price or not quantity or not category:
                messagebox.showerror("Error", "All fields are required")
                return

            query = "INSERT INTO product (name, description, price, quantity, id_category) VALUES (%s, %s, %s, %s, (SELECT id FROM category WHERE name = %s))"
            self.cursor.execute(query, (name, description, price, quantity, category))
            self.conn.commit()
            new_window.destroy()
            self.load_products()
            messagebox.showinfo("Success", "Product added successfully")

        new_window = tk.Toplevel(self.root)
        new_window.title("Add Product")

        tk.Label(new_window, text="Name:").grid(row=0, column=0)
        entry_name = tk.Entry(new_window)
        entry_name.grid(row=0, column=1)

        tk.Label(new_window, text="Description:").grid(row=1, column=0)
        entry_description = tk.Entry(new_window)
        entry_description.grid(row=1, column=1)

        tk.Label(new_window, text="Price:").grid(row=2, column=0)
        entry_price = tk.Entry(new_window)
        entry_price.grid(row=2, column=1)

        tk.Label(new_window, text="Quantity:").grid(row=3, column=0)
        entry_quantity = tk.Entry(new_window)
        entry_quantity.grid(row=3, column=1)

        tk.Label(new_window, text="Category:").grid(row=4, column=0)
        query = "SELECT name FROM category"
        self.cursor.execute(query)
        categories = [row[0] for row in self.cursor.fetchall()]
        combo_category = ttk.Combobox(new_window, values=categories)
        combo_category.grid(row=4, column=1)
        combo_category.current(0)

        tk.Button(new_window, text="Save", command=save_product).grid(row=5, column=1)

    def delete_product(self):
        selected_product = self.table.curselection()
        if not selected_product:
            messagebox.showerror("Error", "Please select a product to delete")
            return

        product_id = self.table.get(selected_product).split(",")[0].split(":")[1].strip()

        query = "DELETE FROM product WHERE id = %s"
        self.cursor.execute(query, (product_id,))
        self.conn.commit()
        self.load_products()
        messagebox.showinfo("Success", "Product deleted successfully")

    def update_product(self):
        selected_product = self.table.curselection()
        if not selected_product:
            messagebox.showerror("Error", "Please select a product to update")
            return

        product_id = self.table.get(selected_product).split(",")[0].split(":")[1].strip()
        selected_text = self.table.get(selected_product)
        values = [v.split(":")[1].strip() for v in selected_text.split(",")]

        def save_update():
            price = entry_price.get()
            quantity = entry_quantity.get()

            if not price or not quantity:
                messagebox.showerror("Error", "Price and quantity are required")
                return

            query = "UPDATE product SET price = %s, quantity = %s WHERE id = %s"
            self.cursor.execute(query, (price, quantity, product_id))
            self.conn.commit()
            update_window.destroy()
            self.load_products()
            messagebox.showinfo("Success", "Product updated successfully")

        update_window = tk.Toplevel(self.root)
        update_window.title("Update Product")

        tk.Label(update_window, text="Price:").grid(row=0, column=0)
        entry_price = tk.Entry(update_window)
        entry_price.grid(row=0, column=1)
        entry_price.insert(0, values[2])

        tk.Label(update_window, text="Quantity:").grid(row=1, column=0)
        entry_quantity = tk.Entry(update_window)
        entry_quantity.grid(row=1, column=1)
        entry_quantity.insert(0, values[3])

        tk.Button(update_window, text="Save", command=save_update).grid(row=2, column=1)

    def on_closing(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = StoreManagementApp(root)
    root.mainloop()
