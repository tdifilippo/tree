class buildTree ():
 """Please run the code  with Python 3"""
 def __init__(self):
  """Class to build your own tree data structure"""
  self.root_status=False
  self.data_list=[]
  self.current_level=1
  
 def our_input(self, prompt):
  val=raw_input(prompt)
  return val
 
 def possible_parents(self):
  result=[]
  for i in range(self.current_level,self.current_level*2):
    if self.data_list[i]!=-999: result.append(i)
  return result

 def addNode(self,node):
  """The following function will add the node on the left side of the parent"""   
  val=self.possible_parents()
  if len(val)==0: 
   print ("Error: No parent available. Cannot add any value as a left node")
   return
  else:
   print ("\n")
   print ("---List of possible parents:")
   print ("---Index: " + str([data for data in val]))
   print ("---Value: " + str([self.data_list[data] for data in val]))
   print ("---Note: The above list shows the indexes and the values of the possible parents. Select the index for which you want to assign the current node as parent")
   while True:
    input_user=int(self.our_input(">>"))
    if input_user not in val: print ("Error: Incorrect input. Try Again")
    else: break
     
   input_value=int(self.our_input("---Enter the value for {} node with  parent {} >> ".format(node,self.data_list[input_user])))
   try:
    if node=="Left": self.data_list[input_user*2]=input_value
    elif  node=="Right": self.data_list[input_user*2+1]= input_value
    return
   except:
    print ("Error: No more space left. Please try again with a higher level/height value")
    return

 def changeLevel(self):
  #Asking the user if they want to continue on the same level or move to another level
  print ("---If you want to move to the  next level type N or S to stay on the same level")
  print ("---Note: Current level is {}".format(self.current_level-1))
  while True:       
   try:
    input_user = self.our_input(">> ")
    if input_user.lower()=="n": 
     self.current_level=self.current_level*2
     break
    elif input_user.lower()=="s": break
   except:
    print ("Error: Exception raised. Incorrect format")
   print ("Error: Incorrect input. Try Again")
  return 


 def addRoot(self):
  """The following function will add the data at root node"""
  self.root_status=True 
  input_user=self.our_input(">>Enter the value for root node >> ")
  self.data_list[1]=input_user
  print ("---Value added at root node\n")
  return

 def message(self):
  """The following function will handle the menu portion and after gathering the input from the user it will perform the corrospondng operations """
  print ("Type \"Add\" to add a node")
  print ("Type \"Show\" to view the current tree structure")
  print ("Type \"Exit\" to \"exit\" the program\n\n")

  try:
   input_user=self.our_input(">>") #Requesting the user for input
  except:
   print ("Error: Incorrect input")

  if input_user=="add": #1 if
   if self.root_status==False: #2 if
    print ("---The first node should be root")
    return self.addRoot()
   else: 
    try:
     input_user=self.our_input("---Type Left to enter a left node or Right to enter a right node >> ")
    except:
     print ("Error: Incorrect input")
    if input_user.lower()=="left": self.addNode("Left") #3 if
    elif input_user.lower()=="right": self.addNode("Right") #3 ends
    self.changeLevel() 
    #-------------2 if ends
  #---------------1 if ends
  elif input_user.lower()=="exit": return -1
  elif input_user.lower()=="show": 
    self.printTree(self.data_list)

 def printTree(self,arr):
  import sys
  i,k,j=1,1,1
  space=int((len(arr))/2)
  while i<len(arr):
   sys.stdout.write (space*" ")
   while k<=i:
    if arr[j]==-999: sys.stdout.write ("N")
    else: sys.stdout.write (str(arr[j]))
    sys.stdout.write (" ")
    j+=1
    k=k+1
    space-=1
   k=1
   i=i*2
   print ("\n")
		 
 def main(self):
  while True:
   try:
    user_input= int(self.our_input("Enter the height of your tree (Note: Level starts at 1) >> "))
    self.data_list=[-999 for i in range(0,2**user_input)] #Initializing the array based on the height of the tree
    break
   except: print ("Error: Incorrect Format. Try again")
  var_a=0
  while var_a!=-1:
   var_a=self.message() 
  

x=buildTree()
x.main()

