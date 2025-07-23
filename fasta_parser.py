import sys

def gc_content(seq):
    if len(seq) == 0:
        return 0
    g = seq.count('G')
    c = seq.count('C')
    return round((g + c) / len(seq) * 100, 2)

def read_fasta(file_path):
    data = {}
    seq_id = None
    seq = ""

    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith(">"):
                    if seq_id:
                        data[seq_id] = seq
                    seq_id = line[1:]
                    seq = ""
                else:
                    seq += line.upper()
            if seq_id:
                data[seq_id] = seq
    except FileNotFoundError:
        print("File not found:", file_path)
        sys.exit(1)

    return data

def process_fasta(data):
    for key in data:
        sequence = data[key]
        length = len(sequence)
        gc = gc_content(sequence)
        n_count = sequence.count('N')

        print("ID:", key)
        print("Length:", length)
        print("GC Content:", gc, "%")
        print("Unknown bases (N):", n_count)
        print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fasta_parser.py <filename.fasta>")
        sys.exit(1)

    file = sys.argv[1]
    result = read_fasta(file)
    process_fasta(result)