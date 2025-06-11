import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ✅ Replace these with your actual API key and bot token
ACCUWEATHER_API_KEY = 'na0TQR9bVQGiZBnhObsxpOAIf3GKKK7G'
TELEGRAM_BOT_TOKEN = '7886254355:AAGhyMXCoaU61FX95cbWoywl7s8rZTR0GsY'

# 🔍 Get location key for city
def get_location_key(city_name):
    url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": ACCUWEATHER_API_KEY,
        "q": city_name
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data:
        location_key = data[0]["Key"]
        localized_name = data[0]["LocalizedName"]
        country = data[0]["Country"]["LocalizedName"]
        return location_key, localized_name, country
    return None, None, None

# 🌤️ Get 5-day forecast for location key
def get_forecast(location_key):
    url = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location_key}"
    params = {
        "apikey": ACCUWEATHER_API_KEY,
        "metric": "true"
    }
    response = requests.get(url, params=params)
    return response.json()

# 👋 /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌤️ Hello! I’m your Weather Bot.\n"
        "Send /weather <city_name> to get a 5-day weather forecast.\n"
        "Example: /weather Hyderabad"
    )

# ☁️ /weather <city> command
async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Please provide a city name. Example:\n/weather Mumbai")
        return

    city = ' '.join(context.args)
    location_key, city_name, country = get_location_key(city)

    if not location_key:
        await update.message.reply_text("❌ City not found. Please check the spelling and try again.")
        return

    forecast_data = get_forecast(location_key)

    if "DailyForecasts" not in forecast_data:
        await update.message.reply_text("⚠️ Unable to fetch weather data. Try again later.")
        return

    message = f"📍 5-Day Forecast for {city_name}, {country}:\n\n"

    for day in forecast_data["DailyForecasts"]:
        date = day["Date"][:10]
        min_temp = day["Temperature"]["Minimum"]["Value"]
        max_temp = day["Temperature"]["Maximum"]["Value"]
        day_phrase = day["Day"]["IconPhrase"]
        night_phrase = day["Night"]["IconPhrase"]

        message += (
            f"📅 {date}\n"
            f"🌞 Day: {day_phrase}, 🌙 Night: {night_phrase}\n"
            f"🌡️ {min_temp}°C - {max_temp}°C\n\n"
        )

    await update.message.reply_text(message)

# 🚀 Run the bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("weather", weather))
    print("✅ Weather bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
