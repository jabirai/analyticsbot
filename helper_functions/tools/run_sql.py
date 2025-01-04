from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
import pandas as pd
from langchain.tools import BaseTool
from sqlalchemy import create_engine


class SQLSchema(BaseModel):
    sql_code: str = Field(description="MUST be valid SQL code.")
    file_name: str = Field(
        description="A unique file name for the data to be saved to.")
    dburi: str = Field(
        description="The URI of the database you need to connect to. This is found in the hierarchy."
    )


class RunSQL(BaseTool):  # Class names should follow PascalCase by convention
    name: str = "run_sql_tool"
    description: str = (
        "This tool is used to run generated SQL code against a database. "
        "It requires SQL code as the input. Aim to format the SQL code nicely with whitespace and line breaks."
    )

    db_connection:str = ""

    args_schema: type = SQLSchema  # Ensure the args_schema is correctly typed
    return_direct: bool = False

    def __init__(self, db_connection: str):
        super().__init__()  # Ensure the parent class is properly initialized
        self.db_connection = db_connection

    def _run(self, sql_code: str, file_name: str, dburi: str):
        """
        Executes the given SQL code against the specified database URI and saves the results.

        Args:
            sql_code (str): The SQL code to execute.
            file_name (str): The name of the file to save the results.
            dburi (str): The database URI.

        Returns:
            dict: A dictionary containing the file path, columns, and data, or an error message.
        """
        # Step 1: Connect to the database
        try:
            engine = create_engine(dburi)
            connection = engine.connect()
        except Exception as e:
            return {
                "error": (
                    f"You have tried to connect to a database that doesn't exist. "
                    f"Ensure you are using one of the URIs from the prompt. Error: {e}"
                )
            }

        # Step 2: Run the SQL query and save results
        try:
            data = pd.read_sql_query(sql_code, connection)
            # Save SQL code
            with open("./output_data/sql_code.sql", "w") as f:
                f.write(sql_code)

            # Save the returned data
            data_directory = f"./output_data/{file_name}.csv"
            data.to_csv(data_directory, index=False)

            return {
                "data_directory": data_directory,
                "columns": list(data.columns),
                # Limit the returned data to avoid token limits
                "data": data.head(100).to_dict(),
            }
        except Exception as e:
            return {
                "error": (
                    f"An error occurred. You are probably calling a table or schema that does not exist. "
                    f"Ensure you are referencing real tables and avoid querying the same column as before. Error: {e}"
                )
            }

    def _arun(self, *args, **kwargs):
        raise NotImplementedError(
            "Async execution is not supported for this tool.")
