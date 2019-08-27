
codon_to_polypeptide = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP",
        }

def proteins(strand):
    protein = []
    #i = 0
    #while i*3 < len(strand):
    for i in range(len(strand)//3):
        codon = strand[i*3: i*3+3]
        if codon_to_polypeptide[codon] != "STOP":
            protein.append( codon_to_polypeptide[codon] )
        else:
            break
        #i = i+1
    return protein
