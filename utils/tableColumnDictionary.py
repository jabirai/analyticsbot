import json
from sqlalchemy import create_engine, inspect
from dotenv import dotenv_values
vars = dotenv_values(".env")


def extract_table_column_mapping_all_schemas(database_url):
    engine = create_engine(database_url)
    inspector = inspect(engine)
    schema_table_column_mapping = {}
    schemas = inspector.get_schema_names()

    for schema in schemas:
        schema_table_column_mapping[schema] = {}
        tables = inspector.get_table_names(schema=schema)
        for table in tables:
            columns = inspector.get_columns(table, schema=schema)
            schema_table_column_mapping[schema][table] = [
                column['name'] for column in columns]

    return schema_table_column_mapping


if __name__ == "__main__":
    schema_table_column_mapping = extract_table_column_mapping_all_schemas(
        vars['db_uri'])
    with open('metadata.json', 'w') as file:
        json.dump(schema_table_column_mapping, file)
        file.close()
