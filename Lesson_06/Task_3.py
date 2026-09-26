locations = [ 
    ("Tbilisi", 41.71, 44.82), 
    ("Batumi", 41.64, 41.63), 
    ("Kutaisi", 42.26, 42.71)
]

for x in locations:
    city, latitude, longitude = x
    print(f"City: {city}, Latitude: {latitude}, Longitude: {longitude}")

print()

city_names = []
for x in locations:
    city, latitude, longitude = x
    city_names.append(city)
print("Cities: ", city_names )

# --მეორე ვერსია--
# city_names = []
# for x in locations:    
#     city_names.append(x[0])

# print("Cities: ", city_names )
