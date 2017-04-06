"""
Create a function with default arguments and arguments unpack:
* Create string variable word
* Create dictionary variable ids
* Create function that include at least 2 arguments word and name from ids dictionary
* Function also should have one default argument age
* If additional arguments will added to function call it should work properly
* During first function calling use unpack arguments from dictionary ids
* During second call use ids key value and some range of values

"""


word = 'deep sense'

"""
Create dictionary variable ids
"""
ids = {'name': 'Bohdan', 'age': 20}

"""
Create function that include at least 2 arguments word and name from ids
dictionary
Function also should have one default argument age
If additional arguments will added to function call it should work properly
"""
def function(word, name, *args, age=None):
    print(word, name, sep='\n', end='\n\n')
    print('Age:', age if age is not None else 'age is not given', end='\n\n')
    print(args if len(args) > 0 else 'no args given', end = '\n\n')

"""
During first function calling use unpack arguments from dictionary ids
"""
function(word, **ids)

"""
During second call use ids key value and some range of values
"""
function(word, ids['age'], *list(range(10)))
function(word, ids['name'], 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)