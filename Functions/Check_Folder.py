import os


def check_folder_video():
    if os.path.exists("./Video/"):
        pass
    else:
        os.mkdir("./Video/")


def check_folder_mp3():
    if os.path.exists("./mp3/"):
        pass
    else:
        os.mkdir("./mp3/")
