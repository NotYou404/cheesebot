# Cheese Bot

The most cheesiest bot on the Planet!
Despite not having the ability to bypass earth's boundaries, I'll try my best serving you lots of cheesecake.

Cheese bot is a several purpose Discord Bot written in Python, using the Pycord API Wrapper.
It was created with the intention to deliver way more cheesecake to Discord!

## Running the bot locally

### Step 1: Clone this repo

For Linux:

```bash
git clone "https://github.com/NotYou404/cheesebot"
cd cheesebot
```

For Windows:

```powershell
git clone "https://github.com/NotYou404/cheesebot"
cd cheesebot
```

Or download the ZIP archive at the top right of this page.

### Step 2: Installing dependencies

Install Python (recommended version: 3.11 or higher)

- <https://www.python.org/downloads>

Create and activate a Virtual Environment (optional)

For Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

For Windows:

```powershell
python3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

\
Install dependencies:

```shell
python3 -m pip install -U pip
python3 -m pip install -r requirements.txt
```

### Step 3: Add your Token and database access

Create a `.env` file in the projects root directory and populate it with the following keys:

```txt
TOKEN = <YOUR_BOT_TOKEN>
MYSQL_HOST = <DATABASE_IP_ADDRESS>
MYSQL_PORT = <DATABASE_PORT>
MYSQL_USERNAME = <MYSQL_USERNAME>
MYSQL_PASSWORD = <MYSQL_PASSWORD>
MYSQL_DATABASE = <DATABASE_NAME>
```

### Step 4: Run the Bot

```shell
python3 cheesebot
```

## Localization

The bot is NOT making use of localized slash commands. This is because people with different languages than the command executor most likely won't understand the output. This is not very useful in multilingual servers. Ability for guild-wide localization may be added in the future.

## Voice Support

For voice support to work, `ffmpeg` should be installed and on PATH. Also make sure `libopus` is installed on your system.

## Required Permissions

The Bots requires following permissions to work properly:

### Text Permissions

- Send Messages
- Manage Messages
- Embed Links
- Attach Files
- Use External Emojis
- Add Reactions
- Use Slash Commands

### Voice Permissions

- Connect
- Speak
