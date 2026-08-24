# PROBLEM
---
<img width="835" height="622" alt="image" src="https://github.com/user-attachments/assets/9b3f7c3d-2366-463b-94ce-ad5207f1cb94" />

We are given a URL. Heading to it reveals this:
<img width="1917" height="1032" alt="image" src="https://github.com/user-attachments/assets/26c63c5c-cce7-4b22-bcb1-80c8be0d656e" />

It's a GIF that plays based on mouse movement, letting you "milkslap" the person in the GIF. Opening the source reveals the following:
<img width="690" height="465" alt="image" src="https://github.com/user-attachments/assets/7c117c34-fde5-4323-85d5-6670cc5f9a90" />

We have our image `concat_v.png` here and we can download it. It seems that the "GIF" is actually just a really tall image and a script is used to jump to different frames to play the animation.

# SOLUTION

We can use zsteg to check for hidden data:
    
    zsteg concat_v.png

<img width="1462" height="377" alt="image" src="https://github.com/user-attachments/assets/5c90a5c4-cb70-4fa1-bad2-e14e16dc8637" />

We get a stack overflow error. The image is probably too large for standard zsteg. We can use another parameter to increase the stack limit:

    RUBY_THREAD_VM_STACK_SIZE=500000000 zsteg concat_v.png

Running this command reveals the flag

<img width="1457" height="490" alt="image" src="https://github.com/user-attachments/assets/065e7999-c810-451b-88a2-c925bc9c679c" />
