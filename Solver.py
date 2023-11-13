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
SafeSolved = copy.deepcopy(Solved)

# U Move
def UTurn(CA):

  RA = np.roll(CA[3], -3)
  return RA

# Rotate Top Face
def URotateTop(RT):
  tempArr=[]
  for i in range(0,3):
    tempArr.append(RT[i,3:6])
  arr = [item for arr in tempArr for item in arr]
  arr = np.array(arr)
  reshapedArr = arr.reshape(3,3)
  rotatedArr = np.rot90(np.rot90(np.rot90(reshapedArr)))
  return rotatedArr

# Combine UTurn and RotateTop into 1 function
def U(CA):
  UT = UTurn(CA)
  CA[3] = UT
  
  Rotated = URotateTop(CA)

  for i in range(0,3):
    for j in range(0,3):
      CA[i,j+3] = Rotated[i,j]
  UT = CA
  
  return UT


# U2
def U2(CA):
  TA = U(U(CA))
  return TA


# U'
def UDashTurn(CA):
  RA = np.roll(CA[3],3)
  return RA

def UDashRotateTop(RT):
  tempArr=[]
  for i in range(0,3):
    tempArr.append(RT[i,3:6])
  arr = [item for arr in tempArr for item in arr]
  arr = np.array(arr)
  reshapedArr = arr.reshape(3,3)
  rotatedArr = np.rot90(reshapedArr)
  return rotatedArr

def UDash(CA):
  UT=UDashTurn(CA)
  CA[3]=UT

  Rotated = UDashRotateTop(CA)

  for i in range(0,3):
    for j in range(0,3):
      CA[i,j+3] = Rotated[i,j]
  UT = CA

  return UT


# u
def uTurn(CA):
  RA=np.roll(CA[3],-3)
  CA[3] = RA
  RA=np.roll(CA[4],-3)
  CA[4] = RA
  return CA

def u(CA):
  UT = uTurn(CA)

  Rotated = URotateTop(CA)

  for i in range(0,3):
    for j in range(0,3):
      CA[i,j+3] = Rotated[i,j]
  UT = CA

  return CA


# u'
def uDashTurn(CA):
  RA=np.roll(CA[3],3)
  CA[3] = RA
  RA=np.roll(CA[4],3)
  CA[4] = RA
  return CA

def uDash(CA):
  UT = uDashTurn(CA)

  Rotated = UDashRotateTop(CA)

  for i in range(0,3):
    for j in range(0,3):
      CA[i,j+3] = Rotated[i,j]
  UT = CA

  return UT


# u2
def u2(CA):
  UT = u(u(CA))
  return UT




# D
def DTurn(CA):
  RA = np.roll(CA[5],3)
  return RA

# Rotate the bottom face
def DBottom(CA):
  tempArr=[]
  for i in range(6,9):
    tempArr.append(CA[i,3:6])
  arr = [item for arr in tempArr for item in arr]
  arr = np.array(arr)
  reshapedArr = arr.reshape(3,3)
  rotatedArr = np.rot90(reshapedArr)
  return rotatedArr

# Combine DTurn and DBottom into one function
def D(CA):
  DT=DTurn(CA)
  CA[5]=DT

  Rotated = DDashBottom(CA)

  for i in range(0,3):
    for j in range(0,3):
      CA[i+6,j+3] = Rotated[i,j]
  UT = CA

  return CA  


# D2
def D2(CA):
  D2A = D(CA)
  DA2 = D(D2A)
  return DA2


# D' Turn
def DDashTurn(CA):
  RA = np.roll(CA[5],-3)
  return RA

# D' Bottom face rotation
def DDashBottom(CA):
  tempArr=[]
  for i in range(6,9):
    tempArr.append(CA[i,3:6])
  arr = [item for arr in tempArr for item in arr]
  arr = np.array(arr)
  reshapedArr = arr.reshape(3,3)
  rotatedArr = np.rot90(np.rot90(np.rot90(reshapedArr)))
  return rotatedArr

