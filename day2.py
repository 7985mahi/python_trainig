# my_data = " mahendra is a good player"
# for x in my_data:
#     print(x, end="")
# print("\n")
# my_data = "kohli is also a good player"
# for data in my_data:
#     print(data, end="*")
# print("\n")
#
# my_data = "rohit is good opening batsman"
# for data in my_data:
#     print(data, end=" ")
#
# two things that work for "for loop"
# first one is __iter__(it holds the state ) and __next__(it pushes to next element )

# my_data = "Rohit is good sports person"
# counter = 0
# for data in my_data:
#     counter += 1
#     print(counter)
# print("\n")
#
# my_data = "Rohit is good sportsperson"
# counter = 0
# for data in my_data:
#     counter += 1
# print(counter)
# print(len(my_data))


#
# my_data = "Rohit is good sportsperson"
# for x in enumerate(my_data):
#     print(x,end="")
#
# print("\n")
# my_data = "Rohit is good sportsperson"
# for x,y in enumerate(my_data):
#     print(x,end=" ")
#
# print("\n")
#
# my_data = "Rohit is good sportsperson"
# for x,y in enumerate(my_data):
#     print(x,y,end=" ")
#
# print("\n")
#
# my_data = "Rohit is good sportsperson"
# for x,y in enumerate(my_data):
#     print(y,end="")
#
# print("\n")
# my_data = "Rohit is good sportsperson"
# for x in enumerate(my_data):
#     print(x[1])

#
# my_data = "Rohit is good sportsperson"
# for x in my_data:
#     if(x=="i"):
#         print("success")
# print("\n")
# my_data = "Rohit is good sportsperson"
# for x in my_data:
#     if (x == "i"):
#         print(x,"success")
#     else:
#         print(x,"failure")
# print("\n")
#
# my_data = "Rohit is good sportsperson"
# for x in my_data:
#     if (x == "i"):
#         print(x,"success")
#     elif(x=="n"):
#         print(x,"success")
#     else:
#         print(x,"failure")
# print("\n")
#
# my_data = "Rohit is good sportsperson"
# for x in my_data:
#     if (x == "i") or (x=="n"):
#         print(x,"success")
#     else:
#         print(x,"failure")
#

# my_data = "Rohit is good sportsperson"
# for x in enumerate(my_data):
#     if x[1]=="i" or x[1]=="n":
#         print(x[1],"success")
#     else:
#         print(x[1],"failure")
#
# print("\n")
#
# my_data = "Rohit is good sportsperson"
# for x,y in enumerate(my_data):
#     if y=="i" or y=="n":
#         print(x,"success",y)
#     else:
#         print(x ,"failure", y)
# print("\n")
# my_data = "Rohit is good sportsperson"
# for x,y in enumerate(my_data):
#     if x%2==0 :
#         print(x,"success",y)
#     else:
#         print(x ,"failure",y)



#
# my_data = "Rohit is good sportsperson"
# for x,y in enumerate(my_data):
#     if y=="i":
#         print(y,"success")
#         break
#     else:
#         print(y,"failure")
# print("\n")
#
#
# my_data = "Rohit is good sportsperson"
# for x,y in enumerate(my_data):
#     if y=="i":
#         print(y,"success")
#         break
# else:
#     print("condition check")
# print("\n")
# # here the for loop id running without any immediate termination of for loop.
# #  so here else statement works after the completion of for loop
# my_data = "Rohit is good sportsperson"
# for x,y in enumerate(my_data):
#     if y=="i":
#         print(y,"success")
#         # break
# else:
#     print("condition check")
#
#


#  for loop using the range
# for i in range(10):
#     print(i,end=" ")
# print("\n")
# for x in range(2,10):
#     print(x, end=" ")
# print("\n")
# for j in range(0,20,2):
#     print(j,end=" ")
# print("\n")
# for j in range(10 ):
#     if(j%3==0):
#         print(j,end=" ")
#
# print("\n")
# out=""
# for x in range(10):
#     if(x%2==0):
#         print(x)
#         out=out+str(x)
# print(out)
#
# print("\n")
# out=0
# for j in range(5):
#     if(j%2==0):
#         out+=j
# print(out)




# my_data="india is history"
# c=0
# for x in my_data:
#     if(x=="i"):
#         c+=1
# print(c)

# so here var have intial length is 8 so for loop will run to legth 8 not more than that
# var="mahendra"
# for c in var:
#     y=c.upper()
#     var=var+y
# print(var)

#it will run to infinite because the list will apooend with new uppercase letter so it will expand . so loop will not stop
# var=["a","b","c"]
# for c in var:
#     y=c.upper()
#     var.append(y)
# print(var)

# var=["a","b","c","d"]
# for x,y in enumerate(var):
#
#     var.pop(x)
# print(var)



# List Compreshension
# out=[]
# for x in range(9):
#     if(x%2==0):
#         out.append(x)
# print(out)
#
#
# print("\n")
# out=[x for x in range(9) if x%2==0] here we are doing operation within list
# print(out)

# out=list(x for x in range(9) if x%3==0)
# print(out)


# s="mahendra123"
# if s.isalnum():
#     print("true")
#
# s1= ("mahi","dhoni","captain cool")
# x = " ".join(s1)
# print(x)
# print(type(x))
#
# s2="mahi is captain cool.and   he is best captain in the world"
# t=s2.partition("captain")
# print(t)
# print(type(t))

# s2="mahi is captain cool.and   he is best captain in the world"
# t=s2.rpartition("captain")
# print(t)
# print(type(t))
#
# s3="Hey there I am Mahendra ratHORE"
# s3=s3.swapcase()
# print(s3)



# for loop in dictionary
#
# var={"name":"mahendra","age":23}
# for x in var:
#     print(x)

# var = {"name": "mahendra", "age": 23}
# for x in var.items():
#     print(x)
#
# var = {"name": "mahendra", "age": 23}
# for x in var.values():
#     print(x)
#
# var = {"name": "mahendra", "age": 23}
# for x in var.keys():
#     print(x)


# d={}
# for i in range(4):
#     # if i not in d:
#     d[i]=i*i
# print(d)

# d={x:x+x for x in range(5)}
# print(d)

# var=[1,"a",2,"b",3,"c"]
# var1={}
# for x in range(len(var)):
#     if(x%2==0):
#         var1[var[x]]=var[x+1]
# print(var1)
#

# # another way to do this
# var=[1,"a",2,"b",3,"c"]
# out=iter(var)
# fina=dict(zip(out,out))
# print(fina)


# /comvert string to dictionary
# import json
# my_data='{"name":"dhoni","age":33}'
# output=json.loads(my_data)
# print(output)
# print(type(output))
#
# my_data={"name":"mahendra","age":23}
# out=json.dumps(my_data)
# print(out)
# print(type(out))


# Seesion start from 2pm to 6pm on day2
# Function definitions with no arguments
# def func():
#     print("welcome to function")
#     print("u are calling function func")
# func()

# def func(name):
#     print("welcome "+name + " to the function")
#     print("u are calling function func")
# func("dhoni")
#
# def func(name):
#     print("welcome  to function",name)
#     print("u are calling function func")
# func("dhoni")
# func(["mahendra","rathore"])
# func(23)

# def func(name ):
#     if isinstance(name,str):
#         print("welcome to function which takes only string",name)
#         print("u are calling function func")
# func("string")
# # func(23)
#
# def func(name,country ):
#     if isinstance(name,str):
#         print("welcome to function which takes only string",name,country)
#         print("u are calling function func")
# func("dhoni","india")
# func(23,"india")
#

# def func(name,country ):
#     if isinstance(name,str) and (isinstance(country,str) or isinstance(country,list) ):
#         print("welcome to function which takes only string",name,country)
#         print("u are calling function func")
# func("dhoni","india")
# func("kohli","india")
# func("virat",["rohit","mahendra"])



