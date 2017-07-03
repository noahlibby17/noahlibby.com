# Noah Libby <nl8800@bard.edu>
# March 9 2017
# CMSC 143
# Lab 5
# I worked on this lab with Meagan Kenney

from Myro import *
from math import *

init("/dev/tty.Fluke2-09CA-Fluke2")
# Connect your own robot to customize the html website!

f = open("lab5.html", "w")

p=takePicture()
savePicture(p, "robot.jpg")
 
def sensing():
    if (sum(getObstacle())/3) > 3200:
        return "You're getting close!"
    else:
        return "All clear"
          
level = str(getBattery())
light = str(getLight(1))
sensors = str(sensing())

page = "<html><head>"
page = page + "<style>"
page = page + "body {background-color: rgb(115, 81, 165); text-align: center;}"
page = page + "h1 {font-size: 200%; font-family: zapfino}"
page = page + "table{font-family: arial, sans-serife; border: 1px solid black; width: 50%; text-align: center;}}"
page = page + "td, th, tr { border: 1px solid black; border-collapse: collapse; text-align: left;padding: 8px;}tr:nth-child(even) {background-color: gray;}"
page = page + "ul {list-style-position: inside;} </style></head>"

page = page + "<body><h1><p>Meagan and Noah's Robot Lounge!</p></h1>"
page = page + "<p> Connect a robot to learn more about it!"
page = page + "<h2>Current robot: My name is "
page = page + "<span font-family:Helvetica Neue-Thin>" + str(getName()) + "</span></h2>"

page = page + "<h2> What would you like to know about me? "
page = page + "<p><button type = " + '"button"' + "onclick=alert(" + level + ")>" + "Battery Level </button></p>"
page = page + "<p><button type = " + '"button"' + "onclick=alert(" + light + ")>" + "Light Level </button></p>"
page = page + "</h2>"

page = page + "<h2> Turn that frown upside down!</h2><p><img src=robot.jpg alt=My test image></p>"

page = page + "<h2>These are a few of our favorite links..." + "</h2>"
page = page + "<ul>"
page = page + "<li>" + "<a href=https://www.youtube.com/watch?v=0IagRZBvLtw>Happy Song" + "</a>" + "</li>"
page = page + "<li>" + "<a href=http://sanger.dk/>Puppy Licks" + "</a>" + "</li>"
page = page + "<li>" + "<a href=http://thenicestplaceontheinter.net/>Hugz 4 All" + "</a>" + "</li>"
page = page + "</ul>"

page = page + "<table align='center'>" + "<caption><b> Fun Primary Color Blending </b></caption>" + "<tr>"
page = page + "<th>Colors</th>"
page = page + "<th>Red</th>"
page = page + "<th>Blue</th>"
page = page + "<th>Yellow</th></tr>"
page = page + "<tr><th>Red</th>"
page = page + "<td>Red</td>"
page = page + "<td>Purple</td>"
page = page + "<td>Orange</td>"
page = page + "<tr><th>Blue</th>"
page = page + "<td>Purple</td>"
page = page + "<td>Blue</td>"
page = page + "<td>Green</td>"
page = page + "<tr><th>Yellow</th>"
page = page + "<td>Orange</td>"
page = page + "<td>Green</td>"
page = page + "<td>Yellow</td></tr></table>"
page = page + "</body></html>"

f.write(page)
f.close()
