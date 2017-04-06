"""
Create function num_sum() with two arguments:
default sum initialized with zero and nums which is variable lenght argument.
Invoke function defined above with different amount of passed numbers as right-hand operand
in assignment expression of initializing new objects.
"""
def num_sum(*nums, sum=0 ):
    try:
        for num in nums:
            sum += num
    except:
        pass
    return sum

def odd_numbers(*nums):
    odds = []
    try:
        for num in nums:
            if num % 2 != 0:
                odds.append(num)
    except None:
        pass
    return odd_numbers

sum_1 = num_sum(10, 12, 15)
sum_2 = num_sum(125, 7568)
sum_3 = num_sum(95632, 458, 12, 3658)
sum_4 = num_sum()

for sum in [sum_1, sum_2, sum_3, sum_4]:
    print(sum)

