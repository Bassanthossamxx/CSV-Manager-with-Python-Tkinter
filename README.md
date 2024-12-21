# CSV File Manager Documentation

## Overview
The CSV File Manager is a simple GUI application built with tkinter that provides basic functionality for managing CSV files. The application allows users to view and modify CSV data through an intuitive graphical interface.

## Features
- Display CSV data in a table format
- Add new rows to the CSV file
- Edit existing rows
- Delete selected rows

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
- Creates columns based on CSV headers
- Sets up column headings and widths
- Configures the display area

##### `_create_button_panel()`
Creates and configures the panel containing action buttons for data operations.
- Creates Add, Edit, and Delete buttons
- Arranges buttons horizontally with proper spacing

##### `load_data()`
Refreshes the Treeview display with current data from memory.
- Clears existing display
- Loads all rows from the data array
- Displays updated content in the table

##### `add_row()`
Opens a dialog to add a new row to the CSV file.
- Creates input fields for each column
- Provides a save button to commit changes

##### `edit_row()`
Edits the selected row in the Treeview.
- Shows a warning if no row is selected
- Opens edit dialog with current values
- Updates both display and file when saved

##### `delete_row()`
Deletes the selected row from the CSV file.
- Shows a warning if no row is selected
- Removes the row from both display and data
- Saves changes to file

##### `show_edit_window(title, values=None)`
Displays a dialog window for adding or editing row data.
- Parameters:
  - `title`: Window title ("Add Row" or "Edit Row")
  - `values`: (Optional) Current values when editing an existing row
- Creates input fields for each column
- Handles saving changes to both display and file

## Usage

1. Setup:
   ```bash
   # Ensure you have the required files
   - main.py
   - csv_utils.py
   - Your CSV file (default: "Titanic-Dataset.csv")
   ```

2. Running the Application:
   ```bash
   python main.py
   ```

3. Basic Operations:
   - **View Data**: Data is automatically displayed in the table upon startup
   - **Add New Row**: 
     1. Click "Add Row"
     2. Fill in the values in the popup window
     3. Click Save
   - **Edit Row**:
     1. Select a row in the table
     2. Click "Edit Row"
     3. Modify values in the popup window
     4. Click Save
   - **Delete Row**:
     1. Select a row in the table
     2. Click "Delete Row"

## Error Handling
The application includes basic error checking:
- Warnings when no row is selected for edit/delete operations
- Automatic data refresh after modifications
- Validation of user actions before processing

## File Handling
- CSV file is read when the application starts
- Changes are immediately written to the CSV file after modifications
- Data integrity is maintained through consistent save operations

## UI Components
1. Main Window:
   - Table display (Treeview)
   - Action buttons panel

2. Edit/Add Dialog:
   - Input fields for each column
   - Save button to commit changes

## Limitations
- Cannot handle very large CSV files efficiently
- No data validation for input fields
- No undo/redo functionality
- No multi-row selection operations

## Best Practices
1. Always select a row before attempting to edit or delete
2. Ensure all required fields are filled when adding/editing rows
3. Wait for operations to complete before starting new ones
