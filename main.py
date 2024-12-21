# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from csv_utils import read_csv, write_csv

# Configuration
CSV_FILE = "Titanic-Dataset.csv"


class CSVManagerApp:
	def __init__(self, root):
		self.root = root
		self.root.title("CSV File Manager")

		# Load initial data and column names from CSV file
		self.data, self.columns = read_csv(CSV_FILE)
		if not self.columns:
			self.columns = ["Column1", "Column2", "Column3"]

		# Set up the main data display using Treeview
		self._setup_treeview()

		# Create the button panel
		self._create_button_panel()

		# Load initial data into the display
		self.load_data()

	def _setup_treeview(self):
		self.tree = ttk.Treeview(self.root, columns=self.columns, show="headings")
		for col in self.columns:
			self.tree.heading(col, text=col)
			self.tree.column(col, width=100)
		self.tree.pack(fill="both", expand=True)

	def _create_button_panel(self):
		btn_frame = ttk.Frame(self.root)
		btn_frame.pack(fill="x")

		buttons = [
			("Add Row", self.add_row),
			("Edit Row", self.edit_row),
			("Delete Row", self.delete_row)
		]

		for text, command in buttons:
			ttk.Button(btn_frame, text=text, command=command).pack(
				side="left", padx=5, pady=5
			)

	def load_data(self):
		self.tree.delete(*self.tree.get_children())
		for row in self.data:
			self.tree.insert("", "end", values=list(row.values()))

	def add_row(self):
		self.show_edit_window("Add Row")

	def edit_row(self):
		selected_item = self.tree.selection()
		if not selected_item:
			messagebox.showwarning("No Selection", "Please select a row to edit.")
			return

		values = self.tree.item(selected_item, "values")
		self.show_edit_window("Edit Row", values)

	def delete_row(self):
		selected_item = self.tree.selection()
		if not selected_item:
			messagebox.showwarning("No Selection", "Please select a row to delete.")
			return

		values = self.tree.item(selected_item, "values")
		self.data = [row for row in self.data if list(row.values()) != list(values)]
		write_csv(CSV_FILE, self.data, self.columns)
		self.load_data()

	def show_edit_window(self, title, values=None):
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
				self.data = [row if list(r.values()) == list(values) else r for r in self.data]
			else:
				self.data.append(row)

			write_csv(CSV_FILE, self.data, self.columns)
			self.load_data()
			edit_win.destroy()

		ttk.Button(edit_win, text="Save", command=save).grid(
			row=len(self.columns), column=0, columnspan=2, pady=10
		)


if __name__ == "__main__":
	root = tk.Tk()
	app = CSVManagerApp(root)
	root.mainloop()