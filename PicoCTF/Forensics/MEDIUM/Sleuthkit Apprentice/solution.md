# PROBLEM
---

<img width="1457" height="610" alt="image" src="https://github.com/user-attachments/assets/3569a7f2-403e-430a-a2bc-52765780d7ed" />

For the final challenge of the Sleuthkit series, we get zero hints.

# SOLUTION

First we extract the file using `gunzip`

    gunzip disk.flag.img


After extracting the file, I checked the partitions using `fdisk`:

    fdisk -l disk.flag.img

<img width="615" height="227" alt="image" src="https://github.com/user-attachments/assets/9a063d52-b28d-4d98-a10e-5cca64a4a0b2" />

I performed forensics on each partition, looking for strings or filenames that match the usual formats for CTF. This is what I found for the third partion:

<img width="460" height="43" alt="image" src="https://github.com/user-attachments/assets/384ae1fa-578a-4fdf-a491-0dc0fb728efc" />

There's a file named `flag.txt`. We can extract it using `icat`:

    icat -o 360448 disk.flag.img 2082 > flag.txt

<img width="422" height="27" alt="image" src="https://github.com/user-attachments/assets/670596b5-6d10-4e22-93e4-d761d36542a2" />

The result is some random numbers. I checked the files for anything unusual and found nothing. Instead, I focused on the directory of the file. I extracted the inode using `fls`:

<img width="500" height="77" alt="image" src="https://github.com/user-attachments/assets/64163064-1ac6-417f-be65-55b8f2b55738" />

Interestingly, there's another file here named `flag.uni.txt`. I extracted it using `icat`:

    icat -o 360448 disk.flag.img 2371 > flag.uni.txt

After extracting the file, I found the flag:

<img width="281" height="28" alt="image" src="https://github.com/user-attachments/assets/b500ad16-d1d9-4f4f-ad72-a087737a0a8c" />
