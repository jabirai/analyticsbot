# script to generate hierarchy of databases supplied by a given config file
from DBconnector import DBConnector

db_connector = DBConnector()
hierarchy = db_connector.get_schema_hierarchy()

with open("./configs/hierarchy.txt", "w") as f:
    f.write(hierarchy)
