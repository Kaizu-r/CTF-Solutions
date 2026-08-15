with open("C:\\Users\\User\\Code\\CTF Solutions\\PicoCTF\\Forensics\\EASY\\Binary_Digits\\digits.bin", "rb") as f:
    data = f.read()

with open("C:\\Users\\User\\Code\\CTF Solutions\\PicoCTF\\Forensics\\EASY\\Binary_Digits\\output.png", "wb") as a:
    for i in range(0, len(data), 8):
        byte = data[i:i+8]
        a.write(bytes([int(byte, 2)]))