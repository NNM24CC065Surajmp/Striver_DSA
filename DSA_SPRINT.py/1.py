def greet(name):
    if name == "Suraj":
        print("Welcome back Suraj")
    else: 
        print("Hello", name)
for i in range(3):
    name = input("Enter your name: ")
    greet(name)