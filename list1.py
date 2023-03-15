colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])
# ---------------------------------------------------
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])
# -------------------------------------------------------
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")
    
# ----------------------------------------
number=[1,2,3,4,56,7]
if 24 in number:
    print("number is present")
else:
    print("number is not present")
#-------------------------------------------------------
#append
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors) 
# ---------------------------------------------------
# extend
colors.extend(number)
print(colors)
#----------------------------------------------------------------
# insert 
colors.insert(0,"orange")
print(colors)
# -------------------------------------------------------------
# remove element list
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
colors.pop()        #removes the last item of the list
print(colors)
colors.pop(2)       
# remove from perticuler position
colors.remove("Red")
# remove any elment form list
print(colors) 
# ------------------------------------------------------
# list comparision
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
# item (for item in names) if "o" in item
print(namesWith_O)
# ------------------------------------------------------
# accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)