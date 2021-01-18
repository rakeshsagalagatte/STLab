def isvalid(v): 
    return v>0 and v<=10

A,B,C=-1,-1,-1

while True: 
    try:
        A,B,C=map(int,input("Enter the sides of the triangle: ").split())
    except: 
        print("Invalid input: Wrong format.")
        continue
    if isvalid(A) and isvalid(B) and isvalid(C):
        break
    else:
        print("Invalid input: Number out of bounds.")

if A+B<=C or A+C<=B or B+C<=A:
    print("Not a triangle!")
elif A==B and B==C:
    print("Equilateral Triangle")
elif A==B or B==C or A==C:
    print("Isoscles triangle")
else: print("Scalene Triangle")
