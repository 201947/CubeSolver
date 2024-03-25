
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
def DDashBottom():
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
def DBottom():
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
def xMove():
  r()
  LDash()
  return

def xDash():
  rDash()
  L()
  return

def x2():
  xMove()
  xMove()
  return


def yMove():
  u()
  DDash()
  return

def yDash():
  uDash()
  D()
  return

def y2():
  yMove()
  yMove()
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
  N = random.randint(4,5)
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
    MovesToDo[i] = random.randint(0,41)
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
             "xMove", "x2", "xDash", "yMove", "y2", "yDash", "z", "z2", "zDash"]

# Total number of combinations to try in worst case for brute force
# 14454520644168104447138647932710521
totalComb = 0
for i in range(21):
  totalComb += (len(MovesList))**i


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


# eval() function: https://www.w3schools.com/python/ref_func_eval.asp

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
  print(finalMoveSet)
  return



# Look at the middle piece on the bottom face
def bottomCentre():
  piece = CurrentCube[7,4]
  return piece

# Find the edges of the same colour
def locateEdges(colour):
  listEdges = [(),(),(),()]
  faceColour = bottomCentre()
  for i in range(0,9):
    for j in range(0,12):
      if CurrentCube[i,j][0] == faceColour[0]:
        if CurrentCube[i,j][1] == "b":
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
            if any(list1[i][0] == list1[i+1][0] for i in range(len(list1)-1)):
                continue
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
            if any(list1[i][0] == list1[i+1][0] for i in range(len(list1)-1)):
                continue
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if checkCorners() == True:
              end = time.time()
              finalMoveSet.append(combination)
              print("Bottom corners finished. ")
              print("Solving combination:",combination)
              print("Time taken:",(end-start),"seconds. ")
              print("Moves so far:",finalMoveSet)
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
def findEdges(colour):
  edges = bottomCentre()
  return edges



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
            if any(list1[i][0] == list1[i+1][0] for i in range(len(list1)-1)):
                continue
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if checkCorners() == True and checkEdges() == True:
              end = time.time()
              finalMoveSet.append(combination)
              print("Bottom face finished. ")
              print("Solving combination:",combination)
              print("Time taken:",(end-start),"seconds. ")
              print("Moves so far:",finalMoveSet)
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
            if any(list1[i][0] == list1[i+1][0] for i in range(len(list1)-1)):
                continue
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if F2LCheck(F2LFaceList) == True and checkCorners() == True and checkEdges() == True:
              end = time.time()
              finalMoveSet.append(combination)
              print("F2L finished. ")
              print("Solving combination:",combination)
              print("Time taken:",(end-start),"seconds. ")
              print("Moves so far:",finalMoveSet)
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
            if any(list1[i][0] == list1[i+1][0] for i in range(len(list1)-1)):
                continue
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if F2LCheck(F2LFaceList) == True and checkFace(bottom) == True and checkFace(top) == True:
              end = time.time()
              finalMoveSet.append(combination)
              print("OLL finished. ")
              print("Solving combination:",combination)
              print("Time taken:",(end-start),"seconds. ")
              print("Moves so far:",finalMoveSet)
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
            if any(list1[i][0] == list1[i+1][0] for i in range(len(list1)-1)):
                continue
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
            if checkColour(faceList) == True:
              end = time.time()
              finalMoveSet.append(combination)
              print("PLL finished. ")
              print("Solving combination:",combination)
              print("Time taken:",(end-start),"seconds. ")
              print("Moves so far:",finalMoveSet)
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
  comCount = 0
  start = time.time()
  if checkColour(faceList) == False:
    k = 0
    while k <= 20:
      for n in range(1,k):
        combinations = itertools.product(MovesList, repeat=n)
        for combination in combinations:
            list1 = combination
            if any(list1[i][0].lower() == list1[i+1][0].lower() for i in range(len(list1)-1)):
                continue
            comCount += 1
            for i in range(len(list1)):
              t = eval(list1[i])
              t()
              moveCount += 1
            if checkColour(faceList) == True:
              end = time.time()
              finalMoveSet.append(combination)
              print("Cube Solved. ")
              print("Solving combination",combination)
              print("Time taken:",(end-start),"seconds. ")
              print(moveCount,'moves')
              print(comCount,'combinations')
              print("Moves so far:",finalMoveSet)
              #print((((end-start)/moveCount)*318579024287754816688664801)/31536000,'years to run in worst case scenario')
              return
            CurrentCube = copy.deepcopy(Stashed)
      k = k + 1
  end = time.time()
  print("Cube already solved. ")
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

