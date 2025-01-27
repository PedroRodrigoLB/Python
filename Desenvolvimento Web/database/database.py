import os
from peewee import PostgresqlDatabase
from dotenv import load_dotenv
load_dotenv()


database_uri = os.getenv('DATABASE_URL','') 

db = PostgresqlDatabase(database_uri)

