# Numbers
sum = 2 + 2
print(sum)

mult = (50 - 5 * 6) / 4
print(mult)

# Using raw strings
print(r'C\this\name')

# String literals
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# Concat
prefix = 'Py'
print(prefix + 'thon')

# Indexes
word = 'Python'
print(word[0])
print(word[-1]) # counts from the right

# Substrings
word = 3 * 'ha'
print(word)

# Indexes
word = 'Carla'
print(word[:2])

print("""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
      """)

longString = 'This is a long ass string'
print(len(longString))

# Slicing
word = 'Python'
print(word[0:2]) # first position is included while the last is excluded
# Slices (start is always included and last is always excluded)

# Using an index out of bounds results into an error
# Out of range slices are handled gracefully

# Unlike strings, which are immutable, 
# lists are a mutable type, 
# i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)

# Simple assignments never copies data, any change will be
# seen through all other variables the refer to it.
rgb = ['Red', 'Blue', 'Green']
rgba = rgb
rgba.append('Alph')
print(rgb)

# However, slices returns a new list of the requested element
correct_rgba = rgba[:] # creates a shallow copy
correct_rgba[3] = 'Alpha'
print(correct_rgba)

# Slicing position
word = 'Python'
print(word[1:4])

# Nesting Lists
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][2])

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b