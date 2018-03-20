Twitter Bot Overview
========

This bot provide the following features:
* Posting feeds
* Liking tweets of a user's followers tweets
* Retweeting tweets of a user's followers tweets

**Liking/Retweeting** will be on applied on those tweets 
which contains any words of a given list.


Input File(s):
=============
    o keywords.txt


Setup Guide:
=============

    o Requirements:
        - python-v2.7
        - keywords.txt file

    o Steps to setup environment for bot:
        - open cmd in the project directory
        - Run following command to install required packages for bot
          pip install -r requirements.txt

    o Commands for different options:
        - For posting
            - python main.py --option post
        - For Liking tweets
            - python main.py --option like
        - For retweeting tweets
            - python main.py --option retweet