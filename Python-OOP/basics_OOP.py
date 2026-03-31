# Working with dictionaries only
def drive(speed):
    print(f"the car is driving at speed {speed} km/h")

car1 = {
    "brand": "Toyota",
    "model": "yaris",
    "year": 2015,
    "tank": 1.6,
    "max_speed": 120,
    "is_active": True,
    "drive": drive
}

car1["drive"](car1["max_speed"])

car2 = {
    "brand": "Toyota",
    "model": "yaris",
    "yaer": 2015,
    "tank": 1.6,
    "is_active": True,
    "gaz": "95"
}