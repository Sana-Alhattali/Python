s = input("enter text: ")
vl = ("a","e","u","i","o")

def count_letter(text):
    vowel_count = 0
    for i in text:
        if (i in vl):
            vowel_count+=1
    return vowel_count


print(count_letter(s))


    