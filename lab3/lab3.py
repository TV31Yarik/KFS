import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("kfs/lab3/dataset/GlobalWeatherRepository.csv")

df['date'] = pd.to_datetime(df['last_updated'])
df['wind_speed'] = df['wind_kph']
df['temperature'] = df['temperature_celsius']
df['felt_temp'] = df['feels_like_celsius']

df['date'] = pd.to_datetime(df['date']).dt.normalize()  

df['month'] = df['date'].dt.month


plt.figure(figsize=(8, 5))
df.groupby('month')['wind_speed'].mean().plot(kind='bar', color='skyblue')
plt.title("Середня швидкість вітру по місяцях")
plt.xlabel("Місяць")
plt.ylabel("Швидкість вітру (км/год)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(x='wind_speed', y='temperature', data=df, alpha=0.5)
plt.title("Залежність температури від сили вітру")
plt.xlabel("Швидкість вітру (км/год)")
plt.ylabel("Температура (°C)")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 5))
sns.lineplot(x='date', y='temperature', data=df, label='Реальна температура', color='blue')
sns.lineplot(x='date', y='felt_temp', data=df, label='Відчутна температура', color='orange')
plt.title("Реальна vs Відчутна температура (з урахуванням вітру)")
plt.xlabel("Дата")
plt.ylabel("Температура (°C)")
plt.legend()
plt.tight_layout()
plt.show()
