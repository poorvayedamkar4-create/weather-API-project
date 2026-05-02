import requests
import matplotlib.pyplot as plt

# API KEY
API_KEY = "9bbf285f6a696e616866c1d651352193"

# CITY NAME
city = "Amravati"

# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# REQUEST DATA
response = requests.get(url)
data = response.json()

print(data)   # check data

# FETCH VALUES
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]

# PRINT OUTPUT
print("City:", city)
print("Temperature:", temperature)
print("Humidity:", humidity)
print("Pressure:", pressure)

# VISUALIZATION
labels = ["Temperature", "Humidity", "Pressure"]
values = [temperature, humidity, pressure]

plt.bar(labels, values)
plt.title("Weather Data Visualization - Amravati")
plt.show()
print(data)
