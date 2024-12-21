# CSV File Manager Documentation

## Overview
The CSV File Manager is a GUI application built with tkinter that provides a user-friendly interface for managing CSV files. This application allows users to view, edit, search, sort, and filter CSV data through an intuitive graphical interface.

## Features
- Display CSV data in a table format
- Add, edit, and delete rows
- Search through data
- Sort data by columns
- Filter data based on specific criteria

## Dependencies
- Python 3.x
- tkinter (standard library)
- Custom csv_utils module (for CSV file operations)

## Classes

### CSVManagerApp
The main application class that creates the window and handles all GUI interactions and data operations.

#### Methods

##### `__init__(root)`
Initializes the application window and sets up all GUI components.
- Parameters:
  - `root`: The main tkinter window

##### `_setup_treeview()`
Configures the Treeview widget for displaying CSV data.

##### `_create_button_panel()`
Creates and configures the panel containing action buttons.

##### `load_data()`
Refreshes the Treeview display with current data.

##### `add_row()`
Opens a dialog to add a new row to the CSV file.

##### `edit_row()`
Edits the selected row in the Treeview.
- Shows a warning if no row is selected.

##### `delete_row()`
Deletes the selected row from the CSV file.
- Shows a warning if no row is selected.

##### `show_edit_window(title, values=None)`
Displays a dialog window for adding or editing row data.
- Parameters:
  - `title`: Window title ("Add Row" or "Edit Row")
  - `values`: (Optional) Current values when editing an existing row

##### `search_data()`
Opens a dialog to search for specific text across all columns.
- Displays matching rows in the Treeview.

##### `sort_data()`
Opens a dialog to sort data by a selected column.
- Updates the display with sorted data.

##### `filter_data()`
Opens a dialog to filter data based on column values.
- Updates the display with filtered results.

## Usage
1. Ensure all dependencies are installed
2. Place the CSV file in the same directory as the script
3. Update the `CSV_FILE` constant if your CSV file has a different name
4. Run the script:
   ```bash
   python main.py
   ```

## Data Operations
- **Adding Data**: Click "Add Row" and fill in the values in the popup window
- **Editing Data**: Select a row and click "Edit Row" to modify values
- **Deleting Data**: Select a row and click "Delete Row" to remove it
- **Searching**: Click "Search" and enter text to find matching rows
- **Sorting**: Click "Sort" and select a column to sort the data
- **Filtering**: Click "Filter", select a column and enter a value to filter rows

## Error Handling
The application includes various error checks and user feedback:
- Warnings when no row is selected for edit/delete operations
- Validation for empty search/filter criteria
- Feedback when no matching results are found
- Confirmation for data modification operations
