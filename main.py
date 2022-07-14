import os
import praw
from scrapper import reddit_scrapper
from dotenv import load_dotenv

load_dotenv()


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

reddit_scrapper.create_file(file_name, table_fields)

for channel in channels:
    print("Channel - ", channel, end="\n")
    posts = reddit_scrapper.read_hot_posts_with_comments(reddit, channel, 200)
    reddit_scrapper.save_posts_into_file(file_name, posts)
