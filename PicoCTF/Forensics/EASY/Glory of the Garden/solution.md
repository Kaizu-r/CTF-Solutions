# PROBLEM 
---
<img width="845" height="251" alt="image" src="https://github.com/user-attachments/assets/19a5cf6a-f903-4c06-80ae-ee9afd56eb26" />

The problem involves a JPEG file. Opening the file reveals this:
<img width="2999" height="2249" alt="garden" src="https://github.com/user-attachments/assets/619b313b-4cc4-45e4-8a0e-c37a50077c0b" />

Not much can be acquired from this. We will use our forensic tools instead

# SOLUTION

I performed the usual forensic strategy of checking the metadata and found nothing unusual. Then I checked for strings using the `strings` command

    strings garden.jpg

It prints out all the bytes as ASCII and at the end, I got the flag:

<img width="475" height="33" alt="image" src="https://github.com/user-attachments/assets/3965314f-8706-40cb-ae68-403392e2e72d" />
