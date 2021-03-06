import os
import shutil
import tkinter.messagebox
from tkinter import *
import webbrowser
import youtube_dl
from PIL import ImageTk, Image
from tkinter import filedialog
from Functions import Check_Folder
from Functions import Get_Miniature_From_Url
from Functions import RegexSpecC

# TODO  : Clean tmp folder when exit programme


version = "Version: 1.2"


# Relative Path for Pyinstaller
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def exit_me():
    master.destroy()


def save_exportation_path():
    global folder_path

    path_file = open("Config\\UserProfile\\ExportPath.ydbi", "w")
    folder_name = filedialog.askdirectory()
    folder_path.set(folder_name)
    path_file.write(folder_name)
    Check_Folder.main(folder_name)


def get_exportation_path():
    if os.path.exists("Config\\UserProfile\\ExportPath.ydbi"):
        path = open("Config\\UserProfile\\ExportPath.ydbi", "r")
        read_path = path.read()
        return read_path


def exportation_information_path():
    tkinter.messagebox.showinfo(title="Exportation Path", message=get_exportation_path())


def about():
    tkinter.messagebox.showinfo(title="About", message="Developed By GOLD_C4TTL3M@N\n" + version)


def read_me():
    webbrowser.open("https://github.com/PA-R29sY2F0bG1hbg/YBDI/blob/main/README.md")


def download_mp3():



    get_url = url.get()

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([getting_url()])

    except:
        pass

    with ydl:
        result = ydl.extract_info(
            '%s' % get_url,
            download=False
        )

    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]

    else:
        # Just a video
        video = result

    # id = video['id']
    mp3_title = video['title']
    mp3_id = video['id']
    n_title = RegexSpecC.extract_word(mp3_title)

    if os.path.exists("Config\\UserProfile\\ExportPath.ydbi"):
        for file in os.listdir("."):

            # Webm Condition
            if file.endswith(".webm"):

                try:

                    shutil.copy(file, get_exportation_path() + "\\mp3\\" + n_title + ".mp3")

                except OSError:
                    pass

                if os.path.exists(get_exportation_path() + "\\mp3\\" + n_title + ".mp3"):

                    # state
                    state = Label(master, text="State:", bg="white")
                    state.place(x=175, y=250)
                    success = Label(master, text="Mp3 Downloaded          ", fg="green3", bg="white")
                    success.place(x=210, y=250)

                    os.remove(file)

                else:
                    # state
                    state = Label(master, text="State:", bg="white")
                    state.place(x=175, y=250)
                    success = Label(master, text="Error During Download webm          ", fg="Red3", bg="white")
                    success.place(x=210, y=250)

            # m4a Condition
            elif file.endswith(".m4a"):
                try:
                    shutil.copy(file, get_exportation_path() + "\\mp3\\" + n_title + ".mp3")

                except OSError:
                    pass

                if os.path.exists(get_exportation_path() + "\\mp3\\" + n_title + ".mp3"):

                    state = Label(master, text="State:", bg="white")
                    state.place(x=175, y=250)
                    succ = Label(master, text="Mp3 Downloaded          ", fg="green3", bg="white")
                    succ.place(x=210, y=250)

                    os.remove(file)

                else:
                    # state
                    state = Label(master, text="State:", bg="white")
                    state.place(x=175, y=250)
                    err = Label(master, text="Error During Download m4a          ", fg="Red3", bg="white")
                    err.place(x=210, y=250)

    else:
        for file in os.listdir("."):

            # Webm Condition
            if file.endswith(".webm"):

                try:

                    shutil.copy(file, ".\\mp3\\" + n_title + ".mp3")

                except OSError:
                    pass

                if os.path.exists(".\\mp3\\" + n_title + ".mp3"):

                    # state
                    state = Label(master, text="State:", bg="white")
                    state.place(x=175, y=250)
                    success = Label(master, text="Mp3 Downloaded          ", fg="green3", bg="white")
                    success.place(x=210, y=250)

                    os.remove(file)

                else:
                    # state
                    state = Label(master, text="State:", bg="white")
                    state.place(x=175, y=250)
                    success = Label(master, text="Error During Download webm          ", fg="Red3", bg="white")
                    success.place(x=210, y=250)

            # m4a Condition
            elif file.endswith(".m4a"):
                try:
                    shutil.copy(file, ".\\mp3\\" + n_title + ".mp3")

                except OSError:
                    pass

                if os.path.exists(".\\mp3\\" + n_title + ".mp3"):

                    state = Label(master, text="State:", bg="white")
                    state.place(x=175, y=250)
                    succ = Label(master, text="Mp3 Downloaded          ", fg="green3", bg="white")
                    succ.place(x=210, y=250)

                    os.remove(file)

                else:
                    # state
                    state = Label(master, text="State:", bg="white")
                    state.place(x=175, y=250)
                    err = Label(master, text="Error During Download m4a          ", fg="Red3", bg="white")
                    err.place(x=210, y=250)


