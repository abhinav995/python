list1=["apple","grape","guava",1,3]
print(list1)

print(len(list1))
print(list1[-1])

list2=[5,2,3,4,5]
list3=["apple","orange"]
c=list2+list3
print(c)
list3[0]="pineapple"
print(list3)
# list3.append("apple","watermelon")
print(list3)
list3.insert(0,"pumpkin")
print(list3)



a=[3,5,8]
b=[7,9,0]
a.extend(b)
print(a)




list7=["realme","samsung","vivo"]
list8=["mi","oneplus","nothing"]
print(list7)
print(len(list7))
print(list7[2])
print(list7+list8)
list7.append("google")
print(list7)
list8.insert(1,"motorola")
print(list8)
list7.extend(list8)
print(list7)
list7.remove("samsung","vivo")
print(list7)


d=[1,2,3,4,5,6,7,8]
print(d[1:2]+d[3:4])


f=[1,2,3,4,5]
print(d[0:2]+d[3:4])
f.clear()
print(f)
del f
print(f)

