contact= {"fred":7235591, #"fred" is key, number is value
          "mary":3841212,
          "jone":9463723} 
newContact = dict(contact)  #crate copy of old dectionary
print(contact)
print(newContact)
print("fred number:" , contact["fred"])

if "said" in contact: #search about the value if it in my dic
    print("said number is: " , contact["said"])
else:
    print("said is not in my contact")
    
number = contact.get("fred",411)
print("dail " , str(number))

contact["mary"]=6521897 #modify the value
print(contact)

delfrid=contact.pop("jone") #delete value from my dictionary
print(contact)

for key in contact: 
     print(key)
     
for item in contact.items(): #function items print the keys with value 
    print(item[0], item[1])




    