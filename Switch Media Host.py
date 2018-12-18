from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import chdir
from sys import stdout
import socket
import json
import os



PORT=8000
ROOTDIR='Nintendo'

#Threading in PyNX is not yet supported, once it is I can do a lot more work on how it handles the photos.


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

    for media in organize('Nintendo/Album'):
        media = str(media)[9:]
        photos.append(
            '''<a download="''' + media + '''" href="''' + media + '''" title="Click to download."><img alt="ImageName" src="''' + media + '''" style="border:0px;margin:5px;float:both;width:200px;height:120px;"</img></a>''')

    with open("Nintendo/resources/gameids.dat") as search:
        for line in search:
            line = line.rstrip()
            if gameid in line:
                game_title = str(str(line).split(': ')[1][1:-2])
                return '''<br><br><br><div style="padding-left: 50px"><font color="white" style="padding-left: 5px;" face="Sitefont">''' + game_title + '''</font><br>''' + ''.join(photos) + '</div>'




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

    open('SwitchMH.dat', 'w').write('')
    if os.path.isfile("Nintendo/games.html") == False:
        open("Nintendo/games.html", "w").write('')

    media_files = []
    # Commented out for now, will be added in a future release.
    organized = []
    for media in reversed(switch_media('Nintendo/Album')):
        filename = str(media).split('/')[5]
        filedir = str(media).split('/')[1] + '/' + str(media).split('/')[2] + '/' + str(media).split('/')[3] + '/' + \
                  str(media).split('/')[4]
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

    open('Nintendo/games.html', 'w').write('''<!DOCTYPE html>
        <html lang="en">
        <title>Switch Media Host</title>
        <link rel=icon href=/resources/icon.png><a href="/" style="float:right; padding-top:30px; padding-right:35px; font-family: Sitefont; font-size: 20px;" face="Sitefont">Home</a>
        <head>
        <style>
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
    <link rel=icon href=/resources/icon.png><a href="/games.html" style="float:right; padding-top:30px; padding-right:35px; font-family: Sitefont; font-size: 20px;" face="Sitefont">Game Folders</a>
    <head>
    <style>
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
    <center><font color="white" face="Sitefont">Video clips are NOT supported as of right now. The clips are not able to be streamed through a browser, and a solution will be found soon!<br>Soon, there will be a way to view by game as well :)</font></center>

    <center><font color="white" face="Sitefont">Currently loaded ''' + str(count) + ''' files.</font></center></font></center></div></a><br><br><br>
    <font color="white" style="padding-left: 55px;" face="Sitefont">All Photos</font><br>
    <div style="padding-left: 50px;">
    ''' + open('SwitchMH.dat', 'r').read() + '''</div>
    </center>
    </body>
    </html>''')
    open('SwitchMH.dat').close()
    open('Nintendo/index.html').close()
    chdir(ROOTDIR)
    server_address = ('',PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    stdout.write("Switch Media Host is now running on %s:%d\n" % (get_ip(),PORT)); stdout.flush()
    httpd.serve_forever()