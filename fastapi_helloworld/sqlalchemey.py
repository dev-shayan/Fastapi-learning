from sqlalchemy import create_engine, Engine, text , MetaData, Table, Column, String
from sqlalchemy.exc import SQLAlchemyError


DATABASE_URL = "postgresql://Shayandb_owner:VjURFkui4AE5@ep-tiny-bar-a1fduq6l-pooler.ap-southeast-1.aws.neon.tech/practice?sslmode=require"

engine: Engine = create_engine(DATABASE_URL)

# with engine.connect() as connection:
#     result = connection.execute(text("select 'Hello world!'"))
#     print(result.scalar())


#MetaData is used to organize and manage database table definitions, and to issue SQL commands to the database to create those tables.
# metadata = MetaData()

# table1 = Table(
#    'table1', metadata, 
#    Column('x', String),
# )

# metadata.create_all(engine)

# with engine.begin() as connection:
#     result = connection.execute(text("INSERT INTO table1 (x) VALUES (:x)"), [{ "x": "Hello Dunya!"},{ "x": "Hello World!"},{ "x": "Hello jannat!"}])
#     print("Insert operation completed successfully.")

# with engine.connect() as connection:
#     result = connection.execute(text("SELECT * FROM table1 WHERE x = :x"), dict(x="Hello Dunya!"))
#     print("Fetch operation completed successfully.")
#     # print(f"Result: {result}")
#     print(f"Result: {result.all()}")


try:
    with engine.connect() as connection:
        # Start a transaction
        with connection.begin():
            result = connection.execute(text("DELETE FROM table1"))
            print("Delete operation completed successfully.")
            print(f"Result: {result.rowcount} rows deleted.")
except Exception as e:
    print(f"An error occurred: {str(e)}")