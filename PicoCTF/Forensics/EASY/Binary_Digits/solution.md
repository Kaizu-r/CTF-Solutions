# PROBLEM
---
<img width="832" height="516" alt="image" src="https://github.com/user-attachments/assets/a53422d5-320b-4e49-9235-20a73408678e" />

We are given a binary file **digits.bin**. It contains a raw binary text. The flag is hidden inside

# SOLUTION

First, let us examine the file. The file contains a raw binary string. This means that we must extract the binary string, convert it into bytes, and open the file. First, let us look at the header bytes.

    11111111110110001111111111100000
  
The first 32 bits look like this. They are not separated every 8th bit. If we separate every 8th bit, it would look like this:
    
    11111111 11011000 11111111 11100000

If we convert it to hexadecimal to view the header bytes, we get this:

    FF D8 FF E0

This is the header bytes of a JPG file. This means we have to convert the file to a JPG. Because of the missing delimiter, a simple copy won't work. We need a script that stores every 8 bits as a byte into a new file.

    with open("C:\\Users\\User\\Code\\CTF Solutions\\PicoCTF\\Forensics\\EASY\\Binary_Digits\\digits.bin", "rb") as f:
        data = f.read()
    
    with open("C:\\Users\\User\\Code\\CTF Solutions\\PicoCTF\\Forensics\\EASY\\Binary_Digits\\output.png", "wb") as a:
        for i in range(0, len(data), 8):
            byte = data[i:i+8]
            a.write(bytes([int(byte, 2)]))

After running the script, a new JPG file is made. Opening it gives you the flag.
