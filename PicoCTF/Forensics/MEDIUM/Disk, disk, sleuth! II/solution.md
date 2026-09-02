# PROBLEM
---

<img width="1443" height="737" alt="image" src="https://github.com/user-attachments/assets/dba4d1af-d46f-4a81-ab70-2dd7576ba2cc" />

# SOLUTION

This task is pretty simple since Sleuthkit has a tool for searching files: `fls`. First, we extract the file using `gunzip`

    gunzip dds2-alpine.flag.img.gz

After extracting the file, I tried running `fls` but I gave this error:

    fls -r -p dds2-alpine.flag.img | grep "down-at-the-bottom.txt"

<img width="535" height="38" alt="image" src="https://github.com/user-attachments/assets/eb924b16-2876-4445-a829-4325091f156d" />

<br><br>
Let's first check the partitions using `fdisk`

    fdisk -l dds2-alpine.flag.img

<img width="560" height="188" alt="image" src="https://github.com/user-attachments/assets/728913cd-fe7a-4bcd-a4d5-ebe34445b6ec" />

<br><br>
This tells us that it is a Linux partition starting at sector **2048**. We can use this to fix the `fls` command.

     fls -r -p -o 2048 dds2-alpine.flag.img | grep "down-at-the-bottom.txt"

<img width="607" height="35" alt="image" src="https://github.com/user-attachments/assets/a8f37e1a-28a9-4891-813b-9895f71e2201" />

<br><br>
It found the file and also the inode of the file. We can extract it using `icat`

    icat -o 2048 dds2-alpine.flag.img 18291 > flag.txt

<br>
This extracts the file, which contains our flag:
<img width="757" height="275" alt="image" src="https://github.com/user-attachments/assets/14f8c5c4-665f-428b-a385-5cd38e039bac" />
