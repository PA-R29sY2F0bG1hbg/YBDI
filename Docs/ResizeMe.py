from PIL import Image

file_name = "../Visual_Data/img.png"
img = Image.open(file_name)
img.save("../Visual_Data/error.png")
img = Image.open("../error.png")
new_img = img.resize((160, 120))
new_img.save("../Visual_Data/error.png")
