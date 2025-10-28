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
docker compose exec backend python -m src.01.hello
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
    * ```src/01/*.py```

## 02 Add Tables

This scenario creates a simple library management system with tables for authors, books, members, and borrowing history. It provides a basic structure for managing library data.

```
docker compose exec backend python -m src.02.create
docker compose exec backend python -m src.02.insertion
docker compose exec backend python -m src.02.top5
docker compose exec backend python -m src.02.clean
```

* related files:
    * ```src/02/*.py```


## 03 CRUD

make SQL interface wrap as crud functions

```
docker compose exec backend python -m src.03.crud

```

* related files:
    * ```src/model/library_crud.py```
    * ```src/03/*.py```

