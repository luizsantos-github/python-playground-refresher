
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