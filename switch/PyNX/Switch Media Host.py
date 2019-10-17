from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import chdir
from sys import stdout
import socket
import random
import os
import datetime
import configparser
config = configparser.ConfigParser()
config.read('../../SwitchMediaHost/Config.ini')
def configReader(group, option):
    global theme
    global textcolor
    global events
    global logoimage
    global themeselection
    global disableVideo
    themeselection = str(config['Display']['theme'])
    if 'Display' in config[group]:
        themeselection = str(config[group], ['theme'])
    if 'events' in config[group][option]:
        if 'true' in config[group][option]:
            events = True
        else:
            events = False
    if 'disable-video' in config[group]:
        if 'true' in config[group][option]:
            disableVideo = True
        else:
            disableVideo = False
    if 'events' in config[group]:
        if 'true' in config[group][option]:
            events = True
        else:
            events = False
def themeReader(group, option):
    global theme
    global textcolor
    global hovercolor
    global logoimage
    global scrollcolor
    global maintext
    global backgroundimage
    theme = str(config[group][option]).split(', ')[0]
    textcolor = str(config[group][option]).split(', ')[1]
    hovercolor = str(config[group][option]).split(', ')[2]
    logoimage = str(config[group][option]).split(', ')[4]
    scrollcolor = str(config[group][option]).split(', ')[3]
    try:
        maintext = str(config[group][option]).split(', ')[5]
    except IndexError:
        maintext = ''
        logoimage = logoimage.replace(',', '')
    try:
        backgroundimage = 'background-image: url("' + str(config[group][option]).split(', ')[6] + '");\n'
    except IndexError:
        backgroundimage = ''
configReader('Other', 'disable-video')
configReader('Display', 'theme')
configReader('Special', 'events')
themeReader('Themes', themeselection)
version_num = '2.0.0'
Data = []

