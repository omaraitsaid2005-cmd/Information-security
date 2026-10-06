# ===== FREQUENCY ANALYSIS TOOL =====
from collections import Counter

def frequency_analysis(text, show=True):
    letters = [c for c in text.upper() if c.isalpha()]   # ignore spaces & punctuation
    total = len(letters)
    counts = Counter(letters)
    result = []
    for letter, n in counts.most_common():                # most -> least frequent
        pct = 100 * n / total
        result.append((letter, n, pct))
        if show:
            print(f"{letter} : {n:3d}  ({pct:5.2f} %)")
    if show:
        print("Total letters:", total)
    return result

if __name__ == "__main__":
    test = input("Paste a ciphertext: ")
    frequency_analysis(test)