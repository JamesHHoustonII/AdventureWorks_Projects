This project focuses on data analysis and reporting automation using Python and Microsoft SQL Server (MSSQL). The script extracts, processes, and exports data into both CSV and PDF reports, enabling structured analysis for business intelligence.

 Key Features
- Data Extraction & Querying: Connects to an MSSQL database using SQLAlchemy, executing queries on AdventureWorks datasets.
- Data Transformation: Cleans, formats, and structures raw SQL results into pandas DataFrames for further analysis.
- Automated Logging: Saves query results to CSV files, appending structured sections to maintain an evolving log.
- PDF Report Generation: Converts results into formatted tables within PDF reports, making key data points easy to share.
- Versioning System: Ensures each log and report file receives a unique version number, preventing overwrites and tracking historical results.
- Modular Functions: Uses reusable functions to handle logging, reporting, and version management efficiently.
- Business Insights: Queries target customer analytics, revenue trends, inventory levels, employee performance, and marketing effectiveness, offering valuable insights into business operations.

 How It Works
1. Data Retrieval: Executes queries to analyze customer spending patterns, revenue trends, inventory shortages, and employee sales performance.
2. Logging & Saving: Stores query results in a new CSV file, appending structured headers for clarity.
3. PDF Report Generation: Converts datasets into tables, applying text styling and formatting, then exports to a new PDF report.
4. Automation & Error Handling: Ensures directory creation, manages output files, and captures exceptions for debugging.

This project demonstrates real-world data engineering techniques, integrating database management, Python scripting, and report automation to streamline analytics workflows.
Let me know if you need any modifications or additional details!


Data Analytics for Each Query


 1. Top Customers by Purchase
- CustomerID 29818: $989,184.08  
- CustomerID 29715: $961,675.86  
- CustomerID 29722: $954,021.92  
- CustomerID 30117: $919,801.82  
- CustomerID 29614: $901,346.85  

 2. Monthly Revenue
- June 2014: $54,151.48  
- May 2014: $6,006,183.21  
- April 2014: $1,985,886.15  
- March 2014: $8,097,036.31  
- February 2014: $1,478,213.29  
- January 2014: $4,798,027.87  
- December 2013: $4,560,577.09  
- November 2013: $3,694,667.99  
- October 2013: $5,374,375.94  
- September 2013: $5,083,505.34  

 3. Low Stock Products
- ProductID 853: Women's Tights, M (Quantity: 0)  
- ProductID 859: Half-Finger Gloves, M (Quantity: 0)  
- ProductID 876: Hitch Rack - 4-Bike (Quantity: 0)  
- ProductID 882: Short-Sleeve Classic Jersey, M (Quantity: 0)  
- ProductID 494: Paint - Silver  

 4. Best Sales Representatives
- SalesPersonID 277: 473 Orders  
- SalesPersonID 275: 279 Orders  
- SalesPersonID 450: 429 Orders  
- SalesPersonID 4: 276 Orders  
- SalesPersonID 289: 418 Orders  

 5. Email Campaign Reach
- No Email Promotion: 11,158 Customers Reached  
- Promotion Level 1: 5,044 Customers Reached  
- Promotion Level 2: 377 Customers Reached  






