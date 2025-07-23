import sys
import csv

def gc_content(seq):
    if len(seq) == 0:
        return 0
    g = seq.count('G')
    c = seq.count('C')
    return round((g + c) / len(seq) * 100, 2)

def at_content(seq):
    if len(seq) == 0:
        return 0
    a = seq.count('A')
    t = seq.count('T')
    return round((a + t) / len(seq) * 100, 2)

def base_counts(seq):
    return {
        'A': seq.count('A'),
        'T': seq.count('T'),
        'G': seq.count('G'),
        'C': seq.count('C'),
        'N': seq.count('N')
    }

def melting_temp(seq):
    # Wallace Rule (simplified): 2(A+T) + 4(G+C)
    counts = base_counts(seq)
    return 2 * (counts['A'] + counts['T']) + 4 * (counts['G'] + counts['C'])

def reverse_complement(seq):
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G', 'N':'N'}
    return ''.join(complement.get(base, 'N') for base in reversed(seq))

def read_fasta(file_path):
    data = {}
    seq_id = None
    seq = ""
    try:
        with open(file_path, ' 'r') as f:
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
    results = []
    for key in data:
        seq = data[key]
        result = {
            "ID": key,
            "Length": len(seq),
            "GC_Content(%)": gc_content(seq),
            "AT_Content(%)": at_content(seq),
            "A_Count": seq.count('A'),
            "T_Count": seq.count('T'),
            "G_Count": seq.count('G'),
            "C_Count": seq.count('C'),
            "N_Count": seq.count('N'),
            "Melting_Temp(°C)": melting_temp(seq),
            "Reverse_Complement": reverse_complement(seq)
        }
        results.append(result)
        # Print to console
        print(f"ID: {result['ID']}")
        print(f"Length: {result['Length']}")
        print(f"GC Content: {result['GC_Content(%)']} %")
        print(f"AT Content: {result['AT_Content(%)']} %")
        print(f"Base Counts: A={result['A_Count']} T={result['T_Count']} G={result['G_Count']} C={result['C_Count']} N={result['N_Count']}")
        print(f"Melting Temp: {result['Melting_Temp(°C)']} °C")
        print(f"Reverse Complement: {result['Reverse_Complement']}\n")
")
    return results

def write_to_csv(results, output_file="results.csv"):
    keys = results[0].keys()
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fasta_parser.py <filename.fasta>")
        sys.exit(1)
    fasta_file = sys.argv[1]
    sequences = read_fasta(fasta_file)
    results = process_fasta(sequences)
    write_to_csv(results)
    print("Results saved to results.csv")
