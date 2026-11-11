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

