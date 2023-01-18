# TUPLES
# Son inmutables, no se pueden modificar.

letras = ("A","B","C")
letra_a, letra_b, letra_c = letras

# NAMED TUPLES

from collections import namedtuple
Stock = namedtuple("Stock", ["symbol","current","high","low"])
stock = Stock("FB", 180.50, 200, 145.25)
high = stock.high

# DATACLASSES
# Otra manera de definir objetos con propiedades.
# No se le puede agregar funcionalidad.
# Con order=True le agrego la posibilidad de comparar entre dos objetos

from dataclasses import dataclass
@dataclass(order=True)
class StockDefault:
    name: str
    current: float = 0.0
    high: float = 0.0
    low: float = 0.0
    
stock_def_1 = StockDefault("FB")
stock_def_2 = StockDefault("FB", 177, 180, 175)

# DICTIONARIES

stocks = {
    "GOOG": (1250.20, 1242.54, 1231.06),
    "MSFT": (110.41, 110.45, 109.84),
}
goog = stocks.get("GOOG", "NOT FOUND")
stocks["GOOG"] = (1245.21, 1252.64, 1245.18)
stocks["IBB"] = (1500.21, 12540.64, 12450.18)

for stock, values in stocks.items():
    print(f"{stock} last value is {values[0]}")
    
# DEFAULTDICT

from collections import defaultdict
def letter_frequency(sentence):
    frecuencies = defaultdict(int)
    for letter in sentence:
        frecuencies[letter] += 1
    return frecuencies

print(letter_frequency("gewropnhnjofewijowfejwfoei"))

# COUNTER

from collections import Counter
def letter_freq(sentence):
    return Counter(sentence)

print(letter_freq("gewropnhnjofewijowfejwfoei"))
responses = ["vanilla","chocolate","vanilla","vanilla","caramel",
 "strawberry","vanilla"]
print(Counter(responses))

# SET
# Util cuando hay que eliminar duplicados

song_library = [
    ("Phantom Of The Opera", "Sarah Brightman"),
    ("Knocking On Heaven's Door", "Guns N' Roses"),
    ("Captain Nemo", "Sarah Brightman"),
    ("Patterns In The Ivy", "Opeth"),
    ("November Rain", "Guns N' Roses"),
    ("Beautiful", "Sarah Brightman"),
    ("Mal's Song", "Vixy and Tony"),
    ]
artists = {artist for _,artist in song_library}
print(artists)