if events == True:
    if str(datetime.date.today())[5:] == '12-24' or str(datetime.date.today()) == '12-25' or str(
            datetime.date.today())[5:] == '12-26' or str(
            datetime.date.today())[5:] == '12-23' or str(
            datetime.date.today())[5:] == '12-22' or str(
            datetime.date.today())[5:] == '12-21':
        theme = "#e3325e"
        textcolor = "black"
        hovercolor = "#D8D8D8"
        scrollcolor = '#00B32C'
        maintext = 'Happy Holidays &#x2603;&#xFE0F;'
        special = random.choice(['''<div class="snowflakes" aria-hidden="true"> <div class="snowflake"> &#10052; </div> <div class="snowflake"> &#10052; </div> <div class="snowflake"> &#10052; </div> <div class="snowflake"> &#10052; </div> <div class="snowflake"> &#10052; </div> <div class="snowflake"> &#10052; </div> <div class="snowflake"> &#10052; </div> <div class="snowflake"> &#10052; </div> <div class="snowflake"> &#10052; </div> <div class="snowflake"> &#10052; </div> <div class="snowflake"> &#10052; </div> <div class="snowflake"> &#10052; </div> </div>''', ''' <div class="snowflakes" aria-hidden="true"> <div class="snowflake"> &#x1f381; </div> <div class="snowflake"> &#x1f381; </div> <div class="snowflake"> &#x1f381; </div> <div class="snowflake"> &#x1f381; </div> <div class="snowflake"> &#x1f381; </div> <div class="snowflake"> &#x1f381; </div> <div class="snowflake"> &#x1f381; </div> <div class="snowflake"> &#x1f381; </div> <div class="snowflake"> &#x1f381; </div> <div class="snowflake"> &#x1f381; </div> <div class="snowflake"> &#x1f381; </div> <div class="snowflake"> &#x1f381; </div> </div>''', '''<div class="snowflakes" aria-hidden="true"> <div class="snowflake"> &#x2603;&#xFE0F; </div> <div class="snowflake"> &#x2603;&#xFE0F; </div> <div class="snowflake"> &#x2603;&#xFE0F; </div> <div class="snowflake"> &#x2603;&#xFE0F; </div> <div class="snowflake"> &#x2603;&#xFE0F; </div> <div class="snowflake"> &#x2603;&#xFE0F; </div> <div class="snowflake"> &#x2603;&#xFE0F; </div> <div class="snowflake"> &#x2603;&#xFE0F; </div> <div class="snowflake"> &#x2603;&#xFE0F; </div> <div class="snowflake"> &#x2603;&#xFE0F; </div> <div class="snowflake"> &#x2603;&#xFE0F; </div> <div class="snowflake"> &#x2603;&#xFE0F; </div> </div>'''])
    elif str(datetime.date.today())[5:] == '10-29' or str(datetime.date.today()) == '10-30' or str(
            datetime.date.today())[5:] == '10-31':
        theme = "black"
        textcolor = "orange"
        hovercolor = "darkorange"
        scrollcolor = 'orange'
        maintext = 'Happy Halloween &#x1F383;'
        special = random.choice(['''<div class="snowflakes" aria-hidden="true"> <div class="snowflake"> &#x1f47b; </div> <div class="snowflake"> &#x1f47b; </div> <div class="snowflake"> &#x1f47b; </div> <div class="snowflake"> &#x1f47b; </div> <div class="snowflake"> &#x1f47b; </div> <div class="snowflake"> &#x1f47b; </div> <div class="snowflake"> &#x1f47b; </div> <div class="snowflake"> &#x1f47b; </div> <div class="snowflake"> &#x1f47b; </div> <div class="snowflake"> &#x1f47b; </div> <div class="snowflake"> &#x1f47b; </div> <div class="snowflake"> &#x1f47b; </div> </div>''', ''' <div class="snowflakes" aria-hidden="true"> <div class="snowflake"> &#x1F383; </div> <div class="snowflake"> &#x1F383; </div> <div class="snowflake"> &#x1F383; </div> <div class="snowflake"> &#x1F383; </div> <div class="snowflake"> &#x1F383; </div> <div class="snowflake"> &#x1F383; </div> <div class="snowflake"> &#x1F383; </div> <div class="snowflake"> &#x1F383; </div> <div class="snowflake"> &#x1F383; </div> <div class="snowflake"> &#x1F383; </div> <div class="snowflake"> &#x1F383; </div> <div class="snowflake"> &#x1F383; </div> </div>''', ''' <div class="snowflakes" aria-hidden="true"> <div class="snowflake"> &#x1f987; </div> <div class="snowflake"> &#x1f987; </div> <div class="snowflake"> &#x1f987; </div> <div class="snowflake"> &#x1f987; </div> <div class="snowflake"> &#x1f987; </div> <div class="snowflake"> &#x1f987; </div> <div class="snowflake"> &#x1f987; </div> <div class="snowflake"> &#x1f987; </div> <div class="snowflake"> &#x1f987; </div> <div class="snowflake"> &#x1f987; </div> <div class="snowflake"> &#x1f987; </div> <div class="snowflake"> &#x1f987; </div> </div>'''])
    elif str(datetime.date.today())[5:] == '02-13' or str(datetime.date.today()) == '02-14' or str(
            datetime.date.today())[5:] == '02-15':
        theme = "pink"
        textcolor = "red"
        hovercolor = "lightred"
        scrollcolor = 'red'
        maintext = 'Happy Valentines Day'
        special = '''<div class="snowflakes" aria-hidden="true"> <div class="snowflake"> &#9829; </div> <div class="snowflake"> &#9829; </div> <div class="snowflake"> &#9829; </div> <div class="snowflake"> &#9829; </div> <div class="snowflake"> &#9829; </div> <div class="snowflake"> &#9829; </div> <div class="snowflake"> &#9829; </div> <div class="snowflake"> &#9829; </div> <div class="snowflake"> &#9829; </div> <div class="snowflake"> &#9829; </div> <div class="snowflake"> &#9829; </div> <div class="snowflake"> &#9829; </div> </div>'''
    else:
        special = ""
else:
    special = ""

randomTip = ['Change your settings and add themes from the Config.ini file', 'Have a great evening :)', 'Experiencing some hang time? When loading large files, like videos, it may take a bit to load.', 'The site might be buggy on Safari, this is best viewed on Chrome :)',
             'Hydrate yourself! Water is good for you :)',
             'Experiencing some hang time? Make sure your Switch screen is not dimmed when in handheld. That could cause some issues.',
             'If you have a lot of photos and videos, it may take longer to load the server up on your Switch system.',
             'If you use PyNX for only Switch Media Host, change the "Switch Media Host.py" file name to "main.py" to have it launch instantly!']

