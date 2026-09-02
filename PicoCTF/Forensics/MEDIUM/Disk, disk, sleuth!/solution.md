# PROBLEM
---

<img width="1446" height="786" alt="image" src="https://github.com/user-attachments/assets/b78b191c-a3ee-4234-8625-d149e8d91679" />

The problem involves a disk image. The instruction tells us to use `srch_strings` inside the disk image and terminal commands.

# SOLUTION

First, let's extract the image using `gunzip`

    gunzip dds1-alpine.flag.img.gz

After extracting the image, let's use the `srch_strings` command to look for strings. This command is a safer Unix wrapper for the standard `strings` command. The `strings` command is vulnerable to code execution, so `srch_strings` is preferred. This is then combined with `grep` to filter the flag.

    srch_strings dds1-alpine.flag.img | grep "picoCTF"

The flag will be displayed after running the command:

<img width="441" height="38" alt="image" src="https://github.com/user-attachments/assets/afb628cb-d9d5-47d5-b055-8f0dbedd78ee" />

