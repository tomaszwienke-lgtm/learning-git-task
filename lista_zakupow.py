zakupy = {
    'piekarnia': ['chleb', 'bułki', 'pączek'],
    'warzywniak': ['marchew', 'seler', 'rukola']
}

print('Lista zakupów')

for sklep, produkty in zakupy.items():
    sklep = sklep.capitalize()
    produkty = [produkt.capitalize() for produkt in produkty]
    print(f'Idę do {sklep}, kupuję tu następujące rzeczy: {produkty}.')

liczba_produktow = sum(len(produkty) for produkty in zakupy.values())
print(f'W sumie kupuję {liczba_produktow} produktów.')