def count(string, sub_string):
    c = 0
    l = len(sub_string)
    for i in range(len(string)):
        if string[i:i + l] == sub_string:
            c = c + 1
    return c

switchVideos = []
switchPhotos = []
switchMedia = []

def switch_media(dir):
    images = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if "jpg" in name:
                Data.append('<!--one--><a download="' + str(os.path.join(root, name)) + '" href="''' + os.path.join(root, name) + '" title="Click to download."><img alt="Loading..." src="' + str(os.path.join(root, name)) + '"</img></a>')
                switchPhotos.append('<!--one--><a download="' + str(os.path.join(root, name)) + '" href="''' + os.path.join(root, name) + '" title="Click to download."><img alt="Loading..." src="' + str(os.path.join(root, name)) + '"</img></a>')
            if "mp4" in name:
                Data.append('''<!--one--><a><video controls><source src="''' + str(os.path.join(root, name)) + '''"type="video/mp4"></a>'''.replace("''", ''))
                switchVideos.append('''<!--one--><a><video controls><source src="''' + str(os.path.join(root, name)) + '''"type="video/mp4"></a>'''.replace("''", ''))
    return images
for root, dirs, files in os.walk('../../Nintendo'):
    for name in files:
        if "jpg" in name:
            switchMedia.append(os.path.join(root, name))
        if "mp4" in name:
            switchMedia.append(os.path.join(root, name))
        if "jpg" in name:
            Data.append('<!--one--><a download="' + str(os.path.join(name)) + '" href="' + str(os.path.join(root, name)) + '"title="Click to download."><img alt="Loading..." src="' + str(os.path.join(root, name)) + '"</img></a>')
            switchPhotos.append('<!--one--><a download="' + str(os.path.join(name)) + '" href="' + str(os.path.join(root, name)) + '" title="Click to download."><img alt="Loading..." src="' + str(os.path.join(root, name)) + '"</img></a>')
        if "mp4" in name:
            Data.append('''<!--one--><a><video controls><source src="''' + str(os.path.join(root, name)) + '''"type="video/mp4"></a>'''.replace("''", ''))
            switchVideos.append('''<!--one--><a><video controls><source src="''' + str(os.path.join(root, name)) + '''"type="video/mp4"></a>'''.replace("''", ''))