def printScramble():
  print(MovesToDo)

def solveLetters():
  count=0
  for n in faceColours:
    locations = [(""),(""),(""),("")]
    for i in edgeCoords:
      if count < 4:
        if CurrentCube[i][0] == n:
          try:
            locations[count] = i
          except:
            continue
          count += 1

    for i in range(4):
      (j,k) = locations[i]
      if k == 4:
          if j == 0:
            index = 3,10
          elif j == 8:
            index = 5,10
          elif j == 3:
            index = 2,4
          elif j == 2:
            index = 3,4
          elif j == 5:
            index = 6,4
          elif j == 6:
            index = 5,4
      elif j == 4:
          if k == 0:
            index = 4,11
          elif k == 2:
            index = 4,3
          elif k == 3:
            index = 4,2
          elif k == 5:
            index = 4,6
          elif k == 6:
            index = 4,5
          elif k == 8:
            index = 4,9
          elif k == 9:
            index = 4,8
          elif k == 11:
            index = 4,0
      elif k == 10:
          if j == 3:
            index = 0,4
          elif j == 5:
            index = 8,4
      elif k == 5:
          if j == 1:
            index = 3,7
          elif j == 7:
            index = 5,7
      elif k == 3:
          if j == 1:
            index = 3,1
          elif j == 7:
            index = 5,1
      elif k == 1:
          if j == 3:
            index = 1,3
          elif j == 5:
            index = 7,3
      elif k == 7:
          if j == 3:
            index = 1,5
          elif j == 5:
            index = 7,5

      if CurrentCube[j,k][0] == 'W':
        if CurrentCube[index][0] == 'B':
          CurrentCube[index] = 'Bh'
          CurrentCube[j,k] = 'Wb'
        elif CurrentCube[index][0] == 'G':
          CurrentCube[index] = 'Gb'
          CurrentCube[j,k] = 'Wh'
        elif CurrentCube[index][0] == 'O':
          CurrentCube[index] = 'Of'
          CurrentCube[j,k] = 'Wd'
        elif CurrentCube[index][0] == 'R':
          CurrentCube[index] = 'Wf'
          CurrentCube[j,k] = 'Rd'

      elif CurrentCube[j,k][0] == 'B':
        if CurrentCube[index][0] == 'W':
          CurrentCube[index] = 'Wb'
          CurrentCube[j,k] = 'Bh'
        elif CurrentCube[index][0] == 'R':
          CurrentCube[index] = 'Rb'
          CurrentCube[j,k] = 'Bf'
        elif CurrentCube[index][0] == 'O':
          CurrentCube[index] = 'Ob'
          CurrentCube[j,k] = 'Bd'
        elif CurrentCube[index][0] == 'Y':
          CurrentCube[index] = 'Yb'
          CurrentCube[j,k] = 'Bb'

      elif CurrentCube[j,k][0] == 'R':
        if CurrentCube[index][0] == 'B':
          CurrentCube[index] = 'Bf'
          CurrentCube[j,k] = 'Rb'
        elif CurrentCube[index][0] == 'W':
          CurrentCube[index] = 'Rd'
          CurrentCube[j,k] = 'Wf'
        elif CurrentCube[index][0] == 'G':
          CurrentCube[index] = 'Rh'
          CurrentCube[j,k] = 'Gf'
        elif CurrentCube[index][0] == 'Y':
          CurrentCube[index] = 'Yd'
          CurrentCube[j,k] = 'Rf'

      elif CurrentCube[j,k][0] == 'G':
        if CurrentCube[index][0] == 'R':
          CurrentCube[index] = 'Gf'
          CurrentCube[j,k] = 'Rh'
        elif CurrentCube[index][0] == 'Y':
          CurrentCube[index] = 'Yh'
          CurrentCube[j,k] = 'Gh'
        elif CurrentCube[index][0] == 'O':
          CurrentCube[index] = 'Oh'
          CurrentCube[j,k] = 'Gd'
        elif CurrentCube[index][0] == 'W':
          CurrentCube[index] = 'Wh'
          CurrentCube[j,k] = 'Gb'

      elif CurrentCube[j,k][0] == 'O':
        if CurrentCube[index][0] == 'B':
          CurrentCube[index] = 'Bd'
          CurrentCube[j,k] = 'Ob'
        elif CurrentCube[index][0] == 'W':
          CurrentCube[index] = 'Wd'
          CurrentCube[j,k] = 'Of'
        elif CurrentCube[index][0] == 'G':
          CurrentCube[index] = 'Gd'
          CurrentCube[j,k] = 'Oh'
        elif CurrentCube[index][0] == 'Y':
          CurrentCube[index] = 'Yf'
          CurrentCube[j,k] = 'Od'

      elif CurrentCube[j,k][0] == 'Y':
        if CurrentCube[index][0] == 'R':
          CurrentCube[index] = 'Rf'
          CurrentCube[j,k] = 'Yd'
        elif CurrentCube[index][0] == 'B':
          CurrentCube[index] = 'Bb'
          CurrentCube[j,k] = 'Yb'
        elif CurrentCube[index][0] == 'G':
          CurrentCube[index] = 'Gh'
          CurrentCube[j,k] = 'Yh'
        elif CurrentCube[index][0] == 'O':
          CurrentCube[index] = 'Od'
          CurrentCube[j,k] = 'Yf'
      else:
        return False
    count = 0

  count = 0
  for n in faceColours:
    locations = [(""),(""),(""),("")]
    for i in cornerCoords:
      if CurrentCube[i][0] == n:
        try:
          locations[count] = i
        except:
          continue
        count += 1

    for i in range(4):
      (j,k) = locations[i]
      if k == 3:
          if j == 0:
            index1 = 3,0
            index2 = 3,11
          elif j == 2:
            index1 = 3,2
            index2 = 3,3
          elif j == 3:
            index1 = 2,3
            index2 = 3,2
          elif j == 5:
            index1 = 5,2
            index2 = 6,3
          elif j == 6:
            index1 = 5,2
            index2 = 5,3
          elif j == 8:
            index1 = 5,0
            index2 = 5,11
      elif k == 0:
          if j == 3:
            index1 = 0,3
            index2 = 3,11
          elif j == 5:
            index1 = 8,3
            index2 = 5,11
      elif k == 11:
          if j == 3:
            index1 = 0,3
            index2 = 3,0
          elif j == 5:
            index1 = 8,3
            index2 = 5,0
      elif k == 5:
          if j == 0:
            index1 = 3,8
            index2 = 3,9
          elif j == 2:
            index1 = 3,5
            index2 = 3,6
          elif j == 3:
            index1 = 2,5
            index2 = 3,6
          elif j == 5:
            index1 = 5,6
            index2 = 6,5
          elif j == 6:
            index1 = 5,5
            index2 = 5,6
          elif j == 8:
            index1 = 5,8
            index2 = 5,9
      elif k == 8:
          if j == 3:
            index1 = 0,5
            index2 = 3,9
          elif j == 5:
            index1 = 8,5
            index2 = 5,9
      elif k == 9:
          if j == 3:
            index1 = 0,5
            index2 = 3,8
          elif j == 5:
            index1 = 8,5
            index2 = 5,8
      elif k == 2:
          if j == 3:
            index1 = 2,3
            index2 = 3,3
          elif j == 5:
            index1 = 5,3
            index2 = 6,3
      elif k == 6:
          if j == 3:
            index1 = 2,5
            index2 = 3,5
          elif j == 5:
            index1 = 5,5
            index2 = 6,5

      if CurrentCube[j,k][0] == 'W':
        if CurrentCube[index1][0] == 'B':
          if CurrentCube[index2][0] == 'O':
            CurrentCube[j,k] = 'Wa'
            CurrentCube[index1] = 'Bg'
            CurrentCube[index2] = 'Oc'
          elif CurrentCube[index2][0] == 'R':
            CurrentCube[j,k] = 'Wc'
            CurrentCube[index1] = 'Bi'
            CurrentCube[index2] = 'Ra'
        elif CurrentCube[index1][0] == 'O':
          if CurrentCube[index2][0] == 'B':
            CurrentCube[j,k] = 'Wa'
            CurrentCube[index1] = 'Oc'
            CurrentCube[index2] = 'Bg'
          elif CurrentCube[index2][0] == 'G':
            CurrentCube[j,k] = 'Wg'
            CurrentCube[index1] = 'Oi'
            CurrentCube[index2] = 'Ga'
        elif CurrentCube[index1][0] == 'R':
          if CurrentCube[index2][0] == 'B':
            CurrentCube[j,k] = 'Wc'
            CurrentCube[index1] = 'Ra'
            CurrentCube[index2] = 'Bi'
          elif CurrentCube[index2][0] == 'G':
            CurrentCube[j,k] = 'Wi'
            CurrentCube[index1] = 'Rg'
            CurrentCube[index2] = 'Gc'
        elif CurrentCube[index1][0] == 'G':
          if CurrentCube[index2][0] == 'O':
            CurrentCube[j,k] = 'Wg'
            CurrentCube[index1] = 'Ga'
            CurrentCube[index2] = 'Oi'
          elif CurrentCube[index2][0] == 'R':
            CurrentCube[j,k] = 'Wi'
            CurrentCube[index1] = 'Gc'
            CurrentCube[index2] = 'Rg'
        
      elif CurrentCube[j,k][0] == 'Y':
        if CurrentCube[index1][0] == 'B':
          if CurrentCube[index2][0] == 'O':
            CurrentCube[j,k] = 'Yc'
            CurrentCube[index1] = 'Ba'
            CurrentCube[index2] = 'Oa'
          elif CurrentCube[index2][0] == 'R':
            CurrentCube[j,k] = 'Ya'
            CurrentCube[index1] = 'Bc'
            CurrentCube[index2] = 'Rc'
        elif CurrentCube[index1][0] == 'O':
          if CurrentCube[index2][0] == 'B':
            CurrentCube[j,k] = 'Yc'
            CurrentCube[index1] = 'Oa'
            CurrentCube[index2] = 'Ba'
          elif CurrentCube[index2][0] == 'G':
            CurrentCube[j,k] = 'Yi'
            CurrentCube[index1] = 'Og'
            CurrentCube[index2] = 'Gg'
        elif CurrentCube[index1][0] == 'R':
          if CurrentCube[index2][0] == 'B':
            CurrentCube[j,k] = 'Ya'
            CurrentCube[index1] = 'Rc'
            CurrentCube[index2] = 'Bc'
          elif CurrentCube[index2][0] == 'G':
            CurrentCube[j,k] = 'Yg'
            CurrentCube[index1] = 'Ri'
            CurrentCube[index2] = 'Gi'
        elif CurrentCube[index1][0] == 'G':
          if CurrentCube[index2][0] == 'O':
            CurrentCube[j,k] = 'Yi'
            CurrentCube[index1] = 'Gg'
            CurrentCube[index2] = 'Og'
          elif CurrentCube[index2][0] == 'R':
            CurrentCube[j,k] = 'Yg'
            CurrentCube[index1] = 'Gi'
            CurrentCube[index2] = 'Ri'
        elif CurrentCube[j,k][0] == 'B' or CurrentCube[j,k][0] == 'O' or CurrentCube[j,k][0] == 'G' or CurrentCube[j,k][0] == 'R':
          continue
        else:
          return False

    count = 0

  CurrentCube[1,4] = CurrentCube[1,4][0]+'e'
  CurrentCube[4,1] = CurrentCube[4,1][0]+'e'
  CurrentCube[4,4] = CurrentCube[4,4][0]+'e'
  CurrentCube[7,4] = CurrentCube[7,4][0]+'e'
  CurrentCube[4,7] = CurrentCube[4,7][0]+'e'
  CurrentCube[4,10] = CurrentCube[4,10][0]+'e'

  return True


