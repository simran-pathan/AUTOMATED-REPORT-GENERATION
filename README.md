# AUTOMATED-REPORT-GENERATION
COMPANY: CODTECH IT SOLUTIONS

NAME: SIMRAN AYUBKHAN PATHAN

INTERN ID: CT08KSV

DOMAIN: PYTHON

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

*CODE EXPLANATION*:
This Python script automates data analysis and report generation for a given CSV file. It reads the data, performs statistical analysis, creates visualizations, and compiles everything into a PDF report. Below is a breakdown of the key components:

Importing Required Libraries
pandas: Handles data manipulation and statistical analysis.
matplotlib.pyplot: Generates histograms for data visualization.
os: Manages file handling and directory operations.
fpdf: Creates and formats the final PDF report.

Reading the CSV File (read_data(file_path))
Reads a CSV file with UTF-8 encoding.
If a UnicodeDecodeError occurs, it retries with "ISO-8859-1" encoding.
on_bad_lines='skip' ensures that malformed rows do not cause failure.

Analyzing the Data (analyze_data(df))
Uses df.describe(include='all') to generate summary statistics.
Provides count, mean, min, max, and unique values for all columns.

Generating Charts (generate_charts(df, output_dir))
Loops through all numerical columns and creates histograms.
Saves each chart as a .png file in the output directory.

Creating the PDF Report (generate_pdf_report(summary, charts, output_path))
Adds a title page labeled Automated Data Analysis Report.
Iterates through each column’s summary statistics and writes them into the report.
Inserts generated charts as separate pages in the PDF.

Main Execution (main())
Prompts the user to enter the CSV file path.
Checks if the file exists before proceeding.
Calls all functions to read, analyze, visualize, and generate the final PDF report.

*OUTPUT*
CSV file used for making the report:
[Feedback.csv](https://github.com/user-attachments/files/18771601/Feedback.csv)

Report generated:
