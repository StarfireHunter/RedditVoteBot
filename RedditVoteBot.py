import os
import time
import logging
from dotenv import load_dotenv
from collections import deque
import praw

# ==========================================
# DEBUG CONFIGURATION
# ==========================================
# Set to False to keep the console clean
DEBUG_MODE = False  

log_date_format = '%Y-%m-%d %H:%M:%S'
log_message_format = '%(asctime)s - [%(levelname)s] - %(message)s'

if DEBUG_MODE:
    logging.basicConfig(
        level=logging.DEBUG, 
        format=log_message_format,
        datefmt=log_date_format,
        force=True
    )
else:
    logging.basicConfig(
        level=logging.INFO, 
        format=log_message_format,
        datefmt=log_date_format,
        force=True  # <--- This handles the formatting when debug is off!
    )
# ==========================================

load_dotenv()

# Read the delay from the .env file, defaulting to 60 seconds if it's missing or invalid
try:
    LOOP_DELAY = int(os.environ.get("DELAY_SECONDS", 60))
except ValueError:
    logging.warning("Invalid DELAY_SECONDS in .env. Defaulting to 60 seconds.")
    LOOP_DELAY = 60

reddit = praw.Reddit(
    client_id=os.environ.get("PRAW_CLIENT_ID"),
    client_secret=os.environ.get("PRAW_CLIENT_SECRET"),
    user_agent=os.environ.get("PRAW_USER_AGENT"),
    username=os.environ.get("PRAW_USERNAME"),
    password=os.environ.get("PRAW_PASSWORD")
)

def process_submissions(user, vote_type, already_done):
    try:
        logging.debug(f"Fetching submissions for user: {user.name}")
        submissions = list(user.submissions.new(limit=25))
        logging.debug(f"Found {len(submissions)} total recent submissions.")

        for submission in submissions:
            if submission.id not in already_done:
                logging.debug(f"Processing submission ID: {submission.id}")
                
                # Dynamically call upvote or downvote
                getattr(submission, vote_type)()
                already_done.append(submission.id)
                
                logging.info(f"Action '{vote_type}' applied to: {submission.permalink}")
                time.sleep(2)  # Short baseline safety delay between individual actions
            else:
                logging.debug(f"Skipping submission ID {submission.id} (Already processed)")
                
    except Exception as e:
        logging.error(f"An error occurred during processing: {e}")

def run_bot():
    username = input('Enter the username of the target: ')
    vote_input = input('Would you like to (U)pvote or (D)ownvote? (U|D): ').lower()
    run_continuously = input('Would you like the bot to run continuously? (Y|N): ').lower()
    
    vote_actions = {'u': 'upvote', 'd': 'downvote'}
    vote_action = vote_actions.get(vote_input)

    if not vote_action:
        logging.error('Invalid vote type entered. Exiting.')
        return

    already_done = deque(maxlen=1000)
    user = reddit.redditor(username)

    while True:
        logging.info(f'Checking submissions for /u/{username}...')
        process_submissions(user, vote_action, already_done)
        
        if run_continuously == 'y':
            logging.info(f"Sleeping for {LOOP_DELAY} seconds before next check...")
            time.sleep(LOOP_DELAY)
        else:
            logging.debug("Run continuously not requested. Exiting loop.")
            break

if __name__ == '__main__':
    run_bot()
