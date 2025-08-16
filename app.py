# from flask import Flask, render_template
# import pandas as pd
# import matplotlib.pyplot as plt
# from scipy.signal import find_peaks

# app = Flask(__name__)

# # Load and process data
# df = pd.read_csv("Sample_Data.csv")
# df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%d-%m-%Y %H:%M")
# df.sort_values("Timestamp", inplace=True)

# # Plot main chart
# plt.figure(figsize=(10,5))
# plt.plot(df['Timestamp'], df['Values'], label='Values')
# plt.title("Main Chart")
# plt.xlabel("Time")
# plt.ylabel("Values")
# plt.legend()
# plt.savefig("static/chart_main.png")
# plt.close()

# # Moving Average
# df['5_day_MA'] = df['Values'].rolling(window=5).mean()
# plt.figure(figsize=(10,5))
# plt.plot(df['Timestamp'], df['Values'], label='Values')
# plt.plot(df['Timestamp'], df['5_day_MA'], label='5-Day Moving Avg', color='orange')
# plt.title("5-Day Moving Average")
# plt.xlabel("Time")
# plt.ylabel("Values")
# plt.legend()
# plt.savefig("static/chart_moving_avg.png")
# plt.close()

# # Peaks and Lows
# peaks, _ = find_peaks(df['Values'])
# lows, _ = find_peaks(-df['Values'])

# plt.figure(figsize=(10,5))
# plt.plot(df['Timestamp'], df['Values'], label='Values')
# plt.plot(df['Timestamp'].iloc[peaks], df['Values'].iloc[peaks], "ro", label='Peaks')
# plt.plot(df['Timestamp'].iloc[lows], df['Values'].iloc[lows], "go", label='Lows')
# plt.title("Peaks & Lows")
# plt.xlabel("Time")
# plt.ylabel("Values")
# plt.legend()
# plt.savefig("static/chart_peaks.png")
# plt.close()

# @app.route('/')
# def index():
#     return render_template('index.html', peaks=df.iloc[peaks], lows=df.iloc[lows])

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

app = Flask(__name__)

# Load and process data
df = pd.read_csv("Sample_Data.csv")
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%d-%m-%Y %H:%M")
df.sort_values("Timestamp", inplace=True)

# ---------- Chart 1: Main Chart ----------
plt.figure(figsize=(10, 5))
plt.plot(df['Timestamp'], df['Values'], label='Values', color='blue')
plt.title("Main Chart")
plt.xlabel("Time")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.savefig("static/chart_main.png")
plt.close()

# ---------- Chart 2: Moving Average ----------
df['5_day_MA'] = df['Values'].rolling(window=5).mean()
plt.figure(figsize=(10, 5))
plt.plot(df['Timestamp'], df['Values'], label='Values', color='blue')
plt.plot(df['Timestamp'], df['5_day_MA'], label='5-Day Moving Avg', color='orange')
plt.title("5-Day Moving Average")
plt.xlabel("Time")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.savefig("static/chart_moving_avg.png")
plt.close()

# ---------- Chart 3: Peaks and Lows ----------
peaks, _ = find_peaks(df['Values'])
lows, _ = find_peaks(-df['Values'])

plt.figure(figsize=(10, 5))
plt.plot(df['Timestamp'], df['Values'], label='Values', color='blue')
plt.plot(df['Timestamp'].iloc[peaks], df['Values'].iloc[peaks], "ro", label='Peaks')
plt.plot(df['Timestamp'].iloc[lows], df['Values'].iloc[lows], "go", label='Lows')
plt.title("Peaks & Lows")
plt.xlabel("Time")
plt.ylabel("Values")
plt.legend()
plt.grid(True)
plt.savefig("static/chart_peaks.png")
plt.close()

# ---------- Chart 4: Custom Style Graph (like your example) ----------
plt.figure(figsize=(12, 6))
plt.plot(df['Timestamp'], df['Values'], label='Values', color='blue', linewidth=2)
plt.scatter(df['Timestamp'].iloc[peaks], df['Values'].iloc[peaks], color='red', s=80, label='Peaks')
plt.scatter(df['Timestamp'].iloc[lows], df['Values'].iloc[lows], color='green', s=80, label='Lows')
plt.plot(df['Timestamp'], df['5_day_MA'], color='orange', linestyle='--', linewidth=2, label='5-Day MA')
plt.title("Custom Graph - Values, Peaks, Lows & Moving Avg", fontsize=16)
plt.xlabel("Timestamp", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig("static/chart_custom.png")
plt.close()

@app.route('/')
def index():
    return render_template(
        'index.html',
        peaks=df.iloc[peaks],
        lows=df.iloc[lows],
        charts=[
            "chart_main.png",
            "chart_moving_avg.png",
            "chart_peaks.png",
            "chart_custom.png"
        ]
    )

if __name__ == "__main__":
    app.run(debug=True)

