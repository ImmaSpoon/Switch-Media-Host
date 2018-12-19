from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import chdir
from sys import stdout
import socket
import threading
import json
import os
import datetime

PORT = 8000
version_num = '1.2.0'
ROOTDIR = 'Nintendo'

if str(datetime.date.today()) == '2018-12-18' or str(datetime.date.today()) == '2018-12-25' or str(datetime.date.today()) == '2018-12-26':
    snowflake = '''
<div class="snowflakes" aria-hidden="true">
  <div class="snowflake">
  &#10052;
  </div>
  <div class="snowflake">
  &#10052;
  </div>
  <div class="snowflake">
  &#10052;
  </div>
  <div class="snowflake">
  &#10052;
  </div>
  <div class="snowflake">
  &#10052;
  </div>
  <div class="snowflake">
  &#10052;
  </div>
  <div class="snowflake">
    &#10052;
  </div>
  <div class="snowflake">
    &#10052;
  </div>
  <div class="snowflake">
    &#10052;
  </div>
  <div class="snowflake">
    &#10052;
  </div>
  <div class="snowflake">
    &#10052;
  </div>
  <div class="snowflake">
    &#10052;
  </div>
</div>'''
else:
    snowflake = ""




def count(string, sub_string):
    c = 0
    l = len(sub_string)
    for i in range(len(string)):
        if string[i:i + l] == sub_string:
            c = c + 1
    return c


def switch_media(dir):
    images = []
    for root, dirs, files in os.walk(dir):
        for name in files:
            if "jpg" in name or "png" in name:
                images.append(os.path.join(root, name))
    return images


