#this one is like your script with argv

def print_two(*args):
    arg1,arg2 = args
    print(f"arg1: {arg1} , arg2:{arg2}")


#ok that *args is actually pointless we can do this without it.

def print_two_again(arg1,arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just take one argument

def print_one(arg1):
    print(f"arg1: {arg1}")

#this one take no arguements

def print_none():
    print("I got nothing")


print_two("prachi","Kiran")
print_two_again("prachi","Kiran")
print_one("Navish")
print_none()