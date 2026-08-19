# PROBLEM
---
<img width="828" height="417" alt="image" src="https://github.com/user-attachments/assets/5126f08d-9d68-4e76-bdd4-baae0bfb3121" />

We are given an image file and the instructions is to modify all timestamps to January 1, 1970 with as much precision as possible. The following are all time time-related metadata in the image:

<img width="487" height="48" alt="image" src="https://github.com/user-attachments/assets/b174bc21-d3ee-4979-ab80-cbe0d231600c" />
<img width="443" height="21" alt="image" src="https://github.com/user-attachments/assets/ed80a07d-ffe9-4d78-a70c-059c0c3e9636" />
<img width="440" height="36" alt="image" src="https://github.com/user-attachments/assets/a42ebfeb-41e4-43a2-b187-2d246de4d3ca" />
<img width="518" height="18" alt="image" src="https://github.com/user-attachments/assets/dd48d36c-8a4f-4efe-837a-8ebcadea0907" />
<img width="475" height="55" alt="image" src="https://github.com/user-attachments/assets/ba7c61d1-d7eb-4405-b622-48a4c77cecae" />

There are a lot of timestamp metadata here. We have to change all of it to the specified date.

# SOLUTION

We will use exiftool to modify the timestamps. We won't modify every metadata one by one, instead we will use the `AllDates` tag. First we will modify the date and hour:

    exiftool -AllDates="1970:01:01 00:00:00" original.jpg

The following tags were affected:
<img width="456" height="41" alt="image" src="https://github.com/user-attachments/assets/8c109aa6-837f-4053-a44b-98af31705c0d" />
<img width="448" height="20" alt="image" src="https://github.com/user-attachments/assets/d2e96e67-fc95-462c-b0c9-c02085f33e6e" />
<img width="472" height="57" alt="image" src="https://github.com/user-attachments/assets/05a821f6-5070-4fa2-8aee-4da9d83561f8" />