# def func(name,country="" ):
#     # if isinstance(name,str) and (isinstance(country,str) or isinstance(country,list) ):
#         print("welcome to function which takes only string",name,country)
#         print("u are calling function func")
# func("dhoni")
#
# def func(name,country=None ):
#     # if isinstance(name,str) and (isinstance(country,str) or isinstance(country,list) ):
#         print("welcome to function which takes only string",name,country)
#         print("u are calling function func")
# func("dhoni")
#
#
# def func(name,country="India" ):
#     # if isinstance(name,str) and (isinstance(country,str) or isinstance(country,list) ):
#         print("welcome to function which takes only string",name,country)
#         print("u are calling function func")
# func("dhoni")
#
# def func(name="mahendra",country="india" ):
#     # if isinstance(name,str) and (isinstance(country,str) or isinstance(country,list) ):
#         print("welcome to function which takes only string",name,country)
#         print("u are calling function func")
# func()


#
# def func(name,country ):
#     # if isinstance(name,str) and (isinstance(country,str) or isinstance(country,list) ):
#         print("welcome to function which takes only string",name,country)
#         print("u are calling function func")
# func(country="india",name="mahendra")
#
# def func(name="dhoni",country):
#     # if isinstance(name,str) and (isinstance(country,str) or isinstance(country,list) ):
#         print("welcome to function which takes only string",name,country)
#         print("u are calling function func")
# func("indai")



# if u want to accept more than one data in single argument function then u have to put * before the parameter in funtion
# it takes all the arguments in the form of tuple elements
# def func(*players):
#     print(players)
# func("dhoni")
# func("ashwin","kohli")
# func("a","b","c")
#
# l=[]
# def func(*players):
#     print(players)
#     for x in players:
#         l.append(x)
# func("dhoni")
# func("ashwin","kohli")
# func("a","b","c")
# print(l)
#


# l=[]
# def func(**players):
#     print(players)
#     for x in players:
#         l.append(x)
# func(name="dhoni")
# func(name="ashwin",country="kohli")
# # func("a","b","c")
# print(l)




# def marks(mark1 , mark2):
#     total=mark2+mark1
#     return
# print(marks(100,80))
#
#
# def marks(mark1 , mark2):
#     total=mark2+mark1
#     return
#     print("welcome after return ")
# out=(marks(100,80))
# print(out)


#
# def marks(mark1 , mark2,name):
#     total=mark2+mark1
#     return total,name
#     print("welcome after return ")
# out=marks(100,80,"mahendra")
# out=marks(10,80,"dhoni")
# print(out[0],out[1])
# if(out[0]>100):
#     print(out[1]," scored first class")
# else:
#     print(out[1]," scored second class")



# FUNCTION SCOPING
# so here preference of data will be first local and second is global
#  so preference will be leg(local>enclosed>global)
# var=10
# def fun():
#     var=1000
#     print(var)
# fun()

# var=10
# def fun():
#     # var=1000
#     def func():
#         var=100
#         print(var)
#     func()
# print(var)
# fun()
# print((var))
#
#
# var=10
# def fun():
#     global var
#
#     var=100
#     print(var)
#     var=var+100
#
# print(var)
# fun()
# print(var)



#
# var=10
# def fun():
#     # global var
#
#     var=100
#     print(var)
#     var=var+100
#
# print(var)
# fun()
# print(var)



# it will go on till the recursion reach the maximum number
# def fun():
#     print("helloe")
#     fun()
# fun()

# i=0
# def fun():
#     global i
#     i=i+1
#     print("helloe",i)
#     if(i==100):
#         return
#     fun()
#
# fun()


# i=0
# def fun():
#     global i
#     i=i+1
#     print("helloe",i)
    # if(i==100):
    #     return
    # fun()
#     while(i<100):
#         fun()
#
# fun()


# i=0
# def fun():
#     global i
#     i+=1
#     print("hello",i)
#     if i<100:
#         fun()
# fun()