def download_video():
    loading = "#"

    if os.path.exists("Config\\UserProfile\\ExportPath.ydbi"):
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

        with ydl:
            result = ydl.extract_info(
                '%s' % getting_url(),
                download=True  # We just want to extract the info
            )

        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]

        else:
            # Just a video
            video = result

        id = video['id']
        video_title = video['title']
        n_title = RegexSpecC.extract_word(video_title)

        if os.path.exists(id + ".mp4"):
            shutil.copy(id + ".mp4", get_exportation_path() + "\\Video\\" + n_title + ".mp4")

            if os.path.exists(get_exportation_path() + "\\Video\\" + n_title + ".mp4"):
                # state
                state = Label(master, text="State:", bg="white")
                state.place(x=175, y=250)
                succ = Label(master, text="Video Downloaded          ", fg="green3", bg="white")
                succ.place(x=210, y=250)

                os.remove('./' + str(id) + ".mp4")

            else:
                # state
                state = Label(master, text="State:", bg="white")
                state.place(x=175, y=250)
                err = Label(master, text="Error During Download video          ", fg="Red3", bg="white")
                err.place(x=210, y=250)
        else:
            print("File not exists")

    else:
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

        with ydl:
            result = ydl.extract_info(
                '%s' % getting_url(),
                download=True  # We just want to extract the info
            )

        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]

        else:
            # Just a video
            video = result

        id = video['id']
        video_title = video['title']
        n_title = RegexSpecC.extract_word(video_title)

        if os.path.exists(id + ".mp4"):
            shutil.copy(id + ".mp4", ".\\video\\" + n_title + ".mp4")

            if os.path.exists(".\\video\\" + n_title + ".mp4"):
                # state
                state = Label(master, text="State:", bg="white")
                state.place(x=175, y=250)
                succ = Label(master, text="Video Downloaded          ", fg="green3", bg="white")
                succ.place(x=210, y=250)

                os.remove('./' + str(id) + ".mp4")

            else:
                # state
                state = Label(master, text="State:", bg="white")
                state.place(x=175, y=250)
                err = Label(master, text="Error During Download video          ", fg="Red3", bg="white")
                err.place(x=210, y=250)
        else:
            print("File not exists")


def submit():
    try:
        get_url = url.get()
        Get_Miniature_From_Url.main(get_url)

        video_information = {}
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s'})

        with ydl:
            result = ydl.extract_info(
                '%s' % get_url,
                download=False
            )

        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]

        else:
            # Just a video
            video = result

        # id = video['id']
        video_title = video['title']

        #    if os.path.exists(Get_Miniature_From_Url.final_file_name()):
        print(Get_Miniature_From_Url.final_file_name())

        # Minia
        get_img = "tmp/img-tmp.png"
        img = Image.open(get_img)
        img = ImageTk.PhotoImage(img)
        panel = Label(master, image=img, relief="groove", bg="gray")
        panel.image = img
        panel.place(x=10, y=160)

        # Info
        label_text_t = Label(master, text="Title: ", bg="white")
        label_text_t.place(x=175, y=160)
        label_title = Label(master, text=video_title, bg="white")
        label_title.place(x=205, y=160)

        # state
        state = Label(master, text="State:", bg="white")
        state.place(x=175, y=250)
        succ = Label(master, text="Youtube Link Working            ", fg="green3", bg="white")
        succ.place(x=210, y=250)

    except:
        img_error = resource_path("error.png")
        img = Image.open(img_error)
        img = ImageTk.PhotoImage(img)
        panel = Label(master, image=img, relief="groove", bg="gray")
        panel.image = img
        panel.place(x=10, y=160)

        # state
        state = Label(master, text="State:", bg="white")
        state.place(x=175, y=250)
        succ = Label(master, text="Error Youtube Link Not Handle", fg="Red3", bg="white")
        succ.place(x=210, y=250)


def getting_url():
    return url.get()


if os.path.exists("Config\\UserProfile\\ExportPath.ydbi"):
    path_file = open("Config\\UserProfile\\ExportPath.ydbi", "r")
    path = path_file.read()
    Check_Folder.main(path)

else:
    Check_Folder.main(".")

master = Tk()
master.geometry("500x400")
master.title('YTDl')

img_bg = resource_path("New_red-ripped-paper_103688-96.png")
ico = resource_path("ico.ico")

bg = PhotoImage(file=img_bg)
bg_l = Label(master, image=bg)
master.iconbitmap(ico)
bg_l.place(x=0, y=0)

# resize
master.resizable(False, False)

# Var
url = StringVar()
folder_path = StringVar()

# Title
label = Label(text="- Youtube Downloader -", bg="white")
label.place(x=180, y=40)

# Menu Bar
menu_bar = Menu(master)
file_menu = Menu(menu_bar, tearoff=0)
edit_menu = Menu(menu_bar, tearoff=0)
help_menu = Menu(menu_bar, tearoff=0)

edit_menu.add_command(label="Set Exportation Path", command=save_exportation_path)
file_menu.add_command(label="Get Actual Exportation Path", command=exportation_information_path)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=exit_me)

help_menu.add_command(label="ReadMe", command=read_me)
help_menu.add_separator()
help_menu.add_command(label="About", command=about)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Object TextBox Top Level
url_box_entry = Entry(master, textvariable=url)
url_box_entry.place(x=10, y=90, width=350)

# Validation Button
val_button = Button(master, text="Validation", command=submit, relief="groove", activebackground="Gray67")
val_button.place(x=400, y=85)

## Download Button
Downvid_button = Button(master, text="Download Video", command=download_video, relief="groove",
                        activebackground="Gray67")
Downvid_button.place(x=380, y=210)

# Mp3 downloader
Downmp3_button = Button(master, text="Download MP3", relief="groove", activebackground="Gray67",
                        command=download_mp3)
Downmp3_button.place(x=380, y=250)

master.config(menu=menu_bar)
master.mainloop()
