import os
import sqlalchemy as sa

server = os.environ.get("POSTGRES_SERVER")
database = os.environ.get("POSTGRES_DB")
username = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")

if server is None or database is None or username is None or password is None:
    raise ValueError('Missing environment variables')

connection_string = f"postgresql+psycopg2://{username}:{password}@{server}/{database}"

def get_sa_engine():
    return sa.create_engine(connection_string)