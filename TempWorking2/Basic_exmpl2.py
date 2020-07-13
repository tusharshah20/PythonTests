#using collections
import collections
l = ["he","she","he","she","he"]
print(sorted(collections.Counter(l)))

#class example
class this_is_class:
  def show(in_place_of_self):
    print("we are using this in place of self")
object = this_is_class()
object.show()

class car:
  def __init__(self,model,color):
    self.model = model
    self.color = color
  def show(self):
    print("model of car is: ",self.model)
    print("color of car is: ",self.color)
audi = car("newModel","blue")
merc = car("newModel","red")

audi.show()
merc.show()
