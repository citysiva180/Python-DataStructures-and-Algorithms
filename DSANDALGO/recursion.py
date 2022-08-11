# Recusion example

def openRussionDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussionDoll(doll-1)
        print(f"doll {doll} opened")


openRussionDoll(100)
