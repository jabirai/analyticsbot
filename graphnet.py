import networkx as nx
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, inspect
from dotenv import dotenv_values
vars = dotenv_values(".env")


def extract_database_metadata(database_url, schema):
    """Extracts database metadata using SQLAlchemy."""
    engine = create_engine(database_url)
    inspector = inspect(engine)

    metadata = {}

    # Extract tables and their columns
    tables = inspector.get_table_names(schema=schema)
    for table in tables:
        columns = inspector.get_columns(table, schema=schema)
        foreign_keys = inspector.get_foreign_keys(table, schema=schema)

        metadata[table] = {
            "columns": [col["name"] for col in columns],
            "foreign_keys": [
                {"column": fk["constrained_columns"][0], "ref_table": fk["referred_table"],
                    "ref_column": fk["referred_columns"][0]}
                for fk in foreign_keys
            ],
        }
    return metadata


def create_database_graph(metadata):
    """Creates a graph from the database metadata."""
    graph = nx.DiGraph()  # Use DiGraph for directed relationships

    for table, details in metadata.items():
        graph.add_node(table)  # Add table as a node

        # Add edges for foreign key relationships
        for fk in details["foreign_keys"]:
            graph.add_edge(
                table, fk["ref_table"], label=f"{fk['column']} -> {fk['ref_column']}")

    return graph


def visualize_graph(graph):
    """Visualizes the graph using Matplotlib."""
    pos = nx.spring_layout(graph)  # Layout for better visualization
    plt.figure(figsize=(12, 8))

    # Draw nodes and edges
    nx.draw_networkx_nodes(graph, pos, node_size=2000, node_color="lightblue")
    nx.draw_networkx_edges(graph, pos, arrowstyle="->", arrowsize=20)
    nx.draw_networkx_labels(graph, pos, font_size=10, font_weight="bold")

    # Draw edge labels for foreign key relationships
    edge_labels = nx.get_edge_attributes(graph, "label")
    nx.draw_networkx_edge_labels(
        graph, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Database Schema Graph", fontsize=16)
    plt.axis("off")
    plt.show()


# Example usage
if __name__ == "__main__":
    metadata = extract_database_metadata(vars['db_uri'], schema='production')
    graph = create_database_graph(metadata)
    visualize_graph(graph)
