# PROBLEM
---

<img width="837" height="752" alt="image" src="https://github.com/user-attachments/assets/d9e2aa5d-7e09-4be2-9f58-8fff28e72dfb" />

We are given a website that contain the flag. Visiting the site reveals this:

<img width="1202" height="1026" alt="image" src="https://github.com/user-attachments/assets/006b0686-2fc3-40cc-b5a1-9e6647c4b838" />

It's a basic html website consisting of country flags. The hint tells us `"In the country that doesn't exist, the flag persists"`, indicating that there's one fake country in the list.

# SOLUTION

Obviously, I won't manually search every country name to see if they're real. I used the View Page Source tool to see the html format of the page.
<img width="428" height="567" alt="image" src="https://github.com/user-attachments/assets/95675fef-2362-4ab5-8718-37e52f236270" />

We get the source html file for the page. In the script tag, we can see the flag names and the file for the flag picture in JSON format. One immediately stans out:

<img width="1011" height="111" alt="image" src="https://github.com/user-attachments/assets/28f895c7-0bdd-46e0-abf1-1df93d77ed47" />

The Upanzi flag has extra arguments, which is suspicious. We can get more evidence by simply searching the country of Upanzi, which reveals that it in fact does not exist. We can't really get any other information in the website other than the image of the flag. I right-clicked the flag image of Upanzi to download it. This is where our forensic skill come in.


After several attempts to find information, such as using zsteg, xxd, grep, steghide, and even online steg tools for LSB and MSB. In fact it was too large for zsteg and I had to add extra parameters only for it to not work, and StegOnline kept crashing whenever I tried to upload the image. 
<img width="1381" height="194" alt="image" src="https://github.com/user-attachments/assets/163b03a4-8206-438d-8113-4459b647e8f8" />

After spending more time with the problem, I found another clue in the problem's name. Stepic is actually a python tool used to hide and extract data using LSB. I wrote a simple script to solve the problem

    from PIL import Image
    import stepic
    
    img = Image.open(r"c:\Users\User\Code\CTF Solutions\PicoCTF\Forensics\MEDIUM\flags are stepic\upz.png")
    print(stepic.decode(img))

Running the script gives us the flag

<img width="298" height="74" alt="image" src="https://github.com/user-attachments/assets/2946ecdf-1c2f-455c-81c7-525259cdde88" />
