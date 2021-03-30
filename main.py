numCases = int(input())
numBases = []
sequence = []
output = ""

# Get input
for x in range(numCases):
    numBases.append(int(input()))
    sequence.append(input())

# Get output
for x in range(numCases):
    #print("x: " + str(x))
    for dna in sequence[x]:
        #print("x: " + str(x) + ", dnd: " + str(dna))
        if(dna == "U"):
            output = "Error RNA nucleobases found!"
            break;
        elif(dna == "A"):
            output += "T"
        elif(dna == "T"):
            output += "A"
        elif(dna == "G"):
            output += "C"
        elif(dna == "C"):
            output += "G"
    print(output)
    output = ""