# D'
def DDash(CA):
  DDA = DDashTurn(CA)
  CA[5] = DDA

  Rotated = DBottom(CA)

  for i in range(0,3):
    for j in range(0,3):
      CA[i+6,j+3] = Rotated[i,j]
  UT = CA

  return UT


# d Turn
def dDashTurn(CA):
  RA=np.roll(CA[4],-3)
  CA[4] = RA
  RA=np.roll(CA[5],-3)
  CA[5] = RA
  return CA

# d
def d(CA):
  dA = dTurn(CA)

  Rotated = DDashBottom(CA)

  for i in range(0,3):
    for j in range(0,3):
      CA[i+6,j+3] = Rotated[i,j]
  UT = CA

  return UT


# d2
def d2(CA):
  d2A = d(CA)
  dA2 = d(d2A)
  return dA2


# d' Turn
def dTurn(CA):
  RA=np.roll(CA[4],3)
  CA[4] = RA
  RA=np.roll(CA[5],3)
  CA[5] = RA
  return CA


# d'
def dDash(CA):
  dDA = dDashTurn(CA)
  CA = dDA

  Rotated = DBottom(CA)

  for i in range(0,3):
    for j in range(0,3):
      CA[i+6,j+3] = Rotated[i,j]
  UT = CA

  return UT



# Turn the pieces connected to the R face
def RTurn(CA):
  x5 = []
  
  for i in range(0,9):
    x5.append(CA[i,5])
  
  x5 = np.roll(x5,-3)
  
  for i in range(0,6):
    CA[i,5] = x5[i]
  
  x5 = np.flip(x5)
  
  tempList = []
  for i in range(0,3):
    tempList.append(CA[i+3,9])
  
  tempList2 = np.flip(tempList)
  
  for i in range(0,3):
    CA[i+6,5] = tempList2[i]
  
  for i in range(0,3):
    CA[i+3,9] = x5[i]
  
  return CA

