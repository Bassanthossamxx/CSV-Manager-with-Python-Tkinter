### Explanation of the Code

#### **Purpose**:
This project provides a graphical interface for managing CSV files. Users can perform operations like adding, editing, deleting, searching, sorting, and filtering rows of data in a CSV file. 

---

### **File Descriptions**:
1. **`main.py`**: This file contains the main application logic using the `tkinter` library to create the graphical interface for managing the CSV file.
2. **`csv_utils.py`**: This file provides utility functions to read and write CSV files.

---

### **Detailed Explanation**:

#### **`main.py`**:

1. **Imports**:
```python
import tkinter as tk
from tkinter import ttk, messagebox
from csv_utils import read_csv, write_csv
```
   - `tkinter` and `ttk`: Used to create and style the graphical user interface (GUI).
   - `messagebox`: Provides pop-up dialogs for warnings or information.
   - `csv_utils`: Provides helper functions to interact with CSV files (`read_csv`, `write_csv`).

2. **Constants**:
```python
CSV_FILE = "Titanic-Dataset.csv"
```
   - Specifies the file path to the dataset being managed.

3. **`CSVManagerApp` Class**:
```python
class CSVManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV File Manager")

        # Initialize data
        self.data, self.columns = read_csv(CSV_FILE)
        if not self.columns:
            self.columns = ["Column1", "Column2", "Column3"]  # Default column names

        # Create Treeview to display CSV content
        self.tree = ttk.Treeview(root, columns=self.columns, show="headings")
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack(fill="both", expand=True)

        # Buttons for operations
        btn_frame = ttk.Frame(root)
        btn_frame.pack(fill="x")

        ttk.Button(btn_frame, text="Add Row", command=self.add_row).pack(side="left", padx=5, pady=5)
        ttk.Button(btn_frame, text="Edit Row", command=self.edit_row).pack(side="left", padx=5, pady=5)
        ttk.Button(btn_frame, text="Delete Row", command=self.delete_row).pack(side="left", padx=5, pady=5)
        ttk.Button(btn_frame, text="Search", command=self.search_data).pack(side="left", padx=5, pady=5)
        ttk.Button(btn_frame, text="Sort", command=self.sort_data).pack(side="left", padx=5, pady=5)
        ttk.Button(btn_frame, text="Filter", command=self.filter_data).pack(side="left", padx=5, pady=5)

        self.load_data()
```
   - **Purpose**: Initializes the main application window and its components.
   - **Details**: 
     - Reads data from the CSV file using `read_csv`.
     - Sets default column names if the CSV file is empty.
     - Displays data in a `Treeview` widget (a tabular data display).
     - Creates buttons for operations like Add, Edit, Delete, Search, Sort, and Filter.

4. **Loading Data**:
```python
def load_data(self):
    """Load data into the Treeview."""
    self.tree.delete(*self.tree.get_children())
    for row in self.data:
        self.tree.insert("", "end", values=list(row.values()))
```
   - **Purpose**: Loads the CSV data into the `Treeview` widget by clearing the current contents and inserting rows from the CSV file.

5. **Adding a Row**:
```python
def add_row(self):
    """Add a new row to the CSV."""
    self.show_edit_window("Add Row")
```
   - **Purpose**: Opens a new window to let the user input data for a new row.
   - **Details**: Saves the new row to the CSV file and updates the display.

6. **Editing a Row**:
```python
def edit_row(self):
    """Edit the selected row."""
    selected_item = self.tree.selection()
    if not selected_item:
        messagebox.showwarning("No Selection", "Please select a row to edit.")
        return

    values = self.tree.item(selected_item, "values")
    self.show_edit_window("Edit Row", values)
```
   - **Purpose**: Opens a new window pre-filled with data from the selected row and allows the user to edit and save changes.

7. **Deleting a Row**:
```python
def delete_row(self):
    """Delete the selected row."""
    selected_item = self.tree.selection()
    if not selected_item:
        messagebox.showwarning("No Selection", "Please select a row to delete.")
        return

    values = self.tree.item(selected_item, "values")
    self.data = [row for row in self.data if list(row.values()) != list(values)]
    write_csv(CSV_FILE, self.data, self.columns)
    self.load_data()
```
   - **Purpose**: Deletes the selected row from the CSV file and updates the display.

8. **Utility Functions for Searching, Sorting, and Filtering**:
   - **Search**:
```python
def search_data(self):
    """Search for rows containing specific text."""
    search_win = tk.Toplevel(self.root)
    search_win.title("Search Data")

    ttk.Label(search_win, text="Search Text:").grid(row=0, column=0, padx=5, pady=5)
    search_entry = ttk.Entry(search_win)
    search_entry.grid(row=0, column=1, padx=5, pady=5)

    def perform_search():
        search_text = search_entry.get()
        if not search_text:
            messagebox.showwarning("Empty Search", "Please enter text to search.")
            return

        matching_rows = [row for row in self.data if search_text.lower() in " ".join(row.values()).lower()]
        if not matching_rows:
            messagebox.showinfo("No Matches", "No matching rows found.")
            return

        self.tree.delete(*self.tree.get_children())
        for row in matching_rows:
            self.tree.insert("", "end", values=list(row.values()))

    ttk.Button(search_win, text="Search", command=perform_search).grid(row=1, column=0, columnspan=2, pady=10)
```
   - **Sort**:
```python
def sort_data(self):
    """Sort the data by a selected column."""
    sort_win = tk.Toplevel(self.root)
    sort_win.title("Sort Data")

    ttk.Label(sort_win, text="Sort by Column:").grid(row=0, column=0, padx=5, pady=5)
    column_combo = ttk.Combobox(sort_win, values=self.columns)
    column_combo.grid(row=0, column=1, padx=5, pady=5)

    def perform_sort():
        selected_col = column_combo.get()
        if not selected_col:
            messagebox.showwarning("No Column Selected", "Please select a column to sort by.")
            return

        self.data.sort(key=lambda x: x[selected_col])
        self.load_data()
        sort_win.destroy()

    ttk.Button(sort_win, text="Sort", command=perform_sort).grid(row=1, column=0, columnspan=2, pady=10)
```

---

#### **`csv_utils.py`**:

1. **Reading CSV Data**:
```python
def read_csv(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader), reader.fieldnames  # Return rows and column names
    except FileNotFoundError:
        return [], []
```
   - **Purpose**: Opens the CSV file in read mode and returns rows as dictionaries.
   - **Error Handling**: Returns empty lists if the file does not exist.

2. **Writing CSV Data**:
```python
def write_csv(file_path, rows, fieldnames):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write column headers
        writer.writerows(rows)  # Write data rows
```
   - **Purpose**: Writes the column headers and data rows to the CSV file.

---

### **How the Application Works**:
1. **Setup**:
   - When the application starts, it reads the CSV file and displays its contents.
2. **Interactivity**:
   - Buttons allow users to perform various operations (e.g., add, edit, delete).
   - Separate pop-up windows are used for adding, editing, searching, sorting, and filtering data.
3. **File Updates**:
   - Each operation updates the CSV file using the `write_csv` function.
   - The `Treeview` display is refreshed to show the latest data.

---

This explanation includes the relevant code parts and explanations for each functionality. Let me know if further clarifications are needed!