open('../../SwitchMediaHost/photos.html', 'w').write('''<!DOCTYPE html> <html lang="en"> <title>''' + maintext + '''</title> <link rel="icon" type="image/png" href="../../SwitchMediaHost/icon.png"/> ''' + special + ''' <head> <style> .snowflake { color: #fff; font-size: 1em; font-family: Arial, sans-serif; text-shadow: 0 0 5px #000; } @-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@-webkit-keyframes snowflakes-shake{0%,100%{-webkit-transform:translateX(0);transform:translateX(0)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}}@keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@keyframes snowflakes-shake{0%,100%{transform:translateX(0)}50%{transform:translateX(80px)}}.snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running;animation-name:snowflakes-fall,snowflakes-shake;animation-duration:10s,3s;animation-timing-function:linear,ease-in-out;animation-iteration-count:infinite,infinite;animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s;animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s;animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s;animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s;animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s;animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s;animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s;animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s;animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s;animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s;animation-delay:3s,1.5s}.snowflake:nth-of-type(10){left:25%;-webkit-animation-delay:2s,0s;animation-delay:2s,0s}.snowflake:nth-of-type(11){left:65%;-webkit-animation-delay:4s,2.5s;animation-delay:4s,2.5s} ::-webkit-scrollbar { width: 15px; } ::-webkit-scrollbar-track { background-color: #FFFFF; border-radius: 6px; } ::-webkit-scrollbar-thumb { height: 6px; border: 4px solid rgba(0, 0, 0, 0); background-clip: padding-box; -webkit-border-radius: 7px; background-color: rgba(0, 0, 0, 0.15); -webkit-box-shadow: inset -1px -1px 0px rgba(0, 0, 0, 0.05), inset 1px 1px 0px rgba(0, 0, 0, 0.05); background-color:   ''' + scrollcolor +  ''' } a:link { color: ''' + textcolor +  '''; background-color: transparent; text-decoration: none; } a:visted { color: ''' + textcolor +  '''; text-decoration: none; } a:active { color: ''' + textcolor +  '''; text-decoration: none; } a:hover { color: ''' + hovercolor + '''; background-color: transparent; } @font-face { font-family: Sitefont; src: url('font.ttf'); } body { ''' + backgroundimage + ''' background-color: ''' + theme + ''' } img { border-radius: 2%; } video { object-fit: cover; border-radius: 2%; } a:visited { color:''' + textcolor +  '''; text-decoration: none; } a:hover { color:''' + hovercolor +  '''; text-decoration: none; } .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); grid-gap: 20px; align-items: stretch; } .grid img { box-shadow: 2px 2px 6px 0px  rgba(0,0,0,0.3); max-width: 100%; } .grid video { box-shadow: 2px 2px 6px 0px  rgba(0,0,0,0.3); max-width: 100%; } </style> </head> <body> <div style="text-align: center;"><img src="''' + logoimage + '''" style="max-height:130px;"></div><center><font color=''' + textcolor +  ''' style="font-family: Sitefont; font-size: 30px; max-height: 30px;" face="Sitefont">''' + maintext + '''</font></center> </font></center></div></a> <div style="padding-left: 50px;"> <br> <p><font color=''' + textcolor +  ''' style="padding-left: 0px; font-size: 17px;" face="Sitefont">All Photos, ''' + str( len(switchPhotos)) + ''' Files</font><span style="float:right;"><link rel=icon href=/resources/icon.png><a href="../SwitchMediaHost/" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">All Files</a><a href="../SwitchMediaHost/videos.html" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">Videos</a><a href="../SwitchMediaHost/games.html" style="padding-top:0px; font-family: Sitefont; font-size: 17px; margin-right: 50px;" face="Sitefont">Sort by Games</a><a href="../" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">SDCard</a> </span> <br> <main class="grid"> ''' + str(''.join(list(reversed(switchPhotos)))) + ''' </main></div> </center><br><br> <footer><center> <font color=''' + textcolor +  ''' style="font-family: Sitefont; font-size: 20px;" face="Sitefont">''' + str(random.choice(randomTip)) + ''' <br> <br> <link rel=icon href=/resources/icon.png><a href="https://github.com/ImmaSpoon/Switch-Media-Host" target="_blank" style="font-family: Sitefont; font-size: 20px;" face="Sitefont">GitHub</a> </center> </footer> </body> <style> .grid { padding-left: 0px; padding-right:50px; display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); grid-gap: 20px; align-items: stretch; } .grid img { max-width: 100%; } </style> </head><br></body></html>''')
open('../../SwitchMediaHost/videos.html', 'w').write('''<!DOCTYPE html>     <html lang="en">     <title>''' + maintext + '''</title>     <link rel="icon" type="image/png" href="../../SwitchMediaHost/icon.png"/>         ''' + special + '''     <head>     <style> .snowflake {   color: #fff;   font-size: 1em;   font-family: Arial, sans-serif;   text-shadow: 0 0 5px #000; }    @-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@-webkit-keyframes snowflakes-shake{0%,100%{-webkit-transform:translateX(0);transform:translateX(0)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}}@keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@keyframes snowflakes-shake{0%,100%{transform:translateX(0)}50%{transform:translateX(80px)}}.snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running;animation-name:snowflakes-fall,snowflakes-shake;animation-duration:10s,3s;animation-timing-function:linear,ease-in-out;animation-iteration-count:infinite,infinite;animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s;animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s;animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s;animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s;animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s;animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s;animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s;animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s;animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s;animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s;animation-delay:3s,1.5s}.snowflake:nth-of-type(10){left:25%;-webkit-animation-delay:2s,0s;animation-delay:2s,0s}.snowflake:nth-of-type(11){left:65%;-webkit-animation-delay:4s,2.5s;animation-delay:4s,2.5s}      ::-webkit-scrollbar {             width: 15px;         }  ::-webkit-scrollbar-track {  	background-color: #FFFFF;     border-radius: 6px; }  ::-webkit-scrollbar-thumb {     height: 6px;     border: 4px solid rgba(0, 0, 0, 0);     background-clip: padding-box;     -webkit-border-radius: 7px;     background-color: rgba(0, 0, 0, 0.15);     -webkit-box-shadow: inset -1px -1px 0px rgba(0, 0, 0, 0.05), inset 1px 1px 0px rgba(0, 0, 0, 0.05); 	background-color:   ''' + scrollcolor + '''; }     a:link {   color: ''' + textcolor +  ''';   background-color: transparent;    text-decoration: none; }     a:visted {       color: ''' + textcolor +  ''';       text-decoration: none;     }     a:active {        color: ''' + textcolor +  ''';       text-decoration: none;     }     a:hover {       color: ''' + hovercolor +  ''';       background-color: transparent;     }      @font-face { font-family: Sitefont; src: url('font.ttf'); }        body {       ''' + backgroundimage + '''         background-color: ''' + theme + '''       }       img {       border-radius: 2%;     }     video {     object-fit: cover;     border-radius: 2%;     }     a:visited { color:''' + textcolor +  '''; text-decoration: none; }     a:hover { color: ''' + hovercolor + '''; text-decoration: none; }   .grid {    display: grid;   grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));   grid-gap: 20px;   align-items: stretch;   } .grid img {   box-shadow: 2px 2px 6px 0px  rgba(0,0,0,0.3);   max-width: 100%; } .grid video {   box-shadow: 2px 2px 6px 0px  rgba(0,0,0,0.3);   max-width: 100%; }     </style>     </head>     <body>     <div style="text-align: center;"><img src="''' + logoimage + '''" style="max-height:130px;"></div><center><font color=''' + textcolor +  ''' style="font-family: Sitefont; font-size: 30px; max-height: 30px;" face="Sitefont">''' + maintext + '''</font></center>  </font></center></div></a>     <div style="padding-left: 50px;"> <br>     <p><font color=''' + textcolor +  ''' style="padding-left: 0px; font-size: 17px;" face="Sitefont">All Videos, ''' + str(len(switchVideos)) + ''' Files</font><span style="float:right;"><link rel=icon href=/resources/icon.png><a href="../SwitchMediaHost/photos.html" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">Photos</a><a href="../SwitchMediaHost/" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">All Files</a><a href="../SwitchMediaHost/games.html" style="padding-top:0px; font-family: Sitefont; font-size: 17px; margin-right: 50px;" face="Sitefont">Sort by Games</a><a href="../" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">SDCard</a> </span>     <br> <main class="grid"> ''' + str(''.join(list(reversed(switchVideos)))) + '''     </main></div>     </center><br><br>     <center>      <footer><center>            <font color=''' + textcolor +  ''' style="font-family: Sitefont; font-size: 20px;" face="Sitefont">''' + str(random.choice(randomTip)) + '''      <br>      <br>       <link rel=icon href=/resources/icon.png><a href="https://github.com/ImmaSpoon/Switch-Media-Host" target="_blank" style="font-family: Sitefont; font-size: 20px;" face="Sitefont">GitHub</a> </center> </footer>      </body> <style> .grid {    padding-left: 0px;   padding-right:50px;      display: grid;   grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));   grid-gap: 20px;   align-items: stretch;   } .grid img {   max-width: 100%; } </style> </head><br></body></html>''')
def organizeall(gameid):
    photos = []
    def organizeall(dir):
        images = []
        for root, dirs, files in os.walk(dir):
            for name in files:
                if str(gameid) + ".jpg" in name or str(gameid) + ".mp4" in name:
                    images.append(os.path.join(root, name))
        return images
    for media in organizeall('../../Nintendo/Album'):
        if 'jpg' in media:
            if str('''href="''' + media) in str(photos):
                pass
            else:
                photos.append(
                    '''<a download="''' + media + '''" href="''' + media + '''" title="Click to download."><img alt="Loading..." src="''' + media + '''" style="border:0px;margin:0px;float:both;"</img></a>''')
        if 'mp4' in media:
            if str('''href="''' + media) in str(photos):
                pass
            else:
                photos.append('''<a><video max-width: 100%; controls><source src="''' + media + '''" type="video/mp4"></video></a>''')
    with open("../../SwitchMediaHost/gameids.dat") as search:
        for line in search:
            line = line.rstrip()
            if gameid in line:
                game_title = str(str(line).split(': ')[1][1:-2])
                return '''<br><br><div style="padding-left: 0px"><font color=''' + textcolor +  ''' style="padding-left: 0px;" face="Sitefont">''' + game_title + '''</font><br><br><main class='grid'>''' + ''.join(list(reversed(photos))) + '</main></div>'

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

