**Dataset Quality Checker - README**
Overview
The Dataset Quality Checker is a graphical user interface (GUI) application built using Tkinter for data exploration and cleaning. It is designed to help users analyze the quality of datasets in CSV format by calculating cleanliness and quality scores, displaying data insights, handling missing values, and plotting various charts.

Features
Load Dataset: Load a CSV file to analyze its contents.
Cleanliness: Check and display the percentage of missing values and duplicate rows.
Quality Score: Calculate and display a quality score based on missing values, duplicate rows, and data type consistency.
Replace Missing Values: Replace missing values in the dataset with user-specified values.
Save as Excel: Save the cleaned dataset as an Excel (.xlsx) file.
Plot Charts: Visualize the dataset's missing values with different types of plots (Bar, Line, Scatter).
Requirements
To run this application, you will need to install the following libraries:

Tkinter (for the GUI)
Pandas (for data manipulation)
Matplotlib (for chart plotting)
openpyxl (for saving Excel files)
You can install the necessary Python packages by running:

bash
Copy
pip install pandas matplotlib openpyxl
Note: Tkinter is generally bundled with Python, but you may need to install it separately depending on your environment.

How to Use
Launch the Application: Run the script, and the GUI window will open.

Load Dataset:

Click the "Load Dataset" button to open a file dialog.
Select a CSV file from your computer to load.
Check Cleanliness:

Click the "Cleanliness" button to calculate and display the percentage of missing values and duplicate rows in the dataset.
Check Quality Score:

Click the "Quality Score" button to calculate and display an overall quality score based on missing values, duplicates, and data type consistency.
Replace Missing Values:

Click the "Replace Missing" button to replace missing values in the dataset. For each column with missing data, you will be prompted to enter a replacement value.
Save as Excel:

Click the "Save as Excel" button to save the dataset as an Excel file.
Plot Charts:

Select the type of chart (Bar, Line, or Scatter) from the dropdown menu.
Click the "Plot Charts" button to visualize missing values across columns.
View Data:

The dataset will be displayed in a table format within the GUI for easy viewing and inspection.
User Interface Overview
Main Title: Displays the name of the application.
Buttons: The following actions are available via buttons:
Load Dataset
Cleanliness
Quality Score
Replace Missing
Save as Excel
Plot Charts
Chart Type Dropdown: Select the chart type for visualizing missing data (Bar, Line, or Scatter).
Result Labels: Shows cleanliness results and quality score information.
Data Table: Displays the dataset in a table format using a Treeview widget.
Example Workflow
Load a CSV dataset by clicking "Load Dataset".
Click "Cleanliness" to see the percentage of missing values and duplicate rows.
Click "Quality Score" to get an overall quality score based on data integrity.
If necessary, replace missing values by clicking "Replace Missing" and entering a value for each column.
Save the cleaned dataset by clicking "Save as Excel".
Visualize missing data by selecting a chart type from the dropdown and clicking "Plot Charts".
Code Breakdown
DatasetQualityChecker Class: The main class that handles the entire GUI and logic.
__init__(self, root): Initializes the main window and sets up the GUI.
create_widgets(): Creates all the necessary widgets such as buttons, labels, and frames.
load_dataset(): Loads a CSV file into a DataFrame using pandas.
calculate_cleanliness(): Calculates missing values and duplicates in the dataset.
calculate_quality_score(): Computes a quality score based on missing values, duplicates, and data type consistency.
replace_missing_values(): Prompts the user to replace missing values in the dataset.
save_as_excel(): Saves the cleaned dataset as an Excel file.
plot_charts(): Plots the selected chart type to visualize missing data.
display_data(): Displays the dataset in a Treeview widget.
clear_chart_frame(): Clears the previous plot before displaying a new one.
Known Issues
The current implementation only supports CSV files for loading datasets.
Some complex datasets (e.g., with mixed data types in a single column) may require additional handling for data type consistency.
Future Enhancements
Support for more file formats (e.g., Excel, JSON).
Advanced data cleaning functions (e.g., outlier detection, normalization).
Better handling of data type inconsistencies (e.g., automatic type conversion).
Export cleaned dataset with better options (e.g., user-defined column filtering)
