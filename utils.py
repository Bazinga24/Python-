def max_val(arr):
  if len(arr)==0:
    print('The array is empty!!')
    return

  maxi=arr[0]
  for i in range(0,len(arr)):
    if arr[i]>maxi:
      maxi=arr[i]

  return maxi     

import random as rd
class Dice:
  def roll(self):
    val1=rd.randint(1,6)
    val2=rd.randint(1,6)
    return val1,val2


d1=Dice()
print(d1.roll())



