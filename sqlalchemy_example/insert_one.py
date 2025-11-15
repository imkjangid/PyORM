from sqlalchemy import create_engine, insert, Table, MetaData

engine = create_engine('sqlite:///example.db', echo=True)

conn = engine.connect()
User = Table('users', MetaData(), autoload_with=engine)
insert_one = insert(User).values(id=1, name='Rahul', age=35)

result = conn.execute(insert_one)
conn.commit()
print(result.inserted_primary_key)