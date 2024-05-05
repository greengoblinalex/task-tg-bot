# Task Telegram Bot

## Disclaimer
This project is purely for educational and evaluation purposes. It may contain simplified implementations and is not intended for production use.

## Description
The Task Manager Bot is designed to help users manage their tasks efficiently through a Telegram bot interface. Users can add tasks and retrieve the list of tasks they have added.

## Installation and Setup
1. Clone the repository:
```
# Clone the repository to your local machine
git clone https://github.com/your_username/task_manager_bot
```
2. Install dependencies:
```
# Install required dependencies
pip install -r requirements.txt
```
3. Configure parameters:
* Create a .env file in the project root directory.
* Copy the contents of .env.example into .env.
* Replace your_bot_token with your Telegram bot token obtained from the BotFather.
* Replace user, pass, host, and dbname in SQL_URL with your PostgreSQL database credentials and connection details.

## Usage
1. Run the script:
```
# Run the main script
python -m src.main
```
2. Adding a task:
* Use the /add command followed by the task description to create a new task.
3. Getting tasks:
* Use the /tsk command to retrieve a list of all tasks you have added.