import CarClass as c 

car = c.Car(2024, 'Tesla')

for c in range(5):
    car.accelerate()
    print(f"The current speed is {car.get_speed()}")

for c in range(5):
    car.brake()
    print(f"The current speed is {car.get_speed()}")


