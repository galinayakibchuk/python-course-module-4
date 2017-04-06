foo = [1, 2, 3, 4, 5]
odd_foo = []
def is_odd(x):
    return x % 2 == 1
for f in foo:
    if is_odd(f):
        odd_foo.append(f)
    print (odd_foo)

"""
Use list comprehension for this task
"""
foo = list([ i for i in range(1,6)])
print(foo)

"""
Use filter with lambda function for this task
"""
