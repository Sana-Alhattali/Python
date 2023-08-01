#finding the first match
string="Hello 9Pyth0n"
found=false
position=0
while not found and position < len(string):
    if string[position].isdigit():
        found = true
    else:
        position+=1
        