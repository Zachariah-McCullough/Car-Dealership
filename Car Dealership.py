import pickle  # Saving the current state of the inventory to a file. || Loading the inventory back, maintaining data persistence between program runs.

class Vehicle:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

class Car(Vehicle):
    def __init__(self, make, model, year, price, doors):
        super().__init__(make, model, year, price)
        self.doors = doors

    def get_doors(self):
        return self.doors

    def set_doors(self, doors):
        self.doors = doors


class Truck(Vehicle):
    def __init__(self, make, model, year, price, drive_type):
        super().__init__(make, model, year, price)
        self.drive_type = drive_type

    def get_drive_type(self):
        return self.drive_type

    def set_drive_type(self, drive_type):
        self.drive_type = drive_type


class SUV(Vehicle):
    def __init__(self, make, model, year, price, passenger_capacity):
        super().__init__(make, model, year, price)
        self.passenger_capacity = passenger_capacity

    def get_passenger_capacity(self):
        return self.passenger_capacity

    def set_passenger_capacity(self, passenger_capacity):
        self.passenger_capacity = passenger_capacity


def save_inventory(inventory):
    with open('inventory.pkl', 'wb') as file:
        pickle.dump(inventory, file)


def load_inventory():
    try:
        with open('inventory.pkl', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {
            "CARS": [],
            "TRUCKS": [],
            "SUVs": []
        }


def edit_vehicle(vehicle):
    print("\nEditing Vehicle:")
    print(f"Current Make: {vehicle.get_make()}")
    new_make = input("Enter new make (or press Enter to keep current): ")
    if new_make:
        vehicle.make = new_make
    
    print(f"Current Model: {vehicle.get_model()}")
    new_model = input("Enter new model (or press Enter to keep current): ")
    if new_model:
        vehicle.model = new_model

    print(f"Current Year: {vehicle.get_year()}")
    new_year = input("Enter new year (or press Enter to keep current): ")
    if new_year:
        vehicle.year = new_year

    print(f"Current Price: ${vehicle.get_price()}")
    new_price = input("Enter new price (or press Enter to keep current): ")
    if new_price:
        vehicle.set_price(float(new_price))  # Assuming price should be a float

    if isinstance(vehicle, Car):
        print(f"Current Doors: {vehicle.get_doors()}")
        new_doors = input("Enter new number of doors (or press Enter to keep current): ")
        if new_doors:
            vehicle.set_doors(int(new_doors))

    elif isinstance(vehicle, Truck):
        print(f"Current Drive Type: {vehicle.get_drive_type()}")
        new_drive_type = input("Enter new drive type (or press Enter to keep current): ")
        if new_drive_type:
            vehicle.set_drive_type(new_drive_type)

    elif isinstance(vehicle, SUV):
        print(f"Current Passenger Capacity: {vehicle.get_passenger_capacity()}")
        new_passenger_capacity = input("Enter new passenger capacity (or press Enter to keep current): ")
        if new_passenger_capacity:
            vehicle.set_passenger_capacity(int(new_passenger_capacity))


def main():
    # Load inventory from file
    inventory = load_inventory()
    sold_inventory = []

    while True:
        print("\nVehicle Inventory Menu:")
        print("1. Add Car")
        print("2. Add Truck")
        print("3. Add SUV")
        print("4. Show Inventory")
        print("5. Delete Inventory")
        print("6. Show Sold Inventory")
        print("7. Restore Sold Vehicle")
        print("8. Edit Vehicle")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            make = input("Enter car manufacturer: ")
            model = input("Enter car model: ")
            year = input("Enter car year: ")
            price = float(input("Enter car price: "))  # Ensure price is a float
            doors = int(input("Enter number of doors: "))  # Ensure doors is an int
            car = Car(make, model, year, price, doors)
            inventory["CARS"].append(car)
            print(f"Added Car: {make} {model}")
            save_inventory(inventory)  # Save inventory after adding

        elif choice == '2':
            make = input("Enter truck manufacturer: ")
            model = input("Enter truck model: ")
            year = input("Enter truck year: ")
            price = float(input("Enter truck price: "))  # Ensure price is a float
            drive_type = input("Enter drive type: ")
            truck = Truck(make, model, year, price, drive_type)
            inventory["TRUCKS"].append(truck)
            print(f"Added Truck: {make} {model}")
            save_inventory(inventory)  # Save inventory after adding

        elif choice == '3':
            make = input("Enter SUV manufacturer: ")
            model = input("Enter SUV model: ")
            year = input("Enter SUV year: ")
            price = float(input("Enter SUV price: "))  # Ensure price is a float
            passenger_capacity = int(input("Enter passenger capacity: "))  # Ensure capacity is an int
            suv = SUV(make, model, year, price, passenger_capacity)
            inventory["SUVs"].append(suv)
            print(f"Added SUV: {make} {model}")
            save_inventory(inventory)  # Save inventory after adding

        elif choice == '4':
            print("\nCurrent Inventory:")
            print("-----------------------------------------------------------------------------------------------")
            for vehicle_type, vehicles in inventory.items():
                print(f"{vehicle_type}:")
                for index, vehicle in enumerate(vehicles, start=1):
                    if isinstance(vehicle, Car):
                        print(f"{index}. Make: {vehicle.get_make()} | Model: {vehicle.get_model()} | Year: {vehicle.get_year()} | Price: ${vehicle.get_price()} | Doors: {vehicle.get_doors()}")
                    elif isinstance(vehicle, Truck):
                        print(f"{index}. Make: {vehicle.get_make()} | Model: {vehicle.get_model()} | Year: {vehicle.get_year()} | Price: ${vehicle.get_price()} | Drive Type: {vehicle.get_drive_type()}")
                    elif isinstance(vehicle, SUV):
                        print(f"{index}. Make: {vehicle.get_make()} | Model: {vehicle.get_model()} | Year: {vehicle.get_year()} | Price: ${vehicle.get_price()} | Passenger Capacity: {vehicle.get_passenger_capacity()}")
                print("-------------------------------------------------------------------------------------------------")

        elif choice == '5':
            vehicle_type_choice = input("Which type of vehicle do you want to delete?\n1. Car\n2. Truck\n3. SUV\nEnter your choice: ")
            if vehicle_type_choice == '1':
                print("Deleting a Car:")
                for index, car in enumerate(inventory["CARS"], start=1):
                    print(f"{index}. Make: {car.get_make()} | Model: {car.get_model()} | Year: {car.get_year()} | Price: ${car.get_price()}")
                selected_index = int(input("Select the number of the vehicle you want to delete: ")) - 1
                if 0 <= selected_index < len(inventory["CARS"]):
                    sold_inventory.append(inventory["CARS"].pop(selected_index))
                    print(f"Deleted Vehicle: {sold_inventory[-1].get_make()} {sold_inventory[-1].get_model()}")
                    save_inventory(inventory)  # Save inventory after deletion
                else:
                    print("Invalid selection.")
            elif vehicle_type_choice == '2':
                print("Deleting a Truck:")
                for index, truck in enumerate(inventory["TRUCKS"], start=1):
                    print(f"{index}. Make: {truck.get_make()} | Model: {truck.get_model()} | Year: {truck.get_year()} | Price: ${truck.get_price()}")
                selected_index = int(input("Select the number of the vehicle you want to delete: ")) - 1
                if 0 <= selected_index < len(inventory["TRUCKS"]):
                    sold_inventory.append(inventory["TRUCKS"].pop(selected_index))
                    print(f"Deleted Vehicle: {sold_inventory[-1].get_make()} {sold_inventory[-1].get_model()}")
                    save_inventory(inventory)  # Save inventory after deletion
                else:
                    print("Invalid selection.")
            elif vehicle_type_choice == '3':
                print("Deleting an SUV:")
                for index, suv in enumerate(inventory["SUVs"], start=1):
                    print(f"{index}. Make: {suv.get_make()} | Model: {suv.get_model()} | Year: {suv.get_year()} | Price: ${suv.get_price()}")
                selected_index = int(input("Select the number of the vehicle you want to delete: ")) - 1
                if 0 <= selected_index < len(inventory["SUVs"]):
                    sold_inventory.append(inventory["SUVs"].pop(selected_index))
                    print(f"Deleted Vehicle: {sold_inventory[-1].get_make()} {sold_inventory[-1].get_model()}")
                    save_inventory(inventory)  # Save inventory after deletion
                else:
                    print("Invalid selection.")
            else:
                print("Invalid vehicle type.")

        elif choice == '6':
            print("\nSold Inventory:")
            if not sold_inventory:
                print("No sold vehicles.")
            else:
                for vehicle in sold_inventory:
                    if isinstance(vehicle, Car):
                        print(f"Car: {vehicle.get_make()} {vehicle.get_model()} | Year: {vehicle.get_year()} | Price: ${vehicle.get_price()}")
                    elif isinstance(vehicle, Truck):
                        print(f"Truck: {vehicle.get_make()} {vehicle.get_model()} | Year: {vehicle.get_year()} | Price: ${vehicle.get_price()}")
                    elif isinstance(vehicle, SUV):
                        print(f"SUV: {vehicle.get_make()} {vehicle.get_model()} | Year: {vehicle.get_year()} | Price: ${vehicle.get_price()}")

        elif choice == '7':
            if not sold_inventory:
                print("No sold vehicles to restore.")
                continue
            print("Restoring Sold Vehicle:")
            for index, vehicle in enumerate(sold_inventory, start=1):
                print(f"{index}. {type(vehicle).__name__}: {vehicle.get_make()} {vehicle.get_model()} | Year: {vehicle.get_year()} | Price: ${vehicle.get_price()}")
            selected_index = int(input("Select the number of the vehicle you want to restore: ")) - 1
            if 0 <= selected_index < len(sold_inventory):
                vehicle = sold_inventory.pop(selected_index)
                if isinstance(vehicle, Car):
                    inventory["CARS"].append(vehicle)
                elif isinstance(vehicle, Truck):
                    inventory["TRUCKS"].append(vehicle)
                elif isinstance(vehicle, SUV):
                    inventory["SUVs"].append(vehicle)
                print(f"Restored Vehicle: {vehicle.get_make()} {vehicle.get_model()}")
                save_inventory(inventory)  # Save inventory after restoring
            else:
                print("Invalid selection.")

        elif choice == '8':
            print("Editing a Vehicle:")
            print("Select the type of vehicle to edit:")
            print("1. Car")
            print("2. Truck")
            print("3. SUV")
            vehicle_type_choice = input("Enter your choice: ")
            if vehicle_type_choice == '1':
                for index, car in enumerate(inventory["CARS"], start=1):
                    print(f"{index}. Make: {car.get_make()} | Model: {car.get_model()} | Year: {car.get_year()} | Price: ${car.get_price()}")
                selected_index = int(input("Select the number of the car you want to edit: ")) - 1
                if 0 <= selected_index < len(inventory["CARS"]):
                    edit_vehicle(inventory["CARS"][selected_index])
                    print("Car details updated.")
                    save_inventory(inventory)  # Save inventory after editing
                else:
                    print("Invalid selection.")
            elif vehicle_type_choice == '2':
                for index, truck in enumerate(inventory["TRUCKS"], start=1):
                    print(f"{index}. Make: {truck.get_make()} | Model: {truck.get_model()} | Year: {truck.get_year()} | Price: ${truck.get_price()}")
                selected_index = int(input("Select the number of the truck you want to edit: ")) - 1
                if 0 <= selected_index < len(inventory["TRUCKS"]):
                    edit_vehicle(inventory["TRUCKS"][selected_index])
                    print("Truck details updated.")
                    save_inventory(inventory)  # Save inventory after editing
                else:
                    print("Invalid selection.")
            elif vehicle_type_choice == '3':
                for index, suv in enumerate(inventory["SUVs"], start=1):
                    print(f"{index}. Make: {suv.get_make()} | Model: {suv.get_model()} | Year: {suv.get_year()} | Price: ${suv.get_price()}")
                selected_index = int(input("Select the number of the SUV you want to edit: ")) - 1
                if 0 <= selected_index < len(inventory["SUVs"]):
                    edit_vehicle(inventory["SUVs"][selected_index])
                    print("SUV details updated.")
                    save_inventory(inventory)  # Save inventory after editing
                else:
                    print("Invalid selection.")
            else:
                print("Invalid vehicle type.")

        elif choice == '9':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()