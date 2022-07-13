import os
import praw
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


def read_hot_posts_with_comments(channel: str, limit: int) -> []:
    posts = []

    for submission in reddit.subreddit(channel).hot(limit=limit):
        submission.comments.replace_more(limit=None)

        for comment in submission.comments.list():
            posts.append({
                'subreddit_id': submission.subreddit_id,
                'subreddit_name': submission.subreddit.display_name,
                'id': submission.id,
                'title': submission.title,
                'permalink': 'https://www.reddit.com' + submission.permalink,
                'link_flair_text': submission.link_flair_text,
                'author': submission.author.name,
                'author_fullname': submission.author_fullname,
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
                'comment_author': comment.author.name,
                'comment_author_fullname': comment.author_fullname,
                'comment_score': comment.score,
                'comment_created': comment.created,
                'comment_date': datetime.utcfromtimestamp(comment.created).strftime('%Y-%m-%d %H:%M:%S'),
                'comment_permalink': 'https://www.reddit.com' + comment.permalink,
            })

    return posts


def clear_string(string: str) -> str:
    special_characters = [";", "\t", "\n", "\r", "\n\r", "<", ">"]
    return ''.join(filter(lambda i: i not in special_characters, string)).strip()


def save_posts_into_file(file_name: str, table_fields, posts):

    with open(file_name, 'w', encoding="utf8") as ouf:

        ouf.write(';'.join(field for field in table_fields) + "\n")

        for post in posts:
            ouf.write(';'.join(clear_string(str(value)) for (field,value) in post.items()))
            ouf.write("\n")

    print("=== Saving has finished ===")


file_name = 'reddit_comments.csv'

table_fields = [
    'subreddit_id',
    'subreddit_name',
    'id',
    'title',
    'permalink',
    'link_flair_text',
    'author',
    'author_fullname',
    'author_premium',
    'subreddit_subscribers',
    'num_comments',
    'score',
    'likes',
    'ups',
    'upvote_ratio',
    'selftext',
    'url',
    'created',
    'date',
    'comment_id',
    'comment_body',
    'comment_author',
    'comment_author_fullname',
    'comment_score',
    'comment_created',
    'comment_date',
    'comment_permalink'
]

channels = [
    'CryptoMarkets',
    'binance',
    'CoinBase',
    'CryptoCurrencies',
    'blockchain',
    'btc',
    'Bitcoin',
    'Metamask',
    'defi',
    'Crypto_General',
    'NFT',
    'CryptoTechnology',
    'ethereum',
    'CryptoCurrency',
    'BitcoinBeginners',
]

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT"),
)

for channel in channels:
    posts = read_hot_posts_with_comments(channel, 2)
    save_posts_into_file(file_name, table_fields, posts)
