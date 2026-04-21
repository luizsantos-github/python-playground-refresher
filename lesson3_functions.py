
# Functions def function_name:
def fib(n):
    """Prints a Fibonacci series less than n"""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()

fib(20)

# (1) Function (Default Argument Values)
def ask_ok(prompt, retries = 4, reminder='Please try again'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
#ask_ok('Are you sure you want to quit?', 3)

# (2) Keyword argument (means defining a parameter via keyword, can also be positional)
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)

    # *argument (receives many kind of parameters)
    for arg in arguments:
        print(arg)
    print("-" * 40)

    # **keyword (receives a dictionary)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
    "It's really very, VERY runny, sir.",
    shopkeeper="Michael Palin",
    client="John Cleese",
    sketch="Cheese Shop Sketch")


# Function Documentations
def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything:

        >>> my_function()
        >>>
    """
    pass

print(my_function.__doc__) # prints the function documentation
