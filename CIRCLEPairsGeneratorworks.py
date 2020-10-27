#  PROJECT:        Campers
################################CIRCLE##########
# Make constraint pairs for Leap
# make Pairs for  z  circular numbers
# starting at a



################### enter z here ########  
z = 21
#########################################


#offset 0 = none
a = 0
#################
i = 1
s = a + 1
pairs = 0


myString = "["


while i < z:
 
  j = str(i+a)
  k = str(i+1+a)
  myString = myString +"("+ j + ", " + k +" )"
  pairs = pairs + 1
  i += 1
  
  # comma between pairs
  myString = myString + ","
  
#last pair skip comma
j = str(i+a)
k = str(a + 1)

myString = myString +"("+ j + ", " + k +" )"
pairs = pairs + 1

#endcap
myString = myString +"]"

  
print("Formatted LINEAR  ADJACENT PAIRS CONSTRAINT")
print("Number of Nodes          ",z)
print("Starting point           ",s)
print("Number of pairs          ", pairs)
print ("")
print (myString)
print ("")
print("Copy and paste including end brackets into Generator")

    
