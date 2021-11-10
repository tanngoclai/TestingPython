def get_start_time(booking_time, number_of_passenger):
    start_time = -1
    if (booking_time <= 23 and booking_time >= 0 and number_of_passenger >= 1 and number_of_passenger <= 7):
        if (number_of_passenger <= 4):
            if (8 < booking_time <= 12):
                start_time = 12
            elif (12 < booking_time <= 16):
                start_time = 16
            else: 
                start_time = 8
        else:
            if (10 < booking_time <= 14):
                start_time = 14
            elif (14 < booking_time <= 18):
                start_time = 18
            else: 
                start_time = 10
    return start_time
    
if __name__ == '__main__':
    booking_time = int(input("Enter the time you booked your trip (format 24h): "))
    number_of_passenger = int(input("Enter number of passengers joining your trip: "))

    start_time = get_start_time(booking_time, number_of_passenger)
    if (start_time >= 0):
        print("Your trip starts {} at o'clock".format(start_time))
    else: 
        print("Invalid input")