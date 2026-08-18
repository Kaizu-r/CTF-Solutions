# PROBLEM
---

<img width="834" height="629" alt="image" src="https://github.com/user-attachments/assets/4bd50c6c-1ca4-49c1-89f9-dbd518956769" />

We are given a disk image that contains the flag. After checking the partitions using `fdisk`, I found three partitions:
<img width="626" height="83" alt="image" src="https://github.com/user-attachments/assets/30652eae-0627-414d-b2d6-bf4830f7eca4" />

The flag must be hidden in one of these partitions.

# SOLUTION

To make my life easier, I won't mount the partitions. Instead, we will use Autopsy, a Sleuthkit tool for analyzing disk images. I will specifically use the legacy version. To start autopsy, paste this command in the terminal:

      sudo autopsy

After the program starts, head to `http://localhost:9999/autopsy` to interact with the GUI.

Create a new case, add a host, and attach the disk image. You should see something like this:

<img width="1916" height="1036" alt="image" src="https://github.com/user-attachments/assets/657e49f3-12ae-4b5b-be68-528a10ef9750" />

After exploring all three partitions, I found that the third partition contains the actual files. Select Analyze and then select File Analysis to view the partition's contents.

<img width="1919" height="1025" alt="image" src="https://github.com/user-attachments/assets/41af4924-4816-4894-a515-3fb4a880ef59" />

There are many folders here. In Linux systems, the working folder is typically the `home/` folder. 

<img width="1304" height="472" alt="image" src="https://github.com/user-attachments/assets/d683e8ce-334e-4241-9dcd-3c59cc6a7786" />

There is a folder named `ctf-player` which tells us that we are on the right path. If we keep diving deeper into the directory, you will find this:

<img width="1286" height="394" alt="image" src="https://github.com/user-attachments/assets/038dfa66-a1ce-44ee-a285-402fad781469" />

There is a GIT folder and a note text file. Opening the text file reveals this:

<img width="1016" height="289" alt="image" src="https://github.com/user-attachments/assets/bd78bf86-440a-4575-a499-be4d9aff54bf" />

All this tells us is the flag format, not the flag itself. If we open the `.git` folder, we find this:

<img width="1281" height="436" alt="image" src="https://github.com/user-attachments/assets/2265ea3f-f3b4-4546-91c9-55a6246c0706" />

It contains the usual GIT config files and folders. There is one peculiar file named `COMMIT EDITMSG`. Opening it reveals the flag
