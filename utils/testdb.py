from sqlalchemy import create_engine, text
from dotenv import dotenv_values
import os

vars = dotenv_values(".env")
dburi = vars['db_uri']

try:
    engine = create_engine(dburi)
    with engine.connect() as connection:
        print("Connected to the database successfully!")
        
except Exception as e:
    print(f"Failed to connect to the database.")
