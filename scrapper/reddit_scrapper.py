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
                    'subreddit_id': submission.subreddit_id,
                    'subreddit_name': getattr(submission.subreddit, "display_name", "None"),
                    'id': submission.id,
                    'title': submission.title,
                    'permalink': 'https://www.reddit.com' + submission.permalink,
                    'link_flair_text': submission.link_flair_text,
                    'author': getattr(submission.author, "name", "None"),
                    'author_fullname': getattr(submission, "author_fullname", "None"),
                    'author_premium': submission.author_premium,
                    'subreddit_subscribers': submission.subreddit_subscribers,
                    'num_comments': submission.num_comments,
                    'score': submission.score,
                    'likes': submission.likes,
                    'ups': submission.ups,
                    'upvote_ratio': submission.upvote_ratio,
                    'selftext': submission.selftext,
                    'url': submission.url,
                    'created': submission.created,
                    'date': datetime.utcfromtimestamp(submission.created).strftime('%Y-%m-%d %H:%M:%S'),
                    'comment_id': comment.id,
                    'comment_body': comment.body,
                    'comment_author': getattr(comment.author, "name", "None"),
                    'comment_author_fullname': getattr(comment, "author_fullname", "None"),
                    'comment_score': comment.score,
                    'comment_created': comment.created,
                    'comment_date': datetime.utcfromtimestamp(comment.created).strftime('%Y-%m-%d %H:%M:%S'),
                    'comment_permalink': 'https://www.reddit.com' + comment.permalink,
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
