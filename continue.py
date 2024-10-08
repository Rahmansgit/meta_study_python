favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes one of my favorite desserts is', dessert)
        continue
    else:
        print('No sorry, not a dessert on my list')

# it will check each, even the condition becomes true, it will check entire things.  skip over a section of the loop but then continue on with the rest.