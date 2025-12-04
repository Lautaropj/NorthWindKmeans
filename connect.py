import pyodbc

def obtener_conexion():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=----------;'
        'DATABASE=Northwind;'
        'Trusted_Connection=yes;'
        'TrustServerCertificate=yes;'
    )

