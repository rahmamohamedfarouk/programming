##threading
import threading
import time
def print_time(threadName,delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(threadName,"-----------",time.ctime())
t1=threading.Thread(target=print_time, args=("Thread 1",1))
t2=threading.Thread(target=print_time, args=("Thread 2",2))
t1.start()
t2.start()
t1.join()
t2.join()
print("done")


#################################

##threading
import threading
def print_cube(num):
    print("Cube: {}".format(num * num * num))
def print_square(num):
    print("Square: {}".format(num * num))
t1 = threading.Thread(target=print_square, args=(10,))
t2 = threading.Thread(target=print_cube, args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Done!")


###################################

##thread

import _thread
import time
def print_time(threadName,delay):
    count = 0
    while count < 3:
        time.sleep(delay)
        count += 1
        print(threadName,"-----------",time.ctime())
try:
    _thread.start_new_thread(print_time,("Thread 1",1)) # the first thread
    _thread.start_new_thread(print_time,("Thread 2",2)) # the second thread
except:
    print("this is an error")
while 1:
    pass


##############################

##Using Locks instead of Sleep:
import threading
from time import sleep, ctime
loops = [4,2]
def loop(nloop, nsec, lock):
    print( 'start loop ',nloop,' at time: ', ctime())
    sleep(nsec)
    print ('done loop ',nloop,' at time: ', ctime())
    lock.release()
if __name__=='__main__':
    print ('starting program at time: ', ctime())
    locks = []
    nloops = range(len(loops))
    for l in nloops:
        lock = threading.Lock()
        lock.acquire()
        locks.append(lock)
    for l in nloops:
        threading.Thread(target=loop, args=(l, loops[l], locks[l])).start()
    for l in nloops:
        while locks[l].locked():
            pass
    print ('done program at time: ', ctime())


##########################
##Simple Server-Client Program
##Server Side

from socket import *
s = socket(AF_INET,SOCK_STREAM) # next create a socket object
print ("Socket successfully created")

host ='127.0.0.1'
port = 40674

s.bind((host, port)) # the arguments in bind is in tuple format
print ("socket binded to ",port)
s.listen(5) # put the socket into listening mode
print ("socket is listening")
# a forever loop until we interrupt it or an error occurs
while True:
    c, addr = s.accept() # Establish connection with client.
    print ('Get connection from', addr )
    c.send(b'Thank you for connecting') # send a message to the client.
    c.close()

##Client Side

from socket import * # Import socket module
s = socket(AF_INET,SOCK_STREAM)
host ='127.0.0.1'
port = 40674
s.connect((host, port))
print(s.recv(1024))
s.close()

################################

##chat program (server-side)
from socket import *
try:
    s=socket(AF_INET, SOCK_STREAM)
    host="127.0.0.1"
    port=7002
    s.bind((host,port))
    s.listen(5)
    client, addr=s.accept()
    print("connection from", addr[0])
    while True:
        x=client.recv(2048)
        print("client : ",x.decode('utf-8'))
        y=input(" server : ")
        client.send(y.encode('utf-8'))
    s.close()
except error as e:
    print(e)
except KeyboardInterrupt :
    print("chat is terminated")

## (client-side)

from socket import *
try:
    s=socket(AF_INET, SOCK_STREAM)
    host="127.0.0.1"
    port=7002
    s.connect((host,port))
    while True:
        y=input("client : ")
        s.send(y.encode('utf-8'))
        x=s.recv(2048)
        print("server : ",x.decode('utf-8'))
    s.close()
except error as e:
    print(e)
except KeyboardInterrupt :
    print("chat is terminated")

#################################

##tkinter

from tkinter import *
parent = Tk()
parent.title("Students")
parent.geometry("300x200")
name = Label(parent,text = "Name : ")
name.grid(row = 0, column = 0,pady=10,padx=5)
e1 = Entry(parent)
e1.grid(row = 0, column = 1)
regno = Label(parent,text = "Regd No : ")
regno.grid(row = 1, column = 0,pady=10,padx=5)
e2 = Entry(parent)
e2.grid(row = 1, column = 1)
btn = Button(parent, text = "Submit")
btn.grid(row = 3, column = 1)
parent.mainloop()


####################
##tkinter

from tkinter import *
parent = Tk()
parent.title("Students")
parent.geometry("300x200")
name = Label(parent,text = "Name : ")
name.place(x=50,y=50)
e1 = Entry(parent)
e1.place(x=100,y=50)
regno = Label(parent,text = "Regd No : ")
regno.place(x=50,y=100)
e2 = Entry(parent)
e2.place(x=110,y=100)
parent.mainloop()

###################
##tkinter

from tkinter import *
from tkinter import messagebox
top = Tk()
top.geometry("300x200")
def fun():
    messagebox.showinfo("Hello", "Blue Button clicked")
btn1 = Button(top, text = "Red",bg="red",fg="white",width=10)
btn1.pack( side = LEFT)
btn2 = Button(top, text = "Green",bg="green",fg="white",width=10,height=5,
activebackground="yellow")
btn2.pack( side = TOP)
btn3 = Button(top, text ="Blue",bg="blue",fg="white",padx=10,pady=10,
command=fun)
btn3.pack( side = BOTTOM)
top.mainloop()


###################
##tkinter

from tkinter import *
top = Tk()
top.geometry("300x200")
tframe = Frame(top,width="100",height="100",bg="yellow")
tframe.pack()
lframe = Frame(top,width="100",height="50",bg="blue")
lframe.pack(side = LEFT)
rframe = Frame(top,width="100",height="50",bg="green")
rframe.pack(side = RIGHT)
btn1 = Button(tframe, text="Submit", fg="red")
btn1.place(x=10,y=10)
top.mainloop()

######################
##tkinter

from tkinter import *
top = Tk()
top.geometry("300x200")
lbl1 = Label(top, text="List of Colours",fg="red",bg="yellow")
lbl1.place(x=10,y=10)
lb = Listbox(top,height=5)
lb.insert(1,"Red")
lb.insert(2, "Yellow")
lb.insert(3, "Green")
lb.insert(4, "Blue")
lb.place(x=10,y=30)
lbl2 = Label(top, text="List of Fruits",fg="blue",bg="green")
lbl2.place(x=160,y=10)
lb1 = Listbox(top,height=5)
lb1.insert(1,"Mango")
lb1.insert(2, "Grapes")
lb1.insert(3, "Banana")
lb1.insert(4, "Berry")
lb1.place(x=160,y=30)
top.mainloop()


#####################
##tkinter

from tkinter import *
top = Tk()
top.geometry("300x200")
lbl1 = Label(top, text="List of Colours",fg="red",bg="yellow")
lbl1.place(x=10,y=10)
lb = Listbox(top,height=5)
lb.insert(1,"Red")
lb.insert(2, "Yellow")
lb.insert(3, "Green")
lb.insert(4, "Blue")
lb.place(x=10,y=30)
lbl2 = Label(top, text="List of Fruits",fg="blue",bg="green")
lbl2.place(x=160,y=10)
lb1 = Listbox(top,height=5)
lb1.insert(1,"Mango")
lb1.insert(2, "Grapes")
lb1.insert(3, "Banana")
lb1.insert(4, "Berry")
lb1.place(x=160,y=30)
top.mainloop()

#####################
##tkinter
import tkinter
from functools import partial
def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label_result.config(text="Result is %d" % result)
    return
root = tk.Tk()
root.geometry('400x200+100+200')
root.title('Simple Calculator')
number1 = tk.StringVar()
number2 = tk.StringVar()
labelTitle = tk.Label(root, text="Simple Calculator").grid(row=0, column=2)
labelNum1 = tk.Label(root, text="Enter a number").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Enter another number").grid(row=2,
column=0)
labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)
entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)
call_result = partial(call_result, labelResult, number1, number2)
buttonCal = tk.Button(root, text="Calculate",
command=callresult).grid(row=3, column=0)
root.mainloop()


