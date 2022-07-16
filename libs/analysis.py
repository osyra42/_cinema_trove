import os
import time
import re
import web_maker
cmd = os.system



def analysis():
        # OPTIONS
    _loop = 1
    txt = ""
    gui = ""
    root = "Z://"
    prefix_ignore = ["_"]
    dir_ignore = ["System Volume Information", "$RECYCLE.BIN"]
    cmd("echo off")
    cmd("cls")


    #categories
    categories = os.listdir(root)
    for category in categories[:]:
        
        if category.startswith(tuple(prefix_ignore)):
            categories.remove(category)
            continue
        if category in dir_ignore:
            categories.remove(category)
            continue
        if not os.path.isdir(f"{root}/{category}"):
            categories.remove(category)
            continue



        titles = os.listdir(f"{root}/{category}")
        txt += f"{category}\n"
        for title in titles:
            _sec = len(categories)
            _per = int(100 / _sec)
            _fill = _per * _loop
            _unfill = 100 - _fill
            _fill = "=" * _fill
            _unfill = " " * _unfill


            gui = f"Please wait..."
            gui += f"[{_fill}{_unfill}]\n"
            gui += f"{category}"
            gui += f"  {title}"
            txt += f"  {title}\n"
            print(gui)


            if title.startswith(tuple(prefix_ignore)):
                titles.remove(title)
                continue
            if not os.path.isdir(f"{root}/{category}/{title}"):
                titles.remove(title)
                continue

            episodes = os.listdir(f"{root}/{category}/{title}")
            for episode in episodes:
                _type = False
                _nums = False
                if episode.endswith(".mp4"):
                    _type = True
                if episode.startswith("s"):
                    _nums = True

                if _type and _nums:
                    txt += f"+   {episode}\n"
                else:
                    txt += f"-   {episode}\n"
                gui = f"    {episode}"
                print(f"{gui}")
                web_maker.web_maker(root, category, title, episode)
            time.sleep(0.05)
            cmd("cls")
        _loop += 1

    with open('libs/results.diff', 'w') as f:
        f.write(txt) 
