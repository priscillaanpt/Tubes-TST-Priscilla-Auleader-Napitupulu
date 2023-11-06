from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

DATABASE_URL = "postgresql://user:password@localhost/dbname"
engine = create_engine(DATABASE_URL)


DATABASE_PASSWORD = "Jeremypanjaitan03"
ENCODED_PASSWORD = quote_plus(DATABASE_PASSWORD)

DATABASE_URL = f"postgresql://priscillaaldr:{ENCODED_PASSWORD}@womencloth.postgres.database.azure.com:5432/WomenCloth_db?sslmode=require"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()