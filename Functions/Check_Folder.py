import os


def check_folder_video(path=""):
    if os.path.exists(path + "/Video/"):
        pass
    else:
        os.mkdir(path + "/Video/")


def check_folder_mp3(path=""):
    if os.path.exists(path + "/mp3/"):
        pass
    else:
        os.mkdir(path + "/mp3/")


def check_folder_tmp():
    if os.path.exists("./tmp/"):
        pass
    else:
        os.mkdir("./tmp/")


def check_folder_config():
    if os.path.exists("./Config/"):
        pass
    else:
        os.mkdir("./Config/")


def check_folder_up():
    if os.path.exists("./Config/UserProfile/"):
        pass
    else:
        os.mkdir("./Config/UserProfile/")


def main(path=""):
    check_folder_video(path)
    check_folder_video(path)
    check_folder_mp3(path)
    check_folder_tmp()
    check_folder_config()
    check_folder_up()
