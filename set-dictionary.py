#集合的運算
s1={3,4,5}
print(3 in s1)
print(10 in s1)
print(10 not in s1)
s1={3,4,5}
s2={4,5,6,7}
#交集：取兩個集合中，相同的資料 &
s3=s1&s2
print(s3)
#|聯集：取兩個集合中的所有資料，但不重複
s4=s1|s2
print(s4)
#差集：從s1中，減去和s2重疊的部分
s5=s1-s2
print(s5)
#反交集：取兩個集合中，不重疊的部分
s6=s1^s2
print(s6)
#set(字串)拆解成集合
s=set("Hello")
print(s)
print("H" in s)
print("z"not in s)
#字典的運算
