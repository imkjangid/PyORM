from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine('sqlite:///example.db')

conn = engine.connect()

metadata = MetaData()

User = Table('users', metadata, autoload_with=engine)

records = conn.execute(select(User)).fetchall()

print(records)

conn.close()