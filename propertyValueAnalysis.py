from monopoly import Monopoly as mp
from tiles import Property
import matplotlib.pyplot as plt

cost=[]
rent0=[]
rent1=[]
rent2=[]
rent3=[]
rent4=[]
rent5=[]

# Gather all of the original costs and rent values of
# all properties
for tile in mp.board:
   if(isinstance(tile,Property)):
      cost.append(tile.cost)
      rent0.append(tile.rent0)
      rent1.append(tile.rent1)
      rent2.append(tile.rent2)
      rent3.append(tile.rent3)
      rent4.append(tile.rent4)
      rent5.append(tile.rent5)

# Plot the data and save/show it
plt.plot(cost,label='Original Cost',linewidth=5.0)
plt.plot(rent0,label='Rent with 0 houses')
plt.plot(rent1,label='Rent with 1 house')
plt.plot(rent2,label='Rent with 2 houses')
plt.plot(rent3,label='Rent with 3 houses')
plt.plot(rent4,label='Rent with 4 houses')
plt.plot(rent5,label='Rent with a hotel')
plt.legend(loc='best')
plt.title('Cost of rent compared to buying price per property')
plt.xlabel('Property ID')
plt.ylabel('Cost')
plt.savefig('./propertyValueAnalysis/RentVsCostPerProperty.png')
plt.show()
