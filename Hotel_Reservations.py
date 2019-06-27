
class reservation_system:
    
    def manage_rooms(inDate,sublist_number,cost):
        global check_out_dates
        global amount_visitors
        for x in rooms[sublist_number]:
            if x in check_out_dates:
                in_date = time.strptime(inDate, "%d-%m-%Y")
                out_date = time.strptime(check_out_dates[x], "%d-%m-%Y")
                if in_date >= out_date:
                    check_out_dates.pop(x)
                else:
                    continue


            print('Room',x,'is available at ',cost,' per night')

import time
import random

rooms = [['1','2','3','4','5'],['6','7','8','9','10'],['11','12','13','14','15']]
check_out_dates = {}

print('Welcome to Los Santos Hotel\n')
while True:
    name = input('Enter your name: ')
    surname = input('Enter your surname: ')
    id = input('Enter your ID number: ')
    tel = input('Enter your telephone number: ')
    email = input('Enter your email [optional]: ')
                    
    check_in = input('Enter check-in date eg.[13-02-2019]: ')
    check_out = input('Enter check-out date eg.[17-02-2019]: ')

    amount_visitors = int(input('Enter amount of people to visit: '))
    if amount_visitors <= 2:
        reservation_system.manage_rooms(check_in,0,'R100')

    elif amount_visitors <= 4:
        reservation_system.manage_rooms(check_in,0,'R250')

    elif amount_visitors <= 6:
        reservation_system.manage_rooms(check_in,1,'R400')

    elif amount_visitors <= 8:
        reservation_system.manage_rooms(check_in,1,'R750')

    else:
        reservation_system.manage_rooms(check_in,2,'R950')

    room_selected = input('Enter room to book: ')

    print('Are you sure you want to book room',room_selected,'?: ')
    answer = input()
    while answer != 'yes' and answer!= 'Yes' and answer != 'YES' and answer!= 'Y' and answer!= 'y':
         room_selected = input('Enter room to book: ')
         print('Are you sure you want to book room',room_selected,'?: ')
         answer = input()

    check_out_dates[room_selected] = check_out
    print('\nThank you for booking!\nYour reference number is',random.randint(3000,4000),'\n\nSee you soon')


        
