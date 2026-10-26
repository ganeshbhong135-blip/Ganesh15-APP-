import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("weather.csv")

print("Weather Data:")
print(df)


print("\nAverage Temperature:", df["Temperature"].mean())
print("Maximum Temperature:", df["Temperature"].max())
print("Minimum Temperature:", df["Temperature"].min())


day = df.loc[df["Temperature"].idxmax()]

print("\nDay with Highest Temperature:")
print(day)


plt.plot(df["Date"], df["Temperature"], marker="o")
plt.title("Daily Temperature Changes")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


plt.hist(df["Temperature"], bins=5, edgecolor="black")
plt.title("Distribution of Temperatures")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


plt.scatter(df["Humidity"], df["Temperature"])
plt.title("Humidity vs Temperature")
plt.xlabel("Humidity")
plt.ylabel("Temperature")
plt.grid(True)
plt.tight_layout()
plt.show()