# If else
#x = int(input("Please enter an integer: "))
x = 1
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Loops
words = ['cat', 'windows', 'defensive']

for w in words:
    print(w, len(w))

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# (1) Iteration in the same collection (iterate over a copy then update the original)
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

# (2) Create a new collection from the iteration source
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)


# Range (the given end point is never part of the general sequence)
print(list(range(5,10)))

# iterate over indices of a sequence
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(f'a length {len(a)}')

# break (breaks out of the innermost enclosing of a loop)
for n in range(2, 10):
    if n > 5:
        break
    print(n)

# continue (continues to the next iteration)
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")


# else in loops 
# executed if the loop finishes its final iteration
# executed if the loop's condition becomes false
for n in range(1, 11):
    for x in range(2, n):
        if n % x == 0:
            print (n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')


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


initial_types = ['water', 'fire', 'ground']
extended_types = ['dragon', 'fairy']

initial_types.extend(extended_types)
print(initial_types)

# list when using append is like a stack. appends add it to the last of the list

# whereas deque is first in, for out
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves
print(queue.popleft())          # The second to arrive now leaves
print(queue)                    # Remaining queue in order of arrival


# List Comprehensions
squares = [x**2 for x in range(10)]
print(squares)

# del (removes items from a list using index (can also be range))
a = [1, 2, 3, 4, 5]
del a[1:2]
print(a)

# Tuple (1, 232, 2323)
# number of values separated by comma.
# immutable
# but can contain mutable objects
t = 21, 'what', 23232, 4242
print(t)
u = t, (44, 44, 44)
print(u)

t = ['test', 2, 3]
print(t)

# Tuple  Usage: is heterogenous, means a single 'record' with different parts (name, age job)
# List Usange: a bunch of the same kind of thing


# Sets
# Unordered collection with no duplicate elements
# Basic Use: membership testing, eliminating duplicated entries
# Also supports mathematical operations
basket = {'apple', 'orange', 'banana', 'pear'}
print(basket)

print('mango' in basket) # simple membership testing
a = set('abracadabra')
b = set('alakazam')
print(a - b) # prints letter in a but not b
print(a | b) # prints members in a or b, or both (uniquely)
print(a & b) # letters in both a and b
print(a ^ b) # letters in a or b but not both

# Dictionaries - is a set of key and value pairs (requiring keys to be unique)
dict = {'code': '000001', 'name' : 'offer-sample'}

# adding
dict['description'] = 'this is a sample offer'
print(dict)

# retrieving
print(dict['code'])

# keys
print(list(dict))

# keys sorted
print(sorted(dict))

# key assertion
print('code' in dict)

# Iteration Techniques

# items()
chessPieces = {'knight' : 'the horse', 'queen' : 'tallest piece', 'king' : 'win condition'}
for k, v in chessPieces.items():
    print(k, v)

# sequence loops
for i,v in enumerate(['tic', 'tac', 'toe']):
    print(i , v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# loop eliminating duplicates and returning as set
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)