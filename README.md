# Reddit scrapper to CSV file with comments by PRAW

## Setup 

### How to start python script in shell (for Windows)

1. Install python 3.7+ https://www.python.org/downloads/windows/ 
2. Install pipenv `pip install --user pipenv`. Docs are here: https://github.com/pypa/pipenv
3. To install all packages run this command: `pipenv install`
4. To start python script: `pipenv run py main.py` (for windows)

### Data
1. You should specify some Subreddits in list (by default subreddits will be sorting by **@hot**).
2. Specify your file name where you want to save data from Reddit (by default file will be in the same folder "**reddit_comments.csv**").
3. Make your own `.env` file in root directory and paste in it your **client_id**, **client_secret** and **user_agent**. Watch this file `.env.example`

**PRAW** project https://github.com/praw-dev/praw

Full documentation https://praw.readthedocs.io/en/stable/index.html