# var =[1,2,3,4,5]
# l=[]
# def fun(arg):
#     return arg*arg
# out=[fun(var[i]) for i in range(len(var))]
# print(out)



# var =[1,2,3,4,5]
# l=[]
# def fun(arg):
#     for x in arg:
#         out=x*x
#         l.append(out)
# fun(var)
# print(l)


# var =[1,2,3,4,5]
# l=[]
# def fun(arg):
#     return arg*arg
# for x in var:
#     out=fun(x)
#     l.append(out)
# print(l)


# important fact about the map using list

# var=[1,2,3,4,5]
# def fun(arg):
#     return arg*arg
# out=list(map(fun,var))
# print(out)


# def d(x):
#     return x*x
# print(d(2))
#
# # lambda function for above funtion
# double=lambda x:x*x
# print(double(3))


                      # Class
# 1) class is basically to have structure for yoy code
# 2) class can produce extendibility
# 3) class generally means collection of objects (anything that occupies memory)
#  4) class just an template or wrapper to keep the data's inside
#  5) chennai is class ,places in chennai is object
# 6) furniture is class , chair , table
# 7) unbounded class (deprecated) and bounded class(constructor)


# class My_class:
#     def Login(ip,pwd):
#         print(ip)
#         print(pwd)
#     def HostName(ip):
#         print(ip)
# My_class.Login("2.2.2.2",234)
# My_class.HostName("2.2.2.2")
#
#

# whenever we create  an object it create a different instance of memory
# class My_class:
#     def Login(ip,pwd):
#         print(ip)
#         print(pwd)
#     def HostName(ip):
#         print(ip)
# my_obj=My_class
# my_obj.Login("2.2.2.2",234)
# my_obj.HostName("2.2.2.2")


# class My_class:
#     def __init__(self,ip,pwd): instance initialised--> Instanitator
#         self.a=ip
#         self.b=pwd
#
#     def Login(mahendra):
#         print(mahendra.a)
#         print(mahendra.b)
#     def HostName(rathore):
#         print(rathore.a)
# my_obj=My_class("2.2.2.2",123)
# # My_class is a constructor
# # my_obj is a object reference (object instance-- single memory)
# # every constructor that gets created will have one hidden object as first argument
#
# my_obj.Login()
# my_obj.HostName()
#__init__ is the constructor
#means when ever you create constructor , this init will be automatically created
#if u need to datas to be initialised then you can use as i did in line no 625
#self is nothing but a name given to the object referenece which got created during cnonstructr
#data that suppose to get passed onto the function is not initialiased in common place


        # disadvantage of unbounded class
# data that suppose to get passed onto the funtion is not initialised in common place





# class My_class:
#     def fun(self):
#         print("welcome to my class")
# obj=My_class()
# obj.fun()

#
# class My_class:
#     def __init__(self):
#         print("init is executed")
#     def fun(self):
#         print("welcome to my class")
# obj=My_class()
# obj.fun()






# Day 3
# class My_class:
#     def __init__(self,book,laptop):
#         self.book=book
#         self.laptop=laptop
#     def moh(self,certifiacte):
#         print(self.book)
#         print(self.laptop)
#     def moh(self):
#         print(self.book)
#
# my_obj=My_class("python ","hp")
# my_obj=My_class("python certifiacates")




# class My_class:
#     def __init__(self,book,laptop):
#         self.book=book
#         self.laptop=laptop
#     def abh(self,certifiacte):
#         print(self.book)
#         print(self.laptop)
#     def moh(self):
#         print(self.book)
#
# my_obj=My_class("python ","hp")
# my_obj.abh("python certifiacates")
# my_obj.moh()



