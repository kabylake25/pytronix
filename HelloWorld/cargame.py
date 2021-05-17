car_started = False

while True:
    command = input('>').lower()
    if command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif command == 'start':
        if car_started:
            print('Car already started!')
        else:
            print('Car started... Ready to go!')
            car_started = True
    elif command == 'stop':
        if not car_started:
            print('Car already stopped!')
        else:
            print('Car stopped.')
            car_started = False
    elif command == 'quit':
        break
    else:
        print("I don't understand that...")
