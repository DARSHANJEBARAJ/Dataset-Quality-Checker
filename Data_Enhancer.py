import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox, simpledialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DatasetQualityChecker:
    def __init__(self, root):
        self.root = root
        root.title("Dataset Quality Checker")
        root.configure(bg='#F0F8FF')  # Light blue background

        # Create a custom style for the buttons
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 12, 'bold'), padding=10, background='#ADD8E6', foreground='#333333')
        self.style.map('TButton', background=[('active', '#87CEEB')])

        # Create and place widgets
        self.create_widgets()
        self.df = None
        self.chart_type = 'bar'

    def create_widgets(self):
        # Center the main title
        title_label = ttk.Label(self.root, text="Dataset Quality Checker", font=('Arial', 18, 'bold'), background='#F0F8FF')
        title_label.pack(pady=20)

        # Create a frame to hold the buttons in a grid
        button_frame = ttk.Frame(self.root, style='TFrame')
        button_frame.pack(pady=15)

        # Buttons in a 3x3 grid layout
        button_config = [
            ("Load Dataset", self.load_dataset),
            ("Cleanliness", self.calculate_cleanliness),
            ("Quality Score", self.calculate_quality_score),
            ("Replace Missing", self.replace_missing_values),
            ("Save as Excel", self.save_as_excel),
            ("Plot Charts", self.plot_charts)
        ]

        # Create buttons and place them in a grid
        for i, (text, command) in enumerate(button_config):
            row = i // 3
            col = i % 3
            btn = ttk.Button(button_frame, text=text, command=command)
            btn.grid(row=row, column=col, padx=10, pady=10)

        # Chart type dropdown (placed separately)
        self.chart_type_var = tk.StringVar(value='bar')
        self.chart_type_dropdown = ttk.Combobox(self.root, textvariable=self.chart_type_var, 
                                                 values=['bar', 'line', 'scatter'], 
                                                 state='readonly', width=20)
        self.chart_type_dropdown.pack(pady=15)
        self.chart_type_dropdown.bind("<<ComboboxSelected>>", self.update_chart_type)

        # Labels
        self.result_label = ttk.Label(self.root, text="Cleanliness results will appear here.", 
                                       font=('Arial', 14), background='#F0F8FF')
        self.result_label.pack(pady=15)

        self.quality_score_label = ttk.Label(self.root, text="Quality score will appear here.", 
                                              font=('Arial', 14), background='#F0F8FF')
        self.quality_score_label.pack(pady=15)

        # Frames
        self.chart_frame = ttk.Frame(self.root, relief=tk.RIDGE, borderwidth=1)
        self.chart_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.tree_frame = ttk.Frame(self.root, relief=tk.RIDGE, borderwidth=1)
        self.tree_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Treeview
        self.tree = ttk.Treeview(self.tree_frame)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def update_chart_type(self, event):
        self.chart_type = self.chart_type_var.get()
        self.plot_charts()

    def calculate_cleanliness(self):
        if self.df is None:
            messagebox.showerror("Error", "No dataset loaded.")
            return

        # Calculate missing values and duplicates
        total_cells = self.df.size
        missing_values = self.df.isnull().sum().sum()
        missing_values_percentage = (missing_values / total_cells) * 100

        duplicate_rows = self.df.duplicated().sum()
        duplicate_rows_percentage = (duplicate_rows / self.df.shape[0]) * 100

        # Display cleanliness results
        result_text = f"Missing Values Percentage: {missing_values_percentage:.2f}%\n" \
                      f"Duplicate Rows Percentage: {duplicate_rows_percentage:.2f}%"
        self.result_label.config(text=result_text)

    def calculate_quality_score(self):
        if self.df is None:
            messagebox.showerror("Error", "No dataset loaded.")
            return

        # Calculate missing values and duplicates
        total_cells = self.df.size
        missing_values = self.df.isnull().sum().sum()
        missing_values_percentage = (missing_values / total_cells) * 100

        duplicate_rows = self.df.duplicated().sum()
        duplicate_rows_percentage = (duplicate_rows / self.df.shape[0]) * 100

        # Data type consistency check
        data_type_issues = 0
        for col in self.df.columns:
            if not pd.api.types.is_numeric_dtype(self.df[col]) and not pd.api.types.is_string_dtype(self.df[col]):
                data_type_issues += 1
        data_type_issues_percentage = (data_type_issues / self.df.shape[1]) * 100

        # Calculate overall quality score
        weight_missing_values = 0.4
        weight_duplicates = 0.3
        weight_data_type_issues = 0.3

        quality_score = 100 - (
            (missing_values_percentage * weight_missing_values) +
            (duplicate_rows_percentage * weight_duplicates) +
            (data_type_issues_percentage * weight_data_type_issues)
        )

        # Display quality score
        score_text = f"Overall Quality Score: {quality_score:.2f}%"
        self.quality_score_label.config(text=score_text)

    def load_dataset(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return

        try:
            self.df = pd.read_csv(file_path)
            messagebox.showinfo("Success", "Dataset loaded successfully.")
            self.display_data()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load dataset: {e}")

    def plot_charts(self):
        if self.df is None:
            messagebox.showerror("Error", "No dataset loaded.")
            return

        plt.figure(figsize=(10, 5))

        if self.chart_type == 'bar':
            self.df.isnull().sum().plot(kind='bar')
            plt.title('Missing Values by Column')
        elif self.chart_type == 'line':
            self.df.isnull().sum().plot(kind='line')
            plt.title('Missing Values Over Columns')
        elif self.chart_type == 'scatter':
            self.df.plot(kind='scatter', x=self.df.columns[0], y=self.df.columns[1])
            plt.title('Scatter Plot')

        plt.xlabel('Columns')
        plt.ylabel('Missing Values')
        plt.tight_layout()

        # Clear the chart frame and embed the plot
        self.clear_chart_frame(self.chart_frame)
        fig = plt.gcf()
        canvas = FigureCanvasTkAgg(fig, master=self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def replace_missing_values(self):
        if self.df is None:
            messagebox.showerror("Error", "No dataset loaded.")
            return

        for column in self.df.columns:
            if self.df[column].isnull().any():
                replacement_value = simpledialog.askstring("Input", f"Enter replacement value for missing data in column '{column}':")
                if replacement_value is not None:
                    if pd.api.types.is_numeric_dtype(self.df[column]):
                        try:
                            replacement_value = float(replacement_value)
                        except ValueError:
                            messagebox.showwarning("Warning", f"Invalid input for numeric column '{column}'.")
                            continue
                    elif pd.api.types.is_string_dtype(self.df[column]):
                        replacement_value = str(replacement_value)
                    self.df[column].fillna(replacement_value, inplace=True)

        messagebox.showinfo("Success", "Missing values have been replaced.")
        self.display_data()

    def save_as_excel(self):
        if self.df is None:
            messagebox.showerror("Error", "No dataset loaded.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if not file_path:
            return

        try:
            self.df.to_excel(file_path, engine='openpyxl', index=False)
            messagebox.showinfo("Success", "Dataset saved as Excel file.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save Excel file: {e}")

    def display_data(self):
        if self.df is None:
            messagebox.showerror("Error", "No dataset loaded.")
            return

        # Clear existing Treeview content
        self.tree.delete(*self.tree.get_children())

        # Set up Treeview columns
        self.tree["columns"] = list(self.df.columns)
        self.tree["show"] = "headings"

        # Define column headings
        for col in self.df.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor='w')

        # Insert new data into Treeview
        for _, row in self.df.iterrows():
            self.tree.insert("", "end", values=list(row))

    def clear_chart_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DatasetQualityChecker(root)
    root.mainloop()