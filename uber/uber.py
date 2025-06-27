import json

map = {"Kolkata":10, "Delhi": 20, "Bangalore": 30, "Mumbai": 40, "Darjeeling": 50, "Pune": 60}
map_keys = list(map.keys())
map_values = list(map.values())
vehicles = {"Bike": 0.75, "Auto": 1, "Cab":1.25, }

def load_data():
    try:
        with open('uber.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return[]
    
def save_data_helper(rides):
    with open('uber.txt', 'w') as file:
        json.dump(rides, file)

def open_map():
    print(map)

def book_ride(map, rides):
    current_location = input("Enter your current location: ")
    if current_location not in map:
        print("Invalid Location")
        return current_location
    destination = input("Enter your destination: ")
    if destination not in map:
        print("Invalid Destination")
        return destination
    distance = abs(map[destination] - map[current_location])
    choose_vehicle = input("Choose your vehicle: ")
    base_fare = distance*10
    final_fare = base_fare*vehicles[choose_vehicle]
    print("Your", choose_vehicle, "ride from", current_location, "to", destination, "of", distance, "kms, will cost you", final_fare,"rupees")
    confirmation = input("Please confirm your ride(yes/no): ")
    confirmation_lower = confirmation.lower()
    if confirmation_lower == "yes":
        print("\n")
        print("Your ride to", destination, "has been booked")
        rides.append({'current_location': current_location, 'destination': destination, 'distance': distance, 'vehicle':choose_vehicle, 'fare':final_fare})
        save_data_helper(rides)
    elif confirmation_lower == "no":
        return main()
    else:
        return main()

def cancel_ride(rides):
    ride_history(rides)
    index = int(input("Enter the video number to be cancelled: "))

    if 1<= index <= len(rides):
        ride = rides[index-1]
        del rides[index-1]
        print(f"{index}. {ride['current_location']} to {ride['destination']}, distance covered {ride['distance']}kms, for rupees {ride['fare']}, in a {ride['vehicle']} has been cancelled")
        save_data_helper(rides)
    else:
        print("Invalid ride index selected")

def ride_history(rides):
    print("\n")
    print("*" * 100)
    for index, ride in enumerate(rides, start=1):
        print(f"{index}. {ride['current_location']} to {ride['destination']}, distance covered {ride['distance']}kms, for rupees {ride['fare']}, in a {ride['vehicle']} ")
    print("*" * 100)

def create_profile():
    pass

def edit_profile():
    pass

def show_profile():
    pass

def main():
    rides = load_data()
    while True:
        print("\n Weclome to Uber")
        print("1. Open Map")
        print("2. Book a ride")
        print("3. Cancel a ride")
        print("4. History of rides")
        print("5. Create your profile")
        print("6. Edit your profile")
        print("7. Show profile")
        choice = int(input("Type your choice: "))

        if choice == 1:
            open_map()

        elif choice == 2:
            book_ride(map,rides)

        elif choice == 3:
            cancel_ride(rides)

        elif choice == 4:
            ride_history(rides)

        elif choice == 5:
            create_profile(rides)

        elif choice == 6:
            edit_profile(rides)
        
        elif choice == 7:
            show_profile(rides)
        
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()
