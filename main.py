 #Using the for loop with Python Lists
            #For Loop 
#syntax:-
#for item in list_of_items:            
  #Do something to each item
#example:- 
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#   print(fruit)
# here, if you will see we have not assigned any thing to the variable "fruit",still it don't throw errors cuz, in "for loop" the things thats written in "something to", is a variable with nothing asssigned to it cuz "each item" gonna get assigned to it, one by one.   

               #Question
#  how to use addition and multiplication with the help of for loop and how to use len function with the help of for loop?
          #Solution(/w Example)
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# total_height = 0 
# for height in student_heights:
#  total_height += height #total height = total_height + height
# # print(total_height) 

# #Use len() with for loop
# no_of_std = 0
# for student in student_heights:
#   no_of_std += 1
# # print(no_of_std)    

#print(round(total_height/no_of_std))  

          #for loop, Range
#Syntax
# for number in range(a, b):
#  print(number)
#example
# for number in range(1, 11, 3): #By adding 3 in the end means the numbers will be written after the gap of 3 like 1 then 4 then 7 and then 10
#   print(number)

           #Sum of Number 1 to 100
# sum = 0           
# for number in range(1, 101):
#  sum += number
# print(f"The sum of number 1 to 100 is {sum}.") 

