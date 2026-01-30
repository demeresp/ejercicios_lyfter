hotel = {'name':'Hotel de lo locoo!',
         'stars':'3',
         'rooms':[{'room': f'room{i}', 'precio': f'${80 + (i % 10)}'} for i in range(1, 31) ]}
print(hotel)