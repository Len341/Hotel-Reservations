
class reservation_system:
    
    def manage_rooms(inDate,sublist_number,cost):#Three parameters (values which can be
        #different for different rooms etc.)The definition manages dates and
        #room prices according to customer input.

        #Globalizing two variables which i have declared in the main program(outside
        #my class and defintion), so for the python to know i want to manipulate or use
        #THAT variables and not new 'Local' variables that can only be seen inside the function
        
        global check_out_dates
        global amount_visitors
        global fair
        for i in cost:
            if i != 'R':
                fair+=i
        fair = int(fair)
        for x in rooms[sublist_number]:#refer to 'rooms' variable, a 2D list
            #the sublists are the lists inside my big 'rooms' list, first index (0) being
            #floor 1 and index (1) being floor 2 etc.
            #therefor the parameter sublist_number is used to identify which floor
            #is being referred to.

            #in this loop x refers to room numbers on which ever floor specified(sublist_number)
            if x in check_out_dates:
                #check out dates is my dictionary where keys are rooms being
                #currently used ands the keys values being the check out date
                #eg check_out_dates = {2: 12-09-2019, 6: 29-04-2020}

                #this statement checks if the room is in the dictionary (meaning it is in use)
    
                in_date = time.strptime(inDate, "%d-%m-%Y")
                out_date = time.strptime(check_out_dates[x], "%d-%m-%Y")
                #creating new date formats so that two dates can be compared to check
                #which is later
                #'inDate' is the date the new customer wants a room for
                #'check_out_dates[x]' will return the check out date found in
                #key values in my dictionary
                #key == room num which is unavailable
                #key's value == room's check out date
                #Therefor, x = room num and if you add key after dictionary name
                #the key's value will be returned, in this case the date.
                if in_date >= out_date:
                    check_out_dates.pop(x)
                    #if check in date is later than check out date the room will be
                    #made available to the customer
                else:
                    continue
                    #otherwise we continue with next loop so that room availability is not
                    #printed(as it will not be available at that time)


            print('Room',x,'is available at ',cost,' per night')
            #if room is available this print block will run

    def validate_date(date):
        while date[2]!='-' or date[5]!='-':
            date = input('Please enter date in correct format\nFormat: d-m-y: (02-04-2019): ')

import time,random
from datetime import datetime
fair = ''
rooms = [['1','2','3','4','5'],['6','7','8','9','10'],['11','12','13','14','15']]
check_out_dates = {}


while True:
    print('Welcome to Los Santos Hotel\n')
    name = input('Enter your name: ')
    surname = input('Enter your surname: ')
    id = input('Enter your ID number: ')
    tel = input('Enter your telephone number: ')
    while len(tel)!=10:
        tel = input('That\'s not a valid telephone number\nTry re-entering: ')
    email = input('Enter your email [optional]: ')
    if '@' in email:
        notify = input('Do you want to be notified about specials etc. with email? ')
    else:
        notify = input('Do you want to be notified about specials etc. with telephone number? ')

    check_in = input('Enter check-in date eg.[day-month-year]: ')
    reservation_system.validate_date(check_in)
    check_out = input('Enter check-out date eg.[day-month-year]: ')
    reservation_system.validate_date(check_out)

    #Not yet implemented data validation so input has to be in same format as
    #example

    #Getting the amount of days to stay 
    date_zero = datetime.strptime(check_in,'%d-%m-%Y')
    date_one = datetime.strptime(check_out,'%d-%m-%Y')
    diff = date_one - date_zero
    days = diff.days
    
    amount_visitors = int(input('Enter amount of people to visit: '))
    while amount_visitors > 10:
        amount_visitors = int(input('You cannot book more than 10 people\nPlease enter at most 10 visitors: '))

    if amount_visitors <= 2:
        reservation_system.manage_rooms(check_in,0,'R100')
        #This line calls my class, then in that class calls my definition
        #I then enter parameters which corresponds to this amount of visitors
        floor = 1
    elif amount_visitors <= 4:
        reservation_system.manage_rooms(check_in,0,'R250')
        floor = 1
    elif amount_visitors <= 6:
        reservation_system.manage_rooms(check_in,1,'R400')
        floor = 2
    elif amount_visitors <= 8:
        reservation_system.manage_rooms(check_in,1,'R750')
        floor = 2
    else:
        reservation_system.manage_rooms(check_in,2,'R950')
        floor = 3
    room_selected = input('Enter room to book: ')

    print('Are you sure you want to book room',room_selected,'? ')
    answer = input()
    #validating room input
    while answer != 'yes' and answer!= 'Yes' and answer != 'YES' and answer!= 'Y' and answer!= 'y':
         room_selected = input('Enter room to book: ')
         print('Are you sure you want to book room',room_selected,'? ')
         answer = input()

    check_out_dates[room_selected] = check_out
    #this line creates new element in my dictionary if a room has been booked

    print('\n____BOOKING INFORMATION____\nCustomer:',name,surname,
          '\nID number:',id,'\nRoom number:',room_selected,'\nFloor number:',floor,
          '\nTotal cost for your stay:','R'+str(int(abs(days*fair))),
          '\nReference number:',random.randint(3000,4000))

    print('\nThank you for booking!\n\nSee you soon!\n')



        
