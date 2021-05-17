weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    weight = weight * 0.45
    print(f'You are {weight} kilos')
elif unit.upper() == 'K':
    weight = weight / 0.45
    print(f'You are {weight} pounds')
else:
    print('Please provide (L)bs or (K)g')