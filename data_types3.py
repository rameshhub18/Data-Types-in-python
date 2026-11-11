#2-TUPLE_datatype
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