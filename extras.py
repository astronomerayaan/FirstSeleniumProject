# When a single variable is declared in the main body of the program,
# it will work as a global variable for functions
x = 300


def myfunc():
    global x # this changes the global variable x
    x = 200 # to 200
    print(x)


myfunc()

print(x)  # it is still 200
