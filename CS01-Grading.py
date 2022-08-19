A = int(input("Input your walking Score: "))
B = int(input("Input your Score Mid-term examination: "))
C = int(input("Input your Score Final examination: "))
Score = A + B + C
if Score >= 80: 
    print("A")
elif Score >= 75: 
    print("B+")
elif Score >= 70: 
    print("B")
elif Score >= 65: 
    print("C+")
elif Score >= 60: 
    print("C")
elif Score >= 55: 
    print("D+")
elif Score >= 50: 
    print("D")
else: 
    print("F")
