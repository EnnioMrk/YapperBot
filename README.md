# YapperBot: A Discord Bot for Fun and Games
This document describes YapperBot, a Python Discord bot designed for entertainment purposes. The bot offers various interactive commands for users to enjoy.

### Libraries
YapperBot utilizes the following libraries:

discord: The core library for interacting with the Discord API.
discord.ext.commands: An extension library for creating Discord commands.
random: Provides functionalities for generating random numbers.
os: Provides functionalities for interacting with the operating system.

## Intents
The bot utilizes the following Discord Intents:

messages: Allows the bot to receive all messages.
guild_messages: Allows the bot to only receive messages from servers (guilds) it is a member of.

## Emoji Mapping
The bot uses a dictionary emoji_map to translate emoji names used in the code to their corresponding custom emoji IDs. This ensures the bot displays the correct emojis whenever these names are encountered.

## Item Categories
The bot stores weapon, specialization, and gadget information for different build categories (Light, Medium, and Heavy) within a dictionary named categories.

## Commands
The bot offers several commands, each with a cooldown to prevent excessive usage:

**spin**: Simulates a slot machine with various emojis as outcomes. The weight assigned to each emoji determines its probability of appearing.
**gofish**: This fishing-themed command presents a random outcome with varying probabilities, often involving emojis.
**wheelspin**: This gambling-themed command offers a variety of funny or challenging dares as outcomes.
**build**: Generates a random build recommendation with a category (Light, Medium, Heavy), weapon, specialization, and three unique gadgets.
**buildlight, buildmedium, buildheavy**: Dedicated commands to generate builds for specific categories (Light, Medium, and Heavy) respectively.
**Note**: All these commands utilize cooldown timers to prevent spam.

## Running the Bot
The bot relies on a Discord token stored in the environment variable DISCORD_TOKEN. The provided code snippet includes a loop that attempts to connect to the Discord API and restarts the bot script upon encountering any errors.

## Additional Notes
The code utilizes helper functions like generate_build to improve readability and maintainability.
Custom emoji IDs are used within string formatting to display the corresponding emojis.
