from rental import Vehicle, Renter, ElectricCar, Motorbike


# Create vehicles and a renter
car = Vehicle("Toyota", "Yaris", "1AB1111")
electric_car = ElectricCar("Tesla", "Model 1", "1EV111", 17)
motorbike = Motorbike("yamaha", "r6", "9M4300", 599)

renter = Renter("Matty", 77777)

# Rent and return a vehicle
print(car)

car.rent()
renter.rented.append(car)
print(car)

car.return_vehicle()
renter.rented.remove(car)
print(car)

# Test invalid renter name
try:
    Renter("", 54321)
except ValueError as e:
    print("Caught ValueError:", e)

# Test invalid license number
try:
    Renter("Mike", 0)
except ValueError as e:
    print("Caught ValueError:", e)

# Test polymorphism
vehicles = [car, electric_car, motorbike]

print("\nAll vehicles:")
for vehicle in vehicles:
    print(vehicle)