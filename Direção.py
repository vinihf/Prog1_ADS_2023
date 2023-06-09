A,B = input().split(" ")

if A==B:
    print(0)
elif A == "norte" or A== "sul":
    if B == "oeste" or B == "leste":
        print(90)
    else:
        print(180)
elif A == "leste" or "oeste":
    if B=="norte" or B=="sul":
        print(90)
    else:
        print(180)

