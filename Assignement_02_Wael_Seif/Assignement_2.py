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
  
# calculateFactorial(4)



# Exercise 2:
# def findDivisors(num):
#     if num <= 0:
#         print("invalid number!!!")
#     else:
#         list1=list()
#         for i in range(1,num+1):
#             if num % i  ==0 :
#                 list1.append(i)
#         print("input: ",num,"output", list1)
                   
        
# findDivisors(5)



# Exercise 3:
# def reverse(text):
#     reversedText = ""
#     for i in range(1, len(text) + 1):
#         reversedText += text[len(text) - i]
#     print("input:  ",text,"output: ",reversedText)
# reverse("abcdefg")


# Exercise 4:
# def evenList(newList):
#     for i in range(len(newList)):
#         if newList[i] % 2 == 0:
#             even_List=[]
#             even_List.append(newList[i])
#             print("Output is: ",even_List,end="")
            
        
     
# array_List = []
# number_of_items = int(input("how many number do you want to enter?: "))

# for i in range(number_of_items):
#   numbers= int(input("enter the numbers: "))
#   array_List.append(numbers)
# evenList(array_List)

#Exercise 5:

def check_String(word):
        
    
    
text=input("Please enter your text: ")
if len(text) > 10:
    print("please enter a text of 10 characters")



check_String(text)