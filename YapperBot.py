import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

# Intents
intents = discord.Intents.all()
intents.messages = True
intents.guild_messages = True

bot = commands.Bot(command_prefix="/", intents=intents)

# Custom emoji IDs
emoji_map = {
    ":OOOO:": "<a:OOOO:1174747281841475644>",  # <a: means animated <: means static>
    ":kek:": "<:kek:1174739752025591828>",
    ":stiixy:": "<:stiixy:1205213506513801227>",
    ":EZ:": "<:EZ:1200091490194563224>",
    ":monkaGIGA:": "<:monkaGIGA:1200079862614982686>",
    ":limeD:": "<:limeD:1174742087544094821>",
    ":wiixy:": "<:wiixy:1203163440714088458>",
    ":HELP:": "<:HELP:1174742018757505155>",
    ":GotEEM:": "<a:GotEEM:1200091830373584966>",
    ":lights:": "<:lights:1205214744789786655>",
    ":ICBM:": "<:ICBM:1170057549408641034>",
    ":lebronJAM:": "<a:lebronJAM:1235281866853187666>",
    ":Lamonster:": "<a:Lamonster:1200092413931302943>",
    ":sleghamber:": "<:sleghamber:1205217372194082858>",
}

# build dictionary
categories = {
    "Light": {
        "weapons": [
            "93R", "Dagger", "LH1", "M11", "SH1900", "SR-84", "Sword", "Throwing Knives", "V9S", "XP-54"
        ],
        "specializations": [
            "Cloaking Device", "Evasive Dash", "Grappling Hook"
        ],
        "gadgets": [
            "Breach Charge", "Gateway", "Glitch Grenade", "Smoke Grenade", "Sonar Grenade",
            "Stun Gun", "Thermal Vision", "Tracking Dart", "Vanishing Bomb", "Flashbang",
            "Frag Grenade", "Gas Grenade", "Goo Grenade", "Pyro Grenade"
        ]
    },
    "Medium": {
        "weapons": [
            "AKM", "CL-40", "FAMAS", "FCAR", "Model 1887", "R.357", "Riot Shield"
        ],
        "specializations": [
            "Dematerializer", "Guardian Turret", "Healing Beam"
        ],
        "gadgets": [
            "APS Turret", "Data Reshaper", "Defibrillator", "Explosive Mine", "Gas Mine", "Glitch Trap",
            "Jump Pad", "Zipline", "Flashbang", "Frag Grenade", "Gas Grenade", "Goo Grenade", "Pyro Grenade"
        ]
    },
    "Heavy": {
        "weapons": [
            "Flamethrower", "KS-23", "Lewis Gun", "M60", "MGL32", "SA1216", "Sledgehammer"
        ],
        "specializations": [
            "Charge 'N' Slam", "Goo Gun", "Mesh Shield"
        ],
        "gadgets": [
            "Anti-Gravity Cube", "Barricade", "C4", "Dome Shield", "Explosive Mine", "Motion Sensor",
            "Pyro Mine", "RPG-7", "Flashbang", "Frag Grenade", "Gas Grenade", "Goo Grenade", "Pyro Grenade"
        ]
    }
}

@commands.cooldown(1, 180, commands.BucketType.user)
@bot.command()
async def spin(ctx):
    emojis = {
        "🦴": 60, "🍎": 40, "🍑": 40, "🍉": 30, "🍋": 20,
        "🍒": 10, "🥒": 10, "🍍": 10, "🍇": 10, "⚡": 5,
        "🌈": 1, "📖": 0.25
    }

    total_weight = sum(emojis.values())
    normalized_emojis = {emoji: weight / total_weight for emoji, weight in emojis.items()}

    selected_emojis = random.choices(
        population=list(normalized_emojis.keys()),
        weights=list(normalized_emojis.values()),
        k=3
    )

    await ctx.send(' '.join(selected_emojis))

