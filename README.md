# Music Genre Classifier

<div class='header'> 
<!-- Your header image here -->

## Sections:
 **[Introduction](#Introduction)**  |
 **[Data](#data)**  |
 **[Exploration](#exploration)**  |
 **[Model](#model)**  |
 **[Results](#results)**  |
 **[Takeaways](#takeaways)**  |
 
 ---
 ## Introduction
In this analysis, I inspect various features of songs extracted from audio, and attempt to find the differences of music based on genre. Using these features, I build a classification model to determine the genre of a song.

<sub>[  **[Back to Sections](#sections)** ]</sub>

 ## Data
The data was taken from the [Free Music Archive](https://github.com/mdeff/fma), a dataset collected by [Michaël Defferrard](https://deff.ch),
[Kirell Benzi](https://kirellbenzi.com),
[Pierre Vandergheynst](https://people.epfl.ch/pierre.vandergheynst),
[Xavier Bresson](https://www.ntu.edu.sg/home/xbresson).  for the International Society for Music Information Retrieval Conference (ISMIR), 2017.
The dataset contains: 

 - Track Metadata: Information on each track including genre (target variable), listen count, composer, creation date.
 
 - Spotify Features: Song features extracted from Spotify API including tempo, danceability, acousticness.
 
 - Audio Features: Features extracted from the audio itself, including MFCC and spectral contrast
 
 - Audio: The audio files themselves in waveform

<img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/Tracks_head.png" width = "800" height = "300">
 
 <sub>[  **[Back to Sections](#sections)** ]</sub>
 

## Exploration
Examining the Audio data:
 - Waveform
<img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/Waveplot30s.png">

 - Waveform for 1 second (44100 Hz)
<img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/Waveplot1s.png">

 - Mel Spectogram
 <img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/Mel_Spectogram.png">

Examining Spotify Audio Features:
There are 8 audio features provided by spotify for each track:
 - Acousticness: Confidence measure between 0.0 and 1.0 of whether a song is acoustic
 <details>
  <summary>
    Show Graph
  </summary>
<br>
<img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/acousticness_by_genre.png">
</details>

 - Danceability: How danceable a song is based on features such as tempo, beat strenght, and rhythm.
  <details>
  <summary>
    Show Graph
  </summary>
<br>
<img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/danceability_by_genre.png">
</details>
 - Energy: Percieved intensity of a track based features such as  on tempo, loudness, and dynamic range
 <details>
  <summary>
    Show Graph
  </summary>
<br>
<img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/energy_by_genre.png">
</details> 
 - Instrumentalness: Confidence measure between 0.0 and 1.0 of whether a song is only instrumental
  <details>
  <summary>
    Show Graph
  </summary>
<br>
<img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/instrumentalness_by_genre.png">
</details>
 - Liveness: Confidence measure between 0.0 and 1.0 of whether a song is a live performance
  <details>
  <summary>
    Show Graph
  </summary>
<br>
<img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/liveness_by_genre.png">
</details>
 - Speechiness: Presence of spoken word in a track, with 1.0 being and audio book or podcast. Most music is < 0.5
  <details>
  <summary>
    Show Graph
  </summary>
<br>
<img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/speachiness_by_genre.png">
</details>
 - Valence: The mood of a song between 0.0 and 1.0, 1.0 being happy and energetic, 0.0 being sad and depressed
  <details>
  <summary>
    Show Graph
  </summary>
<br>
<img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/valence_by_genre.png">
</details>
 - Tempo: Estimated tempo of a track
  <details>
  <summary>
    Show Graph
  </summary>
<br>
<img src="https://github.com/atsai24/music_audio_analysis/blob/master/img/tempo_by_genre.png">
</details>


<sub>[  **[Back to Sections](#sections)** ]</sub>

## Model



<sub>[  **[Back to Sections](#sections)** ]</sub>

## Results


<sub>[  **[Back to Sections](#sections)** ]</sub>

## Takeaways



<sub>[  **[Back to Sections](#sections)** ]</sub>

                                                          
