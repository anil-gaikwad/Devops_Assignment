import geocoder
import datetime
import pendulum
import socket
from geopy.geocoders import Nominatim
from flask import Flask , render_template 
app = Flask(__name__)


ist = pendulum.timezone('Asia/Calcutta')
Timezone=pendulum.now(ist)


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

g = geocoder.ip('me')
list1 = [g.latlng]
Latitude = str(list1[0][0])
Longitude = str(list1[0][1])

geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.reverse(Latitude+","+Longitude)
address = location.raw['address']
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')

@app.route("/pucsd/")
def pucsd():
    return render_template("pucsd.html",content1=Timezone,content2=ip_address,content3=hostname,content4=city,content5=state,content6=country)
if __name__ == "__main__":
    app.run(debug=True)

