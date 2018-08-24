"""
座右铭:将来的你一定会感激现在拼命的自己
@project:正课
@author:Mr.Chen
@file:MongoDB的基本使用.PY
@ide:PyCharm
@time:2018-08-22 10:50:47
"""
import pymongo
# 第一步链接MongoDB
# 创建MongoDB的连接对象
client = pymongo.MongoClient(host="localhost",port=27017)
#第二步：指定数据库(相当于是创建一个数据库)
db = client.test
# 第三步：指定集合（创建数据库中的表）
collection = db.students

# 插入数据
student={
    "id":"20180801",
    "name":"张三",
    "age":"20",
    "sex":"male"
}
# result = collection.insert(student)
# print(result)
student1={
    "id":"20180802",
    "name":"李四",
    "age":"22",
    "sex":"famle"
}
student2={
    "id":"20180801",
    "name":"王五",
    "age":"34",
    "sex":"male"
}
student3={
    "id":"20180804",
    "name":"麻子",
    "age":"18",
    "sex":"male"
}
student4={
    "id":"20180805",
    "name":"小丽",
    "age":"19",
    "sex":"male"
}
student5={
    "id":"20180806",
    "name":"小王里",
    "age":"25",
    "sex":"male"
}
# 插入数据
# result = collection.insert([student1, student2])
# print(result)
# result = collection.insert_many([student3, student4, student5])
# print(result)
# result = collection.insert_one(student1, student2)
# print(result)

# 查询数据
# result = collection.find_one({'name':'王五'})
# print(result)
#
# from bson.objectid import ObjectId
# result1 = collection.find_one({'_id':ObjectId('5b7cdabbfc68e41c1011734f')})
# print(result1)

# result_2 = collection.find({"sex":"male"})
# print(result_2)
# for res in result_2:
#     print(res)


# result3 = collection.find_one({"age":{"$gt":"20"}})
# print(result3)

# result4 = collection.find_one({"age":{"$gt":'22'}})
# print(result4)
# result4 = collection.find({"age":{"$gt":'19'}})
# print(result4)
# for res in result4:
#     print(res)

# result_5 = collection.find_one({"name":{"$regex":"^麻"}})
# print(result_5)


# 修改数据
# condition={"name":"小王里"}
# student7 = collection.find_one(condition)
# print(student7)
# student7["age"]=500
# result = collection.update(condition,{"$set":student7})
# print(result)

# result8 = collection.update({"name":"小丽"},{"$set":{"sex":"m"}})
# result9 = collection.update({"name":"张三"},{"$set":{"score":"99.9"}})
# print(result9)

# result10 = collection.update_one({"name":"王五"},{"$set":{"sex":"qq"}})
# print(result10.matched_count,result10.modified_count)

# result11 = collection.update_many({"name":"张三"},{"$set":{"sex":"gong"}})
# print(result11.matched_count, result11.modified_count)

# result12 = collection.insert_one({"name":"小白","age":20,"sex":"male"})
# print(result12)
# result12 = collection.update_many({"age":{"$gt":19}},{"$inc":{"age":1}})
# print(result12.matched_count, result12.modified_count)

# 删除
# result14 = collection.remove({"name":"小白"})
# print(result14)
# result15 = collection.delete_one({"name":"李四"})
# print(result15)

# result16 = collection.delete_many({"name":"张三"})
# print(result16)
# print(result16.deleted_count)

# 计数
# result17 = collection.find().count()
# print(result17)
# result18 = collection.find({"age":"20"}).count()
# print(result18)

# 排序
# result19 = collection.find().sort("name",pymongo.ASCENDING)
# print([result["name"] for result in result19])

# 偏移:在某些情况下，我们可能想只取某几个元素，这时可以利用skip()方法偏移几个位置，比如偏移2，就忽略前两个元素，得到第三个及以后的元素
# result20 = collection.find().sort('name',pymongo.ASCENDING).skip(2)
# print([result['name'] for result in result20])
result21 = collection.find().sort('name',pymongo.ASCENDING).skip(2).limit(1)
print([result['name'] for result in result21])



