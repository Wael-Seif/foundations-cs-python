#  Exersice 1: 
# def calculateFactorial(num):
#         fact=1
#         if num < 0 :
#             return 0
#         else:
#             list1=list()
#             for i in range(1, num+1):
#              fact = fact * i
#              list1.append(i)
#             print("input:",num,"output:",fact,list1)
  
# calculateFactorial(-1)



# Exercise 2:
# def findDivisors(num):
#     if num <= 0:
#         print("invalid number!!!")
#     else:
#         list1=list()
#         for i in range(1,num+1):
#             if num % i  == 0 :
#                 list1.append(i)
#         print("input: ",num,"output", list1)
                   
# nummber=int(input("enter your number: "))
# findDivisors(nummber)



# Exercise 3:
# def reverse(text):
#     reversedText = ""
#     for i in range(1, len(text) + 1):
#         reversedText += text[len(text) - i]
#     print("input:  ",text,"output: ",reversedText)
# input_Text=input("enter your text please: ")
# reverse(input_Text)


# Exercise 4:
# def evenList(newList):
#     even_List=[]
#     for i in range(len(newList)):
#         if newList[i] % 2 == 0:
#          even_List.append(newList[i])
#     print("input",newList,"Output is: ",even_List,end="")
            
        
     
# array_List = []
# number_of_items = int(input("how many number do you want to enter?: "))

# for i in range(number_of_items):
#   numbers= int(input("enter the numbers: "))
#   array_List.append(numbers)
# evenList(array_List)


# Exercise 5: 
# def check_Password(password):
#     has_digit = False
#     has_uppercase = False
#     has_lowercase = False
#     has_special_char = False

#     for char in password:
#         if char.isdigit():
#             has_digit = True
#         elif char.isupper():
#             has_uppercase = True
#         elif char.islower():
#             has_lowercase = True
#         elif char in ['#', '?', '!', '$']:
#             has_special_char = True

#     if len(password) >= 8 and has_digit and has_uppercase and has_lowercase and has_special_char:
#         print( "Strong password")
#     else:
#         print( "Weak password")

# user_text = input("Please enter your password: ")
# check_Password(user_text)

#Exercise 6: 