@commands.cooldown(1, 180, commands.BucketType.user)  # 1 usage per 180 seconds per user
@bot.command()
async def gofish(ctx):
    outcomes = {
        ":kek: not even a bite": 80,
        ":OOOO: you caught a :wiixy:": 10,
        ":OOOO: you caught a rare :stiixy:": 5,
        ":HELP: GET DOWN YOU CAUGHT AN :ICBM:": 10,
        ":GotEEM: you caught DEEZ NUTS": 5,
        ":OOOO: you caught a :lights:": 5,
        ":HELP: YOU ARE CURSED :Lamonster:": 2,
        ":OOOO: you caught a :sleghamber:": 10,
    }

    total_weight = sum(outcomes.values())
    normalized_outcomes = {outcome: weight / total_weight for outcome, weight in outcomes.items()}

    selected_outcome = random.choices(
        population=list(normalized_outcomes.keys()),
        weights=list(normalized_outcomes.values()),
        k=1
    )[0]

    # Replace emoji names with custom emojis if available
    for emoji_name, emoji_id in emoji_map.items():
        selected_outcome = selected_outcome.replace(emoji_name, emoji_id)

    await ctx.send(selected_outcome)

@commands.cooldown(1, 180, commands.BucketType.user)
@bot.command()
async def wheelspin(ctx):
    outcomes = {
        ":EZ: Scammed": 90,
        ":kek: double down & spin again": 10,
        ":kek: Paste clipboard on Phone/PC OR No messages for 10 minutes": 10,
        ":kek: Ping any user (Not Admins) 3 times in a row": 2,
        ":kek: Compliment the previous chatter": 10,
        ":monkaGIGA: ping admin 3 times in a row (might get banned lul)": 2,
        ":kek: No emotes for 30 minutes": 10,
        ":wiixy: use wiixy at the start of every message for 10 minutes": 10,
        ":kek: Only talk in emotes for 10 minutes in the entire server": 10,
        ":EZ: Post your last THE FINALS outfit in the drip check channel": 5,
        ":kek: Use fully default skins for your next game": 5,
        ":GotEEM: spin these nuts in yo mouth": 10,
        ":limeD: triple down & spin again in 3 minutes": 5,
        ":kek: type /build for your next game (Unranked)": 5,
        ":limeD: quadruple down & spin again in 3 minutes": 1,
        ":kek: Talk in opposites for 10 minutes in the entire server": 10,
        ":kek: Make the next 5 messages a pun": 10,
        ":lebronJAM: Paste the last song you listened to (YouTube Link)": 10,
        ":lebronJAM: Listen to the last song someone posted above": 5,
        ":kek: banned for 1 day": 1,

    }

    total_weight = sum(outcomes.values())
    normalized_outcomes = {outcome: weight / total_weight for outcome, weight in outcomes.items()}

    selected_outcome = random.choices(
        population=list(normalized_outcomes.keys()),
        weights=list(normalized_outcomes.values()),
        k=1
    )[0]

    # Replace emoji names with custom emojis if available
    for emoji_name, emoji_id in emoji_map.items():
        selected_outcome = selected_outcome.replace(emoji_name, emoji_id)

    await ctx.send(selected_outcome)

def generate_build(category_name):
    category = categories[category_name]
    weapon = random.choice(category['weapons'])
    specialization = random.choice(category['specializations'])
    gadgets = random.sample(category['gadgets'], 3)  # make sure gadgets are unique

    return (
        f"**Category:** {category_name}\n"
        f"**Weapon:** {weapon}\n"
        f"**Specialization:** {specialization}\n"
        f"**Gadgets:** {', '.join(gadgets)}"
    )

@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command()
async def build(ctx):
    category_name = random.choice(list(categories.keys()))
    response = generate_build(category_name)
    await ctx.send(response)

@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command()
async def buildlight(ctx):
    response = generate_build("Light")
    await ctx.send(response)

@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command()
async def buildmedium(ctx):
    response = generate_build("Medium")
    await ctx.send(response)

@commands.cooldown(1, 120, commands.BucketType.user)
@bot.command()
async def buildheavy(ctx):
    response = generate_build("Heavy")
    await ctx.send(response)

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

while True:
    try:
        bot.run(discord_token)
    except:
        os.system("python YapperBot.py")