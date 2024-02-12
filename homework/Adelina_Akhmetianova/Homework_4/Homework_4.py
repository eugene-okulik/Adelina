my_dict = {'tuple': (1, 2, 3, 4, 5),
           'list': ['one', 'two', 3, 'four', 5],
           'dict': {'flower1': 'rose', 'flower2': 'daisy', 'flower3': 'lily', 'flower4': 'orchid', 'flower5': 'tulip'},
           'set': {1, 44, False, 4, 5}}
print(my_dict['tuple'][-1])
my_dict['list'].append(6)
my_dict['list'].pop(2)
my_dict['dict'][('i am a tuple',)] = 'no'
my_dict['dict'].pop('flower1')
my_dict['set'].add(55)
my_dict['set'].pop()
print(my_dict)
