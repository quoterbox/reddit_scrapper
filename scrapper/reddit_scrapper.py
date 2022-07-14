from datetime import datetime


def read_hot_posts_with_comments(reddit, channel: str, limit: int) -> []:
    posts = []

    for submission in reddit.subreddit(channel).hot(limit=limit):
        submission.comments.replace_more(limit=None)

        print("-- " + submission.subreddit_id + " --")
        print("Subreddit for -", getattr(submission.subreddit, "display_name", "None"), end="\n")

        for comment in submission.comments.list():

            if (hasattr(comment, "body") and comment.body != "[removed]" and comment.body != "[deleted]"):
                posts.append({
                    'subreddit_id': getattr(submission, "subreddit_id", "None"),
                    'subreddit_name': getattr(submission.subreddit, "display_name", "None"),
                    'id': getattr(submission, "id", "None"),
                    'title': getattr(submission, "title", "None"),
                    'permalink': 'https://www.reddit.com' + getattr(submission, "permalink", "None"),
                    'link_flair_text': getattr(submission, "link_flair_text", "None"),
                    'author': getattr(submission.author, "name", "None"),
                    'author_fullname': getattr(submission, "author_fullname", "None"),
                    'author_premium': getattr(submission, "author_premium", "None"),
                    'subreddit_subscribers': getattr(submission, "subreddit_subscribers", "None"),
                    'num_comments': getattr(submission, "num_comments", "None"),
                    'score': getattr(submission, "score", "None"),
                    'likes': getattr(submission, "likes", "None"),
                    'ups': getattr(submission, "ups", "None"),
                    'upvote_ratio': getattr(submission, "upvote_ratio", "None"),
                    'selftext': getattr(submission, "selftext", "None"),
                    'url': getattr(submission, "url", "None"),
                    'created': getattr(submission, "created", "None"),
                    'date': datetime.utcfromtimestamp(getattr(submission, "created", "None")).strftime('%Y-%m-%d %H:%M:%S'),
                    'comment_id': getattr(comment, "id", "None"),
                    'comment_body': getattr(comment, "body", "None"),
                    'comment_author': getattr(comment.author, "name", "None"),
                    'comment_author_fullname': getattr(comment, "author_fullname", "None"),
                    'comment_score': getattr(comment, "score", "None"),
                    'comment_created': getattr(comment, "created", "None"),
                    'comment_date': datetime.utcfromtimestamp(getattr(comment, "created", "None")).strftime('%Y-%m-%d %H:%M:%S'),
                    'comment_permalink': 'https://www.reddit.com' + getattr(comment, "permalink", "None"),
                })

    return posts


def clear_string(string: str) -> str:
    special_characters = [";", "\t", "\n", "\r", "\n\r", "<", ">"]
    return ''.join(filter(lambda i: i not in special_characters, string)).strip()


def create_file(file: str, fields):
    with open(file, 'a', encoding="utf8") as ouf:
        ouf.write(';'.join(field for field in fields) + "\n")


def save_posts_into_file(file: str, posts):
    with open(file, 'a', encoding="utf8") as ouf:
        for post in posts:
            ouf.write(';'.join(clear_string(str(value)) for (field, value) in post.items()))
            ouf.write("\n")

    print("=== Saving has finished for current Subreddit ===")
