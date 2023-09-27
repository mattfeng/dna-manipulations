import click

CODON_TABLE_ONE_LETTER_CODES = {
    "A": ("GCT", "GCC", "GCA", "GCG"),
    "C": ("TGT", "TGC"),
    "D": ("GAT", "GAC"),
    "E": ("GAA", "GAG"),
    "F": ("TTT", "TTC"),
    "G": ("GGT", "GGC", "GGA", "GGG"),
    "H": ("CAT", "CAC"),
    "I": ("ATT", "ATC", "ATA"),
    "K": ("AAA", "AAG"),
    "L": ("TTA", "TTG", "CTT", "CTC", "CTA", "CTG"),
    "M": ("ATG",),
    "N": ("AAT", "AAC"),
    "P": ("CCT", "CCC", "CCA", "CCG"),
    "Q": ("CAA", "CAG"),
    "R": ("CGT", "CGC", "CGA", "CGG", "AGA", "AGG"),
    "S": ("TCT", "TCC", "TCA", "TCG", "AGT", "AGC"),
    "T": ("ACT", "ACC", "ACA", "ACG"),
    "V": ("GTT", "GTC", "GTA", "GTG"),
    "W": ("TGG",),
    "Y": ("TAT", "TAC"),
    "*": ("TAA", "TAG", "TGA"),
}

CODON_SYNONYMS_ONE_LETTER_CODES = {
    "A": ("ALA", "ALANINE"),
    "C": ("CYS", "CYSTEINE"),
    "D": ("ASP", "ASPARTIC_ACID", "ASPARTATE"),
    "E": ("GLU", "GLUTAMIC_ACID", "GLUTAMATE"),
    "F": ("PHE", "PHENYLALANINE"),
    "G": ("GLY", "GLYCINE"),
    "H": ("HIS", "HISTIDINE"),
    "I": ("ILE", "ISOLEUCINE"),
    "K": ("LYS", "LYSINE"),
    "L": ("LEU", "LEUCINE"),
    "M": ("MET", "METHIONINE"),
    "N": ("ASN", "ASPARAGINE"),
    "P": ("PRO", "PROLINE"),
    "Q": ("GLN", "GLUTAMINE"),
    "R": ("ARG", "ARGININE"),
    "S": ("SER", "SERINE"),
    "T": ("THR", "THREONINE"),
    "V": ("VAL", "VALINE"),
    "W": ("TRP", "TRYPTOPHANE"),
    "Y": ("TYR", "TYROSINE"),
    "*": ("STOP",)
}

def build_codon_table():
    # sources:
    #   https://gist.github.com/juanfal/09d7fb53bd367742127e17284b9c47bf
    #   https://www.genscript.com/Amino_Acid_Code.html
    codon_table = dict()

    for one_letter_code, synonyms in CODON_SYNONYMS_ONE_LETTER_CODES.items():
        codons = CODON_TABLE_ONE_LETTER_CODES[one_letter_code]
        codon_table[one_letter_code] = codons
        for syn in synonyms:
            codon_table[syn] = codons

    return codon_table

def build_codon_synonyms():
    codon_synonyms = dict()

    for one_letter_code, synonyms in CODON_SYNONYMS_ONE_LETTER_CODES.items():
        syns = (one_letter_code, *synonyms)
        for syn in syns:
            codon_synonyms[syn] = syns
        
    return codon_synonyms

CODON_TABLE = build_codon_table()
CODON_SYNONYMS = build_codon_synonyms()

@click.command()
@click.argument("amino_acid", required=True)
def get_codon_info(amino_acid):
    amino_acid = amino_acid.upper()
    amino_acid = amino_acid.replace(" ", "_")

    if amino_acid not in CODON_TABLE:
        click.echo("invalid amino acid")
        return

    syns = CODON_SYNONYMS.get(amino_acid)
    if syns is not None:
        click.echo(f"amino acid: {amino_acid} (={', '.join(syns)})")
    else:
        click.echo(f"amino acid: {amino_acid}")

    click.echo(f"codons: {', '.join(CODON_TABLE[amino_acid.upper()])}")