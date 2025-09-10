# Vehicle Inventory Management System

A simple command-line **Vehicle Inventory Management System** written in Python, allowing users to manage cars, trucks, and SUVs. This project demonstrates object-oriented programming concepts, data persistence using `pickle`, and basic CRUD operations (Create, Read, Update, Delete) for vehicles. This project was completed in CSC500 - Fundamentals of Programming at the University of Southern Mississippi.

---

## Features

- **Add Vehicles**  
  Add cars, trucks, and SUVs to the inventory with specific attributes:
  - Car: Make, Model, Year, Price, Number of Doors
  - Truck: Make, Model, Year, Price, Drive Type
  - SUV: Make, Model, Year, Price, Passenger Capacity

- **View Inventory**  
  Display all vehicles categorized by type (Cars, Trucks, SUVs).

- **Edit Vehicle**  
  Modify vehicle details like make, model, year, price, and type-specific attributes.

- **Delete Vehicle**  
  Remove vehicles from the inventory. Deleted vehicles are stored in a **Sold Inventory** list for potential restoration.

- **Sold Inventory Management**  
  Track and restore sold vehicles back into the inventory.

- **Data Persistence**  
  Inventory data is saved to a file using Python's `pickle` module to maintain state between program runs.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Car-Dealership.git
   cd Car-Dealership

    Ensure you have Python 3 installed:

python --version

Run the program:

    python inventory.py

Usage

    Launch the program.

    Choose an option from the menu to manage vehicles.

    Input vehicle details when prompted.

    Changes are automatically saved to inventory.pkl.

Menu Options:

    Add Car

    Add Truck

    Add SUV

    Show Inventory

    Delete Inventory

    Show Sold Inventory

    Restore Sold Vehicle

    Edit Vehicle

    Exit

Classes

    Vehicle: Base class with make, model, year, and price.

    Car (inherits Vehicle): Additional attribute doors.

    Truck (inherits Vehicle): Additional attribute drive_type.

    SUV (inherits Vehicle): Additional attribute passenger_capacity.

Technologies Used

    Python 3.x

    Object-Oriented Programming

    pickle for data persistence

Contributing

Contributions are welcome! Feel free to submit issues, fork the repository, and submit pull requests.

License

This project is licensed under the MIT License. See the LICENSE file for details.
