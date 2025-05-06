import os
import re
import pandas as pd
from sqlalchemy import create_engine
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Define save path for logs
SAVE_PATH = "C:\\James\\Users\\Documents\\AdventureWorks_Log_Results"
os.makedirs(SAVE_PATH, exist_ok=True)  # Ensure directory exists

# Function to generate next available file version
def get_next_version(prefix, extension):
    """Finds the next available version number for CSV or PDF files."""
    files = [f for f in os.listdir(SAVE_PATH) if f.startswith(prefix) and f.endswith(extension)]
    
    # Use regex to extract numbers at the end of filenames
    versions = [int(re.search(r"_(\d+)\.", f).group(1)) for f in files if re.search(r"_(\d+)\.", f)]
    
    next_version = max(versions) + 1 if versions else 1
    return f"{prefix}_{next_version}{extension}"

# Create SQLAlchemy engine for SQL Server (Windows Authentication)
engine = create_engine("mssql+pyodbc://DESKTOP-FNC2NK0/AdventureWorks2022?trusted_connection=yes&driver=SQL+Server")

# Function to log all data into a **NEW CSV file**
def log_to_csv(dataframe, section_title, filename):
    filepath = os.path.join(SAVE_PATH, filename)
    
    # Append section title before writing data
    with open(filepath, "a") as f:
        f.write(f"\n\n### {section_title} ###\n")
    
    dataframe.to_csv(filepath, mode="a", index=False, header=True)
    print(f"✅ Data logged into {filepath}")

# Function to export all results into a **NEW PDF file**
def export_to_pdf(dataframes, filename):
    filepath = os.path.join(SAVE_PATH, filename)
    doc = SimpleDocTemplate(filepath, pagesize=letter)
    styles = getSampleStyleSheet()

    elements = []

    for section_title, dataframe in dataframes.items():
        # Add section title in bold for separation
        elements.append(Paragraph(f"<b>{section_title}</b>", styles["Title"]))
        elements.append(Spacer(1, 12))  # Space between sections

        if dataframe.empty:
            elements.append(Paragraph("No data available.", styles["Normal"]))
        else:
            # Create table with headers and data rows
            table_data = [list(dataframe.columns)] + dataframe.values.tolist()
            table = Table(table_data)

            style = TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ])
            table.setStyle(style)
            elements.append(table)
        
        elements.append(Spacer(1, 24))  # Space between sections

    doc.build(elements)
    print(f"✅ Results saved as {filepath}")

# Dictionary to store query results for PDF export
results = {}

try:
    # Generate new file names with version numbers
    csv_filename = get_next_version("query_log", ".csv")
    pdf_filename = get_next_version("query_results", ".pdf")

    # 🏆 Customer Analytics
    print("\n🏆 Top Customers by Total Purchase Value")
    query = """SELECT TOP 5 CustomerID, SUM(TotalDue) AS TotalSpent FROM Sales.SalesOrderHeader GROUP BY CustomerID ORDER BY TotalSpent DESC"""
    df_customers = pd.read_sql(query, engine)
    results["Top Customers by Purchase"] = df_customers
    log_to_csv(df_customers, "Top Customers by Purchase", csv_filename)

    # 📦 Monthly Sales Revenue Trends
    print("\n📈 Monthly Sales Revenue")
    query = """SELECT YEAR(OrderDate) AS Year, MONTH(OrderDate) AS Month, SUM(TotalDue) AS Revenue FROM Sales.SalesOrderHeader GROUP BY YEAR(OrderDate), MONTH(OrderDate) ORDER BY Year DESC, Month DESC"""
    df_revenue = pd.read_sql(query, engine)
    results["Monthly Revenue"] = df_revenue
    log_to_csv(df_revenue, "Monthly Revenue", csv_filename)

    # 🏬 Inventory Optimization
    print("\n⚠️ Low Stock Products")
    query = """SELECT TOP 5 p.ProductID, p.Name, pi.Quantity FROM Production.ProductInventory pi JOIN Production.Product p ON pi.ProductID = p.ProductID WHERE pi.Quantity < 5 ORDER BY pi.Quantity ASC"""
    df_low_stock = pd.read_sql(query, engine)
    results["Low Stock Products"] = df_low_stock
    log_to_csv(df_low_stock, "Low Stock Products", csv_filename)

    # 📊 Employee Performance
    print("\n👨‍💼 Best Performing Sales Representatives")
    query = """SELECT TOP 5 SalesPersonID, COUNT(SalesOrderID) AS OrdersHandled FROM Sales.SalesOrderHeader WHERE SalesPersonID IS NOT NULL GROUP BY SalesPersonID ORDER BY OrdersHandled DESC"""
    df_sales_rep = pd.read_sql(query, engine)
    results["Best Sales Reps"] = df_sales_rep
    log_to_csv(df_sales_rep, "Best Sales Reps", csv_filename)

    # 🏷️ Marketing Effectiveness
    print("\n📩 Email Campaign Effectiveness")
    query = """SELECT EmailPromotion, COUNT(BusinessEntityID) AS CustomersReached FROM Person.Person GROUP BY EmailPromotion"""
    df_email_promo = pd.read_sql(query, engine)
    results["Email Campaign Reach"] = df_email_promo
    log_to_csv(df_email_promo, "Email Campaign Reach", csv_filename)

    # 🚀 Export all results to **NEW PDF**
    export_to_pdf(results, pdf_filename)

except Exception as e:
    print("❌ Error:", e)

    #Made change
