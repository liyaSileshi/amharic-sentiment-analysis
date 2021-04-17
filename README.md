# Sentiment Analysis for Amharic Language

# Project Description

Amharic is one of the 86 languages spoken in Ethiopia. It is the "working language" of the federal government. 

The goal of this project is to have a more accurate sentiment analysis for Amharic language. The data that I will be using is an annotated data (tweet_ID with label of Positive, Negative or Neutral).

The potential value is that there isn't a robust sentiment classifier for low-resource languages such as Amharic, so by working on a model hopefully I will improve the accuracy of the model.

The dataset I will be using is composed of 9.4k Amharic tweets that are pre-classified as Positive, Negative or neutral. 

[Link to data](https://github.com/uhh-lt/ASAB/tree/main/data)

## MVP

A more accurate classification/NLP model that predict new Amharic tweets as Positive, Negative or Neutral.

Input: A tweet written in Amharic

Output: Positive, Negative or Neutral

## Goals

The goal of this project is to have a more accurate sentiment analysis for Amharic tweets.

## Stretch Goals

- Add a feature for sarcasm detection

### Justification that the scope of your project is appropriate for 6 weeks with respect to learning curve, compute and storage resources

In order to successfully implement this project, I will do more research on NLP models, measuring and improving accuracy of NLP models. I will be using Google Colab notebook for running my model with GPU runtime.

# Articles and Research Papers

## Research Papers

[https://www.aclweb.org/anthology/2020.coling-main.91.pdf](https://www.aclweb.org/anthology/2020.coling-main.91.pdf)

[https://www.hilcoe.net/wp-content/uploads/2020/08/V2N2Paper12.pdf](https://www.hilcoe.net/wp-content/uploads/2020/08/V2N2Paper12.pdf)

[http://etd.aau.edu.et/bitstream/handle/123456789/3029/Selama Gebremeskel.pdf?sequence=1&isAllowed=y](http://etd.aau.edu.et/bitstream/handle/123456789/3029/Selama%20Gebremeskel.pdf?sequence=1&isAllowed=y)

[https://arxiv.org/pdf/2104.02516v1.pdf](https://arxiv.org/pdf/2104.02516v1.pdf)

[https://www.researchgate.net/publication/331673959_DEEP_LEARNING_APPROACH_FOR_AMHARIC_SENTIMENT_ANALYSIS_UNIVERSITY_OF_GONDAR](https://www.researchgate.net/publication/331673959_DEEP_LEARNING_APPROACH_FOR_AMHARIC_SENTIMENT_ANALYSIS_UNIVERSITY_OF_GONDAR)

## Articles

[https://towardsdatascience.com/sentiment-analysis-for-low-resourced-languages-on-social-media-128bf01f2547](https://towardsdatascience.com/sentiment-analysis-for-low-resourced-languages-on-social-media-128bf01f2547)

# Summary of research and articles

The rise of social media has helped in collecting a lot of data for making analysis, and prediction models. Sentiment analysis is one of the popular benefits that came about due to this mass data. Languages such as English were easier to do a model on because the data was already labeled and there was many available corpus for English. 
However, there are many languages out there that are difficult to do sentiment analysis on. We call them low-resource languages. The structure of these languages makes it really hard to build a model because of lack of availability of labeled data, and because of their many dialects and how their words are structures. 

Amharic is one of the low-resource languages. Because of the scarcity of labeled data, it's been quite difficult to make an NLP model for sentiment analysis. However, recent researchers and Data Scientists are using platforms such as Telegram bots to label already existing Amharic tweets by asking users whether they are Positive, Negative or Neutral. Using this data, they were able to build models to classify Amharic tweets. But even then, it is quite difficult sometimes to classify a tweet since it's hard to tell sarcasm in tweets and their data collection didn't account for that.

# Implementation Plan

- [ ]  Start from analyzing the already built models for the data
- [ ]  Work on improving it's accuracy
- [ ]  Built different types of NLP models and compare their accuracies for the given data

# Resources
https://github.com/uhh-lt/ASAB