def organize(gameid):
    photos = []
    def organize(dir):
        images = []
        for root, dirs, files in os.walk(dir):
            for name in files:
                if str(gameid) + ".jpg" in name or str(gameid) + ".jpg" in name:
                    images.append(os.path.join(root, name))
        return images

    for media in organize('../../Nintendo/Album/'):
        media = str(media)
        photos.append(
            '''<a download="''' + media.replace('Nintendo/', '') + '''" href="''' + media.replace('Nintendo/', '') + '''" title="Click to download."><img alt="ImageName" src="''' + media.replace('Nintendo/', '') + '''" style="border:0px;margin:5px;float:both;width:200px;height:120px;"</img></a>''')

    with open("../../Nintendo/resources/gameids.dat") as search:
        for line in search:
            line = line.rstrip()
            if gameid in line:
                game_title = str(str(line).split(': ')[1][1:-2])
                return '''<br><br><br><div style="padding-left: 50px"><font color="white" style="padding-left: 5px;" face="Sitefont">''' + game_title + '''</font><br>''' + ''.join(
                    photos) + '</div>'


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
    if os.path.isfile("../../Nintendo/games.html") == False:
        chdir('../../Nintendo')
    open('SwitchMH.dat', 'w').write('')
    media_files = []
    organized = []
    for media in reversed(switch_media('../../Nintendo/Album')):
        filename = str(media).split('/')[7]
        filedir = 'Album/' + str(media).split('/')[4] + '/' + str(media).split('/')[5] + '/' + str(media).split('/')[6]
        if str(filedir + '/' + filename) in open('SwitchMH.dat', 'r').read():
            if organize(str(media).split('-')[1].replace('.jpg', '')) in organized:
                pass
            else:
                organized.append(organize(str(media).split('-')[1].replace('.jpg', '')))
            pass
        else:
            if organize(str(media).split('-')[1].replace('.jpg', '')) in organized:
                pass
            else:
                organized.append(organize(str(media).split('-')[1].replace('.jpg', '')))

            allimages = str(open('SwitchMH.dat', 'r').read())
            open('SwitchMH.dat', 'a').write(
                '''<a download="''' + filedir + '/' + filename + '''" href="''' + filedir + '/' + filename + '''" title="Click to download."><img alt="ImageName" src=''' + filedir + '/' + filename + ''' style="border:0px;margin:5px;float:both;width:200px;height:120px;"</img></a>''')
    string = str(open('SwitchMH.dat', 'r').read().strip())
    findTHIS = 'width:200px;height:120px;'
    count = count(string, findTHIS)
    while None in organized:
        organized.remove(None)
    final = ''.join(organized)
    chdir('../../')
    open('Nintendo/games.html', 'w').write('''<!DOCTYPE html>
        <html lang="en">
        <title>Switch Media Host</title>
        ''' + snowflake + '''
        <link rel=icon href=/resources/icon.png><a href="https://github.com/ImmaSpoon/Switch-Media-Host" target="_blank" style="float:right; padding-top:30px; padding-right:35px; font-family: Sitefont; font-size: 20px;" face="Sitefont">GitHub</a>
        <link rel=icon href=/resources/icon.png><a href="/" style="float:right; padding-top:30px; padding-right:35px; font-family: Sitefont; font-size: 20px;" face="Sitefont">Home</a>
        <head>
        <style>
.snowflake {
  color: #fff;
  font-size: 1em;
  font-family: Arial, sans-serif;
  text-shadow: 0 0 5px #000;
}

@-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@-webkit-keyframes snowflakes-shake{0%,100%{-webkit-transform:translateX(0);transform:translateX(0)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}}@keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@keyframes snowflakes-shake{0%,100%{transform:translateX(0)}50%{transform:translateX(80px)}}.snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running;animation-name:snowflakes-fall,snowflakes-shake;animation-duration:10s,3s;animation-timing-function:linear,ease-in-out;animation-iteration-count:infinite,infinite;animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s;animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s;animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s;animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s;animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s;animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s;animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s;animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s;animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s;animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s;animation-delay:3s,1.5s}.snowflake:nth-of-type(10){left:25%;-webkit-animation-delay:2s,0s;animation-delay:2s,0s}.snowflake:nth-of-type(11){left:65%;-webkit-animation-delay:4s,2.5s;animation-delay:4s,2.5s}

        ::-webkit-scrollbar {
            width: 15px;
        }

::-webkit-scrollbar-track {

	background-color: #FFFFF;
    border-radius: 6px;
}

::-webkit-scrollbar-thumb {
    height: 6px;
    border: 4px solid rgba(0, 0, 0, 0);
    background-clip: padding-box;
    -webkit-border-radius: 7px;
    background-color: rgba(0, 0, 0, 0.15);
    -webkit-box-shadow: inset -1px -1px 0px rgba(0, 0, 0, 0.05), inset 1px 1px 0px rgba(0, 0, 0, 0.05);
	background-color:   #737373;
}
        a:link {
      color: white; 
      background-color: transparent; 
      text-decoration: none;
    }
        a:visted {
          color: white; 
          text-decoration: none;
        }
        a:active {

          color: white; 
          text-decoration: none;
        }
        a:hover {
          color: gray;
          background-color: transparent;
        }

        @font-face { font-family: Sitefont; src: url('resources/comic.ttf'); } 
          body {
            background-color: #333435
          }
          img {
          border-radius: 2%;
        }
        a:visited { color:white; text-decoration: none; }
        a:hover { color:#BFBFBF; text-decoration: none; }
        </style>
        </head>
        <body>
        <p style="padding-left: 45px;"><img src="resources/logo.png" style="width:180;height:82px;"></p>
        <center><font color="white" face="Sitefont">Switch screenshots are saved in this format: [time]-[game id].jpg

You can add your own names by taking a screenshot, and looking at the screenshot file name.<br>Then, you can add it to the gameids.dat file! Please enter it in the correct format (Needs to be written within the list)</font></center>
        ''' + str(final) + '''
        </center>
        </body>
        </html>''')

    open('Nintendo/index.html', 'w').write('''<!DOCTYPE html>
    <html lang="en">
    <title>Switch Media Host</title>
    ''' + snowflake + '''
    <link rel=icon href=/resources/icon.png><a href="https://github.com/ImmaSpoon/Switch-Media-Host" target="_blank" style="float:right; padding-top:30px; padding-right:35px; font-family: Sitefont; font-size: 20px;" face="Sitefont">GitHub</a>
    <link rel=icon href=/resources/icon.png><a href="/games.html" style="float:right; padding-top:30px; padding-right:35px; font-family: Sitefont; font-size: 20px;" face="Sitefont">Sort by Games</a>
    <head>
    <style>
.snowflake {
  color: #fff;
  font-size: 1em;
  font-family: Arial, sans-serif;
  text-shadow: 0 0 5px #000;
}

@-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@-webkit-keyframes snowflakes-shake{0%,100%{-webkit-transform:translateX(0);transform:translateX(0)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}}@keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@keyframes snowflakes-shake{0%,100%{transform:translateX(0)}50%{transform:translateX(80px)}}.snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running;animation-name:snowflakes-fall,snowflakes-shake;animation-duration:10s,3s;animation-timing-function:linear,ease-in-out;animation-iteration-count:infinite,infinite;animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s;animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s;animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s;animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s;animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s;animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s;animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s;animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s;animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s;animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s;animation-delay:3s,1.5s}.snowflake:nth-of-type(10){left:25%;-webkit-animation-delay:2s,0s;animation-delay:2s,0s}.snowflake:nth-of-type(11){left:65%;-webkit-animation-delay:4s,2.5s;animation-delay:4s,2.5s}

    ::-webkit-scrollbar {
            width: 15px;
        }

::-webkit-scrollbar-track {

	background-color: #FFFFF;
    border-radius: 6px;
}

::-webkit-scrollbar-thumb {
    height: 6px;
    border: 4px solid rgba(0, 0, 0, 0);
    background-clip: padding-box;
    -webkit-border-radius: 7px;
    background-color: rgba(0, 0, 0, 0.15);
    -webkit-box-shadow: inset -1px -1px 0px rgba(0, 0, 0, 0.05), inset 1px 1px 0px rgba(0, 0, 0, 0.05);
	background-color:   #737373;
}
    a:link {
  color: white; 
  background-color: transparent; 
  text-decoration: none;
}
    a:visted {
      color: white; 
      text-decoration: none;
    }
    a:active {

      color: white; 
      text-decoration: none;
    }
    a:hover {
      color: gray;
      background-color: transparent;
    }

    @font-face { font-family: Sitefont; src: url('resources/comic.ttf'); } 
      body {
        background-color: #333435
      }
      img {
      border-radius: 2%;
    }
    a:visited { color:white; text-decoration: none; }
    a:hover { color:#BFBFBF; text-decoration: none; }
    </style>
    </head>
    <body>
    <p style="padding-left: 45px;"><img src="resources/logo.png" style="width:180;height:82px;"></p>

    </font></center></div></a><br>
    <font color="white" style="padding-left: 55px;" face="Sitefont">All Photos</font><font color="white" style="padding-right: 35px; float: right;" face="Sitefont">''' + str(count) + ''' Files</font>
    <div style="padding-left: 50px;">
    ''' + open('switch/PyNX/SwitchMH.dat', 'r').read() + '''</div>
    </center><br><br>
    <center><font color="white" face="Sitefont">Video clips are NOT supported as of right now. The clips are not able to be streamed through a browser, and a solution will be found soon!</center>
    </body>
    </html>''')
    open('switch/PyNX/SwitchMH.dat').close()
    open('Nintendo/index.html').close()
    chdir(ROOTDIR)
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    stdout.write(''' ::::::::  :::       ::: ::::::::::: :::::::::::  ::::::::  :::    ::: 
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
''' + "\n\n\nVersion " + version_num + "\nPut the address below in your browser on another device:\n\n%s:%d\n" % (get_ip(),PORT)); stdout.flush()
    httpd.serve_forever()
