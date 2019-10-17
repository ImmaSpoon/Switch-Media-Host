<p align="center"><img width="230" src="SwitchMediaHost/icon.png"></p>
<p align="center" style="font-size: 20;"> Host your Switch media over LAN. </br>Screenshots<br>Videos<br>And SDCard Contents</p>

##
<i>Switch Media Host</i> is a simple python script that allows you to see your Switch screenshots, video clips, and all of your SDCard contents directly from your browser! <b>Note: You need to be on the same network as the Switch in order to see your files. </b> This allows for easier transfering, with a simple and clean design. <br><br>It achieves this by hosting a local webserver directly from the Switch, and then the script adjusts the webpage to fit your system accordingly!<br><br>Your Switch must have access to homebrew.

## Tables of Contents
• <a style="font-size: 8px;" href="#features">Features</a><br>
• <a style="font-size: 8px;" href="#install">How to download and install</a><br>
• <a style="font-size: 8px;" href="#use">How to use</a><br>
• <a style="font-size: 8px;" href="#themes">Themes</a><br>
• <a style="font-size: 8px;" href="#config">Config.ini</a><br>
• <a style="font-size: 8px;" href="#useful">Useful links</a><br>

## Features
<p id="features">View Screenshots, Video clips, and SDCard content</p>
<img src="SwitchMediaHost/viewall.png" width="100%" width="100%">
Organize files by file type and game
<img src="SwitchMediaHost/organize.png" width="100%" width="100%">
Simple Custom Themes<a style="font-size: 8px;" href="#themes">Learn more</a><br>
<img src="SwitchMediaHost/defaultthemes.png" width="100%" width="100%">


## How to download and install
<p style="font-size: 14px;" id="install">1.) Go to the <a href="https://github.com/ImmaSpoon/Switch-Media-Host/releases">releases</a> page and download the latest release<br><br>2.) Make sure you have the latest <a href="https://github.com/nx-python/PyNX/releases">PyNX</a><br><br>3.)Extract all of the zips into the root of the SDCard

## How to use
<p style="font-size: 14px;" id="use">1.) Once you have everything installed, turn on your Switch and open PyNX from the Homebrew menu<br><br>2.) Open 'Switch Media Host.py' <br><a style="font-size: 8px;"> Rename this file to 'main.py' to have it launch instantly</a><br><br>3.) Give it a few seconds to load<br><br>4.) Go to the URL printed on the Switch, and you're done!

## Themes
<p id="themes" style="font-size: 14px;">A theme is very easy to make. To find your themes, go into the Config.ini file found in the SwitchMediaHost folder. At the very bottom of this file, you can see your themes. A theme looks like this:<br><br>black = black, white, lightgrey, black, icon.png, Switch Media Host<br><br>(Background color*, Font color*, Hover text color*, Scroll bar color*, Main logo, Title of page, Background Image)<br><br>You can use HTML color codes as well. To change your current theme, edit the line in <i>Config.ini</i> that says 'theme' to the theme you want.
<br><a style="font-size: 10px;">Note: The scroll bar has issues with the background image, HTML issue</a>

## Config.ini
<p id="config">Inside of <i>Config.ini</i>, you will find a few settings.The first setting is the Theme. Change this to the theme you want, all of the themes are found at the bottom of the file. One other setting is <i>disable-video</i>. With this enabled, it will not load videos on the main page (Like 1.2.0 and below). This allows for faster loading times in most cases. Another option is <i>events</i>. With this enabled, on special holidays it'll change your sites theme, like Halloween ;). This setting is on by default.</p>

## Useful links
<p style="font-size: 14px;" id='useful'><a href="https://github.com/ImmaSpoon/Switch-Media-Host/releases">Switch Media Host Latest</a><br><br><a href="https://github.com/nx-python/PyNX/releases">PyNX Latest</a><br><br><a href="https://switch.homebrew.guide/">Getting started with Homebrew</a><br><br>

