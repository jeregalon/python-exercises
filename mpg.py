# converts from liters per 100 km to miles per gallon
def liters_100km_to_miles_gallon(liters):
    return 1 / (liters * 0.264 / 62.137) 

# viceversa
def miles_gallon_to_liters_100km(miles):
    return 1 / (miles * 0.01609 / 3.785)

print(liters_100km_to_miles_gallon(100))
print(miles_gallon_to_liters_100km(80))