# These classes will make up a board object. They have the various properties
# of their respective tile type. For example, a property object will contain
# info describing its name, cost, color, rents, mortgage. Each tile class will
# have an id which is the same as its position on the board. For example, GO
# will have an ID==0, and boardwalk will have ID==39.

class Property:
   def __init__(self,id,name,cost,color,rent0,rent1,rent2,rent3,rent4, \
                rent5,mortgage):
      self.id = id
      self.name = name
      self.cost = cost
      self.color = color
      self.rent0 = rent0
      self.rent1 = rent1
      self.rent2 = rent2
      self.rent3 = rent3
      self.rent4 = rent4
      self.rent5 = rent5
      self.mortgage = mortgage

class Railroad:
   def __init__(self,id,name,cost,rent,mortgage):
      self.id = id
      self.name = name
      self.cost = cost
      self.rent = rent
      self.mortgage = mortgage

class Utility:
   def __init__(self,id,name,cost,mortgage):
      self.id = id
      self.name = name
      self.cost = cost
      self.mortgage = mortgage

class Tax:
   def __init__(self,id,name,cost):
      self.id = id
      self.name = name
      self.cost = cost

class Other:
   def __init__(self,id,name):
      self.id = id
      self.name = name
