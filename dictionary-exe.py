#print the name who hase age > 22:
dec={1:{"name":"John", "age":27, "sex":"Male"},
     2:{"name":"Maria", "age":22, "sex":"Female"},
     3:{"name":"Sali", "age":23, "sex":"Female"}}
for key, item in dec.items():
    if item["age"]>22:
        print(item['name'])
        
        


    