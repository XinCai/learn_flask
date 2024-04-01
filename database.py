import pyodbc
import pandas as pd

# Insert your connection string here
conn_str = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:db-server-demo-2024.database.windows.net,1433;Database=flask-tutorial;Uid=learndatabase;Pwd=Caixin2023!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"


# Establish a connection
conn = pyodbc.connect(conn_str)

# Create a cursor
cursor = conn.cursor()

# Execute SQL queries
cursor.execute("SELECT * FROM Employees;")

# Fetch the results
results = cursor.fetchall()

# Convert results to a pandas DataFrame
df = pd.DataFrame(results)

print(df)

# Close the cursor and connection
cursor.close()
conn.close()


# -- Create a new database
# CREATE DATABASE SampleDB;

# -- Use the new database
# USE SampleDB;

# -- Create a new table
# CREATE TABLE Employees (
#     ID INT PRIMARY KEY,
#     Name NVARCHAR(50),
#     Position NVARCHAR(50),
#     Department NVARCHAR(50)
# );

# -- Insert some sample data
# INSERT INTO Employees (ID, Name, Position, Department) VALUES
# (1, 'John Doe', 'Manager', 'Sales'),
# (2, 'Jane Smith', 'Sales Representative', 'Sales'),
# (3, 'Mike Johnson', 'Developer', 'IT'),
# (4, 'Alice Williams', 'System Administrator', 'IT');


# ======================


# Prerequisites
# An Azure subscription.
# An Azure SQL database configured with Microsoft Entra authentication. You can create one using the Create database quickstart.
# The latest version of the Azure CLI.
# Visual Studio Code with the Python extension.
# Python 3.8 or later. If you're using a Linux client machine, see Install the ODBC driver.

# https://learn.microsoft.com/en-us/azure/azure-sql/database/azure-sql-python-quickstart?view=azuresql&tabs=windows%2Csql-inter

# ==========================