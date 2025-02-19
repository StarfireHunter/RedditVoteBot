# RedditVoteBot

RedditVoteBot is a Python script that can be used to automatically upvote or downvote all Submissions made by a specific Reddit user.

## Prerequisites

- Python 3.x
- PRAW (Python Reddit API Wrapper)
- Reddit account with a registered application and OAuth2 credentials

## Getting Started

1. Clone this repository or download the script `RedditVoteBot.py`.
2. Install requirements: `pip install -r requirements.txt`.
3. Install dotenv: `pip install python-dotenv`
4. Register a Reddit application and obtain OAuth2 credentials by following the instructions [here](https://www.reddit.com/prefs/apps).
5. Set the following environment variables in `.env` with your Reddit OAuth2 credentials:
   - `PRAW_CLIENT_ID`: your client ID
   - `PRAW_CLIENT_SECRET`: your client secret
   - `PRAW_USER_AGENT`: a descriptive user agent string
   - `PRAW_USERNAME`: your Reddit username
   - `PRAW_PASSWORD`: your Reddit password
6. Run the script from the command line: `python3 RedditVoteBot.py`.

## Usage

When you run the script, you will be prompted to enter the username of the target Reddit user, whether you want to upvote or downvote their Submissions, and whether you want the bot to run continuously. The script will then automatically upvote or downvote all Submissions made by the target user. The script will print the permalink of each Submission that is voted on.

### Example usage:

```Enter the username of the target: some_user
Would you like to (U)pvote or (D)ownvote the target? (U|D). D
Would you like the bot to run continuously? (Y|N) Y
Beginning to downvote. The permalink to the Submission will be printed when a Submission is downvoted.
https://www.reddit.com/r/some_subreddit/Submissions/some_post/some_Submission
https://www.reddit.com/r/some_subreddit/Submissions/some_post/another_Submission
```


## Contributing

Feel free to contribute to this project by submitting a pull request. If you find any bugs or have any feature requests, please open an issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
