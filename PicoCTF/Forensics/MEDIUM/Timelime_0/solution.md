# PROBLEM
---
<img width="836" height="671" alt="image" src="https://github.com/user-attachments/assets/ce415237-fab5-407d-b939-7017de6b77ae" />

The problem involves a disk image **partition4.img**. The flag is hidden within the disk image. There are two hints available to guide the solution process.

# SOLUTION

Unzip the file to extract the disk image. Using the hint provided, we must construct a Sleuthkit MAC timeline. Sleuthkit is a tool kit used in forensics. The toolkit we will use is `fls` which can be used to construct a timeline. `MAC` refers to Modified, Accessed, Changed. First, we must construct a body file which contains parameters such as Date Modified, Date Created, etc. which is necessary for creating a MAC timeline.

    fls -r -m / partition4.img > body.txt
    fls: the tool kit
    -r: checks all files recursively
    -m: specifies the output is a body file, with / pointing to the current directory

After creating the body file, `mactime` can construct an organized text file sorted chronologically. 

      mactime -b body.txt > timeline.txt
      mactime: the tool
      -b: specifies the input

We have successfully generated a MAC timeline.

<img width="1553" height="527" alt="image" src="https://github.com/user-attachments/assets/a469381a-3d11-4819-968c-cc2a14668fe8" />

This is the content of the timeline.txt. According the second hint: `Sloppy timestomping can yield strange (very old) timestamps`. We can assume that the flag can be found by looking at the timestamps. One immediately stands out:

<img width="798" height="29" alt="image" src="https://github.com/user-attachments/assets/b58cf411-a6b4-4200-af7d-43ee7ec0ff5b" />

A file timestamp of the year 1985. The rest of the entries are timestamped on 2021 and above. This must be the file containing the flag. We can extract it using `icat`

    icat partition4.img 4945 > bcab
    icat: the tool
    4945: the inode number of the file

After extracting the file, we can see that it's a text file containing ciphered text in base64.

    NzFtMzExbjNfMHU3MTEzcl9oM3JfNDNhMmU3YWYK

Using base64 piping, we can decipher the text to extract the flag.

    echo NzFtMzExbjNfMHU3MTEzcl9oM3JfNDNhMmU3YWYK | base64 -d

