> [!WARNING]
> **This repository is officially ARCHIVED and no longer functional.**
>
> Due to structural updates and stricter OAuth enforcement implemented by Reddit regarding their API endpoints, programmatic and automated voting actions via personal script applications are strictly blocked by the platform. As a result, this script will now return a `404 Not Found` error upon attempting any vote modifications.
> 
> Because this is a platform-side restriction enforced on Reddit's servers, there is no workaround or code patch to fix it. This repository remains online purely for historical/educational reference and will not receive further updates or support.

# RedditVoteBot

RedditVoteBot is a Python script that was used to automatically upvote or downvote all Submissions made by a specific Reddit user.

> **Note:** Due to the API changes detailed in the warning above, the setup instructions below are preserved strictly for historical reference.

## Prerequisites

- Python 3.x
- PRAW (Python Reddit API Wrapper)
- Reddit account with a registered application and OAuth2 credentials

## Getting Started

1. Clone this repository or download the script `RedditVoteBot.py`.
2. Install Praw: `pip install praw`.
3. Install dotenv: `pip install python-dotenv`
4. Register a Reddit application and obtain OAuth2 credentials by following the instructions [here](https://www.reddit.com/prefs/apps).
5. Set the following environment variables in `.env` with your Reddit OAuth2 credentials:
   - `PRAW_CLIENT_ID`: your client ID
   - `PRAW_CLIENT_SECRET`: your client secret
   - `PRAW_USER_AGENT`: a descriptive user agent string
   - `PRAW_USERNAME`: your Reddit username
   - `PRAW_PASSWORD`: your Reddit password
6. Configure the delay for checking for a new post by changing the following variables in `.env`
   - `DELAY_SECONDS`:  Time to wait (in seconds)
7. Run the script from the command line: `python3 RedditVoteBot.py`.

## Usage

When the script was functional, running it would prompt you to enter the target Reddit user's username, whether you wanted to upvote or downvote their Submissions, and whether you wanted the bot to run continuously. The script would then automatically upvote or downvote all Submissions made by the target user, printing the permalink of each Submission that was voted on.

### Example usage (Historical):

```text
Enter the username of the target: some_user
Would you like to (U)pvote or (D)ownvote the target? (U|D). D
Would you like the bot to run continuously? (Y|N) Y
Beginning to downvote. The permalink to the Submission will be printed when a Submission is downvoted.
[https://www.reddit.com/r/some_subreddit/Submissions/some_post/some_Submission](https://www.reddit.com/r/some_subreddit/Submissions/some_post/some_Submission)
[https://www.reddit.com/r/some_subreddit/Submissions/some_post/another_Submission](https://www.reddit.com/r/some_subreddit/Submissions/some_post/another_Submission)
