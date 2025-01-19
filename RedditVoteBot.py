import praw
import os
from dotenv import load_dotenv
from collections import deque
from concurrent.futures import ThreadPoolExecutor

load_dotenv()

reddit = praw.Reddit(
    client_id=os.environ.get("PRAW_CLIENT_ID"),
    client_secret=os.environ.get("PRAW_CLIENT_SECRET"),
    user_agent=os.environ.get("PRAW_USER_AGENT"),
    username=os.environ.get("PRAW_USERNAME"),
    password=os.environ.get("PRAW_PASSWORD")
)

def vote_on_submissions(user, vote_type, already_done):
    for submission in user.submissions.new(limit=None):
        if submission.id not in already_done:
            getattr(submission, vote_type)()
            already_done.append(submission.id)
            print(submission.permalink)
            time.sleep(30) 

def run_bot():
    username = input('Enter the username of the target: ')
    vote_type = input('Would you like to (U)pvote or (D)ownvote the target? (U|D). ')
    run_continuously = input('Would you like the bot to run continuously? (Y|N) ')
    vote_actions = {'u': 'upvote', 'd': 'downvote'}
    run_continuously_actions = {'y': True, 'n': False}

    already_done = deque(maxlen=1000)
    user = reddit.redditor(username)

    while True:
        vote_action = vote_actions.get(vote_type.lower())
        if vote_action:
            print(f'Beginning to {vote_action}. The permalink to the submission will be printed when a submission is {vote_action}d.')
            with ThreadPoolExecutor() as executor:
                executor.submit(vote_on_submissions, user, vote_action, already_done)
        else:
            print('Invalid vote type.')
            break

        if run_continuously_actions.get(run_continuously.lower()):
            pass
        else:
            break

if __name__ == '__main__':
    run_bot()