# class My_class:
#     """__author__:Mahendra
#         __data__: Aug 18 2021
#         Class contains function which takes arguments"""
#     def __init__(self,book,laptop):
#         self.book=book
#         self.laptop=laptop
#     def abh(self,certifiacte):
#         print(self.book)
#         print(self.laptop)
#     def moh(self):
#         print(self.book)
#
# my_obj=My_class("python ","hp")
# my_obj.abh("python certifiacates")
# my_obj.moh()
# print(my_obj.__doc__)



# access specifier -- Public, Private , Protected
# i have only public and private access modifier not the protected one
# class My_class:
#     """__author__:Mahendra
#         __data__: Aug 18 2021
#         Class contains function which takes arguments"""
#     def __init__(self,book,laptop):
#         self.book=book
#         self.laptop=laptop
#     def __abh(self,certifiacte):
#         print(self.book,certifiacte)
#         print(self.laptop)
#     def moh(self):
#         print(self.book)
#
# my_obj=My_class("python ","hp")
# my_obj.abh("python certifiacates")
# my_obj.moh()
#  and also we do not have method overloading




# class My_class:
#     """__author__:Mahendra
#         __data__: Aug 18 2021
#         Class contains function which takes arguments"""
#     def __init__(self,book,laptop):
#         self.book=book
#         self.laptop=laptop
#     def abh(s,certifiacte):
#         print(s.book,certifiacte)
#         print(s.laptop)
#     def moh(self):
#         print(self.book)
#
# my_obj=My_class("python ","hp")
# my_obj.abh("python certifiacates")
# my_obj.moh()

# class My_class:
#     def __init__(dhoni,book,laptop):
#         dhoni.book=book
#         dhoni.laptop=laptop
#     def abh(kohli,certificate):
#         print(kohli.book,certificate)
#         print(kohli.laptop)
#     def moh(self):
#         print(self.book)
# my_obj=My_class("python","hp")
# my_obj.abh("pythoncertificate")
# my_obj.moh()


# Inheritance in python
# class My_class:
#     def __init__(dhoni,book,laptop):
#         dhoni.book=book
#         dhoni.laptop=laptop
#     def abh(kohli,certificate):
#         print(kohli.book,certificate)
#         print(kohli.laptop)
#
# class Second_class(My_class):
#     def moh(self):
#         print(self.book)
# my_obj=Second_class("python","hp")
# my_obj.abh("pythoncertificate")
# my_obj.moh()


# here we cannot access the pricvate method
# class My_class:
#     def __init__(dhoni,book,laptop):
#         dhoni.book=book
#         dhoni.laptop=laptop
#     def abh(kohli,certificate):
#         print(kohli.book,certificate)
#         print(kohli.laptop)
#
# class Second_class(My_class):
#     def __moh(self):
#         print(self.book)
# my_obj=Second_class("python","hp")
# my_obj.abh("pythoncertificate")
# my_obj.moh()


# here we can access the private method by doing below

# class My_class:
#     def __init__(dhoni,book,laptop):
#         dhoni.book=book
#         dhoni.laptop=laptop
#     def abh(kohli,certificate):
#         print(kohli.book,certificate)
#         print(kohli.laptop)
#
# class Second_class(My_class):
#     def __moh(self):
#         print(self.book)
# my_obj=Second_class("python","hp")
# my_obj.abh("pythoncertificate")
# # my_obj.moh()
# my_obj._Second_class.__moh()




# here parent class access the def init of child method why?
# both trying to access common data in both the class that is written in init function
# we have to write one init either on the parent class or in child class to access the common data
#  python has a better touch in inheritance so it can share data from child to parent class

# class parent:
#     def m1(self):
#         print("parent class")
#         print(self.age)
# class child(parent):
#     def __init__(self,age):
#         self.age=age
#         print("child class object created")
#     def m2(self):
#         print("child class method created")
#         print(self.age)
#
# obj=child(23)
# obj.m1()
# obj.m2()


