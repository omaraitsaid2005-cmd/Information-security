PLAIN  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CIPHER = "QMJZTGFKPWLSBOXNCRYEVHIADU"

enc_table = dict(zip(PLAIN, CIPHER))
dec_table = dict(zip(CIPHER, PLAIN))

def sub_encrypt(text):
    return "".join(enc_table.get(c, c) for c in text.upper())

def sub_decrypt(text):
    return "".join(dec_table.get(c, c) for c in text.upper())

print("Task 1 - Encrypt 'KEEP THE SECRET SAFE' :", sub_encrypt("KEEP THE SECRET SAFE"))
print("Task 2 - Decrypt 'ERVYE DXVR SXFPJ'     :", sub_decrypt("ERVYE DXVR SXFPJ"))