#!/usr/bin/env python3
# RedditVoteBot v3.0 - Originally by @spediso, modified by @starfirehunter

import os
import time
import logging
from dotenv import load_dotenv
from collections import deque
import praw

# ==========================================
# DEBUG CONFIGURATION
# ==========================================
DEBUG_MODE = False  

log_date_format = '%Y-%m-%d %H:%M:%S'
log_message_format = '%(asctime)s - [%(levelname)s] - %(message)s'

if DEBUG_MODE:
    logging.basicConfig(level=logging.DEBUG, format=log_message_format, datefmt=log_date_format, force=True)
else:
    logging.basicConfig(level=logging.INFO, format=log_message_format, datefmt=log_date_format, force=True)
# ==========================================

load_dotenv()

# Read the loop cycle delay from the .env file, defaulting to 60 seconds
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

def process_items(user, target_type, vote_type, already_done):
    try:
        logging.debug(f"Fetching recent content for user: {user.name}")
        
        # Dynamically select either user.submissions.new or user.comments.new
        if target_type == 'p':
            items = list(user.submissions.new(limit=25))
            label = "submission"
        else:
            items = list(user.comments.new(limit=25))
            label = "comment"

        logging.debug(f"Found {len(items)} total recent {label}s.")

        for item in items:
            if item.id not in already_done:
                logging.debug(f"Processing {label} ID: {item.id}")
                
                # Dynamically call upvote or downvote
                getattr(item, vote_type)()
                already_done.append(item.id)
                
                logging.info(f"Action '{vote_type}' applied to: {item.permalink}")
                time.sleep(2)  # Baseline standard safety delay between API actions
            else:
                logging.debug(f"Skipping {label} ID {item.id} (Already processed)")
                
    except Exception as e:
        logging.error(f"An error occurred during processing: {e}")

def run_bot():
    username = input('Enter the username of the target: ')
    
    target_input = input('Would you like to target (P)osts or (C)omments? (P|C): ').lower()
    if target_input not in ['p', 'c']:
        logging.error('Invalid target type entered. Exiting.')
        return

    vote_input = input('Would you like to (U)pvote or (D)ownvote? (U|D): ').lower()
    vote_actions = {'u': 'upvote', 'd': 'downvote'}
    vote_action = vote_actions.get(vote_input)

    if not vote_action:
        logging.error('Invalid vote type entered. Exiting.')
        return

    run_continuously = input('Would you like the bot to run continuously? (Y|N): ').lower()
    
    already_done = deque(maxlen=1000)
    user = reddit.redditor(username)
    
    target_label = "submissions" if target_input == 'p' else "comments"

    while True:
        logging.info(f'Checking {target_label} for /u/{username}...')
        process_items(user, target_input, vote_action, already_done)
        
        if run_continuously == 'y':
            logging.info(f"Sleeping for {LOOP_DELAY} seconds before next check...")
            time.sleep(LOOP_DELAY)
        else:
            logging.debug("Run continuously not requested. Exiting loop.")
            break

if __name__ == '__main__':
    run_bot()