# Rotate the R face
def RRotate(CA):
  tempArr = []

  for i in range(3,6):
    for j in range(6,9):
      tempArr.append(CA[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(np.rot90(np.rot90(temp2)))


  for i in range(0,3):
    for j in range(0,3):
      CA[i+3,j+6] = temp2[i,j]
  
  return CA

# Combine RTurn and RRotate into R
def R(CA):
  CA = RTurn(CA)
  CA = RRotate(CA)

  return CA


# R2
def R2(CA):
  CA = R(CA)
  CA = R(CA)
  return CA


# R'
def RDashTurn(CA):
  x5 = np.array(CA[0:9,5])

  temp = x5[6:9]
  temp = np.array(temp)
  temp = np.flip(temp)

  x5 = x5[0:6]

  for i in range(0,6):
    CA[i+3:i+9,5] = x5[i]

  temp2 = np.array(CA[3:6,9])
  temp2 = np.flip(temp2)

  for i in range(0,3):
    CA[i,5] = temp2[i]

  for i in range(0,3):
    CA[i+3,9] = temp[i]

  return(CA)


# R' Face Rotation
def RDashRotate(CA):
  tempArr = []

  for i in range(3,6):
    for j in range(6,9):
      tempArr.append(CA[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(temp2)


  for i in range(0,3):
    for j in range(0,3):
      CA[i+3,j+6] = temp2[i,j]

  return(CA)


# R'
def RDash(CA):
  CA = RDashTurn(CA)
  CA = RDashRotate(CA)
  return CA



# rTurn
def rTurn(CA):
  x5 = []
  
  for i in range(0,9):
    x5.append(CA[i,4])
  
  x5 = np.roll(x5,-3)
  
  for i in range(0,6):
    CA[i,4] = x5[i]
  
  x5 = np.flip(x5)
  
  tempList = []
  for i in range(0,3):
    tempList.append(CA[i+3,10])
  
  tempList2 = np.flip(tempList)
  
  for i in range(0,3):
    CA[i+6,4] = tempList2[i]
  
  for i in range(0,3):
    CA[i+3,10] = x5[i]
  
  return CA

# r
def r(CA):
  CA = rTurn(CA)
  CA = RTurn(CA)
  CA = RRotate(CA)
  return CA

# r2
def r2(CA):
  CA = r(r(CA))
  return CA

# r' Turn
def rDashTurn(CA):
  x5 = np.array(CA[0:9,4])

  temp = x5[6:9]
  temp = np.array(temp)
  temp = np.flip(temp)

  x5 = x5[0:6]

  temp2 = np.array(CA[3:6,10])
  temp2 = np.flip(temp2)

  for i in range(0,3):
    CA[i,4] = temp2[i]

  for i in range(0,3):
    CA[i+3,10] = temp[i]

  for i in range(0,6):
    CA[i+3,4] = x5[i]
  
  return(CA)



# r'
def rDash(CA):
  CA = rDashTurn(CA)
  CA = RDashTurn(CA)
  CA = RDashRotate(CA)
  return CA


# L
def LTurn(CA):
  x5 = np.array(CA[0:9,3])

  temp = x5[6:9]
  temp = np.array(temp)
  temp = np.flip(temp)

  x5 = x5[0:6]

  for i in range(0,6):
    CA[i+3:i+9,3] = x5[i]

  temp2 = np.array(CA[3:6,11])
  temp2 = np.flip(temp2)

  for i in range(0,3):
    CA[i,3] = temp2[i]

  for i in range(0,3):
    CA[i+3,11] = temp[i]

  return(CA)


# Rotate the Left Face
def LRotate(CA):
  tempArr = []

  for i in range(3,6):
    for j in range(0,3):
      tempArr.append(CA[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(np.rot90(np.rot90(temp2)))


  for i in range(0,3):
    for j in range(0,3):
      CA[i+3,j] = temp2[i,j]

  return(CA)

# L
def L(CA):
  CA = LTurn(CA)
  CA = LRotate(CA)
  return CA


# L2
def L2(CA):
  CA = L(L(CA))
  return CA


# L Dash Turn
def LDashTurn(CA):
  x5 = []
  
  for i in range(0,9):
    x5.append(CA[i,3])
  
  x5 = np.roll(x5,-3)
  
  for i in range(0,6):
    CA[i,3] = x5[i]
  
  x5 = np.flip(x5)
  
  tempList = []
  for i in range(0,3):
    tempList.append(CA[i+3,11])
  
  tempList2 = np.flip(tempList)
  
  for i in range(0,3):
    CA[i+6,3] = tempList2[i]
  
  for i in range(0,3):
    CA[i+3,11] = x5[i]
  
  return CA

# Rotate the Left Face the Other Way to LRotate
def LDashRotate(CA):
  tempArr = []

  for i in range(3,6):
    for j in range(0,3):
      tempArr.append(CA[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(temp2)


  for i in range(0,3):
    for j in range(0,3):
      CA[i+3,j] = temp2[i,j]

  return(CA)


# Combine LDashTurn and LDashRotate
def LDash(CA):
  CA = LDashTurn(CA)
  CA = LDashRotate(CA)
  return CA


# Turn the middle layer for l turn
def lTurn(CA):
  x5 = np.array(CA[0:9,4])

  temp = x5[6:9]
  temp = np.array(temp)
  temp = np.flip(temp)

  x5 = x5[0:6]

  temp2 = np.array(CA[3:6,10])
  temp2 = np.flip(temp2)

  for i in range(0,3):
    CA[i,4] = temp2[i]

  for i in range(0,3):
    CA[i+3,10] = temp[i]

  for i in range(0,6):
    CA[i+3,4] = x5[i]
  
  return(CA)

# l Function
def l(CA):
  CA = lTurn(CA)
  CA = L(CA)
  return CA

# l2
def l2(CA):
  CA = l(l(CA))
  return CA


# l' Tunr center column
def lDashTurn(CA):
  x5 = []
  
  for i in range(0,9):
    x5.append(CA[i,4])
  
  x5 = np.roll(x5,-3)
  
  for i in range(0,6):
    CA[i,4] = x5[i]
  
  x5 = np.flip(x5)
  
  tempList = []
  for i in range(0,3):
    tempList.append(CA[i+3,10])
  
  tempList2 = np.flip(tempList)
  
  for i in range(0,3):
    CA[i+6,4] = tempList2[i]
  
  for i in range(0,3):
    CA[i+3,10] = x5[i]

  return CA

# l'
def lDash(CA):
  CA = lDashTurn(CA)
  CA = LDash(CA)
  return CA

# M
def M(CA):
  CA = rDashTurn(CA)
  return(CA)

# M'
def MDash(CA):
  CA = rTurn(CA)
  return CA


# M2
def M2(CA):
  CA = M(M(CA))
  return CA

# Front Face
def FRotate(CA):
  tempArr = []

  for i in range(3,6):
    for j in range(3,6):
      tempArr.append(CA[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(np.rot90(np.rot90(temp2)))


  for i in range(0,3):
    for j in range(0,3):
      CA[i+3,j+3] = temp2[i,j]

  return(CA)

# Shift edges around F Face
def FTurn(CA):
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CA[2,i+3])
    left.append(CA[i+3,2])
    right.append(CA[i+3,6])
    bottom.append(CA[6,i+3])

  temp = top
  top = np.flip(left)
  left = bottom
  bottom = np.flip(right)
  right = temp

  for i in range(0,3):
    CA[2,i+3] = top[i]
    CA[i+3,2] = left[i]
    CA[i+3,6] = right[i]
    CA[6,i+3] = bottom[i]

  return CA


# Combine FTurn and FRotate
def F(CA):
  CA = FTurn(CA)
  CA = FRotate(CA)
  return CA
  

# F2
def F2(CA):
  CA = F(F(CA))
  return CA


# Turn the edges for F' Turn
def FDashTurn(CA):
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CA[2,i+3])
    left.append(CA[i+3,2])
    right.append(CA[i+3,6])
    bottom.append(CA[6,i+3])

  temp = top
  top = right
  right = np.flip(bottom)
  bottom = left
  left = np.flip(temp)  

  for i in range(0,3):
    CA[2,i+3] = top[i]
    CA[i+3,2] = left[i]
    CA[i+3,6] = right[i]
    CA[6,i+3] = bottom[i]

  return CA

# Rotate the F face anticlockwise 90 degrees
def FDashRotate(CA):
  tempArr = []

  for i in range(3,6):
    for j in range(3,6):
      tempArr.append(CA[i,j])

  temp2 = tempArr
  temp2 = np.array(temp2)
  temp2 = temp2.reshape(3,3)
  temp2 = np.rot90(temp2)


  for i in range(0,3):
    for j in range(0,3):
      CA[i+3,j+3] = temp2[i,j]

  return(CA)

# Combine FDashTurn and FDashRotate into FDash
def FDash(CA):
  CA = FDashTurn(CA)
  CA = FDashRotate(CA)
  return CA



# Turn the centre horizontal layer
def fTurn(CA):
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CA[1,i+3])
    left.append(CA[i+3,1])
    right.append(CA[i+3,7])
    bottom.append(CA[7,i+3])

  temp = top
  top = np.flip(left)
  left = bottom
  bottom = np.flip(right)
  right = temp

  for i in range(0,3):
    CA[1,i+3] = top[i]
    CA[i+3,1] = left[i]
    CA[i+3,7] = right[i]
    CA[7,i+3] = bottom[i]

  return CA

# Combine fTurn with F into f
def f(CA):
  CA = fTurn(CA)
  CA = F(CA)
  return CA


# f2
def f2(CA):
  CA = f(f(Solved))
  return CA



# fDashTurn
def fDashTurn(CA):
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CA[1,i+3])
    left.append(CA[i+3,1])
    right.append(CA[i+3,7])
    bottom.append(CA[7,i+3])

  temp = top
  top = right
  right = np.flip(bottom)
  bottom = left
  left = np.flip(temp)  

  for i in range(0,3):
    CA[1,i+3] = top[i]
    CA[i+3,1] = left[i]
    CA[i+3,7] = right[i]
    CA[7,i+3] = bottom[i]

  return CA

# f'
def fDash(CA):
  CA = fDashTurn(CA)
  CA = FDash(CA)
  return CA



# Back Face Rotate
def BRotate(CA):
  BF = []
  for i in range(0,3):
    for j in range(0,3):
      BF.append(CA[i+3,j+9])

  BF = np.array(BF)
  BF = BF.reshape(3,3)
  BF = np.rot90(np.rot90(np.rot90(BF)))


  for i in range(0,3):
    for j in range(0,3):
      CA[i+3,j+9] = BF[i,j]


  return CA

# B Edge Rotation
def BTurn(CA):
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CA[0,i+3])
    left.append(CA[i+3,0])
    right.append(CA[i+3,8])
    bottom.append(CA[8,i+3])

  temp = top
  top = right
  right = np.flip(bottom)
  bottom = left
  left = np.flip(temp)  

  for i in range(0,3):
    CA[0,i+3] = top[i]
    CA[i+3,0] = left[i]
    CA[i+3,8] = right[i]
    CA[8,i+3] = bottom[i]

  return CA

# Combine BTurn and BRotate
def B(CA):
  CA = BRotate(CA)
  CA = BTurn(CA)
  return CA


# B2
def B2(CA):
  CA = B(B(CA))
  return CA


# B'
def BDashTurn(CA):
  top = []
  left = []
  right = []
  bottom = []

  for i in range(0,3):
    top.append(CA[0,i+3])
    left.append(CA[i+3,0])
    right.append(CA[i+3,8])
    bottom.append(CA[8,i+3])

  temp = top
  top = np.flip(left)
  left = bottom
  bottom = np.flip(right)
  right = temp

  for i in range(0,3):
    CA[0,i+3] = top[i]
    CA[i+3,0] = left[i]
    CA[i+3,8] = right[i]
    CA[8,i+3] = bottom[i]

  return CA

# B' Rotate Face
def BDashRotate(CA):
  BF = []
  for i in range(0,3):
    for j in range(0,3):
      BF.append(CA[i+3,j+9])

  BF = np.array(BF)
  BF = BF.reshape(3,3)
  BF = np.rot90(BF)


  for i in range(0,3):
    for j in range(0,3):
      CA[i+3,j+9] = BF[i,j]


  return CA

# Combine BDashTurn and BDashRotate into BDash
def BDash(CA):
  CA = BDashTurn(CA)
  CA = BDashRotate(CA)
  return CA


def b(CA):
  CA = fDashTurn(CA)
  CA = B(CA)
  return CA


def b2(CA):
  CA = b(b(CA))
  return CA

def bDash(CA):
  CA = fTurn(CA)
  CA = BDash(CA)
  return CA


# E functions
def E(CA):
  RA=np.roll(CA[4],3)
  CA[4] = RA
  return CA

def EDash(CA):
  RA=np.roll(CA[4],-3)
  CA[4] = RA
  return CA

def E2(CA):
  CA = E(E(CA))
  return CA



# S functions
def S(CA):
  CA = fTurn(CA)
  return CA

def SDash(CA):
  CA = fDashTurn(CA)
  return CA

def S2(CA):
  CA = S(S(CA))
  return CA



# Generate how many moves to apply
def numMoves():
  N = random.randint(1,5)
  return N

# Make an empty list N items long to fill with the moves
MovesToDo = [" "] * numMoves()

# Generate Moves
def genMoves(CA):  
  for i in range(len(CA)):
    CA[i] = random.randint(0,35)
  return CA

# Convert the numbers generated to the corresponding functions
def convToMove(CA):
  for i in range(len(CA)):
    j = CA[i]
    CA[i] = MovesList[j]
    
  return CA

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
             "B", "B2", "BDash", "E", "EDash", "E2", "S", "SDash", "S2"]


# Make another list that outputs what the user sees
MovesListForUser = ["U", "U'", "U2", "u", "u'", "u2", "D", "D'", "D2",
                   "d", "d'", "d2", "R", "R2", "R'", "r", "r2", "r'",
                   "L", "L2", "L'", "l", "l2", "l'", "M", "M2", "M'",
                   "F", "F2", "F'", "f", "f2", "f'", "B", "B2", "B'",
                   "E", "E'", "E2", "S", "S'", "S2"]



# Make a list of turns
def genList():
  list1 = convToMove(genMoves(MovesToDo))[0:len(MovesToDo)]
  return list1


# Apply the moves to the cube
def scrambleCube(CA):
  function = genList()
  for i in range(len(MovesToDo)):
    nextfunction = function[i]
    SA = eval(nextfunction)
    CA = SA(CA)
  return CA



# Look at the middle piece on the bottom face
def bottomCentre(CA):
  piece = CA[7,4]
  return piece

# Find the edges of the same colour
def locateEdges(CA):
  global Solved
  listEdges = [(),(),(),()]
  colour = bottomCentre(CA)
  for i in range(0,9):
    for j in range(0,12):
      if Solved[i,j][0] == colour[0]:
        if Solved[i,j][1] == "b":
          print("b",i,j)
          listEdges[0] = i,j
        elif Solved[i,j][1] == "d":
          listEdges[1] = i,j
        elif  Solved[i,j][1] == "f":
          listEdges[2] = i,j
        elif Solved[i,j][1] == "h":
          listEdges[3] = i,j
  return listEdges
  



def tempName(CA):
  global MovesList
  global Solved
  colour = bottomCentre(CA)
  if Solved[6,4][0] != colour[0] and Solved[6,4][1] != "b":
    for i in range(len(MovesToDo)):
      nextfunction = function[i]
      SA = eval(nextfunction)
      Solved = SA(Solved)
  
  
  return Solved




# Recursive approach
def bottomEdges(CA):
  global Solved
  global MovesList
  colour = bottomCentre(Solved)
  moveCount = 0
  
  while checkEdges(CA) == False:
    x = 0
    while x < 10:
      for i in range(x):
        pool=[MovesList]*(i+1)

        for n in itertools.product(*pool):
          function = []
          for a in range(x):
            function.append([])
          for j in range(len(function)):
            function[j] = n
            for move in n:
              t = eval(move)
              CA = t(CA)
              moveCount = moveCount + 1
              if checkEdges(CA) == True:
                print("Combinations attempted:",moveCount)
                print("Successful combination:",function[0])
                return CA
            CA = Solved
      x = x + 1
  return CA
      

  
def checkEdges(CA):
  colour = bottomCentre(Solved)
  if CA[6,4][0] == colour[0] and CA[6,4][1] == "b" and CA[8,4][0] == colour[0] and CA[8,4][1] == "h" and CA[7,3][0] == colour[0] and CA[7,3][1] == "d" and CA[7,5][0] == colour[0] and CA[7,5][1] == "f":
    return True
  else:
    return False


# Brute force corners into position
def corners(CA):
  colour = bottomCentre(CA)
  moveCount = 0
  while checkCorners(CA) == False:
    x = 0
    while x < 10:
      for i in range(x):
        pool=[MovesList]*(i+1)

        for n in itertools.product(*pool):
          function = []
          for a in range(x):
            function.append([])
          for j in range(len(function)):
            function[j] = n
            for move in n:
              t = eval(move)
              CA = t(CA)
              moveCount = moveCount + 1
              if checkCorners(CA) == True:
                print("Combinations attempted:",moveCount)
                print("Successful combination:",function[0])
                return CA
          CA = Solved
      x = x + 1
  return CA



# Check for corner and corresponding edge piece locations
def findCorners(CA):
  colour = bottomCentre(CA)
  cornerPositions = [(""),(""),(""),("")]
  for i in range(0,9):
    for j in range(0,12):
      if CA[i,j][0] == colour[0] and CA[i,j][1] == "a":
        cornerPositions[0] = i,j
      elif CA[i,j][0] == colour[0] and CA[i,j][1] == "c":
        cornerPositions[1] = i,j
      elif  CA[i,j][0] == colour[0] and CA[i,j][1] == "g":
        cornerPositions[2] = i,j
      elif CA[i,j][0] == colour[0] and CA[i,j][1] == "i":
        cornerPositions[3] = i,j
  return cornerPositions


def checkCorners(CA):
  colour = bottomCentre(CA)
  if CA[6,3][0] == colour[0] and CA[6,3][1] == "a" and CA[6,5][0] == colour[0] and CA[6,5][1] == "c" and CA[8,3][0] == colour[0] and CA[8,3][1] == "g" and CA[8,5][0] == colour[0] and CA[8,5][1] == "i":
    return True
  else:
    return False



# Locate the edge pieces that correspond with the corners found with findCorners
def findEdges(CA):
  corners = findCorners(CA)
  return corners



# Solve the edges and corners of the bottom face using brute force
def bottomFace(CA):
  moveCount = 0
  global MovesList
  while checkCorners(CA) == False or checkEdges(CA) == False:
    x = 0
    if x < 10:
      for i in range(x):
        pool=[MovesList]*(i+1)

        for n in itertools.product(*pool):
          function = []
          for a in range(x):
            function.append([])
          for j in range(len(function)):
            function[j] = n
            for move in n:
              t = eval(move)
              CA = t(CA)
              moveCount = moveCount + 1
              print(moveCount)
              if checkCorners(CA) == True and checkEdges(CA) == True:
                print("Bottom face solving sequence:",function[0])
                print(moveCount,"combinations attempted")
                return CA
          CA = Solved
      x = x + 1
  return CA

















def bruteForce(CA):
  global Solved
  global MovesList
  moveCount = 0
  while check() == False:
    x = 0
    while x < 20:
      for i in range(x):
        pool=[MovesList]*(i+1)

        for n in itertools.product(*pool):
          function = []
          for a in range(x):
            function.append([])
          for j in range(len(function)):
            function[j] = n
            for move in n:
              t = eval(move)
              CA = t(CA)
              moveCount = moveCount + 1
              if check() == True:
                return CA
              CA = Solved
      x = x + 1
  return CA






# Restore Solved State
def restore():
  global Solved
  global SafeSolved
  Solved = copy.deepcopy(SafeSolved)



# Output the Current State of 'Solved'
def solved():
  global Solved
  print(Solved)



# Check if Solved is the same as SafeSolved
def check():
  global Solved
  global SafeSolved
  return np.array_equal(Solved,SafeSolved)
# Only works first few runs, compares correctly,
# but SafeSolved is changed at some point, don't know where/what conditions



# Better check function
# Check each 3x3 face individually

top = (0,3,3,6)
front = (3,6,3,6)
bottom = (6,9,3,6)
left = (3,6,0,3)
right = (3,6,6,9)
back = (3,6,9,12)

def checkFace(CF):
  global Solved
  
  num1 = CF[0]
  num2 = CF[1]
  num3 = CF[2]
  num4 = CF[3]  
  
  face = Solved[num1:num2, num3:num4]
  middlePiece = face[1,1][0]
  for i in range(0,3):
    for j in range(0,3):
      if face[i,j][0] != middlePiece:
        return False
  return True



