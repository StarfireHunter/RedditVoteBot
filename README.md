> [!WARNING]
> **This repository is officially ARCHIVED and no longer functional.**
>
> Due to structural updates and stricter OAuth enforcement implemented by Reddit regarding their API endpoints, programmatic and automated voting actions via personal script applications are strictly blocked by the platform. As a result, this script will now return a `404 Not Found` error upon attempting any vote modifications.
> 
> Because this is a platform-side restriction enforced on Reddit's servers, there is no workaround or code patch to fix it. This repository remains online purely for historical/educational reference and will not receive further updates or support.

# RedditVotingBot

RedditVotingBot is a Python script that was used to automatically upvote or downvote submissions (posts) or comments made by a specific Reddit user. 

This repository was originally programmed by [spediso](https://github.com/spediso/) to target comments and was subsequently modified and expanded by [starfirehunter](https://github.com/StarfireHunter) to support both submissions and custom delay intervals.

> **Note:** Due to the API restrictions detailed in the archive warning above, the setup instructions below are preserved strictly for historical reference.

## Prerequisites

- Python 3.x
- PRAW (Python Reddit API Wrapper)
- Reddit account with a registered application and OAuth2 credentials

## Getting Started

1. Clone this repository or download the `RedditVotingBot.py` & `.env` files and put them in the same directory.
2. Install Praw: `pip install praw`.
3. Install dotenv: `pip install python-dotenv`
4. Register a Reddit application and obtain OAuth2 credentials by following the instructions [here](https://www.reddit.com/prefs/apps).
5. Set the following environment variables in `.env` with your Reddit OAuth2 credentials:
   - `PRAW_CLIENT_ID`: your client ID
   - `PRAW_CLIENT_SECRET`: your client secret
   - `PRAW_USER_AGENT`: a descriptive user agent string
   - `PRAW_USERNAME`: your Reddit username
   - `PRAW_PASSWORD`: your Reddit password
6. Configure the operational loop delay by modifying the following variable in your `.env` file:
   - `DELAY_SECONDS`: Time to wait between checking cycles (in seconds)
7. Run the script from the command line: `python3 RedditVotingBot.py`.

## Usage

When the script was functional, running it would interactively prompt you to enter the target username, select whether you wanted to scan their **Posts** or **Comments**, choose between upvoting or downvoting, and opt to run the scanner continuously on a timer cycle. 

### Example usage (Historical/Outdated):

```text
Enter the username of the target: some_user
Would you like to target (P)osts or (C)omments? (P|C): p
Would you like to (U)pvote or (D)ownvote? (U|D): u
Would you like the bot to run continuously? (Y|N): y
2026-07-11 13:41:46 - [INFO] - Checking submissions for /u/some_user...
2026-07-11 13:41:48 - [INFO] - Action 'upvote' applied to: [https://www.reddit.com/r/example_subreddit/submissions/abc123/example_post_title/](https://www.reddit.com/r/example_subreddit/submissions/abc123/example_post_title/)
2026-07-11 13:41:50 - [INFO] - Action 'upvote' applied to: [https://www.reddit.com/r/example_subreddit/submissions/def456/another_generic_title/](https://www.reddit.com/r/example_subreddit/submissions/def456/another_generic_title/)
2026-07-11 13:41:52 - [INFO] - Sleeping for 60 seconds before next check...
