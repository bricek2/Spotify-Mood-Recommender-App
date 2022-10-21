# Spotify Mood Recommender App
-------------------------
#### Brice Kramer

## Problem Statement
Provide a recommendation application that will allow users to select the key they would like to listen to and which audio features to be used. The goal of this application is for exploring different Keys and Audio features in regards to the similarity of other songs based on their mood. 

## Overview
Data was obtained through a library called Tekore and Spotify's API client authorization. I gravitated towards Tekore because of its chunking and paging functionality which allows you to request more than 100 songs at a time. I also used Beautiful Soup to inconsistantly scrape lyrics from "songlyrics.com". I have succesfully scraped lyrics for about half of the songs I have obtained. 

I started off by building an item to item recommender based on the the songs audio features. The recommender is determinded from the users input of audio features. Radial graphs will be included to compare and contrast different songs audio features. 

Once that recommender is succesful, I will focus on the lyrics and developing a sentiment analysis that goes beyond Spotify's audio feature "Valence". Bearing time constrains, I am going to explore a multi-class sentiment analysis. I may classify songs based on playlist names like "Top 50 happy songs" or "Motivational Songs". From there, create a bag of words of the lyrics contained in those songs. Ideas for sentiment characteristics are happy, sad, anger, peace, romantic/love, social impact/political, inspirational, party, ect. Another limitation is that I would like the recommender to filter or weigh values based on the key characteristics. This is just a fun pet project that I will be expanding upon. 