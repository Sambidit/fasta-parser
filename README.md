# FASTA Parser 

A Python-based tool to parse and analyze DNA sequences from FASTA files.

### Features

- Supports multiple FASTA entries
- Calculates:
  - GC content (%)
  - AT content (%)
  - Base counts (A, T, G, C, N)
  - Melting temperature (Wallace rule)
  - Reverse complement
- Saves output to a CSV file for further analysis

---

### How to Use

1. Download this repository
2. Place your `.fasta` file in the folder (e.g., `sample.fasta`)
3. Run:
   ```bash
   python fasta_parser_final.py sample.fasta
