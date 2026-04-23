from Sensor import TemperatureSensor, LightSensor

temp = TemperatureSensor("Temp1")
light = LightSensor("Light")
name = NameSensor("Name")
humidity = HumiditySensor("Humidity")

print(f"Temp: {temp.read()}")
print(f"Light: {light.read()}")
print(f"Name: {name.read()}")
print(f"Humidity: {humidity.read()}")
