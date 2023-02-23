def duplicate_count(text):

    thisset = set()
    A=text.upper()
    for letter in A:
        x = A.count(letter)
        if x >=2:
            thisset.add(letter)



    return len(thisset)


print(duplicate_count("Indivisibilities"))