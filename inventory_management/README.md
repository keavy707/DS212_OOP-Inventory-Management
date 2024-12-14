

# README!

This application is a Python-based Inventory Management System that aims to streamline the stocking, storing, and utilization of inventory by effectively tracking products and/or services. The GUI-based system allows users to add, update, delete, and retrieve items, as well as monitor inventory thresholds for efficient management.

---

## Members

- Ablanque, Alex  
- Aganan, Phoebe  
- Balistoy, Zynea  
- Bitco, Yvonne  
- Galorio, Vincent  
- Mallari, Kyle  
- Ocay, Andrea Keavy  
- Ramirez, Gabriel  

---

## Features

1. **Add Items**  
   Input items with classifications: ID Number, Name, Quantity, Price, Minimum Threshold, Maximum Threshold, and store them in the inventory.

2. **Update Items**  
   Modify the existing item’s Quantity and Price by entering the item ID.

3. **Delete Items**  
   Remove an item from the inventory using its unique ID.

4. **Retrieve Items**  
   Display a specific item or the entire inventory with details such as ID, Name, Quantity, Price, and Thresholds.

5. **Threshold Alerts**  
   View items that are either below the minimum threshold or above the maximum threshold.

6. **View All Items**  
   Display all items in a scrollable table format in a separate window.

7. **Save Inventory**

   Save the current inventory to a user-specified file in a human-readable .txt format. This ensures data is preserved and can be reviewed or reloaded later.

9. **Load Inventory**

   Load previously saved inventory data from a user-specified .txt file. Restores the inventory for continued management after reopening the application.


---

## Installation Instructions

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or higher
- `pip` (Python package manager)

### Steps to Install the Package

1. Navigate to desired directory for the repository:
   ```bash
   cd "repository_directory"
   ```
2. Clone this repository:
   ```bash
   git clone "repository URL"
   ```
   
3. Navigate to setup.py
   ```bash
   cd "DS212_OOP-Inventory-Management"
   ```
   ```bash
   cd "inventory_management"
   ```

4. Install the package using `pip`:
   ```bash
   pip install .
   ```

5. Verify the installation by running the following command:
   ```bash
   inventory_management
   ```

   This should launch the Inventory Management GUI application.

---

## Usage Examples

1. **Add Items**  
   - Input items with their classifications: ID Number, Name, Quantity, Price, Minimum Threshold, Maximum Threshold.
   - Click the **Add Item** button.

2. **Update Items**  
   - Input an item’s ID along with its new Quantity and Price to modify the existing data.
   - Click the **Update Item** button.

3. **Delete Items**  
   - Input an item’s ID to remove it from the inventory.
   - Click the **Delete Item** button.

4. **Retrieve Items**  
   - Click the **File** menu in the menu bar.
   - Select **View All Items** to retrieve and view the list of items.

5. **Check Thresholds**  
   - Click the **File** menu in the menu bar.
   - Select **Check Thresholds** to identify items that are below the minimum or above the maximum threshold.

---

## Project Structure

```
inventory_management/
├── inventory_management/
│   ├── __init__.py
│   ├── inventory.py
│   ├── ui.py
│   └── asset/
│       └── bg.png
├── setup.py
├── README.md
```

### Key Files

- **`inventory.py`**: Handles backend logic for managing inventory items.
- **`ui.py`**: Implements the graphical user interface (GUI) for the application.
- **`bg.png`**: Background image for the GUI.
- **`setup.py`**: Script to package and install the application.

---

Thank you for using our Inventory Management System! If you encounter any issues, please reach out to the project contributors.