if __name__ == '__main__':
    media_files = []
    organized = []
    for media in switchMedia:
        if str(media) in media_files:
            organized.append(organizeall(str(media).split('-')[1].replace('.jpg', '')))
            organized.append(organizeall(str(media).split('-')[1].replace('.mp4', '')))
        else:
            if organizeall(str(media).split('-')[1].replace('.jpg', '')) in organized:
                ()
            else:
                organized.append(organizeall(str(media).split('-')[1].replace('.jpg', '')))
            if organizeall(str(media).split('-')[1].replace('.mp4', '')) in organized:
                ()
            else:
                organized.append(organizeall(str(media).split('-')[1].replace('.mp4', '')))
    while None in organized:
        organized.remove(None)
    final = ''.join(organized).replace(str(''.join(organized)).split('<main class=')[0], '<div style="padding-left: 0px;">')
    open('../../SwitchMediaHost/games.html', 'w').write('''<!DOCTYPE html> <html lang="en"> <title>''' + maintext + '''</title> <link rel="icon" type="image/png" href="../../SwitchMediaHost/icon.png"/> ''' + special + ''' <head> <style> .snowflake { color: #fff; font-size: 1em; font-family: Arial, sans-serif; text-shadow: 0 0 5px #000; } @-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@-webkit-keyframes snowflakes-shake{0%,100%{-webkit-transform:translateX(0);transform:translateX(0)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}}@keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@keyframes snowflakes-shake{0%,100%{transform:translateX(0)}50%{transform:translateX(80px)}}.snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running;animation-name:snowflakes-fall,snowflakes-shake;animation-duration:10s,3s;animation-timing-function:linear,ease-in-out;animation-iteration-count:infinite,infinite;animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s;animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s;animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s;animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s;animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s;animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s;animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s;animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s;animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s;animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s;animation-delay:3s,1.5s}.snowflake:nth-of-type(10){left:25%;-webkit-animation-delay:2s,0s;animation-delay:2s,0s}.snowflake:nth-of-type(11){left:65%;-webkit-animation-delay:4s,2.5s;animation-delay:4s,2.5s} ::-webkit-scrollbar { width: 15px; } ::-webkit-scrollbar { background: #FFFFF; } ::-webkit-scrollbar-track { border-radius: 6px; display: none; } ::-webkit-scrollbar-thumb { height: 6px; border: 4px solid rgba(0, 0, 0, 0); background-clip: padding-box; background-image: SwitchMediaHost/nothing.png; -webkit-border-radius: 7px; -webkit-box-shadow: inset -1px -1px 0px rgba(0, 0, 0, 0.05), inset 1px 1px 0px rgba(0, 0, 0, 0.05); background-color:   ''' + scrollcolor +  ''' } a:link { color: ''' + textcolor +  '''; background-color: transparent; text-decoration: none; } a:visted { color: ''' + textcolor +  '''; text-decoration: none; } a:active { color: ''' + textcolor +  '''; text-decoration: none; } a:hover { color: ''' + hovercolor + '''; background-color: transparent; } @font-face { font-family: Sitefont; src: url('font.ttf'); } body { ''' + backgroundimage + ''' background-color: ''' + theme + ''' } img { border-radius: 2%; } video { object-fit: cover; border-radius: 2%; } a:visited { color:''' + textcolor +  '''; text-decoration: none; } a:hover { color:''' + hovercolor +  '''; text-decoration: none; } .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); grid-gap: 20px; align-items: stretch; } .grid img { box-shadow: 2px 2px 6px 0px  rgba(0,0,0,0.3); max-width: 100%; } .grid video { box-shadow: 2px 2px 6px 0px  rgba(0,0,0,0.3); max-width: 100%; } </style> <div style="text-align: center;"><img src="''' + logoimage + '''" style="max-height:130px;"></div><center><font color=''' + textcolor +  ''' style="font-family: Sitefont; font-size: 30px; max-height: 30px;" face="Sitefont">''' + maintext + '''</font></center> </head> <body> </font></center></div></a> <div style="padding-left: 50px;"> <font color=''' + textcolor +  ''' style="padding-left: 0px; font-size: 17px;" face="Sitefont">''' + str(str(organized).split('</font><br><br><main class=')[0]).split('<div style="padding-left: 0px"><font color=' + textcolor + 'padding-left: 0px;" face="Sitefont">')[0].replace("['", '') + '''</font><span style="float:right;"><link rel=icon href=/resources/icon.png><a href="../SwitchMediaHost/photos.html" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">Photos</a><a href="../SwitchMediaHost/videos.html" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">Videos</a><a href="../SwitchMediaHost/" style="padding-top:0px; font-family: Sitefont; font-size: 17px; margin-right: 50px;" face="Sitefont">All Photos</a><a href="../" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">SDCard</a> </span> <br> <br> ''' + str(final) + '''</div> </center><br><br> <center><font color=''' + textcolor +  ''' face="Sitefont">''' + str( random.choice(randomTip)) + '''</center> <footer><center> <br> <link rel=icon href=/resources/icon.png><a href="https://github.com/ImmaSpoon/Switch-Media-Host" target="_blank" style="font-family: Sitefont; font-size: 20px;" face="Sitefont">GitHub</a> </center> </footer> </body> <style> .grid { padding-left: 0px; padding-right:50px; display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); grid-gap: 20px; align-items: stretch; } .grid img { max-width: 100%; } </style> </head><br></body></html>''')
    if disableVideo == True:
        Data = switchPhotos
    open('../../SwitchMediaHost/index.html', 'w').write('''<!DOCTYPE html>     <html lang="en">     <title>''' + maintext + '''</title>     <link rel="icon" type="image/png" href="../../SwitchMediaHost/icon.png"/>     ''' + special + '''     <head>     <style> .snowflake {   color: #fff;   font-size: 1em;   font-family: Arial, sans-serif;   text-shadow: 0 0 5px #000; } @-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@-webkit-keyframes snowflakes-shake{0%,100%{-webkit-transform:translateX(0);transform:translateX(0)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}}@keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@keyframes snowflakes-shake{0%,100%{transform:translateX(0)}50%{transform:translateX(80px)}}.snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running;animation-name:snowflakes-fall,snowflakes-shake;animation-duration:10s,3s;animation-timing-function:linear,ease-in-out;animation-iteration-count:infinite,infinite;animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s;animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s;animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s;animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s;animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s;animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s;animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s;animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s;animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s;animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s;animation-delay:3s,1.5s}.snowflake:nth-of-type(10){left:25%;-webkit-animation-delay:2s,0s;animation-delay:2s,0s}.snowflake:nth-of-type(11){left:65%;-webkit-animation-delay:4s,2.5s;animation-delay:4s,2.5s}     ::-webkit-scrollbar {             width: 15px;         } ::-webkit-scrollbar-track {  	background-color: #FFFFF;     border-radius: 6px; }  ::-webkit-scrollbar-thumb {     height: 6px;     border: 4px solid #ffffff00;     background-clip: padding-box;     -webkit-border-radius: 7px;     background-color: rgba(0, 0, 0, 0.15); 	background-color:   ''' + scrollcolor + '''; }     a:link {   color: ''' + textcolor +  ''';    background-color: transparent;    text-decoration: none; }     a:visted {       color: ''' + textcolor + ''';        text-decoration: none;     }     a:active {       text-color: ''' + textcolor + ''';        text-decoration: none;     }     a:hover {       color: ''' + hovercolor + ''';       background-color: transparent;     }      @font-face { font-family: Sitefont; src: url('font.ttf'); text-color: ''' + textcolor + ''';}        body {       ''' + backgroundimage + '''         background-color: ''' + theme + '''       }       img {       border-radius: 2%;     }     video {     object-fit: cover;     border-radius: 2%;     }     a:visited { color:''' + textcolor + '''; text-decoration: none; }     a:hover { color:''' + hovercolor + '''; text-decoration: none; }   .grid {    display: grid;   grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));   grid-gap: 20px;   align-items: stretch;   } .grid img {   box-shadow: 2px 2px 6px 0px  rgba(0,0,0,0.3);   max-width: 100%; } .grid video {   box-shadow: 2px 2px 6px 0px  rgba(0,0,0,0.3);   max-width: 100%; }     </style>     </head>     <body>     <div style="text-align: center;"><img src="''' + logoimage + '''" style="max-height:130px;"></div><center><font color=''' + textcolor +  ''' style="font-family: Sitefont; font-size: 30px; max-height: 30px;" face="Sitefont">''' + maintext + '''</font></center>      <div style="padding-left: 50px;"> <br>     <p><font color=''' + textcolor +  ''' style="padding-left: 0px; font-size: 17px;" face="Sitefont">All Files, ''' + str(         len(switchPhotos) + len(switchVideos)) + ''' Files</font><span style="float:right;"><link rel=icon href=/resources/icon.png><a href="../SwitchMediaHost/photos.html" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">Photos</a><a href="../SwitchMediaHost/videos.html" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">Videos</a><a href="../SwitchMediaHost/games.html" style="padding-top:0px; font-family: Sitefont; font-size: 17px; margin-right: 50px;" face="Sitefont">Sort by Games</a><a href="../" style="padding-top:0px; font-family: Sitefont; font-size: 17px; padding-right: 50px;" face="Sitefont">SDCard</a> </span>     <br> <main class="grid">     ''' + ''.join(reversed(Data)) + '''</main></div>     </center><br><br>      <footer><center>      <font color=''' + textcolor +  ''' style="font-family: Sitefont; font-size: 20px;" face="Sitefont">''' + str(random.choice(randomTip)) + '''      <br><br>       <link rel=icon href=../SwitchMediaHost/icon.png><a href="https://github.com/ImmaSpoon/Switch-Media-Host" target="_blank" style="font-family: Sitefont; font-size: 20px;" face="Sitefont">GitHub</a> </center> </footer>  </body> <style> .grid {    padding-left: 0px;   padding-right:50px;      display: grid;   grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));   grid-gap: 20px;   align-items: stretch;   } .grid img {   max-width: 100%; } </style> </head><br></body></html>''')
