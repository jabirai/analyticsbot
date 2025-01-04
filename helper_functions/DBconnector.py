from helper_functions.get_credentials import get_credentials
from sqlalchemy import create_engine
import sqlalchemy
import io


class DBConnector:
    def __init__(self):
        self.get_credentials_object = get_credentials()
        self.db_details = self.get_credentials_object.get_db_conn()
    def get_schema_hierarchy(self):
        output_stream = io.StringIO()
        for db, details in self.db_details.items():
            uri = details["uri"]
            schemas = details["schemas"]
            self.engine = create_engine(uri)
            self.inspector = sqlalchemy.inspect(self.engine)

            db_hierarchy = {}

            schema_hierarchy = {}
            # table_names = self.inspector.get_table_names(schema=schema)
            for schema, tables in schemas.items():
                table_names = tables
                col_details = [
                    self.inspector.get_columns(schema=schema, table_name=table)
                    for table in table_names
                ]
                schema_hierarchy[schema] = {
                    table: col for table, col in zip(table_names, col_details)
                }
            db_hierarchy[uri] = schema_hierarchy
            # Create a StringIO object to capture the output, i.e this is the string we paste into the prompt.
            for db in db_hierarchy.keys():
                output_stream.write(f"- {db}\n")
                for schema in db_hierarchy[db].keys():
                    output_stream.write(f"   - {schema}\n")
                    for table in db_hierarchy[db][schema].keys():
                        output_stream.write(f"      - {table}\n")
                        for column in db_hierarchy[db][schema][table]:
                            output_stream.write(
                                f'         - {column["name"]}, {column["type"]}\n'
                            )
            output_stream.write("\n")
        hierarchy = output_stream.getvalue()
        output_stream.close()
        return hierarchy
