from http.server import SimpleHTTPRequestHandler, HTTPServer
from os import chdir
from sys import stdout
import socket
import os



PORT=8000
ROOTDIR='Nintendo'

#Threading in PyNX is not yet supported, once it is I can do a lot more work on how it handles the photos.
try:
    os.remove('SwitchMH.dat')
except:
    pass

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


if os.path.isfile('SwitchMH.dat') == False:
    open('SwitchMH.dat', 'w').write('')

media_files = []
#Commented out for now, will be added in a future release.
#organized = []
for media in switch_media('Nintendo/Album'):
    filename = str(media).split('/')[5]
    filedir = str(media).split('/')[1] + '/' + str(media).split('/')[2] + '/' + str(media).split('/')[3] + '/' + str(media).split('/')[4]
    if str(filedir + '/' + filename) in open('SwitchMH.dat', 'r').read():
        pass
        #if organize(str(media).split('-')[1].replace('.jpg', '')) in organized:
        #    pass
        #else:
        #    organized.append(organize(str(media).split('-')[1].replace('.jpg', '')))
    else:
        #if organize(str(media).split('-')[1].replace('.jpg', '')) in organized:
        #    pass
        #else:
        #    organized.append(organize(str(media).split('-')[1].replace('.jpg', '')))

        allimages = str(open('SwitchMH.dat', 'r').read())
        open('SwitchMH.dat', 'w').write('''<a download="''' + filedir + '/' + filename + '''" href="''' + filedir + '/' + filename + '''" title="Click to download."><img alt="ImageName" src=''' + filedir + '/' + filename + ''' style="border:0px;margin:5px;float:both;width:200px;height:120px;"</img></a>''' + allimages)

string = str(open('SwitchMH.dat', 'r').read().strip())
findTHIS = 'width:200px;height:120px;'
count = count(string, findTHIS)


#final = ''.join(list(filter(None, organized[1:])))

open('Nintendo/index.html', 'w').write('''<!DOCTYPE html>
<html lang="en">
<title>Switch Media Host</title>
<link rel=icon href=/resources/icon.png>
<head>
<style>
@font-face { font-family: Sitefont; src: url('resources/comic.ttf'); } 
  body {
    background-color: #333435
  }
  img {
  border-radius: 2%;
}

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
    chdir(ROOTDIR)
    server_address = ('',PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    stdout.write("Switch Media Host is now running on %s:%d\n" % (get_ip(),PORT)); stdout.flush()
    httpd.serve_forever()