################
##Design pattern
##Facade pattern with an example of WashingMachine"""

class Washing:
	'''Subsystem # 1'''

	def wash(self):
		print("Washing...")


class Rinsing:
	'''Subsystem # 2'''

	def rinse(self):
		print("Rinsing...")


class Spinning:
	'''Subsystem # 3'''

	def spin(self):
		print("Spinning...")


class WashingMachine:
	'''Facade'''

	def __init__(self):
		self.washing = Washing()
		self.rinsing = Rinsing()
		self.spinning = Spinning()

	def startWashing(self):
		self.washing.wash()
		self.rinsing.rinse()
		self.spinning.spin()

""" main method """
if __name__ == "__main__":

	washingMachine = WashingMachine()
	washingMachine.startWashing()

##Memento Method is a "Behavioral Design pattern"which provides the ability to restore an object to its previous state.


class Memento:


	def __init__(self, file, content):

		self.file = file     
		self.content = content

class X:
    """Constructor Function"""

    def __init__(self, file_path):
        """store the input file data"""
        self.file = file_path
        self.content = ""

    """Append the data into content attr"""

    def write(self, string):
        self.content += string

    """save the data into the Memento"""

    def save(self):
        return Memento(self.file, self.content)

    """UNDO feature provided"""

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


class Y:
    """saves the data"""

    def save(self, x):
        self.mem = x.save()

    """undo the content"""

    def undo(self, x):
        x.undo(self.mem)


