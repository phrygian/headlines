import pyowm

owm = pyowm.OWM('09eae7f84a2bf6a02bb93e9f31ee80a8')  

observation = owm.weather_at_place('Bangkok, TH')
w = observation.get_weather()
print(w)                      # <Weather - reference time=2013-12-18 09:20,
print(w.['time'])                             

w.get_wind()                  # {'speed': 4.6, 'deg': 330}
w.get_humidity()              # 87
w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}


observation_list = owm.weather_around_coords(-22.57, -43.12)

temp_list = w.get_temperature('celsius')

print(temp_list['temp'])
print(w.get_humidity())