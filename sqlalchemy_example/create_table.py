from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///example.db', echo=True)

conn = engine.connect()

metadata = MetaData()

User = Table('users', metadata,
             Column('id', Integer(), primary_key=True),
             Column('name', String(255), nullable=False),
             Column('age', Integer(), nullable=False))

metadata.create_all(engine)

conn.close()