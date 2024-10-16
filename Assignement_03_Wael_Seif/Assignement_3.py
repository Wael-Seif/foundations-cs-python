def countDigit(num):
   
    if num < 10:
     return 1
    else:
     return  1 + countDigit(num / 10)
    
    
def findMax(list1):
  
  length=len(list1)
  if length <= 1 :
   return list1[0]
      
  firstNum = list1[0]
  max = findMax(list1[1:])
    
  return firstNum if firstNum > max  else max
    
def countTags(html_code,tag):
   
      count = 0
      start_tag =  f"<{tag}>" # i used google to solve this exersice.
      end_tag =  f"</{tag}>"

      start_pos = html_code.find(start_tag)

      if start_pos == -1:
        return 0

      end_pos = html_code.find(end_tag, start_pos)

      if end_pos == -1:
        return 0

      count = 1 + countTags(html_code[end_pos + len(end_tag):], tag)

      return count


         

    
def displayMenu():
  print("Choose From The Menu please :\n" + "1-count Digits\n" + "2-find max\n" + "3-count tags\n" +
        "4-exit\n")
    

def mainFunction():
  displayMenu()
  choice = int(input("please enter your choice here: "))

  while (choice != 4):
    
    if (choice == 1):
     num=int(input("please enter a number: "))
     print(countDigit(num))
     break
     
     
    elif (choice == 2): 
     list1=[]
     n=int(input("please specify the length of the list: "))
     for i in range(n):
      num=int(input("please fill the list: "))
      list1.append(num)
     print(list1)
     print(findMax(list1))
     break
     
     
    elif (choice == 3):
      html_code="""
      <html>
      <head>
      <title>My Website</title>
      </head>
      <body>
      <h1>Welcome to my website!</h1> 
      <p>Here you ll find information about me and my hobbies</p>
      <h2>Hobbies</h2>
      <ul>
      <li>Playing guitar</li>
      <li>Reading books</li>
      <li>Traveling</li>
      <li>Writing cool h1 tags</li>
      </ul>
      </body>
      </html>"""

      tag=input("enter your tag please: ")
      print(countTags(html_code,tag))
      break
      
   
    else:
      print("this is an invalid choice ")
      displayMenu()
      choice = int(input("please enter your choice: "))
  displayMenu()
  choice = int(input("please enter your choice here: "))
    
  
mainFunction()
