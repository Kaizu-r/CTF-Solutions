# PROBLEM
---
<img width="1450" height="690" alt="image" src="https://github.com/user-attachments/assets/d923ae05-9d14-4f7e-9e3a-f85e63a855d6" />

The problem involves a disc image file. The instruction is simple: identify the size of the `Linux` partition and check it with the remote checker service.

# SOLUTION

First, extract the disc image using `gunzip`

    gunzip disk.img.gz

After extracting the disc image, using the `mmls` command from the Sleuthkit toolkit

    mmls disk.img

After executing the command, we get this:


<img width="611" height="157" alt="image" src="https://github.com/user-attachments/assets/047f9192-e5b0-4102-ada3-6d95b9071f0d" />

Since the instruction tells us to get the partition size, we just need the `length` value of the `Linux` partition, which is **202752**. Let's run the remote checker service

    nc saturn.picoctf.net 54473


<img width="535" height="35" alt="image" src="https://github.com/user-attachments/assets/aefb5a7c-9739-476c-b432-ef64467f0a7d" />

Upload the right lenght and you'll get the flag.


<img width="165" height="41" alt="image" src="https://github.com/user-attachments/assets/bf5c6845-4d90-41b3-99d8-eed406e22e92" />

