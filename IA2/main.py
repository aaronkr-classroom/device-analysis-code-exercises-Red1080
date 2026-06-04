from Sensor import TemperatureSensor, LightSensor

temp = TemperatureSensor("Temp1")
light = LightSensor("Light")

print(f"Temp: {temp.read()}")
print(f"Light: {light.read()}")