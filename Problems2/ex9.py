list1 = [1,1,2,2,3,3,4,4,5]
list1.count(1)
list2 = [ ('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'), 
          ('Cat', 'Bat', 'Sat'), [1, 2], [1, 2, 3], [1, 2] ]
for i in list2:
    print(i)
list3 = []
for i in list2:
    list3.extend(i)
list3

def testf(x = []):
    my = []
    for i in x:
        my.append([i,x.count(i)])
    return my
list3
list4 = [[l,list3.count(l)] for l in set(list3) if type(l) == str]
for i in list4:
    print(i)

lis2 = [ ('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'), 
          ('Cat', 'Bat', 'Sat'), [1, 2], [1, 2, 3], [1, 2] ]

def newd(l=[]):
    lis = []
    for i in lis2:
        lis.extend(i)
    lis3 = [[lis.count(l),l] for l in set(lis) if type(l)==str]
    return sorted(lis3,reverse = True)

def newe(l=[],listnew=[]):
    lis = []
    for i in lis2:
        lis.extend(i)
    lis3 = [[lis.count(l),l] for l in set(lis) if l in listnew]
    sorted(lis3,reverse = True)

    
