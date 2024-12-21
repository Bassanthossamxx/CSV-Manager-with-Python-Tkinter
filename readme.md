# CSV Manager with Python and Tkinter
## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [File Structure](#file-structure)
4. [Installation](#installation)
5. [Code Explanation](#code-explanation)
    - [Modules Used](#modules-used)
    - [GUI with Tkinter](#gui-with-tkinter)
    - [CSV Operations](#csv-operations)
6. [How to Use](#how-to-use)
7. [Contributing](#contributing)
8. [License](#license)

---

## Overview
This project is a simple desktop application that helps users manage CSV files. It allows you to edit, update, add, and remove data from CSV files in an intuitive graphical user interface (GUI). It’s perfect for beginners to understand both Python programming and the usage of Tkinter for creating GUIs.

---

## Features
- **Load CSV Files:** Open and display the contents of a CSV file.
- **Edit Rows:** Modify existing data in the table.
- **Add Rows:** Insert new rows of data.
- **Delete Rows:** Remove unwanted rows from the file.
- **Save Changes:** Save the changes back to the CSV file.

---

## File Structure
Here is an example of the typical file structure for the project:

```
CSV-Manager-with-Python-Tkinter/
|-- main.py
|-- requirements.txt
|-- README.md
```

### Explanation:
1. **main.py:** The main script that runs the application.
2. **requirements.txt:** A list of required Python libraries (if any).
3. **README.md:** This documentation.

---

## Installation
To run the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Bassanthossamxx/CSV-Manager-with-Python-Tkinter.git
   cd CSV-Manager-with-Python-Tkinter
   ```

2. Install Python dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## Code Explanation

### Modules Used
- **`tkinter`**: Used for creating the graphical user interface (GUI).
- **`csv`**: Used to read and write CSV files.
- **`os`**: Helps in handling file operations.

### GUI with Tkinter
Tkinter provides the tools for building the interface. The project includes components like:

- **Buttons**: Trigger actions such as opening a file, saving changes, or adding/removing rows.
- **Labels and Entry Widgets**: Display and take input from the user.
- **Treeview (from ttk)**: Displays the contents of the CSV file in a tabular format, similar to a spreadsheet.

Example snippet for the GUI:
```python
root = Tk()
root.title("CSV Manager")

# Create a Treeview to display the CSV data
tree = ttk.Treeview(root, columns=("Name", "Age", "Country"), show='headings')
```

### CSV Operations
- **Load CSV**: Opens a file dialog to select a CSV file and loads its content into the Treeview.
  ```python
  with open(filename, 'r') as file:
      reader = csv.reader(file)
      for row in reader:
          tree.insert('', 'end', values=row)
  ```

- **Add Row**: Appends a new row to the Treeview and prepares to save it to the file.
  ```python
  tree.insert('', 'end', values=("", "", ""))
  ```

- **Edit Row**: Selects a specific row for editing. The user can input new data.
- **Delete Row**: Deletes the selected row from the Treeview and marks it for removal from the file.
  ```python
  selected_item = tree.selection()[0]  # Get selected item
  tree.delete(selected_item)
  ```

- **Save Changes**: Writes the updated data back to the CSV file.
  ```python
  with open(filename, 'w', newline='') as file:
      writer = csv.writer(file)
      for row_id in tree.get_children():
          row = tree.item(row_id)['values']
          writer.writerow(row)
  ```

---

## How to Use
1. Open the application.
2. Click "Load CSV" to select and load a CSV file.
3. Use the "Add Row," "Edit Row," or "Delete Row" buttons to manage data.
4. Save your changes by clicking "Save."

---

## Contributing
Feel free to contribute by forking the repository and submitting a pull request. Any enhancements, bug fixes, or additional features are welcome!

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

### Happy Coding!

