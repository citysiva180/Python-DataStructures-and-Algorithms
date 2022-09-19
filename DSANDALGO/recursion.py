# Recursion example

def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)
        print(f"doll {doll} opened")


openRussianDoll(100)
