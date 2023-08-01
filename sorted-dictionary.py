#sort the dictionary by the age
dec = {
    1: {"name": "John", "age": 27, "sex": "Male"},
    2: {"name": "Maria", "age": 22, "sex": "Female"},
    3: {"name": "Sali", "age": 23, "sex": "Female"}
}

# Convert the dictionary items into a list of tuples (key, value)
items_list = list(dec.items())

# Sort the list of tuples based on the "age" value in the inner dictionary
for i in range(len(items_list)):
    for j in range(i + 1, len(items_list)):
        if items_list[i][1]["age"] > items_list[j][1]["age"]:
            items_list[i], items_list[j] = items_list[j], items_list[i]

# Convert the sorted list back to a dictionary
sorted_dec = dict(items_list)

# Print the sorted dictionary
for key, value in sorted_dec.items():
    print(f"Key: {key}, Value: {value}")
