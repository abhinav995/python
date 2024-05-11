a={1,2,3,4,5}
print(a)

print(len(a))
b={"banana","apple","orange","grape"}
print(b)
b.add("lemon")
print(b)
b.update(["guava","cucumber"])
print(b)
(b.remove("banana"))
print(b)
(b.discard("apple"))
print(b)
# (b.remove("carrot"))
# print(b)
(b.discard("carrot"))
print(b)

f={"car","bike","bus","ship"}
g={"bike","bus"}
f=f.difference_update(g)
print(f)


set1={1,2,3,4,5}
removeset1={1,2,3}
set2=set1.difference_update(removeset1)
print(set2)