# Q1)	Create a class “Programmer” for storing information of few programmers working at Microsoft


# This is wrong approach 
# class programmer:
#     language = "python"
#     company = "microsoft"
#     age = 20

#     def __init__(self,name):
#         self.name = name
#         print(name,programmer.language,programmer.company,programmer.age)   #this line is the error you cannot just print output you need to store it in objects 

# s1 =programmer("Neel")
# s2 =programmer("zeel")


class programmer:
    
    company = "microsoft"          #class attribute
    

    def __init__(self,name,language,age):
        self.name = name                  #instance attributes
        self.language = language
        self.age = age

    #Printing should be a separate action, not inside __init__
    #__init__ → only initialize data
    # methods → perform actions
    def show(self):
     print(f"Hello my name is {self.name}, i am a {self.language} developer and my age is{self.age},and i work at     {self.company}")
s1 = programmer("Zeel","python",20)
        

s1.show()