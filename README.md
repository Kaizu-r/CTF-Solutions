# CTF Solutions

This repository is dedicated for showcasing my own CTF Solutions from various CTF Challenges websites. Simply navigate the directory to find the solution to a CTF you're struggling on. The markdown files contains the guide for solving the puzzle.

## WEBSITES COVERED
* [PicoCTF](https://play.picoctf.org/)

## INCLUDED IN THE SOLUTIONS FOLDER
1. Problem File (excluding disc images and large files)
2. solution.md
3. Any scripts used (Python)

## NOT INCLUDED IN THE SOLUTIONS FOLDER
1. The flag
2. Extracted files

## TOOLS

### Operating System
- Kali Linux (using WSL)

### General 
| Tool | Use | Installation |
| :--- | :--- | :--- |
|Linux CLI Utilities| General purpose | Pre-installed|

### Forensics
| Tool | Use | Installation |
| :--- | :--- | :--- |
|exiftool| Checking file metadata | `sudo apt install exiftool` |
|file| Checking file type and file information| Pre-installed |
|grep| Output filtering| Pre-installed |
|cat| Output file contents| Pre-installed |
|strings|Checking strings inside files| Pre-installed|
|xxd| For hexdunp | Pre-installed|
|hexedit| Editing hex bytes | `sudo apt install hexedit` |
|fdisk| Checking disk images for partitions | Pre-installed |
|Autopsy| File system analysis | [Install Autopsy](https://www.autopsy.com/download/)
|Sleuthkit| Digital forensics, file recovery, and disk analysis | sudo apt install sleuthkit |

### Steganography
| Tool | Use | Installation |
| :--- | :--- | :--- |
|zsteg| Checking LSB of png files| `sudo gem install zsteg` |
|steghide| Extracting data hidden using steghide| `sudo apt install steghide`|
|StegOnline| General purpose steganography | [StegOnline](https://georgeom.net/StegOnline/upload)|

### Networks
| Tool | Use | Installation |
| :--- | :--- | :--- |
|WireShark| General-purpose network traffic inspection| [Install WireShark](https://www.wireshark.org/download.html)|
|tshark| CLI-version of WireShark| [Install WireShark](https://www.wireshark.org/download.html)|

### Reverse Engineering
| Tool | Use | Installation |
| :--- | :--- | :--- |
|Ghidra|Decompiling executable files to equivalent C code| [Install Ghidra](https://ghidralite.com/)|


**Work in Progress**



