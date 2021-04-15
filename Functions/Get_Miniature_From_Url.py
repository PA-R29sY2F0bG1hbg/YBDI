import os

import requests
from PIL import Image

file_name = "img-tmp"


def check_tmp_folder():
    if os.path.exists("tmp"):
        pass
    else:
        os.mkdir("tmp")


def url_cutter(url_source):
    url_split = url_source.split("/")
    url_scut = url_split[-1].replace("watch?v=", "")
    url_sscut = url_scut.split("&")
    url_target = "https://i.ytimg.com/vi/%s/maxresdefault.jpg" % url_sscut[0]
    return url_target


def download_mini(url_source):
    img_data = requests.get(url_cutter(url_source)).content
    with open("tmp/" + str(file_name) + ".jpg", "wb") as handler:
        handler.write(img_data)
        handler.close()


def png_conv():
    img = Image.open("tmp/" + str(file_name) + ".jpg")
    img.save("tmp/" + str(file_name) + ".png")
    os.remove("tmp/" + str(file_name) + ".jpg")


def png_resize():
    img = Image.open("tmp/" + str(file_name) + ".png")
    new_img = img.resize((160, 120))
    new_img.save("tmp/" + str(file_name) + ".png")


def final_file_name():
    f_file_name = "tmp/" + str(file_name) + ".png"
    return f_file_name


def main(url_source):
    check_tmp_folder()
    url_cutter(url_source)
    download_mini(url_source)
    png_conv()
    png_resize()
