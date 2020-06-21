lst = [ ('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'), 
           ('Cat', 'Bat', 'Sat'), [1, 2], [1, 2, 3], [1, 2] ]
newlst = []
for i in lst:
    newlst.extend(i)
newlst
result = [{l:newlst.count(l)} for l in set(newlst)]









