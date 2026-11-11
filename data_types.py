#SINGLE VALUE DATA TYPES

#int datatype
goal=4
print(type(goal))

print(int())#default value

#float datatype
player_average=50.25
print(type(player_average))

print(float())#default value

#bool data type
iscitizen=True
print(type(iscitizen))

iscitizen=False
print(type(iscitizen))

print(bool())#default value

#complex
c=3+2j
print(type(c))

c=-3.1+2.5J
print(type(c))

print(complex())#default value

#MULTI VALUE DATA TYPES

#list
empty_list=[]#emply list
print(empty_list)

print(type(empty_list))

print(list())#2nd way to create empty list 

size=len(empty_list)
print(size)

marks=[25,35,65,85,98]
print(type(marks))
print(len(marks))
print(marks[-1])#98
print(marks[4])#98
print(marks)

list=[25,25,55,85,85]#allows duplicates
print(list)

num=[25,"45",True,45.45]
print(num)#support hetrogenous data type

#syntax for modification
list=[25,25,55,85,85]#mutable
list[2]=999
print(list)

#METHODS 0F LIST
# 1-Append
list1=[]
list1.append(25)
list1.append(30)
list1.append(35)
print(list1)

# 2-Insert
list2=[25,263,2,852,25,12,5,3]
list2.insert(2,252)
print(list2)

list3=[25,263,2,852,25,12,5,3]
list3.insert(25,252)#it adds element at the last
print(list3)

list4=[25,263,2,852,25,12,5,3]
list4.insert(-25,252)#it adds element at the first
print(list4)

# 3-Extend
aa=[1,2,3]
bb=[4,5,6]
aa.extend(bb)
print(aa)#combine 2 lists

# 4-Pop
#it removes last element
list5=[10,20,30,41]
list5.pop()
print(list5)

#pop perticular element
list6=[1,2,3,4]
list6.pop(-1)
print(list6)

# 5-remove
list7=[20,30,20,50,20,20]
list7.remove(20)
print(list7)#it removes 1st occuring object/element only

# 6-clear
list8=[20,30,20,50,20,20]
list8.clear()
print(list8)

# 7 sort
list9=[1,2,5,8,3,4,-5,-6,-2,-5,-8]
list9.sort()
print(list9)

lis1=[1,2,5,8,3,4,-5,-6,-2,-5,-8]
print (sorted(lis1))#sort in ascending order

# 8-Reverse
lis2=[1,2,5,8,3,4]
lis2.reverse()
print(lis2)

lis3=["cat","dog","panda"]
lis3.reverse()
print(lis3)

# 9-Count
lis3=[22,5,6,22,5,22,22,22,23]
num=lis3.count(22)
print(num)

lis4=lis3=[22,5,6,22,5,22,22,23]
print(lis4.count(27))

# 10-Index
lis5=[1,2,5,8,3,4]
print(lis5.index(2))#it returns index of the object

lis6=[22,5,6,22,5,22,22,23]
print(lis6.index(22))#it returns index of first occurence

lis7=[22,5,6,22,5,22,22,23]
nums=lis7.index(22,2)
print(nums)

lis8=[2,5,6,2,5,7,2,3,2,5,8]
nums=lis8.index(7,2,8)
print(nums)

rs=[10,20,30]
er=[40,50,60]
ps=rs+er
print(ps)

s=[10,20,30]
r=[40,50,60]
k=s.extend(r)
print(s)

# 2-TUPLE_datatype
t1=()
print(type(t1))

t2=tuple()
print(type(t2))

t3=()
print(len(t3))

t4=(24,65,85,63,25,45)
print(len(t4))

t5=(24,65,85,63,25,45)
ine=t5.index(65)
print(ine)

t6=(24,65,85,63,25,45)
print(t6[5])

ti=(60,)#whenever a single value is inside a tuple,remember to have comma at the end,otherwise it shows int dt
print(type(ti))

tuple1=(20,35,65,98,35,52,625,52)
inde=tuple1.index(35)
print(inde)
print(tuple1[1])

# SET DATA TYPE
remi=set()
print(remi)
print(type(remi))
print(len(remi))

set1={25,35,69,85,35}
print(set1)


#Methods Of Set
#ADD
qw=set()
qw.add(25)
qw.add(45)
qw.add(45)
print(qw)#{25,45}

#Update
sp={1,2,3,4}
ps={5,6,7,8}
sp.update(ps)
print(sp)

dance=["Any","Ben","Ched"]
sing=["Den","Ched"]
draw=["Any","Eric"]
student=dance+sing+draw
s=set()
s.update(student)
print(s)

#Pop
pp={5,6,7,8}
rem=pp.pop()
print(rem)
print(pp)

#Remove
pwe={5,6,7,8,9}
wer=pwe.remove(8)
print(pwe)

#Discard
d1={10,20,30,40}
d1.discard(30)
print(d1)

d1.clear()
print(d1)

#issubset
o1={2,3,5,}
o2={1,2,3,4,5,6}
bv=o1.issubset(o2)
print(bv)
lv=o2.issubset(o1)
print(lv)

print("+++++++++++++++++")
#issuperset
bv=o1.issuperset(o2)
print(bv)

lv=o2.issuperset(o1)
print(lv)

#isdisjoint
x1={2,3,5,}
x2={1,2,3,4,5,6}
mn=x1.isdisjoint(x2)
print(mn)

#Union
x1={2,3,5,}
x2={1,2,3,}
hg=x1.union(x2)
print(hg)

#intersection
x1={2,3,5,}
x2={1,2,3,}
pou=x1.intersection(x2)
print(pou)

#difference
x1={2,3,5,}
x2={1,2,3,}
re=x1.difference(x2)
print(re)

#symmatric_difference
x1={2,3,5,}
x2={1,2,3,}
hm=x1.symmetric_difference(x2)
print(hm)

#DICTIONARY

empty_dict={}
print(empty_dict)
print(type(empty_dict))

dict_items={"rap":10 , 100:35 , 582:985}
print(dict_items)
print(type(dict_items))
print(len(dict_items))

dict_items={220:10 , 100:35 , 582:985}
dict_items[220]=250
print(dict_items)
print(dict_items[100])

dict_items[101]=999
print(dict_items)

#Methods of Dictionary
#setdefault
d1={}
d1.setdefault(3,45.9)
d1.setdefault(5)
print(d1)

#update
d2={1:10,2:20,3:30}
d3={4:40,5:50,6:60}
d3.update(d2)
print(d3)

#get
d4={2:85,5:65,3:75}
print(d4.get(3))
print(d4.get(6))

#pop
d5={2:85,5:65,3:75}
print(d5.pop(5))
print(d5)

#popitem
d6={2:85,5:65,3:75}
print(d6.popitem())
print(d6)

#clear
d7={2:85,5:65,3:75}
pri=d7.clear()
print(d7)

#keys
d8={2:85,5:65,3:75}
print(d8.keys())

#values

print(d8.values())




#String
s1='Ramesh'
print(type(s1))
print(len(s1))
print(s1[2])

relation={"friend":"qwer","enemy":"pokj","guru":"jhgf"}
print(relation["enemy"])
print(len(relation["enemy"]))

































































