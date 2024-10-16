# Exercise 1: 
# def SumTuples(tup1,tup2):
#     newTuple= tuple(map(sum, zip(tup1, tup2)))
#     return newTuple
# def exportJson(user_dict,user_file_Name):

#    json_object = json.dumps(user_dict, indent=4)
#    with open(user_file_Name, "w") as outfile:
#     outfile.write(json_object)
  
# def importJson(data):
#     return data
   
   
    
# def displayMenu():
#   print("Choose From The Menu please :\n" + "1-Sum Tuples\n" + "2-Export Json\n" + "3-Import Json\n" +
#         "4-exit\n"+"-----------\n")
    

# def mainFunction():
#   displayMenu()
#   choice = int(input("Enter a choice : "))

#   while (choice != 4):
    
#     if (choice == 1):
#         list1=[]
#         num1=int(input("please specify the length of the list1: "))

#         for i in range (num1):
#          n1=int(input("Enter the items of the first tuple please: "))
#          list1.append(n1)
#          tup1=tuple(list1)

#         list2=[]
#         num2=int(input("please specify the length of the list2: "))
#         if num1 == num2:
#          for i in range (num2):
#           n2=int(input("Enter the items of the first tuple please: "))
#           list2.append(n2)
#           tup2=tuple(list2)
#           print(SumTuples(tup1,tup2))
#         else:
#             print("The Length of the two list is not equal!!!")
#             break
        
     
#     elif (choice == 2):
#         user_dict = {}
#         num_entries = int(input("please specify the length of the dictionary: "))

#         for i in range(num_entries):
#          key=input("please enter the key: ")
#          value = input("please enter the value: ")
#          user_dict.update({key: value})
#         user_file_Name=input("please enter the name of the file:")
#         print(exportJson(user_dict,user_file_Name))
#         break

#     elif (choice == 3):
#          with open('test', 'r') as file:
#           data = json.load(file)
#           print(importJson(data))
#           break   
   
#     else:
#       print("this is an invalid choice ")
#       displayMenu()
#       choice = int(input("Enter a choice : "))
#   displayMenu()
#   choice = int(input("Enter a choice : "))
    
# import json
# print(mainFunction())


#Exercise 2:

# a. 1/6N+8000N3+24          O(N)
# b. 1/6N3                   O(N)
# c. 1/6N! +200N4            O(N!)
# d. NlogN +1000             O(NlogN)
# e. logN +N                 O(N)
# f. 1⁄2N(N-1)               O(N^2)
# g. N2+220NlogN2+3N+9000    O(N)
# h. N!+3N+2N+N3+N2          O(N!)

