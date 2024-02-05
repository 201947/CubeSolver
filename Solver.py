# Working:
# U, U', U2, u, u', u2, D, D', D2, d, d', d2, R, R2,R', r, r2, r',
# L, L2, L', l, l2, l', M, M2, M', F, F2, F', f, f2, f', B, B2, B',
# E, E', E2, S, S', S2
# Applying the moves randomly
# Brute force solve bottom cross
# Brute force to solve bottom corners without keeping edges
# Brute force to solve the entire bottom face (THEORETICALLY)
# Brute force to solve the entire cube (THEORETICALLY)


import numpy as np
import copy
import random
import itertools
import time
import cv2


# Start with the cube in a solved state
Solved = np.array([['  ','  ','  ','Ba','Bb','Bc','  ','  ','  ','  ','  ','  '],
                   ['  ','  ','  ','Bd','Be','Bf','  ','  ','  ','  ','  ','  '],
                   ['  ','  ','  ','Bg','Bh','Bi','  ','  ','  ','  ','  ','  '],
                   ['Oa','Ob','Oc','Wa','Wb','Wc','Ra','Rb','Rc','Ya','Yb','Yc'],
                   ['Od','Oe','Of','Wd','We','Wf','Rd','Re','Rf','Yd','Ye','Yf'],
                   ['Og','Oh','Oi','Wg','Wh','Wi','Rg','Rh','Ri','Yg','Yh','Yi'],
                   ['  ','  ','  ','Ga','Gb','Gc','  ','  ','  ','  ','  ','  '],
                   ['  ','  ','  ','Gd','Ge','Gf','  ','  ','  ','  ','  ','  '],
                   ['  ','  ','  ','Gg','Gh','Gi','  ','  ','  ','  ','  ','  ']])

# Make a copy of the array in a solved state
CurrentCube = copy.deepcopy(Solved)



# U Move
def UTurn():
  CurrentCube[3] = np.roll(CurrentCube[3], -3)
  return

# Rotate Top Face
def URotateTop():
  tempArr=[]
  for i in range(0,3):
    tempArr.append(CurrentCube[i,3:6])
  arr = [item for arr in tempArr for item in arr]
  arr = np.array(arr)
  face = arr.reshape(3,3)
  rotated = np.rot90(np.rot90(np.rot90(face)))
  for i in range(3):
    for j in range(3):
      CurrentCube[i,j+3] = rotated[i,j]
  return

# Combine UTurn and RotateTop into 1 function
def U():
  UTurn()
  URotateTop()
  return



# U2
def U2():
  U()
  U()
  return


# U'
def UDashTurn():
  CurrentCube[3] = np.roll(CurrentCube[3],3)
  return CurrentCube


def UDashRotateTop():
  tempArr=[]
  for i in range(0,3):
    tempArr.append(CurrentCube[i,3:6])
  arr = [item for arr in tempArr for item in arr]
  arr = np.array(arr)
  face = arr.reshape(3,3)
  rotated = np.rot90(face)
  for i in range(3):
    for j in range(3):
      CurrentCube[i,j+3] = rotated[i,j]
  return


def UDash():
  UDashTurn()
  UDashRotateTop()
  return


# u
def uTurn():
  CurrentCube[4]=np.roll(CurrentCube[4],-3)
  return

def u():
  uTurn()
  U()
  return


# u'
def uDashTurn():
  CurrentCube[4]=np.roll(CurrentCube[4],3)
  return

def uDash():
  uDashTurn()
  UDash()
  return


# u2
def u2():
  u()
  u()
  return


# D
def DTurn():
  CurrentCube[5] = np.roll(CurrentCube[5],3)
  return

# Rotate the bottom face
def DBottom():
  tempArr=[]
  for i in range(6,9):
    tempArr.append(CurrentCube[i,3:6])
  arr = [item for arr in tempArr for item in arr]
  arr = np.array(arr)
  face = arr.reshape(3,3)
  rotated = np.rot90(face)
  for i in range(3):
    for j in range(3):
      CurrentCube[i+6,j+3] = rotated[i,j]
  return

# Combine DTurn and DBottom into one function
def D():
  DTurn()
  DBottom()
  return


# D2
def D2():
  D()
  D()
  return


# D' Turn
def DDashTurn():
  CurrentCube[5] = np.roll(CurrentCube[5],-3)
  return

# D' Bottom face rotation
def DDashBottom():
  tempArr=[]
  for i in range(6,9):
    tempArr.append(CurrentCube[i,3:6])
  arr = [item for arr in tempArr for item in arr]
  arr = np.array(arr)
  face = arr.reshape(3,3)
  rotated = np.rot90(np.rot90(np.rot90(face)))
  for i in range(3):
    for j in range(3):
      CurrentCube[i+6,j+3] = rotated[i,j]
  return

# D'
def DDash():
  DDashTurn()
  DDashBottom()
  return


# d Turn
def dDashTurn():
  CurrentCube[4]=np.roll(CurrentCube[4],-3)
  return

# d
def d():
  dTurn()
  D()
  return


# d2
def d2():
  d()
  d()
  return


