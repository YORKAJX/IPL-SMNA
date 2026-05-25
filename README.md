IPL 2022 Twitter — Social Media and Network Analysis
COSC2671 Assignment 2 | Group 9
Members:

Keshav Khurana (4117077)
Sahil Choudhary (4074816)

Research Question
Which hashtags and communities are most influential in IPL 2022 Twitter discourse, and how does fan sentiment evolve across the tournament?
How to Run

Place cleaned_ipl_tweets.csv in the data/ folder
Run notebooks/network_analysis.ipynb
Run notebooks/sentiment_lda.ipynb

this is the link for google drive folder conating the data 
https://drive.google.com/drive/folders/1KN9Kh_229NtppQGAUW1RfxiXJaeMwrH8?usp=drive_link

Required Packages
bashpip install pandas networkx matplotlib python-louvain vaderSentiment gensim nltk wordcloud
Notes

Full dataset not included due to file size — download from Kaggle (IPL 2022 tweets)
Sample of 50,000 tweets used for analysis (random_state=42)