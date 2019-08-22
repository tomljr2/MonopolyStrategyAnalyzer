class Player:
   def __init__(self,id,name):
      self.id=id
      self.name=name
      self.__pos__=0
      self.__money__=1500
      self.__properties__=[]
      self.__bankrupt__=False

   def move(self,numSpaces):
      self.__pos__=(self.__pos__+numSpaces)%40

   def getPos(self):
      return self.__pos__

   def addMoney(self,amount):
      self.__money__-=amount

   def getMoney(self):
      return self.__money__

   def getProperties(self):
      return self.__properties__

   def addProperty(self,property):
      self.__properties__.append(property)
