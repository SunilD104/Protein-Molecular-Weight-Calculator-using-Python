Protein Analysis Tool
A Python-based tool for calculating molecular weight and charge of protein sequences using amino acid dictionaries and iterative processing.

Overview
This tool analyzes protein sequences by:

Calculating total molecular weight from amino acid composition

Computing net charge based on charged amino acid residues

Providing step-by-step processing details for educational purposes

Features
Weight Calculator: Computes total molecular weight of a protein sequence using predefined amino acid weights

Charge Calculator: Determines net charge considering:

N-terminal charge (-0.002)

Charged amino acids: C, D, E, H, K, R, Y

Detailed Output: Shows running totals for both weight and charge calculations

Input Flexibility: Accepts both uppercase and lowercase amino acid codes

Error Handling: Uses .get() method to gracefully handle unrecognized amino acids

Technology Stack
Python 3.x

Standard libraries only (no external dependencies)
