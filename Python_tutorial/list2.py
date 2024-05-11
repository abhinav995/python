a=["cat","dog","cow","goat"]
print(a)
print(len(a))
print(a[2])
b=["tiger","lion","bear","cheetah"]
print(b)
print(a+b)
b[2]="elephant"
print(b)
b.append("snake")
print(b)
a.extend(b)
print(a)
a.insert(3,"ox")
print(a)
a.remove("snake")
print(a)
print(a[1:3])
print(a[2:3]+a[5:6]+a[7:8])

c=["p","y","t","h","o","n"]
print(c)
c.clear()
print(c)
del c
print(c)