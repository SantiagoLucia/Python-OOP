
# LEN 
lista = ["A","B","C","D","E","F"]
print(len(lista))

# REVERSED
for _ in reversed("in reverse order"):
    print(_, end="")
print()

# ENUMERATE
for index, item in enumerate(lista):
    print(f"{index+1}: {item}")
    
# I/O
from pathlib import Path
p = Path.cwd()
with open(p / "ejemplo.py") as file:
    for line in file:
        print(line, end="")
print()

# Variable arguments

def print_letter(*letters):
    for letter in letters:
        print(letter)
        
print_letter('A')
print_letter('A','B','C')

class Options:
    default_options = {
        'port': 21,
        'host': 'localhost',
        'username': None,
        'password': None,
        'debug': False,
        }
    def __init__(self, **kwargs):
        # self.options = dict(Options.default_options)
        # self.options.update(kwargs)
        self.options = {**Options.default_options, **kwargs}
    
    def __getitem__(self, key):
        return self.options[key]

options = Options(username="Santiago", password="santi1234")
print(options["username"])