from PIL import Image
import stepic

img = Image.open(r"c:\Users\User\Code\CTF Solutions\PicoCTF\Forensics\MEDIUM\flags are stepic\upz.png")
print(stepic.decode(img))