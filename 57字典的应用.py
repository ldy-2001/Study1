#思考1：如果有多个数据，如'Tom'.'男'，20，如何快速存储
#答案：列表list1 = ['Tom','男',20]
#如果数据顺序发生变化，如list1 = ['男','Tom',20]，还能list1[0]访问到数据'Tom'吗？
#答案：不能，数据下标发生变化。
#字典里的数据是以键值的形式出现，字典数据和数据顺序没有关系，即字典不支持下标。后期无论数据如何变化，只需要按照对应的键的名字查找数据即可