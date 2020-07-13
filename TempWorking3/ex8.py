x = [1,2,3,4,5,6,]
type(x)
y = (1,2,3,4,5)
type(y)
z = set(x)
type(z)
a = [['hello','world'],['test','winter'],[1,2,3]]
type(a)
a[0][0]
a[1][0]
d = []
for i in range(0,4):
    d.append(i)
d
d.append(y)
d.append(z)
d
type(d[4])
type(d[5])
d.append(x)
d
type(d[6])
del d[0]
d
e = []
e.extend([1,2,3])
e
e.extend(x)
e
e.extend(y)
e
e.extend(z)
e
for i in e:
    print(i+1)
newl=sorted(e)
set(newl[-1:])
e.remove(2)
e
e.remove(2)
e.pop(1)
e
e.pop()

e[::-1]
e[1:]
e[2:-2]
e
e[-1:-3]
