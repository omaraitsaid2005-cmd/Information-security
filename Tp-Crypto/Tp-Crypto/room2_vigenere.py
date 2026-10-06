from frequency import frequency_analysis

ct = ("VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZL"
      "GFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVC"
      "OPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWL"
      "GOFGGGVAQFGIEZLTUS")

KEY_LENGTH = 4          # clue from Room 1

key = ""
for i in range(KEY_LENGTH):
    group = ct[i::KEY_LENGTH]                     # split into 4 groups
    print(f"\n=== Group {i+1} (positions {i}, {i+KEY_LENGTH}, ...) ===")
    freqs = frequency_analysis(group, show=False)
    for letter, n, pct in freqs[:5]:
        print(f"{letter} : {n:3d}  ({pct:5.2f} %)")
    top = freqs[0][0]                             # most frequent cipher letter
    shift = (ord(top) - ord('E')) % 26            # assume it is plaintext 'E'
    key_letter = chr(shift + ord('A'))
    print(f"Most frequent: {top}  ->  assume E  ->  shift {shift}  ->  key letter {key_letter}")
    key += key_letter

print("\nRECOVERED KEY:", key)

def vigenere_decrypt(text, key):
    out = ""
    for i, c in enumerate(text):
        k = ord(key[i % len(key)]) - ord('A')
        out += chr((ord(c) - ord('A') - k) % 26 + ord('A'))
    return out

plain = vigenere_decrypt(ct, key)
print("\nPLAINTEXT:\n", plain)