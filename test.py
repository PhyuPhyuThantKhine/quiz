#name = "Bro code"
#print(len(name))
#print(name*3)
#name = input("What is your name")
#print("Hello"+name)
#age = input("Enter your age")
#print("Age is"+str(age))
##################################  Import Math ############################################
import math
pi = 3.1415
a = 123
b = 234
c = 567
#print(round(pi))
#print(math.floor(pi))
#print(math.ceil(pi)
#print(abs(pi))
#print(pow(pi,2))
#print(max(a,b,c))
#print(min(a,b,c))

##################################  Slicing ############################################
  #Slicing = #options [ start: stop: step] {First Method}
name = "Phyu Phyu Thant Khine"
#f_name = name[0]
#print(f_name)
#f_name = name[0:3]
#print(f_name)
#f_name = name[0:4:2]
#if step=2(every second area)
#print(f_name)
  #Obj  Methhod
#slice = slice(2,-1)
#name1 = "phyu sin"
#print(name1[slice])

##################################  If Elif ############################################
#age = int(input("enter your age")
#if age>=18:
 #   print("You are adult now")
#elif age==100:
    #print("Woowwww")    
#else:


##################################  While Loop ############################################
#while 1==1:
#    print("Infinity")

#name = ""
#while len(name)==0:
#    name = input("What is your name")
#print("Hello"+name)


##################################  For Loop #########################################
#for i in range(10):
#    print(i)
#for i in range(3,9+1):
#    print(i)
#for i in range(3,10,2):
#    print(i)
#for i in "PhyuSin":
#    print(i)

################################## Timer with ForLoop############################################
#import time
#for seconds in range(10,0,-1):
#    print(seconds)
#    time.sleep(1) #For each one time eteration 
#print("Happy New Year")    

##################################  Nested  Loop ############################################
#row =int(input("HOw many rows"))
#column =int(input("How many columns"))
#symbol =input("Enter Symbol")
#for i in range(row):
#    for j in range(column):
#        print(symbol, end="")
#    print()   

##################################  Loop  Control############################################ 
##break=   used to terminate the loop entirely
##continue=  skip the next iteration of the loop
##pass=  does nothing but as a placeholder

####################################   List  ################################################
##List = store multiple items in Single Variable
#number = [234,344,677,987,908,231,546,732,187]
#print(number[0])
#for i in number:
#   print(i)
#number.append("234")
#number.pop()
#number.insert(2,600)
#number.sort()
#number.clear()

##################################  2D List ############################################
#drink = ["coffe","soda","cola"]
#dinner =["pizza","hambuger","hotdog"]
#desert =["cake","candy","ice"]
#food =[drink,dinner,desert]
#print(food[0])
#print(food[1][2])    

##################################  Tuples  ############################################
#student = ("Phyu",19,"Sin")  ###Tuples are ordered and unchangeable
#print(student.count("Phyu"))
#for x in student:
#    print(x)

##################################  Set ############################################
###unordered and unindexed values (No Duplicate Value)
#book ={"b1","b2","b3"}
#for x in book:
#    print(x)

##################################  Dictionary ############################################
###Changeable , unordered collection of unique key:value pairs

#pairs = {'koko':'mama','mg':'nyima','girl':'boy'}
#print(pairs['koko'])
#print(pairs['mg'])
#print(pairs.keys()) #display only key
#print(pairs.values()) #Only Value
#print(pairs.items()) #Display pairs(key : value)
#for key,value in pairs.items():
#    print(key,value)

##################################  Index Operator ############################################
###Give access to a sequence's elements (str,list,tuples)

#name = "Phyu Sin"
#if(name[0].isupper ()):
#    name = name.lower()
#print(name)    
#first_name = name[0:4].upper()
#print(first_name)
#last_character = name[-1]
#print(last_character)

##################################  Function ############################################
#def hello(name):
#    print("heeloooo  "+name)
#hello("pptk")

##################################  Return Statement ############################################ 

#def sum(n1,n2):
#    re=n1+n2
#    return re
#x=sum(6,8)
#print(x) 

##################################  Scope  ############################################ 

#name="phyu"   #Global scope(Available inside and outside of the function)
#def display():
#    name="pptk" #Locla scope(Available only inside tis function)
#    print(name)
#display()
#print(name)

##################################  args ############################################ 
### args= parameter that packs all the arguments into tuple  useful so that a function can accepts a varying amount of arguments

#def sum(*args):
#    total=0
#    args = list(args) # if you want to change the tuples , turn into List first As list are mutuable and tuple are immutable
#    args[0]=5
#    for i in args:
#        total+=i
#    return total
#print(sum(1,2,3,4,5))    

##################################  kwargs ############################################ 
### kwargs= parameters that packs all arguments into dictionary useful so that a function can accept a varying amount of keyword arguments

#def hello(**kwargs):
#    for key,values in kwargs.items():
#        
#        print(values,end=" ")
#hello(first="phyu",second="phyu",third="thant",fourth="khine")     

##################################  format Method ############################################ 
### str.format()= optional method that gives a user more control when displaying output

#name="phyuphyu"
#adj="Beautiful"
#number=345678
#print("Of course {} is very {}".format(name,adj)) #{} serve as a place holder #keyword argument
#                            #OR
#print("Of course!! {} is very {}".format("phyuphyu","Beautiful"))
#print("Of course!! {1} is very {0}".format(name,adj)) #positional argument
#text="Of course {} is very {}"
#print(text.format(name,adj))
#print("My name is {:20}.Nice to meet you".format(name)) #Add Padding
#print("My number is {:3f}".format(number)) # 3digit decimal
#print("My number is {:,}".format(number))
#print("My number is {:E}".format(number)) #Scientific Notation
#print("My number is {:X}".format(number)) #Hexadecimal
#print("My number is {:b}".format(number)) #Binary

##################################  Random Method ############################################ 

#import random
#x = random.randint(1,2)
#y=random.random()
#list =["aa","bb","cc","dd"]
#z=random.choice(list)
#card =[1,2,3,4,5,6,7,8,9]
#random.shuffle(card)
#print(card)
#print(x)
#print(z)
#print(y)

##################################  Exception Handling ############################################ 
#try:
#    numerator =int(input("Enter a number"))
#    denominator =int(input("Enter Denomator Number"))
#    result =numerator/denominator
#    print(result)
#except ZeroDivisionError:
#    print("Something worng")    
#except Exception:
#    print("Sorry Try Again")    
#except ValueError:
#else:
#    print(result)
#finally :
#    print("This will always Execute")
#    print("Enter Only Number Plzz")

##################################  File Detection ############################################ 

#import os
#path = "C:\\Users\\DELL\\Desktop\\text.txt"
#if os.path.exists(path):
#   print("That Location exist")
#else:
#    print("That isnot Exist")




        