def fillWithX():
  for i in range(9):
    for j in range(12):
      if CurrentCube[i,j] != '  ':
        CurrentCube[i,j] = CurrentCube[i,j][0]+'x'
  return


red_Lower = np.array([159,45,135])
red_upper = np.array([180,255,255])

yellow_lower = np.array([16,53,173])
yellow_upper = np.array([40,135,255])

blue_lower = np.array([71,120,128])
blue_upper = np.array([135,255,255])

green_lower = np.array([45,15,124])
green_upper = np.array([74,169,255])

orange_lower = np.array([0,60,135])
orange_upper = np.array([16,143,255])

white_lower = np.array([0,120,0])
white_upper = np.array([180,169,255])

#  whole frame = img[100:345,190:430]
coordinates = [(105,182,189,268),(105,182,270,352),(105,182,354,430),
               (184,265,189,268),(184,265,270,352),(184,265,354,430),
               (267,345,189,268),(267,345,270,352),(267,345,354,430)]


face = np.array([["  ","  ","  "],
                 ["  ","  ","  "],
                 ["  ","  ","  "]])


#  3x3 box in centre of frame = img[100:345,190:430]
coordinates = [(105,182,189,268),(105,182,270,352),(105,182,354,430),
               (184,265,189,268),(184,265,270,352),(184,265,354,430),
               (267,345,189,268),(267,345,270,352),(267,345,354,430)]


