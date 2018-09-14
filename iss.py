import json
import turtle
import urllib.request
import time

#url = 'http://api.open-notify.org/astros.json' #returns people on space stations
url = 'http://api.open-notify.org/iss-now.json' #returns position of iss
response = urllib.request.urlopen(url)

result = json.loads(response.read())
# print(result) #prints out a bunch of info

#print('People in Space: ', result['number'])

#people = result['people']
#print(people)
#for p in people:
 #   print(p['name'])

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longitude: ', lon)

#screen = turtle.Screen()
#screen.setup(259, 194)
#screen.setworldcoordinates(-180, -90, 180, 90)
#screen.bgpic(r'C:\Users\Harry Torrenegra\Desktop\map.jpg')

#screen.register_shape('iss.png')
#iss = turtle.Turtle()
#iss.shape('iss.png')
#iss.setheading(90)

#iss.penup()
#iss.goto(lon, lat)

#above me
lat = 40.039439
lon = -75.372115

url = 'http://api.open-notify.org/iss-pass.json'
url = url + '?lat=' + str(lat) + '&lon=' + str(lon)
response = urllib.request.urlopen(url)
result = json.loads(response.read())
over = result['response'][1]['risetime']
print(time.ctime(over))

style = ('Arial', 10, 'bold')


