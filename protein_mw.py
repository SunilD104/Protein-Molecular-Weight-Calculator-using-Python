# Protein weight calculation using a dictionary and for loop

# Define amino acid weights
protweight = {
    "A": 89,
    "V": 117,
    "L": 131,
    "I": 131,
    "P": 115,
    "F": 165,
    "W": 204,
    "M": 149,
    "G": 75,
    "S": 105,
    "C": 121,
    "T": 119,
    "Y": 181,
    "N": 132,
    "Q": 146,
    "D": 133,
    "E": 147,
    "K": 146,
    "R": 174,
    "H": 155
}

# Get protein sequence from user
protseq = input("Enter your protein sequence: ")

# Calculate total weight
totalw = 0
for aa in protseq:
    print("Current amino acid:", aa)
    print("Weight:", protweight.get(aa.upper(), 0))
    totalw = totalw + protweight.get(aa.upper(), 0)
    print("Running total:", totalw)

print("\nFinal protein weight:", totalw)


# Protein charge calculation

# Define amino acid charges
AACharge = {
    "C": -0.045,
    "D": -0.999,
    "E": -0.998,
    "H": 0.091,
    "K": 1,
    "R": 1,
    "Y": -0.001
}

# Get protein sequence and convert to uppercase
protseq = input("\nEnter protein sequence: ").upper()

# Initialize charge
charge = -0.002

# Calculate charge with detailed output
for aa in protseq:
    if aa in AACharge:
        print("Amino acid:", aa)
        print("Charge:", AACharge[aa])
        charge = charge + AACharge[aa]
        print("Running charge:", charge)

print("\nFinal charge:", charge)


# Alternative: Using .get() method with default value
print("\n--- Using .get() method ---")
charge = -0.002
for aa in protseq:
    charge = charge + AACharge.get(aa, 0)

print("Final charge using .get():", charge)