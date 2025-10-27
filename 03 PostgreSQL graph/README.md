# SQL Learning - 02 PostgreSQL Graph


## Scenario: Demonstrating Graph-like Behavior in PostgreSQL Using BFS

In this example, we explore how PostgreSQL can simulate graph-like operations using tables to represent **nodes** and **edges**. We model a small logistics network as a graph, where locations such as factories, warehouses, stores, and distribution hubs are nodes, and the connections (routes) between them are edges.

The scenario includes:
1. **Nodes (Locations):** 
   Locations like "Factory A," "Warehouse B," and "Retail Center G."
2. **Edges (Routes):** 
   Connections between locations, such as "Factory A → Warehouse B."

To analyze this network, we use **Breadth-First Search (BFS)** to traverse from a starting node (e.g., Factory A) and explore connections level by level. This simulates how goods might flow through a supply chain or how information propagates in a network.

### Key Features
1. **Node and Edge Representation:** 
   Nodes are stored in a `locations` table, and edges are stored in a `routes` table with attributes like distance and cost.
2. **Recursive CTE for BFS:** 
   We leverage PostgreSQL's recursive queries to explore connected nodes, tracking the traversal level and connections dynamically.
3. **Application Example:** 
   This setup can represent real-world problems like finding optimal routes, modeling dependencies, or visualizing network relationships.

By running the BFS query, we can analyze the graph-like structure and gain insights, all within the relational database paradigm. This demonstrates how PostgreSQL can handle graph-like problems without needing specialized graph database tools.


## how to run this
```
docker compose build
docker compose up -d
docker compose exec py2db python create_graph.py
docker compose exec py2db python data_insertion.py
docker compose exec py2db python bfs_query.py
```