# Coordinates to check when detecting a colour
vertVals = (142, 225, 308)
horizVals = (225, 310, 395)

edgeCoords = [(0,4),(1,3),(1,5),(2,4),(3,1),(4,0),(4,2),(5,1),
              (3,4),(4,3),(4,5),(5,4),(3,7),(4,6),(4,8),(5,7),
              (3,10),(4,9),(4,11),(5,10),(6,4),(7,3),(7,5),(8,4)]

cornerCoords = [(0,3),(3,0),(3,11),(0,5),(3,8),(3,9),(2,3),(3,2),
                (3,3),(2,5),(3,5),(3,6),(5,2),(5,3),(6,3),(5,5),
                (5,6),(6,5),(8,3),(5,0),(5,11),(8,5),(5,8),(5,9)]

faceColours = ['W','Y','O','R']#,'B','G']

def scan():
  cap = cv2.VideoCapture(0)


  finishedScanning=0
  completelyFinished = False
  scan = input("Would you like to scan the cube? ")
  if scan.lower() == "y" or scan.lower() == "yes":
    count1=0
    count2=0
    done = False
    faceCount = 0
    solveProperly = False
    while completelyFinished == False:
      while finishedScanning==0:
        if count1>5:
          count1=0
        if count2>2:
          count2=0


        _, img = cap.read()
        img = cv2.flip(img,1)

        for i in range(len(coordinates)):
            frame = img[coordinates[i][0]:coordinates[i][1],coordinates[i][2]:coordinates[i][3]]

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            hls = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

            w_mask = cv2.inRange(hls,white_lower,white_upper)
            b_mask = cv2.inRange(hsv,blue_lower,blue_upper)
            r_mask = cv2.inRange(hsv,red_Lower,red_upper)
            y_mask = cv2.inRange(hls,yellow_lower,yellow_upper)
            g_mask = cv2.inRange(hls,green_lower,green_upper)
            o_mask = cv2.inRange(hls,orange_lower,orange_upper)

            kernel = np.ones((5, 5), "uint8")

            r_mask = cv2.dilate(r_mask, kernel)
            g_mask = cv2.dilate(g_mask, kernel)
            b_mask = cv2.dilate(b_mask, kernel)
            y_mask = cv2.dilate(y_mask, kernel)
            o_mask = cv2.dilate(o_mask, kernel)
            w_mask = cv2.dilate(w_mask, kernel)

            counter = 0

            # Red
            contours, hierarchy = cv2.findContours(r_mask,
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

        cv2.rectangle(img,(185,100),(435,350),(255,255,255),2)

        colour = ["White","Orange","Yellow","Red","Blue","Green"]
        colour2 = ["Blue","Orange","Red"]
        text = "Please position the "+colour[count1]+" face in the centre"
        text2 = "of the screen, with "+colour2[count2]+" on the top face"
        inst = "Controls:"
        inst1a = "Space - Take screenshot"
        inst2a = "n - Next face"
        inst3a = "t - Top face"
        inst4a = "b - Bottom face"
        inst5a = "f - Finish scanning"
        inst6a = "Order to press keys:"
        inst6b = "n,n,n,t,b,f"

        img = cv2.putText(img,text,(50,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)
        img = cv2.putText(img,text,(50,50),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),1)
        
        img = cv2.putText(img,text2,(50,75),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)
        img = cv2.putText(img,text2,(50,75),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),1)
        
        img = cv2.putText(img,inst,(10,345),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)
        img = cv2.putText(img,inst,(10,345),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),1)
        
        img = cv2.putText(img,inst1a,(10,385),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)
        img = cv2.putText(img,inst1a,(10,385),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),1)

        img = cv2.putText(img,inst2a,(10,415),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)
        img = cv2.putText(img,inst2a,(10,415),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),1)
        
        img = cv2.putText(img,inst3a,(10,445),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)
        img = cv2.putText(img,inst3a,(10,445),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),1)
        
        img = cv2.putText(img,inst4a,(375,385),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)
        img = cv2.putText(img,inst4a,(375,385),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),1)
        
        img = cv2.putText(img,inst5a,(375,415),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)
        img = cv2.putText(img,inst5a,(375,415),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),1)
        
        img = cv2.putText(img,inst6a,(225,445),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)
        img = cv2.putText(img,inst6a,(225,445),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),1)

        img = cv2.putText(img,inst6b,(485,445),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),8)
        img = cv2.putText(img,inst6b,(485,445),cv2.FONT_HERSHEY_COMPLEX,0.7,(178,163,255),1)

        cv2.imshow("Multiple Colour Detection in Real-Time", img)

        keypress = cv2.waitKey(1)
        if keypress==32:
            screenshot = img
            cv2.imshow("screenshot",screenshot)
            cv2.imwrite("Screenshot.jpeg", screenshot)
            colours = cv2.imread("Screenshot.jpeg", cv2.IMREAD_UNCHANGED)
          
            for i in range(3):
                for j in range(3):
                    pixel = colours[vertVals[i],horizVals[j]]
                    if pixel[0] < 10:
                        if pixel[1] < 10:
                            if pixel[2] > 245:
                                face[i,j] = "Rx"
                        elif pixel[1] > 117 and pixel[1] < 137:
                            if pixel[2] > 245:
                                face[i,j] = "Ox"
                        elif pixel[1] > 245:
                            if pixel[2] < 10:
                                face[i,j] = "Gx"
                            elif pixel[2] > 245:
                                face[i,j] = "Yx"
                    elif pixel[0] > 245:
                        if pixel[1] < 10:
                            if pixel[2] < 10:
                                face[i,j] = "Bx"
                        elif pixel[1] > 245:
                            if pixel[2] > 245:
                                face[i,j] = "Wx"
                    else:
                        face[i,j] = "██"
            face = np.flip(face,1)
            for i in range(3):
              for j in range(3):
                CurrentCube[i+3,j+3] = face[i,j]

        elif keypress==27:
          done = True
          completelyFinished = True
          break

        elif keypress==110:
          print("\n")
          yDash()
          if count1 < 3:
            count1 += 1
          else:
            count1 = 0
          print("Rotate with y then scan face")

        elif keypress==112:
          print("\n")
          print(CurrentCube)

        elif keypress==116:
          print("\n")
          xDash()
          count2 = 1
          count1 = 4
          print("Ready to scan top face")
        
        elif keypress==98:
          print("\n")
          x2()
          count2 = 2
          count1 = 5
          print("Ready to scan bottom face")
        
        elif keypress==102:
          finishedScanning=1
          solveProperly = True
        
        elif keypress==114:
          finishedScanning=1

      if done == False:
        print("Solving letters")
        solveLetters()
        found_x = False
        if solveProperly == False:
          CurrentCube[5,4] = 'Wx'
        for i in range(9):
            for j in range(12):
                if CurrentCube[i, j][1] == 'x':
                    print('Problem at index',i,str(j)+'.','Piece is:',CurrentCube[i, j])
                    found_x = True
                    retry = input("There was a problem. One or more pieces were not in the correct place/didn't scan correctly. Would you like to scan again? ")
                    if retry.lower() == 'y' or retry.lower() == 'yes':
                        finishedScanning = 0
                        break
                    elif retry.lower() == 'n' or retry.lower() == 'no' or retry == '':
                      completelyFinished=1
            if found_x == True:
                break
            elif finishedScanning == 0:
              break
        if found_x == False:
            break
    current()
  cap.release()
  cv2.destroyAllWindows()
  return


def Test():
  start = time.time()
  for i in range(100000):
    restore()
    scrambleCube()
    fillWithX()
    solveLetters()
    for j in range(9):
      for k in range(12):
        if CurrentCube[j,k][1] == 'x':
          printScramble()
          current()
  end = time.time()
  print(end-start)
  return


def testAllMoves():
  count = 0
  for i in MovesList:
    restore()
    fillWithX()
    eval(i)()
    if not solveLetters():
      print(False,i)
    else:
      print(True,i)
      count += 1
  print(count)
  return

#restore()
#scrambleTest()
#bruteForce()

#input('Press enter to close. ')

