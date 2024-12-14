from inventory_management.inventory import Inventory
from tkinter import *
from tkinter import Tk, Entry, Label, Button, Frame, messagebox, Toplevel, Scrollbar, Menu, ttk, filedialog
from tkinter.ttk import Treeview
from inventory_management.inventory import Inventory
import json
from pkg_resources import resource_filename


inventory = Inventory()


image_path = resource_filename("inventory_management", "asset/bg.png")
def main():
    window = Tk()
    window.title("Inventory Management System")
    window.geometry("500x450")
    window.resizable(False, False)
    window.config(bg = "#F0F8FF")

    menu = Menu(window)
    window.config(menu = menu)
     # UI Functions
    def add_item():
        item_id = entry_id.get()
        name = entry_name.get()
        try:
            quantity = int(entry_quantity.get())
            price = float(entry_price.get())
            min_threshold = int(entry_min_threshold.get())
            max_threshold = int(entry_max_threshold.get())
            result = inventory.add_item(item_id, name, quantity, price, min_threshold, max_threshold)
            messagebox.showinfo("Success", result)
        except ValueError:
            messagebox.showerror("Error", "Quantity, Price, Min Threshold, and Max Threshold must be numeric.")

    def save_inventory():
        try:
            # Open a file dialog to ask the user for a filename
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if not file_path:
                return  # If the user cancels, do nothing

            # Serialize the inventory items to JSON format and save to the chosen file
            with open(file_path, "w") as f:
                json.dump(inventory.items, f, indent=4)
            messagebox.showinfo("Save", f"Inventory saved successfully to {file_path}.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the inventory: {e}")

    def load_inventory():
        try:
            # Open a file dialog to ask the user for the file to load
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if not file_path:
                return  # If the user cancels, do nothing

            # Read the JSON data from the selected file and deserialize it back into the inventory
            with open(file_path, "r") as f:
                inventory.items = json.load(f)
            messagebox.showinfo("Load", f"Inventory loaded successfully from {file_path}.")
        except FileNotFoundError:
            messagebox.showerror("Error", "The selected file does not exist.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error decoding inventory data. The file may be corrupted.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while loading the inventory: {e}")


    def update_item():
        item_id = entry_id.get()
        try:
            quantity = int(entry_quantity.get())
            price = float(entry_price.get())
            result = inventory.update_item(item_id, quantity, price)
            messagebox.showinfo("Success", result)
        except ValueError:
            messagebox.showerror("Error", "Quantity and Price must be numeric.")

    def delete_item():
        item_id = entry_id.get()
        result = inventory.delete_item(item_id)
        messagebox.showinfo("Delete Item", result)

    def retrieve_items():
        item_id = entry_id.get()
        try:
            quantity_requested = int(entry_quantity.get()) if entry_quantity.get() else None
            result = inventory.retrieve_items(item_id, quantity_requested)
            messagebox.showinfo("Inventory Items", result)
        except ValueError:
            messagebox.showerror("Error", "Quantity must be numeric.")
    def check_thresholds():
        low_stock, over_stock = inventory.check_thresholds()
        message = "Low Stock Items:\n"
        message += "\n".join([f"{item['name']} (ID: {item['id']}, Quantity: {item['quantity']})" for item in low_stock])
        message += "\n\nOver Stock Items:\n"
        message += "\n".join([f"{item['name']} (ID: {item['id']}, Quantity: {item['quantity']})" for item in over_stock])
        if not low_stock and not over_stock:
            messagebox.showinfo("Stock Levels", "All stock levels are within thresholds.")
        else:
            messagebox.showinfo("Stock Levels", message)

    def view_all_items():
        new_window = Toplevel(window)
        new_window.title("All Inventory Items")
        new_window.geometry("700x400")

        frame = Frame(new_window)
        frame.pack(fill="both", expand=True)

        tree = Treeview(
            frame,
            columns=("ID", "Name", "Quantity", "Price", "Min Threshold", "Max Threshold"),
            show="headings"
        )
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Quantity", text="Quantity")
        tree.heading("Price", text="Price")
        tree.heading("Min Threshold", text="Min Threshold")
        tree.heading("Max Threshold", text="Max Threshold")
        tree.column("ID", width=100)
        tree.column("Name", width=150)
        tree.column("Quantity", width=100)
        tree.column("Price", width=100)
        tree.column("Min Threshold", width=120)
        tree.column("Max Threshold", width=120)

        vsb = Scrollbar(frame, orient="vertical", command=tree.yview)
        hsb = Scrollbar(frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side="right", fill="y")
        hsb.pack(side="bottom", fill="x")
        tree.pack(fill="both", expand=True)

        for item in inventory.items:
            tree.insert("", "end", values=(
                item["id"], item["name"], item["quantity"], item["price"],
                item["min_threshold"], item["max_threshold"]
            ))

    def exit_application():
        if messagebox.askyesno("Exit", "Are you sure you want to exit the application?"):
            window.destroy() 


    file_menu = Menu(menu, tearoff = False)
    menu.add_cascade(label = "File", menu = file_menu)
    file_menu.add_command(label = "Check Thresholds", command=check_thresholds)
    file_menu.add_command(label = "View All Items", command=view_all_items)
    file_menu.add_separator()
    file_menu.add_command(label="Save Inventory", command=save_inventory)
    file_menu.add_command(label="Load Inventory", command=load_inventory)
    file_menu.add_separator()
    file_menu.add_command(label = "Exit", command = exit_application)

    frame= Frame(window,bg="red")
    frame.pack(fill=Y)
    #Bg Image
    background_image = PhotoImage(master = window, file=image_path)
    Label(frame, image=background_image).pack()


    #User Entry

    def create_entry(frame, x, y, label_text):
        label = Label(frame, text=label_text, fg="white", bg="#424669", font=('Arial Bold', 12), anchor="e")  # Right-align the label text
        label.place(x=x-110, y=y-3, width=170)  # Adjust label position to lean right

        entry = Entry(frame, width=20, fg="#000", border=0, bg="#676F9D", font=('Arial Bold', 12))
        entry.place(x=x+73, y=y)  # Position the entry to the right of the label

        return entry

    # Create entries with right-aligned labels
    entry_id = create_entry(frame, x=130, y=110, label_text='ID Number')
    entry_name = create_entry(frame, x=130, y=146, label_text='Name')
    entry_quantity = create_entry(frame, x=130, y=182, label_text='Quantity')
    entry_price = create_entry(frame, x=130, y=218, label_text='Price')
    entry_min_threshold = create_entry(frame, x=130, y=254, label_text='Minimum Threshold')
    entry_max_threshold = create_entry(frame, x=130, y=290, label_text='Maximum Threshold')

    add_button= Button(text="Add Item", fg="#F5FFFA",bg = "#F8B179", command=add_item, width=11, height= 1, font= ('Arial Bold', 12), bd=0)
    add_button.place(x=110, y=342)
    update_button= Button(text="Update Item", fg="#F5FFFA",bg = "#F8B179", command=update_item, width=10, height= 1, font= ('Arial Bold', 12), bd=0)
    update_button.place(x=311, y=342)
    delete_button= Button(text="Delete Item", fg="#F5FFFA",bg = "#F8B179", command=delete_item, width=11, height= 1, font= ('Arial Bold', 12), bd=0)
    delete_button.place(x=110, y=387)
    retrieve_button= Button(text="Retrieve Items", fg="#F5FFFA",bg = "#F8B179", command=retrieve_items, width=10, height= 1, font= ('Arial Bold', 12), bd=0)
    retrieve_button.place(x=311, y=387)
   
    window.mainloop()