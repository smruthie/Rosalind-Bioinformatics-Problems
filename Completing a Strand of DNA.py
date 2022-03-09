# Complementing 5' to 3' DNA Strand

wrong_letter = 0
while True:
	DNA = (input("Enter 5' to 3' DNA Sequence: "))
	DNA = list(DNA.upper())
	nucleotides = ['A', 'T', 'C', 'G']
	reverse_DNA = []
	for i in DNA:
		if i == 'A':
			reverse_DNA.append('T')
		if i == 'T':
			reverse_DNA.append('A')
		if i == 'C':
			reverse_DNA.append('G')
		if i == 'G':
			reverse_DNA.append('C')
		if i not in nucleotides:
			wrong_letter += 1
	if wrong_letter > 0:
		print("One or more of the letters entered do not represent a DNA nucleotide. Please try again.", "\n")
		wrong_letter = 0
	else:
		print("\n")
		print("      5' to 3' DNA Sequence:", ''.join(DNA))
		print("      3' to 5' DNA Sequence:", ''.join(reverse_DNA))
		break
