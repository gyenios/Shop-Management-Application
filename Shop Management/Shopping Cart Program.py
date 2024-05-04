# Shopping Cart Program
foods = []
prices = []
total = []

while True:
    food = input('Enter a food to buy (q to quit): ')
    if food.lower() == 'q':
        break
    else:
        price = float(input(f'Enter the price of a {food}: $ '))
        foods.append(food)
        prices.append(price)

print('''
    ----YOUR CART----
      ''')
print('   ITEM','  PRICE',sep='\t\t')

for i in foods:
    n = foods.index(i)
    print(f'{n+1}. {foods[n]:<15} {prices[n]}')
