#nested dict and get/update
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#print(myfamily)
#print(myfamily.get("child3"))
myfamily["child3"].update({"year":2022})
print(myfamily)

#creating dicts from seq
mapping = dict(zip(range(5), reversed(range(5))))
mapping
