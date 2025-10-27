# SQL Learning

This project is a set of exercises for learning SQL with PostgreSQL. It includes examples of creating databases, tables, inserting data, and querying information using PostgreSQL, all executed in a Docker environment with Python scripts.

## 01 Hello PostgreSQL

.env like
```
POSTGRES_USER=your_usr
POSTGRES_PASSWORD=your_pwd
POSTGRES_DB=your_db
```
starting services
```
docker compose up
```

connect db
```
docker compose exec backend python src/01/main.py
```

leave
```
docker compose down
```

* related files:
    * ```.env```
    * Dockerfile
    * docker-compose.yml
    * requirements.txt
    * ```src/model/__init__.py```
    * ```src/model/db.py```
    * ```src/01/main.py```


## 02 Add Tables

This scenario creates a simple library management system with tables for authors, books, members, and borrowing history. It provides a basic structure for managing library data.


docker compose exec py2db python library/create_library.py
docker compose exec py2db python library/data_insertion.py
docker compose exec py2db python library/top5.py

## Basic Hello World SQL

This section started with running SQL queries in a PostgreSQL database using Python.

```
docker compose build
docker compose up -d
docker compose exec py2db python app.py
docker compose exec py2db python create.py
docker compose exec py2db python add.py
docker compose exec py2db python print_all.py
```
## 03 CRUD

```
## Scenario: E-Commerce Database for a Company

This scenario simulates an e-commerce platform with customers, orders, products, payments, and reviews. It allows you to manage orders, products, customer details, and payments.

```
docker compose exec py2db python eCommerce/create_store.py
docker compose exec py2db python eCommerce/data_insertion.py
docker compose exec py2db python eCommerce/query.py
```