if __name__ == '__main__':
    """create the caretaker object"""
    y = Y()

    """create the writer object"""
    x = X("GFG.txt")  # file = object , content = ""

    """write data into file using writer object"""
    x.write("First vision of Data\n")  # file = object , content = "First vision of Data \n"
    print(x.content + "\n\n")

    """save the file"""
    y.save(x)  # Memento file = object , content = "First vision of Data \n"

    """again write using the writer """
    x.write("Second vision of Data\n")  # file = object , content = "First vision of Data \n Second vision of Data"

    print(x.content + "\n\n")

    """undo the file"""
    y.undo(x)

    print(x.content + "\n\n")  # file = object , content = "First vision of Data "

##Adapter

class ClassA():
    "A Sample Class the implements IA"

    def method_a(self):
        print("method A")


class ClassB():
    "A Sample Class the implements IB"

    def method_b(self):
        print("method B")


class ClassBAdapter():
    "ClassB does not have a method_a, so we can create an adapter"

    def __init__(self):
        self.class_b = ClassB()

    def method_a(self):
        "calls the class b method_b instead"
        self.class_b.method_b()


# Before the adapter I need to test the objects class to know which
# method to call.
ITEMS = [ClassA(), ClassB()]
for item in ITEMS:
    if isinstance(item, ClassB):
        item.method_b()
    else:
        item.method_a()

# After creating an adapter for ClassB I can reuse the same method
# signature as ClassA (preferred)
ITEMS = [ClassA(), ClassBAdapter()]
for item in ITEMS:
    item.method_a()

##Factory Method is a Creational Design Pattern that allows an interface or a class to create an object,but lets subclasses decide which class or object to instantiate.

class ConcreteProductA():
    "A Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductA"



class ConcreteProductB():
    "A Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductB"



class ConcreteProductC():
    "A Class that implements the IProduct interface"

    def __init__(self):
        self.name = "ConcreteProductC"



class Creator:
    "The Factory Class"

    @staticmethod
    def create_object(some_property):
        "A static method to get a concrete product"
        if some_property == 'a':
            return ConcreteProductA()
        if some_property == 'b':
            return ConcreteProductB()
        if some_property == 'c':
            return ConcreteProductC()
        return None

# The Client
PRODUCT = Creator.create_object('b')
print(PRODUCT.name)

##The Builder Pattern is a creational pattern whose intent is to separate the construction of a complex object from its representation so that you can use the same construction process to create different representations.
from abc import ABCMeta, abstractmethod

class IBuilder(metaclass=ABCMeta):
    "The Builder Interface"

    @staticmethod
    @abstractmethod
    def build_part_a():
        "Build part a"

    @staticmethod
    @abstractmethod
    def build_part_b():
        "Build part b"

    @staticmethod
    @abstractmethod
    def build_part_c():
        "Build part c"

    @staticmethod
    @abstractmethod
    def get_result():
        "Return the final product"

