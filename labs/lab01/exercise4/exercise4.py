# Lab 01 Exercise 4: Dynamic Parking Rate
def get_hourly_rate(vehicle_type, hour) :
    if vehicle_type == "Electric":
        price = 2.0
    elif vehicle_type == "Hybrid" and (hour >= 22 and hour <=23) or (hour >= 0 and hour <=6) :
        price = 2.0
    elif vehicle_type == "Hybrid" and (hour >= 7 and hour <=21):
        price = 5.0
    else :
        price = 5.0
    return price