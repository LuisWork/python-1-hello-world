name = 'Luis'
age = 30
text = f'Me llamo {name} y tengo {age} años'

print(text)

a = 5
b = 3

print(f"La suma de {a} y {b} es: {a + b}")

result = f'El precio es: {a * b} dolares'

print(result)

price = 50
txt = f'Este producto es muy {'Caro' if price > 50 else 'Barato'}'

print(txt)

fruit = 'Manzanas'
txt = f"Me encantan las {fruit.upper()}"

print(txt)

price = 59
txt = 'El precio es {price} dolares'

print(txt.format(price = 49))

txt = 'Óferta por solo {price:.4f} dolares'

print(txt.format(price = 60))