open('../../SwitchMediaHost/index.html').close()
chdir('../../')
class MyHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    def log_request(self, code='-', size='-'):
        pass
    def log_error(self, format, *args):
        pass
    def handle(self):
        try:
            SimpleHTTPRequestHandler.handle(self)
        except socket.error:
            pass
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)
stdout.write('''\n\n\n\n\n\n\n
     ::::::::  :::       ::: ::::::::::: :::::::::::  ::::::::  :::    ::: 
    :+:    :+: :+:       :+:     :+:         :+:     :+:    :+: :+:    :+: 
    +:+        +:+       +:+     +:+         +:+     +:+        +:+    +:+ 
    +#++:++#++ +#+  +:+  +#+     +#+         +#+     +#+        +#++:++#++ 
           +#+ +#+ +#+#+ +#+     +#+         +#+     +#+        +#+    +#+ 
    #+#    #+#  #+#+# #+#+#      #+#         #+#     #+#    #+# #+#    #+# 
     ########    ###   ###   ###########     ###      ########  ###    ### 
 
 
 
         ::::    ::::  :::::::::: :::::::::  :::::::::::     :::     
        +:+:+: :+:+:+ :+:        :+:    :+:     :+:       :+: :+:   
        +:+ +:+:+ +:+ +:+        +:+    +:+     +:+      +:+   +:+  
        +#+  +:+  +#+ +#++:++#   +#+    +:+     +#+     +#++:++#++: 
        +#+       +#+ +#+        +#+    +#+     +#+     +#+     +#+ 
        #+#       #+# #+#        #+#    #+#     #+#     #+#     #+# 
        ###       ### ########## #########  ########### ###     ### 



                :::    :::  ::::::::   ::::::::  ::::::::::: 
                :+:    :+: :+:    :+: :+:    :+:     :+:     
                +:+    +:+ +:+    +:+ +:+            +:+     
                +#++:++#++ +#+    +:+ +#++:++#++     +#+     
                +#+    +#+ +#+    +#+        +#+     +#+     
                #+#    #+# #+#    #+# #+#    #+#     #+#     
                ###    ###  ########   ########      ###
                
''' + "\n\n\n\nVersion " + version_num + "\nPut the address below in your browser on another device:\n\n%s:%d/SwitchMediaHost/\n" % (get_ip(), 8000));
stdout.flush()
httpd.serve_forever()
