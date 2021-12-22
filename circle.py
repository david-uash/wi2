import math 

def circleArea(radius):
  if(radius<0):
     raise ValueError("radius must be >=0")
  return ((radius*radius)*math.pi)

#if __name__ == '__main__':
#    circleArea(2)

#
