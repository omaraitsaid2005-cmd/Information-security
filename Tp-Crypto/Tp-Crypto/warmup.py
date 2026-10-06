
def caesar_encrypt(text, k):
    result = ""
    for c in text.upper():
        if c.isalpha():
            result += chr((ord(c) - ord('A') + k) % 26 + ord('A'))
        else:
            result += c          # spaces stay unchanged
    return result

def caesar_decrypt(text, k):
    return caesar_encrypt(text, -k)

def brute_force(ciphertext):
    print("Trying all 26 possible keys:")
    for k in range(26):
        print(f"K = {k:2d} : {caesar_decrypt(ciphertext, k)}")

# --- Task 1 : Encrypt with K = 4
msg1 = "CRYPTO IS FUN UNTIL THE PROFESSOR SAYS QUIZ"
print("Task 1 - Encrypted :", caesar_encrypt(msg1, 4))
print()

msg2 = "GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA"
print("Task 2 - Decrypted :", caesar_decrypt(msg2, 8))
print()

msg3 = "ESP VPJ TD FYVYZHY ECJ MCFEP QZCNP"
print("Task 3 - Brute force")
brute_force(msg3)