# d' Turn
def dTurn():
  CurrentCube[4]=np.roll(CurrentCube[4],3)
  return


# d'
def dDash():
  dDashTurn()
  DDash()
  return



# Turn the pieces connected to the R face
def RTurn():
  x5 = []
  
  for i in range(0,9):
    x5.append(CurrentCube[i,5])
  
  x5 = np.roll(x5,-3)
  
  for i in range(0,6):
    CurrentCube[i,5] = x5[i]
  
  x5 = np.flip(x5)
  
  tempList = []
  for i in range(0,3):
    tempList.append(CurrentCube[i+3,9])
  
  tempList2 = np.flip(tempList)
  
  for i in range(0,3):
    CurrentCube[i+6,5] = tempList2[i]
  
  for i in range(0,3):
    CurrentCube[i+3,9] = x5[i]
  
  return

# Rotate the R face
def RRotate():
  tempArr = []

  for i in range(3,6):
    for j in range(6,9):
      tempArr.append(CurrentCube[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(np.rot90(np.rot90(temp2)))


  for i in range(0,3):
    for j in range(0,3):
      CurrentCube[i+3,j+6] = temp2[i,j]
  
  return

# Combine RTurn and RRotate into R
def R():
  RTurn()
  RRotate()
  return


# R2
def R2():
  R()
  R()
  return


# R'
def RDashTurn():
  x5 = np.array(CurrentCube[0:9,5])

  temp = x5[6:9]
  temp = np.array(temp)
  temp = np.flip(temp)

  x5 = x5[0:6]

  for i in range(0,6):
    CurrentCube[i+3:i+9,5] = x5[i]

  temp2 = np.array(CurrentCube[3:6,9])
  temp2 = np.flip(temp2)

  for i in range(0,3):
    CurrentCube[i,5] = temp2[i]

  for i in range(0,3):
    CurrentCube[i+3,9] = temp[i]

  return


# R' Face Rotation
def RDashRotate():
  tempArr = []

  for i in range(3,6):
    for j in range(6,9):
      tempArr.append(CurrentCube[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(temp2)


  for i in range(0,3):
    for j in range(0,3):
      CurrentCube[i+3,j+6] = temp2[i,j]

  return


# R'
def RDash():
  RDashTurn()
  RDashRotate()
  return



# rTurn
def rTurn():
  x5 = []
  
  for i in range(0,9):
    x5.append(CurrentCube[i,4])
  
  x5 = np.roll(x5,-3)
  
  for i in range(0,6):
    CurrentCube[i,4] = x5[i]
  
  x5 = np.flip(x5)
  
  tempList = []
  for i in range(0,3):
    tempList.append(CurrentCube[i+3,10])
  
  tempList2 = np.flip(tempList)
  
  for i in range(0,3):
    CurrentCube[i+6,4] = tempList2[i]
  
  for i in range(0,3):
    CurrentCube[i+3,10] = x5[i]
  
  return

# r
def r():
  rTurn()
  R()
  return

# r2
def r2():
  r()
  r()
  return

# r' Turn
def rDashTurn():
  x5 = np.array(CurrentCube[0:9,4])

  temp = x5[6:9]
  temp = np.array(temp)
  temp = np.flip(temp)

  x5 = x5[0:6]

  temp2 = np.array(CurrentCube[3:6,10])
  temp2 = np.flip(temp2)

  for i in range(0,3):
    CurrentCube[i,4] = temp2[i]

  for i in range(0,3):
    CurrentCube[i+3,10] = temp[i]

  for i in range(0,6):
    CurrentCube[i+3,4] = x5[i]
  
  return



# r'
def rDash():
  RDash()
  rDashTurn()
  return


# L
def LTurn():
  x5 = np.array(CurrentCube[0:9,3])

  temp = x5[6:9]
  temp = np.array(temp)
  temp = np.flip(temp)

  x5 = x5[0:6]

  for i in range(0,6):
    CurrentCube[i+3:i+9,3] = x5[i]

  temp2 = np.array(CurrentCube[3:6,11])
  temp2 = np.flip(temp2)

  for i in range(0,3):
    CurrentCube[i,3] = temp2[i]

  for i in range(0,3):
    CurrentCube[i+3,11] = temp[i]

  return


# Rotate the Left Face
def LRotate():
  tempArr = []

  for i in range(3,6):
    for j in range(0,3):
      tempArr.append(CurrentCube[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(np.rot90(np.rot90(temp2)))


  for i in range(0,3):
    for j in range(0,3):
      CurrentCube[i+3,j] = temp2[i,j]

  return

# L
def L():
  LTurn()
  LRotate()
  return


# L2
def L2():
  L()
  L()
  return


# L Dash Turn
def LDashTurn():
  x5 = []
  
  for i in range(0,9):
    x5.append(CurrentCube[i,3])
  
  x5 = np.roll(x5,-3)
  
  for i in range(0,6):
    CurrentCube[i,3] = x5[i]
  
  x5 = np.flip(x5)
  
  tempList = []
  for i in range(0,3):
    tempList.append(CurrentCube[i+3,11])
  
  tempList2 = np.flip(tempList)
  
  for i in range(0,3):
    CurrentCube[i+6,3] = tempList2[i]
  
  for i in range(0,3):
    CurrentCube[i+3,11] = x5[i]
  
  return

# Rotate the Left Face the Other Way to LRotate
def LDashRotate():
  tempArr = []

  for i in range(3,6):
    for j in range(0,3):
      tempArr.append(CurrentCube[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(temp2)


  for i in range(0,3):
    for j in range(0,3):
      CurrentCube[i+3,j] = temp2[i,j]

  return


# Combine LDashTurn and LDashRotate
def LDash():
  LDashTurn()
  LDashRotate()
  return


# Turn the middle layer for l turn
def lTurn():
  x5 = np.array(CurrentCube[0:9,4])

  temp = x5[6:9]
  temp = np.array(temp)
  temp = np.flip(temp)

  x5 = x5[0:6]

  temp2 = np.array(CurrentCube[3:6,10])
  temp2 = np.flip(temp2)

  for i in range(0,3):
    CurrentCube[i,4] = temp2[i]

  for i in range(0,3):
    CurrentCube[i+3,10] = temp[i]

  for i in range(0,6):
    CurrentCube[i+3,4] = x5[i]
  
  return

# l Function
def l():
  lTurn()
  L()
  return

# l2
def l2():
  l()
  l()
  return


# l' Tunr center column
def lDashTurn():
  x5 = []
  
  for i in range(0,9):
    x5.append(CurrentCube[i,4])
  
  x5 = np.roll(x5,-3)
  
  for i in range(0,6):
    CurrentCube[i,4] = x5[i]
  
  x5 = np.flip(x5)
  
  tempList = []
  for i in range(0,3):
    tempList.append(CurrentCube[i+3,10])
  
  tempList2 = np.flip(tempList)
  
  for i in range(0,3):
    CurrentCube[i+6,4] = tempList2[i]
  
  for i in range(0,3):
    CurrentCube[i+3,10] = x5[i]

  return

# l'
def lDash():
  lDashTurn()
  LDash()
  return

# M
def M():
  rDashTurn()
  return

# M'
def MDash():
  rTurn()
  return 


# M2
def M2():
  M()
  M()
  return 

# Front Face
def FRotate():
  tempArr = []

  for i in range(3,6):
    for j in range(3,6):
      tempArr.append(CurrentCube[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(np.rot90(np.rot90(temp2)))


  for i in range(0,3):
    for j in range(0,3):
      CurrentCube[i+3,j+3] = temp2[i,j]

  return

# Shift edges around F Face
def FTurn():
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CurrentCube[2,i+3])
    left.append(CurrentCube[i+3,2])
    right.append(CurrentCube[i+3,6])
    bottom.append(CurrentCube[6,i+3])

  temp = top
  top = np.flip(left)
  left = bottom
  bottom = np.flip(right)
  right = temp

  for i in range(0,3):
    CurrentCube[2,i+3] = top[i]
    CurrentCube[i+3,2] = left[i]
    CurrentCube[i+3,6] = right[i]
    CurrentCube[6,i+3] = bottom[i]

  return


# Combine FTurn and FRotate
def F():
  FTurn()
  FRotate()
  return
  

# F2
def F2():
  F()
  F()
  return


# Turn the edges for F' Turn
def FDashTurn():
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CurrentCube[2,i+3])
    left.append(CurrentCube[i+3,2])
    right.append(CurrentCube[i+3,6])
    bottom.append(CurrentCube[6,i+3])

  temp = top
  top = right
  right = np.flip(bottom)
  bottom = left
  left = np.flip(temp)  

  for i in range(0,3):
    CurrentCube[2,i+3] = top[i]
    CurrentCube[i+3,2] = left[i]
    CurrentCube[i+3,6] = right[i]
    CurrentCube[6,i+3] = bottom[i]

  return

# Rotate the F face anticlockwise 90 degrees
def FDashRotate():
  tempArr = []

  for i in range(3,6):
    for j in range(3,6):
      tempArr.append(CurrentCube[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(temp2)


  for i in range(0,3):
    for j in range(0,3):
      CurrentCube[i+3,j+3] = temp2[i,j]

  return

# Combine FDashTurn and FDashRotate into FDash
def FDash():
  FDashTurn()
  FDashRotate()
  return



# Turn the centre horizontal layer
def fTurn():
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CurrentCube[1,i+3])
    left.append(CurrentCube[i+3,1])
    right.append(CurrentCube[i+3,7])
    bottom.append(CurrentCube[7,i+3])

  temp = top
  top = np.flip(left)
  left = bottom
  bottom = np.flip(right)
  right = temp

  for i in range(0,3):
    CurrentCube[1,i+3] = top[i]
    CurrentCube[i+3,1] = left[i]
    CurrentCube[i+3,7] = right[i]
    CurrentCube[7,i+3] = bottom[i]

  return

# Combine fTurn with F into f
def f():
  fTurn()
  F()
  return


# f2
def f2():
  f()
  f()
  return


# fDashTurn
def fDashTurn():
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CurrentCube[1,i+3])
    left.append(CurrentCube[i+3,1])
    right.append(CurrentCube[i+3,7])
    bottom.append(CurrentCube[7,i+3])

  temp = top
  top = right
  right = np.flip(bottom)
  bottom = left
  left = np.flip(temp)  

  for i in range(0,3):
    CurrentCube[1,i+3] = top[i]
    CurrentCube[i+3,1] = left[i]
    CurrentCube[i+3,7] = right[i]
    CurrentCube[7,i+3] = bottom[i]

  return

# f'
def fDash():
  fDashTurn()
  FDash()
  return



# Back Face Rotate
def BRotate():
  BF = []
  for i in range(0,3):
    for j in range(0,3):
      BF.append(CurrentCube[i+3,j+9])

  BF = np.array(BF)
  BF = BF.reshape(3,3)
  BF = np.rot90(np.rot90(np.rot90(BF)))


  for i in range(0,3):
    for j in range(0,3):
      CurrentCube[i+3,j+9] = BF[i,j]


  return

# B Edge Rotation
def BTurn():
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CurrentCube[0,i+3])
    left.append(CurrentCube[i+3,0])
    right.append(CurrentCube[i+3,8])
    bottom.append(CurrentCube[8,i+3])

  temp = top
  top = right
  right = np.flip(bottom)
  bottom = left
  left = np.flip(temp)  

  for i in range(0,3):
    CurrentCube[0,i+3] = top[i]
    CurrentCube[i+3,0] = left[i]
    CurrentCube[i+3,8] = right[i]
    CurrentCube[8,i+3] = bottom[i]

  return

# Combine BTurn and BRotate
def B():
  BRotate()
  BTurn()
  return


# B2
def B2():
  B()
  B()
  return


# B'
def BDashTurn():
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CurrentCube[0,i+3])
    left.append(CurrentCube[i+3,0])
    right.append(CurrentCube[i+3,8])
    bottom.append(CurrentCube[8,i+3])

  temp = top
  top = np.flip(left)
  left = bottom
  bottom = np.flip(right)
  right = temp

  for i in range(0,3):
    CurrentCube[0,i+3] = top[i]
    CurrentCube[i+3,0] = left[i]
    CurrentCube[i+3,8] = right[i]
    CurrentCube[8,i+3] = bottom[i]

  return

# B' Rotate Face
def BDashRotate():
  BF = []
  for i in range(0,3):
    for j in range(0,3):
      BF.append(CurrentCube[i+3,j+9])

  BF = np.array(BF)
  BF = BF.reshape(3,3)
  BF = np.rot90(BF)


  for i in range(0,3):
    for j in range(0,3):
      CurrentCube[i+3,j+9] = BF[i,j]


  return

# Combine BDashTurn and BDashRotate into BDash
def BDash():
  BDashTurn()
  BDashRotate()
  return


def b():
  fDashTurn()
  B()
  return


def b2():
  b()
  b()
  return

def bDash():
  fTurn()
  BDash()
  return


# E functions
def E():
  uDashTurn()
  return

def EDash():
  uTurn()
  return

def E2():
  E()
  E()
  return



# S functions
def S():
  fTurn()
  return

def SDash():
  fDashTurn()
  return

def S2():
  S()
  S()
  return


# Whole cube rotations
def x():
  r()
  LDash()
  return

def xDash():
  rDash()
  L()
  return

def x2():
  x()
  x()
  return


def y():
  u()
  DDash()
  return

def yDash():
  uDash()
  D()
  return

def y2():
  y()
  y()
  return


def z():
  f()
  BDash()
  return

def zDash():
  fDash()
  B()
  return

def z2():
  z()
  z()
  return



# Generate how many moves to apply
def numMoves():
  N = random.randint(1,10)
  return N

# Make an empty list N items long to fill with the moves
def makeEmptyList():
  global MovesToDo
  x = numMoves()
  MovesToDo = [" "] * numMoves()

# Generate Moves
def genMoves():
  makeEmptyList()
  for i in range(len(MovesToDo)):
    MovesToDo[i] = random.randint(0,50)
  return

# Convert the numbers generated to the corresponding functions
def convToMove():
  genMoves()
  for i in range(len(MovesToDo)):
    j = MovesToDo[i]
    MovesToDo[i] = MovesList[j]
  return

def convToMoveOutput(CA):
  for i in range(len(CA)):
    j = CA[i]
    CA[i] = MovesListForUser[j]
  return CA



# Make a list of the moves to call them easier, separate from the output the user sees
MovesList = ["U", "UDash", "U2", "u", "uDash", "u2", "D", "DDash",
             "D2", "d", "dDash", "d2", "R", "R2", "RDash", "r", "r2",
             "rDash", "L", "L2", "LDash", "l", "l2", "lDash", "M",
             "M2", "MDash", "F", "F2", "FDash", "f", "f2", "fDash",
             "B", "B2", "BDash", "E", "EDash", "E2", "S", "SDash", "S2",
             "x", "x2", "xDash", "y", "y2", "yDash", "z", "z2", "zDash"]


# Make another list that outputs what the user sees
MovesListForUser = ["U", "U'", "U2", "u", "u'", "u2", "D", "D'", "D2",
                    "d", "d'", "d2", "R", "R2", "R'", "r", "r2", "r'",
                    "L", "L2", "L'", "l", "l2", "l'", "M", "M2", "M'",
                    "F", "F2", "F'", "f", "f2", "f'", "B", "B2", "B'",
                    "E", "E'", "E2", "S", "S'", "S2", "x", "x2", "x'",
                    "y", "y2", "y'", "z", "z2", "z'"]



# Make a list of turns
def genList():
  list1 = convToMove()
  return list1


# Apply the moves to the cube
def scrambleCube():
  genList()
  print("Scramble:",MovesToDo)
  for i in range(len(MovesToDo)):
    nextfunction = MovesToDo[i]
    t = eval(nextfunction)
    t()
  return



# Apply a pre-set scramble for testing purposes
def scrambleTest():
  moves = ["UDash", "fDash","M2"]
  print("Test scramble:",moves)
  for i in range(len(moves)):
    t = eval(moves[i])
    t()
  return


# Create a list that contains all of the moves to solve the cube
finalMoveSet = []

# Reset the list
def clearFinalMoves():
  global finalMoveSet
  finalMoveSet = []

# Convert the moves into the proper notation
def convMoves():
  for i in range(len(finalMoveSet)):
    print(finalMoveSet[i])
    temp = []
    for k in finalMoveSet[i]:
      for j in range(len(MovesList)):
        if k == MovesList[j]:
          temp.append(MovesListForUser[j])
    finalMoveSet[i] = temp
  return



# Look at the middle piece on the bottom face
def bottomCentre():
  piece = CurrentCube[7,4]
  return piece

# Find the edges of the same colour
def locateEdges():
  listEdges = [(),(),(),()]
  colour = bottomCentre()
  for i in range(0,9):
    for j in range(0,12):
      if CurrentCube[i,j][0] == colour[0]:
        if CurrentCube[i,j][1] == "b":
          print("b",i,j)
          listEdges[0] = i,j
        elif CurrentCube[i,j][1] == "d":
          listEdges[1] = i,j
        elif  CurrentCube[i,j][1] == "f":
          listEdges[2] = i,j
        elif CurrentCube[i,j][1] == "h":
          listEdges[3] = i,j
  return listEdges


# Recursive approach
def bottomEdges():
  global CurrentCube
  Stashed = copy.deepcopy(CurrentCube)
  start = time.time()
  while checkEdges() == False:
    k = 0
    while k < 10:
      for n in range(1,k):
        combinations = itertools.product(MovesList, repeat=n)
        for combination in combinations:
            list1 = combination
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if checkEdges() == True:
              end = time.time()
              finalMoveSet.append(combination)
              print("Bottom cross finished. ")
              print("Solving combination:",combination)
              print("Time taken:",(end-start),"seconds. ")
              return
            CurrentCube = copy.deepcopy(Stashed)
      k = k + 1
  end = time.time()
  print("Edges already in correct positions. ")
  print("Time taken:",(end-start),"seconds. ")
  return

  
def checkEdges():
  colour = bottomCentre()
  if CurrentCube[6,4][0] == colour[0] and CurrentCube[6,4][1] == "b" and CurrentCube[8,4][0] == colour[0] and CurrentCube[8,4][1] == "h" and CurrentCube[7,3][0] == colour[0] and CurrentCube[7,3][1] == "d" and CurrentCube[7,5][0] == colour[0] and CurrentCube[7,5][1] == "f":
    return True
  else:
    return False


# Brute force corners into position
def corners():
  global CurrentCube
  Stashed = copy.deepcopy(CurrentCube)
  moveCount = 0
  start = time.time()
  while checkCorners() == False:
    k = 0
    while k < 10:
      for n in range(1,k):
        combinations = itertools.product(MovesList, repeat=n)
        for combination in combinations:
            list1 = combination
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if checkCorners() == True:
              end = time.time()
              finalMoveSet.append(combination)
              print("Bottom corners finished. ")
              print("Solving combination:",combination)
              print("Time taken:",(end-start),"seconds. ")
              return
            CurrentCube = copy.deepcopy(Stashed)
      k = k + 1
  end = time.time()
  print("Corners already in correct positions. ")
  print("Time taken:",(end-start),"seconds. ")
  return



# Find the positions of the bottom corner pieces
def findCorners():
  colour = bottomCentre()
  cornerPositions = [(""),(""),(""),("")]
  for i in range(0,9):
    for j in range(0,12):
      if CurrentCube[i,j][0] == colour[0] and CurrentCube[i,j][1] == "a":
        cornerPositions[0] = i,j
      elif CurrentCube[i,j][0] == colour[0] and CurrentCube[i,j][1] == "c":
        cornerPositions[1] = i,j
      elif  CurrentCube[i,j][0] == colour[0] and CurrentCube[i,j][1] == "g":
        cornerPositions[2] = i,j
      elif CurrentCube[i,j][0] == colour[0] and CurrentCube[i,j][1] == "i":
        cornerPositions[3] = i,j
  return cornerPositions


def checkCorners():
  colour = bottomCentre()
  if CurrentCube[6,3][0] == colour[0] and CurrentCube[6,3][1] == "a" and\
     CurrentCube[6,5][0] == colour[0] and CurrentCube[6,5][1] == "c" and\
     CurrentCube[8,3][0] == colour[0] and CurrentCube[8,3][1] == "g" and\
     CurrentCube[8,5][0] == colour[0] and CurrentCube[8,5][1] == "i" and\
     CurrentCube[7,4][0] == colour[0] and CurrentCube[7,4][1] == "e":
    return True
  else:
    return False



# Locate the edge pieces that correspond with the corners found with findCorners
def findEdges():
  corners = findCorners()
  return corners



# Solve the edges and corners of the bottom face using brute force
def bottomFace():
  global CurrentCube
  Stashed = copy.deepcopy(CurrentCube)
  moveCount = 0
  start = time.time()
  while checkCorners() == False or checkEdges() == False:
    k = 0
    while k < 10:
      for n in range(1,k):
        combinations = itertools.product(MovesList, repeat=n)
        for combination in combinations:
            list1 = combination
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if checkCorners() == True and checkEdges() == True:
                end = time.time()
                finalMoveSet.append(combination)
                print("Bottom face finished. ")
                print("Solving combination:",combination)
                print("Time taken:",(end-start),"seconds. ")
                return
            CurrentCube = copy.deepcopy(Stashed)
      k = k + 1
  end = time.time()
  print("Bottom face already solved. ")
  print("Time taken:",(end-start),"seconds. ")
  return



# Check each corner of F2L independently
def BruteF2L():
  global CurrentCube
  Stashed = copy.deepcopy(CurrentCube)
  moveCount = 0
  start = time.time()
  while F2LCheck(F2LFaceList) == False or checkCorners() == False or checkEdges() == False:
    k = 0
    while k < 10:
      for n in range(1,k):
        combinations = itertools.product(MovesList, repeat=n)
        for combination in combinations:
            list1 = combination
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if F2LCheck(F2LFaceList) == True and checkCorners() == True and checkEdges() == True:
                end = time.time()
                finalMoveSet.append(combination)
                print("F2L finished. ")
                print("Solving combination:",combination)
                print("Time taken:",(end-start),"seconds. ")
                return
            CurrentCube = copy.deepcopy(Stashed)
      k = k + 1
  end = time.time()
  print("F2L already completed. ")
  print("Time taken:",(end-start),"seconds. ")
  return



def BruteOLL():
  global CurrentCube
  Stashed = copy.deepcopy(CurrentCube)
  moveCount = 0
  start = time.time()
  while F2LCheck(F2LFaceList) == False or checkFace(bottom) == False or checkFace(top) == False:
    k = 0
    while k < 10:
      for n in range(1,k):
        combinations = itertools.product(MovesList, repeat=n)
        for combination in combinations:
            list1 = combination
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if F2LCheck(F2LFaceList) == True and checkFace(bottom) == True and checkFace(top) == True:
                end = time.time()
                finalMoveSet.append(combination)
                print("OLL finished. ")
                print("Solving combination:",combination)
                print("Time taken:",(end-start),"seconds. ")
                return
            CurrentCube = copy.deepcopy(Stashed)
      k = k + 1
  end = time.time()
  print("OLL already completed. ")
  print("Time taken:",(end-start),"seconds. ")
  return

# Longest PLL is 21 moves
def BrutePLL():
  global CurrentCube
  Stashed = copy.deepcopy(CurrentCube)
  moveCount = 0
  start = time.time()
  while checkColour(faceList) == False:
    k = 0
    while k < 10:
      for n in range(1,k):
        combinations = itertools.product(MovesList, repeat=n)
        for combination in combinations:
            list1 = combination
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if checkColour(faceList) == True:
                end = time.time()
                finalMoveSet.append(combination)
                print("PLL finished. ")
                print("Solving combination:",combination)
                print("Time taken:",(end-start),"seconds. ")
                return
            CurrentCube = copy.deepcopy(Stashed)
      k = k + 1
  end = time.time()
  print("PLL already completed. ")
  print("Time taken:",(end-start),"seconds. ")
  return







# Solve the whole cube by iterating through every possible set of 20 or less moves
def bruteForce():
  global CurrentCube
  Stashed = copy.deepcopy(CurrentCube)
  moveCount = 0
  start = time.time()
  if checkColour(faceList) == False:
    k = 0
    while k < 10:
      for n in range(1,k):
        combinations = itertools.product(MovesList, repeat=n)
        for combination in combinations:
            list1 = combination
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if checkColour(faceList) == True:
              end = time.time()
              finalMoveSet.append(combination)
              print("Cube Solved. ")
              print("Solving combination",combination)
              print("Time taken:",(end-start),"seconds. ")
              return
            CurrentCube = copy.deepcopy(Stashed)
      k = k + 1
  end = time.time()
  print("Cube is already solved. ")
  print("Time taken:",(end-start),"seconds. ")
  return





# Restore Solved State
def restore():
  global CurrentCube
  CurrentCube = copy.deepcopy(Solved)
  return


# Output the Current State of 'Solved'
def current():
  print(CurrentCube)
  return


# Check if CurrentCube is the same as Solved, doesn't work for a
# solved cube rotated differently
def check():
  return np.array_equal(Solved,CurrentCube)




# Better check function
# Check each 3x3 face individually
# Works for a rotated but solved cube

top = (0,3,3,6)
front = (3,6,3,6)
bottom = (6,9,3,6)
left = (3,6,0,3)
right = (3,6,6,9)
back = (3,6,9,12)

faceList = [top,front,bottom,left,right,back]
F2LFaceList = [front,left,right,back]

def checkFace(CF):
  num1 = CF[0]
  num2 = CF[1]
  num3 = CF[2]
  num4 = CF[3]
  face = CurrentCube[num1:num2, num3:num4]
  middlePiece = face[1,1][0]
  for i in range(0,3):
    for j in range(0,3):
      if face[i,j][0] != middlePiece:
        return False
  return True


def checkColour(CF):
  for i in range(len(CF)):
    num1 = CF[i][0]
    num2 = CF[i][1]
    num3 = CF[i][2]
    num4 = CF[i][3]
    face = CurrentCube[num1:num2,num3:num4]
    middlePiece = face[1,1][0]
    for j in range(3):
      for k in range(3):
        if face[j,k][0] != middlePiece:
          return False
  return True


def F2LCheck(CF):
  for i in range(len(CF)):
    num1 = CF[i][0]
    num2 = CF[i][1]
    num3 = CF[i][2]
    num4 = CF[i][3]
    face = CurrentCube[num1:num2,num3:num4]
    middlePiece = face[1,1][0]
    for i in range(1,3):
      if face[i,2][0] != middlePiece:
        return False
  return True


def OLLCheck():
  num1 = top[0]
  num2 = top[1]
  num3 = top[2]
  num4 = top[3]
  face = CurrentCube[num1:num2, num3:num4]
  middlePiece = face[1,1][0]
  for i in range(0,3):
    for j in range(0,3):
      if face[i,j][0] != middlePiece:
        return False
  return True


cap = cv2.VideoCapture(0) 

red1_Lower = np.array([169,124,60])
red1_upper = np.array([180,255,255])

#red2_lower = np.array([0,181,127])
#red2_upper = np.array([3,255,255])

yellow_lower = np.array([29,131,120])
yellow_upper = np.array([40,218,221])

blue_lower = np.array([93,173,71])
blue_upper = np.array([138,255,199])

green_lower = np.array([40,90,0])
green_upper = np.array([79,255,255])

orange_lower = np.array([3,0,150])
orange_upper = np.array([11,255,169])

white_lower = np.array([0,130,0])
white_upper = np.array([255,140,255])

#  whole frame = img[100:345,190:430]
coordinates = [(105,182,189,268),(105,182,270,352),(105,182,354,430),
               (184,265,189,268),(184,265,270,352),(184,265,354,430),
               (267,345,189,268),(267,345,270,352),(267,345,354,430)]


face = np.array([["","",""],
                 ["","",""],
                 ["","",""]])

cap = cv2.VideoCapture(0) 

red1_Lower = np.array([169,124,60])
red1_upper = np.array([180,255,255])

#red2_lower = np.array([0,181,127])
#red2_upper = np.array([3,255,255])

yellow_lower = np.array([29,203,105])
yellow_upper = np.array([45,255,180])

blue_lower = np.array([93,173,71])
blue_upper = np.array([138,255,199])

green_lower = np.array([40,90,0])
green_upper = np.array([79,255,255])

orange_lower = np.array([0,180,139])
orange_upper = np.array([19,255,221])

white_lower = np.array([0,110,0])
white_upper = np.array([255,140,255])

#  whole frame = img[100:345,190:430]
coordinates = [(105,182,189,268),(105,182,270,352),(105,182,354,430),
               (184,265,189,268),(184,265,270,352),(184,265,354,430),
               (267,345,189,268),(267,345,270,352),(267,345,354,430)]

vertVals = (142, 225, 308)
horizVals = (225, 310, 395)

scan = input("Would you like to scan the cube? ")
if scan.lower() == "y" or scan.lower() == "yes":
  while True:

    _, img = cap.read()
    img = cv2.flip(img,1)

    for i in range(len(coordinates)):
        frame = img[coordinates[i][0]:coordinates[i][1],coordinates[i][2]:coordinates[i][3]]

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

        w_mask = cv2.inRange(hls,white_lower,white_upper)
        b_mask = cv2.inRange(hsv,blue_lower,blue_upper)
        r1_mask = cv2.inRange(hsv,red1_Lower,red1_upper)
#        r2_mask = cv2.inRange(hsv,red2_lower,red2_upper)
        y_mask = cv2.inRange(hsv,yellow_lower,yellow_upper)
        g_mask = cv2.inRange(hsv,green_lower,green_upper)
        o_mask = cv2.inRange(hsv,orange_lower,orange_upper)

        kernel = np.ones((5, 5), "uint8")

        r1_mask = cv2.dilate(r1_mask, kernel)
#        r2_mask = cv2.dilate(r2_mask, kernel)
        g_mask = cv2.dilate(g_mask, kernel)
        b_mask = cv2.dilate(b_mask, kernel)
        y_mask = cv2.dilate(y_mask, kernel)
        o_mask = cv2.dilate(o_mask, kernel)
        w_mask = cv2.dilate(w_mask, kernel)

        counter = 0



        # Red 1
        contours, hierarchy = cv2.findContours(r1_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 4000):
                counter += 1
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.rectangle(frame, (x, y),
                                        (x + w, y + h),
                                        (0, 0, 255), -1)


        # Red 2
#        contours, hierarchy = cv2.findContours(r2_mask,
#                                            cv2.RETR_TREE,
#                                            cv2.CHAIN_APPROX_SIMPLE)
#
#        for pic, contour in enumerate(contours):
#            area = cv2.contourArea(contour)
#            if(area > 4000):
#                counter += 1
#                x, y, w, h = cv2.boundingRect(contour)
#                frame = cv2.rectangle(frame, (x, y),
#                                        (x + w, y + h),
#                                        (0, 0, 0), 2)


        # Green
        contours, hierarchy = cv2.findContours(g_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)

        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 4000):
                counter += 1
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.rectangle(frame, (x, y),
                                        (x + w, y + h),
                                        (0, 255, 0), -1)

        # Blue
        contours, hierarchy = cv2.findContours(b_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 4000):
                counter += 1
                x, y, w, h = cv2.boundingRect(contour)
                frame = cv2.rectangle(frame, (x, y),
                                        (x + w, y + h),
                                        (255, 0, 0), -1)

        # Yellow
        contours, hierarchy = cv2.findContours(y_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if area > 4000:
                    counter += 1
                    x,y,w,h = cv2.boundingRect(contour)
                    frame = cv2.rectangle(frame, (x,y),
                                        (x+w,y+h),
                                        (0,255,255), -1)

        # Orange
        contours, hierarchy = cv2.findContours(o_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if area > 4000:
                    counter += 1
                    x,y,w,h = cv2.boundingRect(contour)
                    frame = cv2.rectangle(frame, (x,y),
                                        (x+w,y+h),
                                        (0,127,255), -1)

        # White
        contours, hierarchy = cv2.findContours(w_mask,
                                            cv2.RETR_TREE,
                                            cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
                area = cv2.contourArea(contour)
                if area > 4000:
                    counter += 1
                    x,y,w,h = cv2.boundingRect(contour)
                    frame = cv2.rectangle(frame, (x,y),
                                        (x+w,y+h),
                                        (255,255,255), -1)

    colour = "White"
    colour2 = "Blue"
    text = "Please position the "+colour+" face in the centre"
    text2 = "of the screen, with "+colour2+" on the top face"

    img = cv2.putText(img,text,(50,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)
    img = cv2.putText(img,text2,(50,75),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)

    img = cv2.putText(img,text,(50,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),2)
    img = cv2.putText(img,text2,(50,75),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),2)
    
    cv2.rectangle(img,(185,100),(435,350),(255,255,255),2)
    cv2.imshow("Multiple Colour Detection in Real-Time", img)


    if cv2.waitKey(1)==32:
        screenshot = img
        #for i in range(3):
            #for j in range(3):
                #cv2.rectangle(screenshot,(vertVals[i],horizVals[j]),(vertVals[i],horizVals[j]),(255,0,255),-1)
        cv2.imshow("screenshot",screenshot)
        cv2.imwrite("Screenshot.jpeg", screenshot)
        colours = cv2.imread("Screenshot.jpeg", cv2.IMREAD_UNCHANGED)
        
        for i in range(3):
            for j in range(3):
                pixel = colours[vertVals[i],horizVals[j]]
                if pixel[0] < 10:
                    if pixel[1] < 10:
                        if pixel[2] > 245:
                            face[i,j] = "R"
                    elif pixel[1] > 117 and pixel[1] < 137:
                        if pixel[2] > 245:
                            face[i,j] = "O"
                    elif pixel[1] > 245:
                        if pixel[2] < 10:
                            face[i,j] = "G"
                        elif pixel[2] > 245:
                            face[i,j] = "Y"
                elif pixel[0] > 245:
                    if pixel[1] < 10:
                        if pixel[2] < 10:
                            face[i,j] = "B"
                    elif pixel[1] > 245:
                        if pixel[2] > 245:
                            face[i,j] = "W"
                else:
                    face[i,j] = "X"
        print("\n")
        face = np.flip(face,1)
        for i in range(3):
          for j in range(3):
            CurrentCube[i+3,j+3] = face[i,j]
        print(CurrentCube)

    if cv2.waitKey(1)==27:
        break



cap.release()

cv2.destroyAllWindows()

