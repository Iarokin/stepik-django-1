from random import randint


def counter_tours(dict, departure):
    counter = 0
    min_price = max_price = 0
    min_nights = max_nights = 0
    j = len(dict) + 1
    for i in range(1, j):
        if dict[i]['departure'] == str(departure):
            counter = counter + 1
            if dict[i]['price'] < min_price or min_price == 0:
                min_price = dict[i]['price']
            if dict[i]['price'] > max_price:
                max_price = dict[i]['price']
            if dict[i]['nights'] < min_nights or min_nights == 0:
                min_nights = dict[i]['nights']
            if dict[i]['nights'] > max_nights:
                max_nights = dict[i]['nights']
    found = {'departure': str(departure), 'counter': counter, 'min_price': min_price, 'max_price': max_price,
             'min_nights': min_nights, 'max_nights': max_nights}
    return found


def random_cards(dict):
    id_mass = [0, 0, 0, 0, 0, 0]
    i = 0
    cards = {}
    while i < 6:
        id = randint(1, 16)
        for j in range(len(id_mass)):
            if id_mass[j] == id:
                break
            if id_mass[j] == 0:
                id_mass[j] = id
                i = i + 1
                break
    for i in range(len(id_mass)):
        cards[id_mass[i]] = dict[id_mass[i]]
    return cards
