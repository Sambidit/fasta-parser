# FASTA Parser

This is a small Python script I wrote to analyze DNA sequences from a `.fasta` file.

It reads multiple sequences, and for each one, it prints:
- Sequence ID
- Length of the sequence
- GC content (percentage of G and C bases)
- Number of unknown bases ('N')

### Why I built it:
I'm studying Life Sciences and recently started learning Python. This was a small project to combine both — parsing DNA sequences and doing some basic analysis without using any fancy libraries.

---

### How to run

Save your DNA sequences in a `.fasta` file. Example format:

```
>seq1
ATGCGTACGTAGCTAGCTAGCTAGCTA
>seq2
GGCGATCGATCGNNNNNNNNNATCGATCG
```

Then run the script from the terminal:

```bash
python fasta_parser.py sample.fasta
```

It will show output like:

```
ID: seq1
Length: 27
GC Content: 51.85 %
Unknown bases (N): 0

ID: seq2
Length: 35
GC Content: 40.0 %
Unknown bases (N): 9
```

---

### Tools Used
- Python 3
- No external libraries

---

### Files in this repo
- `fasta_parser.py` — the main script
- `sample.fasta` — example input
- `README.md` — this file

---

### Note
This is a beginner project and I'm still learning. Any feedback or suggestions are welcome!
