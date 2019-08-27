def to_rna(dna_strand):
    RNA_OF = { 'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    return ''.join((RNA_OF[nucl] for nucl in dna_strand))
