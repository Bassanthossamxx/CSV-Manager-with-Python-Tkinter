# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from csv_utils import read_csv, write_csv

CSV_FILE = "Titanic-Dataset.csv"


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

    def load_data(self):
        """Load data into the Treeview."""
        self.tree.delete(*self.tree.get_children())
        for row in self.data:
            self.tree.insert("", "end", values=list(row.values()))

    def add_row(self):
        """Add a new row to the CSV."""
        self.show_edit_window("Add Row")

    def edit_row(self):
        """Edit the selected row."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a row to edit.")
            return

        values = self.tree.item(selected_item, "values")
        self.show_edit_window("Edit Row", values)

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

    def show_edit_window(self, title, values=None):
        """Show a window to add or edit a row."""
        edit_win = tk.Toplevel(self.root)
        edit_win.title(title)

        entries = {}
        for idx, col in enumerate(self.columns):
            ttk.Label(edit_win, text=col).grid(row=idx, column=0, padx=5, pady=5)
            entry = ttk.Entry(edit_win)
            entry.grid(row=idx, column=1, padx=5, pady=5)
            if values:
                entry.insert(0, values[idx])
            entries[col] = entry

        def save():
            row = {col: entry.get() for col, entry in entries.items()}
            if values:
                # Edit existing row
                self.data = [row if list(r.values()) == list(values) else r for r in self.data]
            else:
                # Add new row
                self.data.append(row)

            write_csv(CSV_FILE, self.data, self.columns)
            self.load_data()
            edit_win.destroy()

        ttk.Button(edit_win, text="Save", command=save).grid(row=len(self.columns), column=0, columnspan=2, pady=10)

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

    def filter_data(self):
        """Filter data based on a condition."""
        filter_win = tk.Toplevel(self.root)
        filter_win.title("Filter Data")

        ttk.Label(filter_win, text="Filter Column:").grid(row=0, column=0, padx=5, pady=5)
        column_combo = ttk.Combobox(filter_win, values=self.columns)
        column_combo.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(filter_win, text="Filter Value:").grid(row=1, column=0, padx=5, pady=5)
        filter_entry = ttk.Entry(filter_win)
        filter_entry.grid(row=1, column=1, padx=5, pady=5)

        def perform_filter():
            selected_col = column_combo.get()
            filter_value = filter_entry.get()
            if not selected_col or not filter_value:
                messagebox.showwarning("Incomplete Filter", "Please select a column and enter a value to filter.")
                return

            filtered_rows = [row for row in self.data if filter_value.lower() in row[selected_col].lower()]
            if not filtered_rows:
                messagebox.showinfo("No Matches", "No matching rows found.")
                return

            self.tree.delete(*self.tree.get_children())
            for row in filtered_rows:
                self.tree.insert("", "end", values=list(row.values()))

        ttk.Button(filter_win, text="Filter", command=perform_filter).grid(row=2, column=0, columnspan=2, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = CSVManagerApp(root)
    root.mainloop()
