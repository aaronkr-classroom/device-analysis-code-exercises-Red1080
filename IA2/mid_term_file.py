#Sensor.py
import random as r

class Sensor: 
    """
    Base sensor class.
    """
    def __init__(self, name: str) -> None:
        self.name = name

    def read(self) -> float:
        return 0.0 

# Inheritance (google collab help)
class TemperatureSensor(Sensor):
    """
    Simulated temp sensor.
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)

        def read(self) -> float: 
            return round(r.uniform(20.0, 30.0),2)

class LightSensor(Sensor):
    """
    Simulated light sensor.
    """
    def read(self) -> float: 
        return round(r.uniform(0, 100), 2)

class RoomSensor:
    """
    A class to represent a room sensor with temperature, humidity, and light.
    """
    def __init__(self, name: str, temperature: float, humidity: float, light: float) -> None:
        self.name = name
        self.temperature = temperature
        self.humidity = humidity
        self.light = light

    def show_info(self):
        print(f"Sensor: {self.name}")
        print(f"Temperature: {self.temperature}")
        print(f"Humidity: {self.humidity}")
        print(f"Light: {self.light}")

    def comfort_level(self) -> str:
        if 20 <= self.temperature <= 26 and 40 <= self.humidity <= 60:
            return "Comfortable"
        elif self.temperature >= 30 or self.humidity >= 70:
            return "Warning"
        else:
            return "Normal"

    def light_status(self) -> str:
        if self.light < 200:
            return "Dark"
        else:
            return "Bright"
        
#create & store multiple objects
sensors = [
    RoomSensor("Kitchen", 31.0, 72.0, 180.0),
    RoomSensor("Bedroom", 22.0, 50.0, 250.0),
    RoomSensor("Balcony", 18.0, 30.0, 500.0)
    ]

#initialize counters

counts = {"Comfortable": 0, "Normal":0, "Warning":0}

#Loop Through the List

for sensor in sensors:
    sensor.show_info()
    level = sensor.comfort_level()
    status = sensor.light_status()
    
    print(f"Comfort Level: {level}") #(google collab help)
    print(f"Light Status: {status}")
    print("-" * 20)
    
    # Update counts (google collab help)
    if level in counts:
        counts[level] += 1

#for bonus (google collab help)
print("Summary Totals:")
for category, count in counts.items():
    print(f"{category}: {count}")