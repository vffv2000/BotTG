# Project 
This project is a Telegram bot developed in Python using the telebot, requests, random, yaml, and time libraries. The bot provides weather information and additional features, such as sending random photos of cats or dogs. The bot also has an administrator panel that allows the administrator to manage bot functions, such as sending messages to users or changing bot settings.
# Description

The bot uses the telebot library to handle user requests and respond with up-to-date weather information obtained from a weather service API. Users can send requests to the bot to get the current weather in a specific city. The bot also has a feature that allows users to get a random photo of a cat or dog by sending a specific command.

The administrator panel provides additional functionality for the bot. The administrator can send messages to users, change bot settings, and manage user data. The bot uses a YAML file to store configuration settings, making it easy to modify the bot's behavior.
# Usage

To use the bot, users need to search for it on Telegram and start a conversation with it. Users can then send commands to the bot to get weather information, photos of cats or dogs, or interact with the administrator panel.

The following commands are available:

-   -   `/start` - start the conversation with the bot.
-   `/help` - display a list of available commands.
-   `/weather <city>` - display the current weather in the specified city.
-   `/cat` - display a random photo of a cat.
-   `/dog` - display a random photo of a dog.
-   `/admin` - display the administrator panel (only available to the administrator).

The administrator panel commands are:

-   `/send <user_id> <message>` - send a message to a specific user.
-   `/broadcast <message>` - send a message to all users.
-   `/settings` - display and modify bot settings.
-   `/users` - display a list of registered users.


# Technologies Used

-   Python

> Main programming language used for the project.

-   telebot

> Python library used for building Telegram bots.

-   requests

> Python library used for making HTTP requests to weather service APIs.

-   random

> Python library used for generating random numbers.

-   yaml

> Used for storing and reading configuration settings.

-   time

> Used for pausing the program execution for a specified amount of time.

# How to Run

-   Clone the repository
-   Create a virtual environment and activate it
-   Install the required packages using the command `pip install -r requirements.txt`
-   Create a file named `config.yaml` and add the necessary configuration settings (Telegram bot token, weather service API key)
-   Run the bot using the command `python bot.py`

# Contributing

If you want to contribute to the project, you can fork the repository, make your changes, and submit a pull request. Please make sure to follow the coding style used in the project and include tests for your changes.
