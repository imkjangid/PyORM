from sqlalchemy import create_engine, insert, Table, MetaData

engine = create_engine('sqlite:///example.db', echo=True)

conn = engine.connect()
User = Table('users', MetaData(), autoload_with=engine)

insert_many = insert(User)

values_list = [{'id':'2', 'name':'Nisha', 'age': 28},
              {'id':'3', 'name':'Nikunj', 'age': 22},
              {'id':'4', 'name':'Arjun', 'age': 30}]

result = conn.execute(insert_many, values_list)

conn.commit()
print(f"{result.rowcount} records inserted.")

conn.close()