class Builder(IBuilder):
    "The Concrete Builder."

    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append('a')
        return self

    def build_part_b(self):
        self.product.parts.append('b')
        return self

    def build_part_c(self):
        self.product.parts.append('c')
        return self

    def get_result(self):
        return self.product

class Product():
    "The Product"

    def __init__(self):
        self.parts = []

class Director:
    "The Director, building a complex representation."

    @staticmethod
    def construct():
        "Constructs and returns the final product"
        return Builder()\
            .build_part_a()\
            .build_part_b()\
            .build_part_c()\
            .get_result()

# The Client
PRODUCT = Director.construct()
print(PRODUCT.parts)

##Singleton Method is a type of Creational Design pattern that makes sure that only one instance of a class exists. such as db connection
import copy

class Singleton():
    "The Singleton Class"
    value = []

    def __new__(cls):
        return cls #override the classes __new__ method to return a reference to itself
        #return object.__new__(cls) #what would be the out? and why?

    # def __init__(self):
    #     print("in init")

    @staticmethod
    def static_method():
        "Use @staticmethod if no inner variables required"

    @classmethod
    def class_method(cls):
        "Use @classmethod to access class level variables"
        print(cls.value)

# The Client
# All uses of singleton point to the same memory address (id)
print(f"id(Singleton)\t= {id(Singleton)}")

OBJECT1 = Singleton()
print(f"id(OBJECT1)\t= {id(OBJECT1)}")

OBJECT2 = copy.deepcopy(OBJECT1)
print(f"id(OBJECT2)\t= {id(OBJECT2)}")

OBJECT3 = Singleton()
print(f"id(OBJECT3)\t= {id(OBJECT3)}")


####The Chain of Responsibility design pattern is a "behavioral design pattern" that allows an object to pass a request along a chain of handlers. Each handler in the chain decides either to process the request or to pass it along the chain to the next handler
class Request:
    def __init__(self, data):
        self.data = data
        self.valid = True

class RequestHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if self.successor:
            self.successor.handle_request(request)

class AuthenticationHandler(RequestHandler):
    def handle_request(self, request):
        if "token" not in request.data:
            request.valid = False
            print("Authentication failed")
        print("AuthenticationHandler Done.....")
        super().handle_request(request)

class DataValidationHandler(RequestHandler):
    def handle_request(self, request):
        if not request.valid:
            return
        if "data" not in request.data:
            request.valid = False
            print("Data validation failed")
        print("DataValidationHandler Done.....")
        super().handle_request(request)

class LoggingHandler(RequestHandler):
    def handle_request(self, request):
        if not request.valid:
            return
        print("Logging request")
        super().handle_request(request)

# Client code
if __name__ == "__main__":
    request = Request({"token": "abc123", "data": "some_data"})

    authentication_handler = AuthenticationHandler()
    validation_handler = DataValidationHandler(authentication_handler)
    logging_handler = LoggingHandler(validation_handler)

    logging_handler.handle_request(request)

    if request.valid:
        print("Request processing successful")
    else:
        print("Request processing failed")

from abc import ABCMeta, abstractmethod

class IObservable(metaclass=ABCMeta):
    "The Subject Interface"

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        "The subscribe method"

    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        "The unsubscribe method"

    @staticmethod
    @abstractmethod
    def notify(observer):
        "The notify method"

class Subject(IObservable):
    "The Subject (Observable)"

    def __init__(self):
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args):
        for observer in self._observers:
            observer.notify(*args)


###observe
class IObserver(metaclass=ABCMeta):
    "A method for the Observer to implement"

    @staticmethod
    @abstractmethod
    def notify(subject, *args):
        "Receive notifications"

class Observer(IObserver):
    "The concrete observer"

    def __init__(self, subject):
        subject.subscribe(self)

    def notify(self, *args):
        print(f"Observer id:{id(self)} received {args}")

# The Client
SUBJECT = Subject()
OBSERVER_A = Observer(SUBJECT)
OBSERVER_B = Observer(SUBJECT)

SUBJECT.notify("First Notification", [1, 2, 3])

SUBJECT.unsubscribe(OBSERVER_B)
SUBJECT.notify("Second Notification", {"A": 1, "B": 2, "C": 3})


##########################################

##flask
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
if __name__ == '__main__':
    app.run(debug = True)