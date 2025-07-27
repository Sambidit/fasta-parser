import sys
import csv
import matplotlib.pyplot as plt


def parse_fasta(file_content):
    sequences = {}
    current_seq = ""
    for line in file_content:
        line = line.strip()
        if line.startswith(">"):
            current_seq = line[1:]
            sequences[current_seq] = ""
        else:
            sequences[current_seq] += line.upper()
    return sequences


def calculate_gc_content(seq, ignore_n=False):
    if ignore_n:
        seq = seq.replace("N", "")
    gc_count = seq.count("G") + seq.count("C")
    return round((gc_count / len(seq)) * 100, 2) if len(seq) > 0 else 0.0


def calculate_at_content(seq, ignore_n=False):
    if ignore_n:
        seq = seq.replace("N", "")
    at_count = seq.count("A") + seq.count("T")
    return round((at_count / len(seq)) * 100, 2) if len(seq) > 0 else 0.0


def count_bases(seq):
    return {
        "A": seq.count("A"),
        "T": seq.count("T"),
        "G": seq.count("G"),
        "C": seq.count("C"),
        "N": seq.count("N"),
    }


def melting_temp(seq):
    return 2 * (seq.count("A") + seq.count("T")) + 4 * (seq.count("G") + seq.count("C"))


def reverse_complement(seq):
    comp = {"A": "T", "T": "A", "G": "C", "C": "G", "N": "N"}
    return ''.join(comp.get(base, base) for base in reversed(seq))


def dna_to_rna(seq):
    return seq.replace("T", "U")


def save_to_csv(results):
    with open("results.csv", "w", newline="") as csvfile:
        fieldnames = [
            "ID", "Length", "GC_Content", "AT_Content",
            "A", "T", "G", "C", "N", "Melting_Temp",
            "Reverse_Complement", "RNA"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)


def plot_gc_content(results):
    ids = [r['ID'] for r in results]
    gc_values = [r['GC_Content'] for r in results]

    plt.figure(figsize=(10, 6))
    plt.bar(ids, gc_values, color='green')
    plt.xlabel("Sequence ID")
    plt.ylabel("GC Content (%)")
    plt.title("GC Content per Sequence")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("gc_content_plot.png")
    plt.close()


def process_sequences(sequences, ignore_n):
    results = []
    for seq_id, seq in sequences.items():
        base_counts = count_bases(seq)
        result = {
            "ID": seq_id,
            "Length": len(seq),
            "GC_Content": calculate_gc_content(seq, ignore_n),
            "AT_Content": calculate_at_content(seq, ignore_n),
            "A": base_counts["A"],
            "T": base_counts["T"],
            "G": base_counts["G"],
            "C": base_counts["C"],
            "N": base_counts["N"],
            "Melting_Temp": melting_temp(seq),
            "Reverse_Complement": reverse_complement(seq),
            "RNA": dna_to_rna(seq),
        }
        results.append(result)
    return results


def main():
    print("FASTA Parser – DNA Analysis Tool\n")
    print("Choose Input Method:")
    print("1. Load from FASTA file")
    print("2. Enter sequence manually")
    choice = input("Enter 1 or 2: ").strip()

    ignore_n_flag = input("Ignore 'N' bases in GC/AT% calculations? (y/n): ").strip().lower() == 'y'

    if choice == "1":
        file_path = input("Enter FASTA file path: ").strip()
        try:
            with open(file_path, 'r') as f:
                sequences = parse_fasta(f.readlines())
        except FileNotFoundError:
            print("File not found. Please check the path.")
            return
    elif choice == "2":
        seq_id = input("Enter sequence ID (e.g., seq1): ").strip()
        seq = input("Enter DNA sequence: ").strip().upper()
        sequences = {seq_id: seq}
    else:
        print("Invalid choice. Exiting.")
        return

    results = process_sequences(sequences, ignore_n_flag)
    save_to_csv(results)
    plot_gc_content(results)

    for res in results:
        print("\n---", res['ID'], "---")
        print(f"Length: {res['Length']}")
        print(f"GC%: {res['GC_Content']} | AT%: {res['AT_Content']}")
        print(f"Counts - A:{res['A']} T:{res['T']} G:{res['G']} C:{res['C']} N:{res['N']}")
        print(f"Melting Temp: {res['Melting_Temp']}°C")
        print(f"Reverse Complement: {res['Reverse_Complement']}")
        print(f"RNA Sequence: {res['RNA']}")

    print("\nAnalysis complete. Results saved to 'results.csv' and 'gc_content_plot.png'.")


if __name__ == "__main__":
    main()
