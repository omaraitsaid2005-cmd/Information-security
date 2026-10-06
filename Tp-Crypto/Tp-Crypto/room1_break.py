# ===== ROOM 1 : BREAKING AN UNKNOWN SUBSTITUTION =====
from frequency import frequency_analysis

ct = """EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK.
STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,
MVE PE FPHTY Q FXXZ YEQRE.
SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,
QOZ YKXRE IXRZY.
IKTO DXV RTJXHTR EKT BTYYQFT,
EKT HPFTOTRT LTD KQY GXVR STEETRY."""

def apply(mapping, text):
    # known letters -> UPPERCASE plaintext, unknown letters -> '_'
    return "".join(mapping.get(c, "_") if c.isalpha() else c for c in text)

# ---- 1) Frequency analysis
print("=== 1) FREQUENCIES ===")
frequency_analysis(ct)

# ---- 2) Hypothesis from frequencies (hint: E > T > R > S/O > A > H > N > D > I > G > L)
partial = {
    'T':'E', 'E':'T', 'R':'R', 'Y':'S', 'X':'O', 'Q':'A',
    'K':'H', 'O':'N', 'Z':'D', 'P':'I', 'F':'G', 'S':'L'
}
print("\n=== 2) PARTIAL DECRYPTION (frequency hypothesis) ===")
print(apply(partial, ct))

# ---- 3) Complete the key using words / context
full = dict(partial)
full.update({
    'J':'C',   # SE_RET  -> SECRET
    'B':'M',   # _ESSAGE -> MESSAGE
    'N':'P',   # _ARAGRA_H -> PARAGRAPH
    'G':'F',   # _RE_UEN_Y -> FREQUENCY
    'C':'Q', 'V':'U', 'D':'Y',
    'H':'V',   # RE_EAL -> REVEAL
    'I':'W',   # _HOLE -> WHOLE
    'L':'K',   # _EY -> KEY
    'M':'B'    # _UT -> BUT
})
print("\n=== 3) FULL DECRYPTION ===")
print(apply(full, ct))

print("\nRecovered key (cipher -> plain):")
for c in sorted(full):
    print(f"{c}->{full[c]}", end="  ")
print()