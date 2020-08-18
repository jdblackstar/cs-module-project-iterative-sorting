def print_list(arr):
    for thing in arr:
        print (thing)

# if we increase input size, how many more steps does this function need to take?

my_list = [1, 2, 3, 4, 5]

print_list(my_list)   # expect this function to run 5 times

longer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print_list(longer_list)   # expect this function to run 10 times

# doubled input size
# doubled steps
# one-to-one ratio
# linear
# 0(n)

def nested_loop(arr):
    for thing in arr:
        for other_thing in arr:
            print(thing, other_thing)

nested_loop(my_list) # expect this to take 25 steps

nested_loop(longer_list) # expect this to take 100 steps

# doubled input size
# quadrupled the steps!
# one-to-two ratio
# exponential

# count all the steps
# then caluclate Big O

def my_func(arr):
    a = 1
    b = 2
    c = a * b

    for x in range(1000):
        print(x)

    for thing in arr:
        x = 10
        y = 20
        z = x * y
        print(thing)

my_func(my_list)
my_func(longer_list)

# 3 + 1000 + (4 * len(arr))

# O(3 + 1000 + (4 (len(arr))))
# O(4 (len(arr)))
# O(len(arr))
# O(n) - BIG 'O'

# big O = 'on the order of'
# n, n**2, n**3

def two_loops(arr):
    for x in range(1000000000):
        z = x * x
        print(z)

    for thing in arr:
        print(thing)

    for thing in arr:
        print(thing_again)

# Big O?

# line by line walkthrough
# (big_num * 2) + len(arr) + len(arr)
# O(2 * n)
# O(n)

# just trying to find if we're dealing with n, n**2, or n**3, etc.
# this example was linear time complexity

def foo(n):
    sq_root = int(math.sqrt(n))
    for i in range(0, sq_root):
        print(i)

# 36 --> 6
# 100 --> 10
# 10000 --> 100
# O(log(n))

def bisect(n): # O(log(n))
    while n > 1:
        n = n / 2

def linear(n):
    while n > 1:
        n -= 1

# 16
# 8
# 4
# 2
# 1
# 2**4

# 800
# 400
# 200
# 100
# 50
# 25
# 12.5
# 6.25
# 3
# 1.5
# 0.75~

# (2**10)
# log_2 (16) --> (2**4)

def bar(x):
    sum = 0
    for i in range(0, 1463):
        i += 1
        for j in range(0, x):
            for k in range(x, x + 15):
                sum += 1

# 1463 * (1 + (n * (15 * 1)))
# 1463 * (1 + 15n)
# 1463 + (1463 + 15n)
# O(n)

def baz(array):
    print(array[1])
    midpoint = len(array) // 2
    for i in range(0, midpoint):
        print(array[i])
    for _ in range(1000):
        print('hi')

# 1 + 1 + n/2 + 1000
# 1002 + n/2
# O(n * 1/2)
# O(n)

# n == 2n == n * 1/2

# array of length 10 vs 100
## 5 vs 50

## increase input size
## compare the increase in the function steps

def make_num_pairs(n):
    for num_one in range(n):
        for num_two in range(n):
            print(num_one, num_two)

def make_item_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)

def simple_recurse(n):
    if n <= 1:
        return n 
    simple_recurse(n - 1)

simple_recurse(5) # 10 steps
simple_recurse(10) # 20 steps
# O(n)

def weird_recurse(num):
    if n<= 1:
        return n 
    simple_recurse(n - 1)
    simple_recurse(n - 1)
    simple_recurse(n - 1)

# double last time: O(n)?
# quadratic? O(n^2)
# exponential: 3^n