class Player:
   def __init__(self,id,name):
      self.id=id
      self.name=name
      self.__pos__=0
      self.__money__=0
      self.__properties__=[]

   def move(self,numSpaces):
      self.__pos__=(self.__pos__+numSpaces)%40

   def getPos(self):
      return self.__pos__
