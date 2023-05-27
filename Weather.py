import eel
import pyowm

own = pyowm.OWM("853f97b74f28575725a60fd492a011fc")

@eel.expose
def get_weather(place):
    mgr = own.weather_manager()

    observation = mgr.weather_at_place()
    w = observation.weather

    temp = w.temperature('celsius')['temp']

    return "In the city " + " now " + str(temp) + " degrees!"


eel.init("web")
eel.start("gt.html", size=(700, 700))
