# PROBLEM

<img width="840" height="235" alt="image" src="https://github.com/user-attachments/assets/4b670e68-5c4d-4e7e-a59e-9855738b5c80" />

The forensics challenge involves a JPG file `cat.jpg`. Opening the image reveals this:
<img width="2560" height="1598" alt="cat" src="https://github.com/user-attachments/assets/222bc96a-03f1-4e7f-baf1-9ff8f622075b" />

It's a picture of a cute cat, though its cuteness won't help us solve the challenge.

# SOLUTION

Like every challenge involving a JPG file, I checked the metadata using `exiftool`

    exiftool cat.jpg

It reveals the following information:

<img width="657" height="517" alt="image" src="https://github.com/user-attachments/assets/3caf6de9-bbe1-4061-a00d-1da1744c898c" />

There is a suspicious base64 text in the License tag. We can decode it like this:

    echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | base64 -d

Running this command reveals the flag:
<img width="281" height="24" alt="image" src="https://github.com/user-attachments/assets/784cef39-d56f-4467-8a6a-dd0d572219f1" />



