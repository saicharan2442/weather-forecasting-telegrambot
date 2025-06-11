# 🌦️ Telegram Weather Bot

A simple Python-based Telegram bot that fetches a **5-day weather forecast** using the AccuWeather API.

---

## 🔧 Features

- `/start` – Welcomes the user and explains usage
- `/weather <city>` – Returns the 5-day weather forecast for the specified city
- Uses the **AccuWeather API** for reliable forecasts
- Powered by `python-telegram-bot` library

---

## 🚀 How to Set Up

### 1. Create a Telegram Bot via BotFather

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Start a chat and type `/newbot`
3. Follow the instructions and choose a name and username for your bot
4. You will receive a **Bot Token** (keep this safe!)

---

### 2. Get Your AccuWeather API Key

1. Go to the [AccuWeather Developer Portal](https://developer.accuweather.com)
2. Sign up for a free account and verify your email
3. Navigate to **[My Apps](https://developer.accuweather.com/user/me/apps)**  
4. Click **"Add a new App"**
5. Fill in the form:
   - **App Name**: `WeatherBot`
   - **App Purpose**: `Telegram weather bot for personal use`
   - **API Products**: Select `Locations` and `Forecasts`
6. Submit the form – you’ll receive your **API Key**

---

### 3. Set Up the Script

1. Download or clone this repository
2. Open the `weather.py` file in any code editor (e.g., VS Code)
3. Replace the placeholder values with your actual keys:
   ```python
   ACCUWEATHER_API_KEY = 'your_accuweather_api_key'
   TELEGRAM_BOT_TOKEN = 'your_telegram_bot_token'
   
---

### Install required packages: 
pip install python-telegram-bot==20.0b1 requests

### Run the bot using:
python weather.py

---

### 💬 How to Use
Open Telegram and search for your bot (by the username you gave it)

Send /start to begin

### Type:
/weather <city_name>
### Example:
/weather Mumbai

You will receive a 5-day weather forecast for the specified city.

---

### 🛠 Built With
Python
python-telegram-bot
AccuWeather API
