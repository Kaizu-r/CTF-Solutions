# PROBLEM
---

<img width="845" height="267" alt="image" src="https://github.com/user-attachments/assets/9cad3bde-a01d-4c7b-a6e1-d6c10f6ae12c" />
We are given a zip file. We can extract it using `unzip`

    unzip challenge.zip

After extracting, I found one file within nested directories `flag.png`

<img width="99" height="99" alt="flag" src="https://github.com/user-attachments/assets/3bbf2826-f723-43cf-84f1-01e5103ad64a" />

# SOLUTION

Since the problem file is a QR code, we can just extract the information within. QR code typically contains strings. We can use ZBAR for this:

    zbarimg flag.png

Running the command gives the flag:
<img width="317" height="20" alt="image" src="https://github.com/user-attachments/assets/7cba9ef3-a8da-48c1-818f-0a9f76b40c78" />
