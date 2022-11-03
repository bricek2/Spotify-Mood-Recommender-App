from tkinter import *
from turtle import st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics.pairwise import pairwise_distances
from sklearn.preprocessing import StandardScaler

import streamlit as st



if __name__ == '__main__':
    st.title('What song are you in the mood for?')

    st.markdown("**C Major:** Completely Pure. Its character is: innocence, simplicity, naïvety, childrens talk.")
    st.markdown("**C Minor:** Declaration of love and at the same time the lament of unhappy love. All languishing, longing, sighing of the love-sick soul lies in this key.")
    st.markdown("**D♭ Major:** A leering key, degenerating into grief and rapture. It cannot laugh, but it can smile; it cannot howl, but it can at least grimace its crying.--Consequently only unusual characters and feelings can be brought out in this key.")
    st.markdown("**C# Minor:** Penitential lamentation, intimate conversation with God, the friend and help-meet of life; sighs of disappointed friendship and love lie in its radius.")
    st.markdown("**D Major:** The key of triumph, of Hallejuahs, of war-cries, of victory-rejoicing. Thus, the inviting symphonies, the marches, holiday songs and heaven-rejoicing choruses are set in this key.")
    st.markdown("**D Minor:** Melancholy womanliness, the spleen and humours brood.")
    st.markdown("**E♭ Major:** The key of love, of devotion, of intimate conversation with God.")
    st.markdown("**D# Minor:** Feelings of the anxiety of the soul's deepest distress, of brooding despair, of blackest depresssion, of the most gloomy condition of the soul. Every fear, every hesitation of the shuddering heart, breathes out of horrible D# minor. If ghosts could speak, their speech would approximate this key.")
    st.markdown("**E Major:** Noisy shouts of joy, laughing pleasure and not yet complete, full delight lies in E Major.")
    st.markdown("**E Minor:** Naïve, womanly innocent declaration of love, lament without grumbling; sighs accompanied by few tears; this key speaks of the imminent hope of resolving in the pure happiness of C major.")
    st.markdown("**F Major:** Complaisance & Calm.")
    st.markdown("**F Minor:** Deep depression, funereal lament, groans of misery and longing for the grave.")
    st.markdown("**F# Major:** Triumph over difficulty, free sigh of relief utered when hurdles are surmounted; echo of a soul which has fiercely struggled and finally conquered lies in all uses of this key.")
    st.markdown("**F# Minor:** A gloomy key: it tugs at passion as a dog biting a dress. Resentment and discontent are its language.")
    st.markdown("**G Major:** Everything rustic, idyllic and lyrical, every calm and satisfied passion, every tender gratitude for true friendship and faithful love,--in a word every gentle and peaceful emotion of the heart is correctly expressed by this key.") 
    st.markdown("**G Minor:** Discontent, uneasiness, worry about a failed scheme; bad-tempered gnashing of teeth; in a word: resentment and dislike.")
    st.markdown("**A♭ Major:** Key of the grave. Death, grave, putrefaction, judgment, eternity lie in its radius.")
    st.markdown("**A♭ Minor:** Grumbler, heart squeezed until it suffocates; wailing lament, difficult struggle; in a word, the color of this key is everything struggling with difficulty.")
    st.markdown("**A Major:** This key includes declarations of innocent love, satisfaction with one's state of affairs; hope of seeing one's beloved again when parting; youthful cheerfulness and trust in God.")
    st.markdown("**A Minor:** Pious womanliness and tenderness of character.")
    st.markdown("**B♭ Major:** Cheerful love, clear conscience, hope aspiration for a better world.")
    st.markdown("**B♭ Minor:** A quaint creature, often dressed in the garment of night. It is somewhat surly and very seldom takes on a pleasant countenance. Mocking God and the world; discontented with itself and with everything; preparation for suicide sounds in this key.")
    st.markdown("**B Major:** Strongly coloured, announcing wild passions, composed from the most glaring coulors. Anger, rage, jealousy, fury, despair and every burden of the heart lies in its sphere.")
    st.markdown("**B Minor:** This is as it were the key of patience, of calm awaiting ones's fate and of submission to divine dispensation.")
    


    pitch = st.radio(
    "What key best describes your mood?",
    ("C Major.",
     "C Minor",
     "D♭ Major",
     "C# Minor",
     "D Major",
     "D Minor",
     "E♭ Major",
     "D# Minor",
     "E Major",
     "E Minor",
     "F Major",
     "F Minor",
     "F# Major",
     "F# Minor",
     "G Major",
     "G Minor",
     "A♭ Major",
     "A♭ Minor",
     "A Major",
     "A Minor",
     "B♭ Major",
     "B♭ Minor",
     "B Major",
     "B Minor",
     ), index=1)

    if pitch == 'C Major':
        which_key = 0
        mm = 1
    elif pitch == 'C Minor':
        which_key = 0
        mm = 0
    elif pitch == "D♭ Major":
        which_key = 1
        mm = 1
    elif pitch == "C# Minor":
        which_key = 1
        mm = 0
    elif pitch == "D Major":
        which_key = 2
        mm = 1
    elif pitch == "D Minor":
        which_key = 2
        mm = 0
    elif pitch == "E♭ Major":
        which_key = 3
        mm = 1
    elif pitch == "D# Minor":
        which_key = 3
        mm = 0
    elif pitch == "E Major":
        which_key = 4
        mm = 1
    elif pitch == "E Minor":
        which_key = 4
        mm = 0
    elif pitch == "F Major":
        which_key = 5
        mm = 1
    elif pitch == "F Minor":
        which_key = 5
        mm = 0
    elif pitch == "F# Major":
        which_key = 6
        mm = 1
    elif pitch == "F# Minor":
        which_key = 6
        mm = 0
    elif pitch == "G Major":
        which_key = 7
        mm = 1
    elif pitch == "G Minor":
        which_key = 7
        mm = 0
    elif pitch == "A♭ Major":
        which_key = 8
        mm = 1
    elif pitch == "A♭ Minor":
        which_key = 8
        mm = 0
    elif pitch == "A Major":
        which_key = 9
        mm = 1
    elif pitch == "A Minor":
        which_key = 9
        mm = 0
    elif pitch == "B♭ Major":
        which_key = 10
        mm = 1
    elif pitch == "B♭ Minor":
        which_key = 10
        mm = 0
    elif pitch == "B Major":
        which_key = 11
        mm = 1
    elif pitch == "B Minor":
        which_key = 11
        mm = 0 

    st.write("Audio feature descriptions found on spotify api documentations, https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features")
    dance = st.slider("Select a level of danceability. Elements include beat, rhythm, tempo and overall regularity ", 0 , 100 , 1)
    dance = dance / 100

    energy = st.slider("Select a level of energy. Energy represents intensity and activity. High energy feels fast, loud and noisy.", 0, 100, 1)
    energy = energy / 100

    loud = st.slider("Select a level of loudness(Average decibles in a track)", -60, 0, step =1)

    speech = st.slider("Select a level of speechiness. Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.", 0, 100, 1)
    speech = speech / 100

    acoust = st.slider("Select a level of acoustincness.")
    acoust = acoust / 100

    valence = st.slider("Select a level of valence.  Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).")
    valence = valence / 100

    tempo = st.slider("Select a tempo in beats per minute.", 60, 215, step=1)
    
    import os
    st.write(os.getcwd)
    
    df = pd.read_csv('datasets/checkpoint2.csv')
    df.drop(columns=['Unnamed: 0'], inplace=True)
    df = df.drop_duplicates(subset = ['track_name'])

    data = df.drop(columns=[
    'track_id',
    'track_pop',
    'artist_name', 
    'featured_artist', 
    'album_name',
    'artist_id',
    'intrumentalness',
    'track_lyrics',
    'playlist_name',
    ])

    data.set_index('track_name', inplace=True)
    
    data.loc[len(df.index)+1] = [dance, energy, which_key, loud, mm, speech, acoust, valence, tempo]

    ss = StandardScaler()
    scaled = ss.fit_transform(data)
    scaled = pd.DataFrame(scaled)

    similairity_matrix = pairwise_distances(scaled, metric='cosine')

    recommender_df = pd.DataFrame(
        similairity_matrix,
        index=data.index,
        columns=data.index
    )

    rec_songs = recommender_df[len(data)].sort_values(ascending=False).head(5)
    st.dataframe(rec_songs)

    d2 = pd.DataFrame({'track_name': [rec_songs.index[0],
                                 rec_songs.index[1],
                                 rec_songs.index[2],
                                 rec_songs.index[3],
                                 rec_songs.index[4]],
                  'arist_name': [df[df['track_name'] == rec_songs.index[0]][['artist_name']].iloc[0][0],
                                df[df['track_name'] == rec_songs.index[1]][['artist_name']].iloc[0][0],
                                 df[df['track_name'] == rec_songs.index[2]][['artist_name']].iloc[0][0],
                                df[df['track_name'] == rec_songs.index[3]][['artist_name']].iloc[0][0],
                                df[df['track_name'] == rec_songs.index[4]][['artist_name']].iloc[0][0]]})

    st.dataframe(d2)







        

    
