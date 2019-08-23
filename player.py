import random
from strategy import *
from monopolypower import *

class Player:
   def __init__(self,id,name):
      self.id=id
      self.name=name
      self.__pos__=0
      self.__money__=1500
      self.__properties__=[]

      # Randomly set the player's strategy for the sim
      self.buyingStrategy = random.randint(0,6)
      self.auctioningStrategy = random.randint(0,6)
      self.tradingStrategy = random.randint(0,6)

      self.__bankrupt__=False

   def shouldIBuy(self):
      return self.makeDecision(self.buyingStrategy)

   def shouldIAuction(self):
      return self.makeDecision(self.auctioningStrategy)

   def shouldITrade(self):
      return self.makeDecision(self.tradingStrategy)

   def makeDecision(self,strat):
       decision = random.randint(1,100)
       if strat == NEVER:
          return False
       elif strat == RARELY:
          if decision < 20:
             return True
          else:
             return False
       elif strat == SOMETIMES:
          if decision < 40:
             return True
          else:
             return False
       elif strat == OCCASIONALLY:
          if decision < 60:
             return True
          else:
             return False
       elif strat == OFTEN:
          if decision < 80:
             return True
          else:
             return False
       elif strat == ALWAYS:
          return True

   def makeOffer(self,currentAuctionValue):
      addedValue = random.randint(1,int(currentAuctionValue/2)+1)
      if currentAuctionValue+addedValue > self.__money__+self.propertyValue:
         if self.__money__+self.propertyValue > currentAuctionValue:
            return self.__money__+self.propertyValue
         else:
            return 0
      else:
         if currentAuctionValue > self.__money__:
            mortgageProperties(currentAuctionValue-self.__money__)
         return currentAuctionValue+addedValue

   def mortgageProperties(self,neededValue):
      # Assume we always want mortgage non-monopolies first
      monopolies = findMonopolies()
      mortVal = 0

      for prop in properties:
         if prop.color not in monopolies and mortVal < neededValue:
            if prop.mortgaged == False:
               prop.mortgaged = True
               mortVal += prop.mortgage
         elif mortVal >= neededValue:
            break

      if mortVal < neededValue:
         for prop in properties:
            if prop.mortgaged == False:
               prop.mortgaged = True
               mortVal += prop.mortgage
            if mortVal >= neededVal:
               break

      if mortVal < neededValue:
         print("you didnt check that they had enough money before calling mortgageProperties bucko")
         import sys
         sys.exit()
      self.addMoney(mortVal)

   def move(self,numSpaces):
      self.__pos__=(self.__pos__+numSpaces)%40

   def getPos(self):
      return self.__pos__

   def addMoney(self,amount):
      self.__money__+=amount

   def getMoney(self):
      return self.__money__

   def getProperties(self):
      return self.__properties__

   def addProperty(self,property):
      self.__properties__.append(property)

   def findMonopolies(self):
      # Return a list of monopolies that the player has
      colorProps = {"brown":0,"lblue":0,"pink":0,"orange":0,"red":0, \
                    "yellow":0,"green":0,"blue":0}
      monopolies = []


      for prop in properties:
         if(isinstance(tile,Property)):
            colorProps[prop.color]+=1
            if (prop.color == 'brown' and colorProps["brown"] == 2) or \
               (prop.color == 'blue' and colorProps["blue"] == 2):
               monopolies.append(prop.color)
            elif colorProps[prop.color] == 3:
               monopolies.append(prop.color)
      return monopolies
