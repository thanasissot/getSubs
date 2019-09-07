# getSubs

I am automating downloading subs with vlc using kubuntu(ubuntu is the same).
This is just a noobish way of doing it and i will refactor it a later date using OPENSUBTITLES API
Currently i work with os, subprocess, time and pyautogui
to open each file and click on the correct tabs and butttons to download the subs for each item in a folder
This method will not work everytime, some glitches may occur due to slow interent or systems response
That's why if one decides to use it you can change the time.wait() values or add pyautogui.PAUSE = 1 (or more)
to have more control over the application

Precautions; make sure you have vlc as default for opening video format files
Also make sure there is no other type of file in the folder. (just thought i can work around this but after i commited, oh well next commit it is then)

How it works: it will print directions but here goes nothing.
After you input the specified folder of the videos you need to hover the mouse pointer over the locations that are printed on
the console. And you are done. It will do the rest of the work.
