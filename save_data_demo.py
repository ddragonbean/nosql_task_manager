from tinydb import TinyDB, Query

db = TinyDB('db.json')
table = db.table('my_table', cache_size = 30)
# for i in range(1000):
# 	table.insert({'name':'Alex', 'index': i})
Query = Query()
QueryUser = Query({'index':988})
QueryProduct = Query()
# db.insert({'name':'John', 'age':30})

# print(123)

result = db.search(Query.name == 'John')
print(result)


result = table.search(IndexQuery.index == 877)
print(result)