a = "hello"
b = 'world'
c = '''a multiple
line string'''
d = """More
multiple"""
e = ("Three " "Strings "
 "Together")

s = "hello world"
s.count('l')
s.find('l')

s = "hello world, how are you"
s2 = s.split(' ')
'#'.join(s2)
s.replace(' ', '**')
s.partition(' ')

orders = [("burger", 2, 5), ("fries", 3.5, 1), ("cola", 1.75, 3)]
print("PRODUCT   QUANTITY  PRICE   SUBTOTAL")
for product, price, quantity in orders:
    subtotal = price * quantity
    print(
        f"{product:10s}{quantity: ^9d} "
        f"${price: <8.2f}${subtotal: >7.2f}"
        )