#
# class Rectangle :
#     def __init__(self,length,width):
#         self.legth=length
#         self.width=width
#     def area(self):
#         return 2*self.legth*self.width
#     def perimeter(self):
#         return 2*self.legth+2*self.width
# class square:
#     def __init__(self,length):
#         self.length=length
#
#     def area(self):
#         return self.length*self.length
#     def perimeter(self):
#         return 4*self.length
#
# Square=square(4)
# Square.area()
# rectangle=Rectangle(2,4)
# rectangle.area()
#
#
# class a:
#     def __init__(self,age):
#         self.age=age
#     def fun(self):
#         print("hello")
#         print(self.age)
#     def new(self):
#         print(self.age)
# class b(a):
#     def __init__(self,rank):
#         self.rank=rank
#         super().__init__(self.rank)
#     def fun(self):
#         print("hi")
#         print(self.rank)
#         print(self.age)
#
# B=b(33)
# B.fun()
# B.new()



# every class in python is inherited something that is object
# class A():
#     def fun(self):
#         print("hello")
# a=A()
# a.fun()

# class A(object):
#     def fun(self):
#         print("hello")
# a=A()
# a.fun()

# class A(object):
#     def __init__(self):
#         print("default constructor")
#     def fun(self):
#         print("hello")
# a=A()
# a.fun()
#
#
# class a:
#     def fun(self):
#         print("A")
# class b(a):
#     def fun(self):
#         print("B")
# class c(a):
#     def fun(self):
#         print("C")
# class d(b,c):
#     print("D")
#
# D=d()
# D.fun()
#
# here we preferenced the order of method by MRO(Method Resolution Order)
# class a:
#     def fun(self):
#         print("A")
# class b(a):
#     def fun(self):
#         print("B")
# class c(a):
#     def fun(self):
#         print("C")
# class d(b, c):
#     pass
# D = d()
# D.fun()



# Exception Handling
# try should at least one except method


# try:
#     var=10/0
#     print(var)
# except:
#     print("sorry for that")

# if u know the specific error then mention in the except method
# as many as except method as u want
# try:
#     var=10/0
#     print(var)
# except ZeroDivisionError:
#     print("sorry for zero division")
# except:
#     print("sorry for that")


# try:
#     var=10/0
#     print(var)
# except ZeroDivisionError as ex:
#     print(ex)
# except:
#     print("sorry for that")

# try:
#     var="a"/0
#     print(var)
# except ZeroDivisionError as ex:
#     print(ex)
# except TypeError as ex:
#     print(ex)
# except:
#     print("sorry for that")

# here we can caught only one error at a time
# try:
#     var = "a"/0
#     print(var)
# except (ZeroDivisionError,TypeError) as ex:
#     print(ex)
# except:
#     print("sorry for that")

# if u want to know what error will be then mention below
# try:
#     var=10+9
#     print(var)
# except Exception as ex:
#     print(ex)

# two important statement which is not mandatory to add in code
# when u get an error u have except statemnet as well as finally block
# but if u did not get any error then i have else block and also finally block

# try:
#     var=67/3
#     print(var)
# except Exception as ex:
#     print(ex)
# else:
#     print("u r in else statment")
# finally:
#     print("welcome to finally")
#
#



# how to write ur own exception(raise error)
# try :
#     var=10
#     if(var>5):
#         raise  IOError
# except IOError:
#     print("sorry")
#
# try :
#     var=10
#     if(var>5):
#         raise  IOError
# except IOError as ex:
#     print(ex)


# try :
#     var=10
#     if(var>5):
#         raise  IOError("this is my error")
# except IOError as ex:
#     print(ex)



# if u want user defined exception then create a classs with error name
# class Myerror(Exception):
#     pass
# try:
#     var=10
#     if var>3:
#         raise  Myerror
# except Myerror:
#     print("user defined error")


# here we have object in error class so to retrive the data of object we have
# to take ex.object_name through the error class name
# class Myerror(Exception):
#     meaning="user defined exception"
#     # print("nskjcdns")
# try:
#     var=10
#     if var>3:
#         raise  Myerror
# except Myerror as ex:
#     print(ex.meaning)



# day 3 after noon training
# importing module in python
