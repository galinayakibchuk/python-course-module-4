string_1 = input('Please, enter a first word:')
string_2 = input('Please, enter a second word:')
list_1 = [string_1, string_2]

def difference_amount(*strings):
    max_vallue = 0
    for string in strings:
        if len(string)> max_vallue:
            max_vallue = len(string)
    return max_vallue

print('max leng of passed strings is:{}'.format(difference_amount(*list_1)))
