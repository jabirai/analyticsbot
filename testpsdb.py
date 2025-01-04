from sqlalchemy import create_engine, text

dburi = "mssql+pyodbc://sa:password123#@localhost:1433/BikeStores?driver=ODBC+Driver+17+for+SQL+Server"

try:
    engine = create_engine(dburi)

    with engine.connect() as connection:
        print("Connected to the database successfully!")
        result = connection.execute(text("SELECT * FROM production.products;"))
        rows = result.fetchall()
        for row in rows:
            print(row)
 
except Exception as e:
    print(f"Failed to connect to the database.")
