import discord
from discord.ext import commands

# Bot configuration
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Data storage
flights = []
flight_log = []
leaderboard = {}

# /book command to schedule flights
@bot.command()
async def book(ctx, name: str, destination: str):
    flight_info = {
        "customer": name,
        "destination": destination,
        "date": "TBD",
        "departure": "TBD",
        "gate": "TBD"
    }
    flights.append(flight_info)
    await ctx.send(f"Thank you for choosing AerEuroRegalia🇪🇺👑, {name}!")

# /flights command to show scheduled flights
@bot.command()
async def flights(ctx):
    if len(flights) == 0:
        await ctx.send("No flights are currently scheduled.")
    else:
        flight_list = "Scheduled Flights:\n"
        for flight in flights:
            flight_list += f"Customer: {flight['customer']}, Destination: {flight['destination']}, Date: {flight['date']}, Departure: {flight['departure']}, Gate: {flight['gate']}\n"
        await ctx.send(flight_list)

# /log command to log flight hours
@bot.command()
async def log(ctx, hours: float, aircraft: str, route: str, callsign: str):
    log_entry = {
        "hours": hours,
        "aircraft": aircraft,
        "route": route,
        "callsign": callsign
    }
    flight_log.append(log_entry)

    # Update leaderboard
    if callsign in leaderboard:
        leaderboard[callsign] += hours
    else:
        leaderboard[callsign] = hours

    await ctx.send(f"Flight logged: {hours} hours on {aircraft} from {route} with callsign {callsign}.")

# /leaderboard command to show top pilots by hours
@bot.command()
async def leaderboard(ctx):
    if len(leaderboard) == 0:
        await ctx.send("No flights have been logged yet.")
    else:
        sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
        leaderboard_message = "Leaderboard (Top Pilots by Hours):\n"
        for callsign, hours in sorted_leaderboard:
            leaderboard_message += f"{callsign}: {hours} hours\n"
        await ctx.send(leaderboard_message)

# Run the bot
bot.run('YOUR_DISCORD_BOT_TOKEN')
