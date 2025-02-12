import pandas as pd
import matplotlib.pyplot as plt
import os
from fpdf import FPDF

def read_data(file_path):
#Reading the csv file and performing the exception handling
    try:
        return pd.read_csv(file_path, encoding='utf-8', on_bad_lines='skip')
    except UnicodeDecodeError:
        return pd.read_csv(file_path, encoding='ISO-8859-1', on_bad_lines='skip')

def analyze_data(df):
#Generating summary statistics of the dataset
    return df.describe(include='all')

def generate_charts(df, output_dir):
#Creating histograms for numerical columns and saving them as images
    charts = []
    for column in df.select_dtypes(include=['number']).columns:
        plt.figure()
        df[column].plot(kind='hist', title=f'Distribution of {column}')
        chart_path = os.path.join(output_dir, f"{column}_chart.png")
        plt.savefig(chart_path)
        plt.close()
        charts.append(chart_path)
    return charts

def generate_pdf_report(summary, charts, output_path):
#Generating Pdf report incuding everything
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Automated Data Analysis Report", ln=True, align='C')
    pdf.ln(10)

# Adding summary statistics
    for col in summary.columns:
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(0, 10, f"Column: {col}", ln=True)
        pdf.set_font("Arial", size=10)
        for stat in summary.index:
            value = summary.loc[stat, col]
            pdf.cell(0, 8, f"{stat}: {value}", ln=True)
        pdf.ln(5)

# Adding charts
    for chart in charts:
        pdf.add_page()
        pdf.image(chart, x=10, y=20, w=180)

    pdf.output(output_path)

def main():
#Main function to handle file selection and report generation."""
    input_file = input("Enter the path of the CSV file: ").strip()
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist. Please check the path and try again.")
        return
    
    output_dir = os.path.dirname(input_file)  # Get the directory of the input file
    output_file = os.path.join(output_dir, "report.pdf")

    try:
        data = read_data(input_file)
        summary = analyze_data(data)
        charts = generate_charts(data, output_dir)
        generate_pdf_report(summary, charts, output_file)
        print(f"Report generated successfully: {output_file}")
    except pd.errors.ParserError as pe:
        print(f"Parsing error: {pe}. Check if the CSV file has inconsistent rows.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
