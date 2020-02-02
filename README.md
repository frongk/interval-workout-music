# interval-workout-music
Automatically generate an mp3 track that guides you through an interval workout.

## About
`main.py` generates an mp3 file that provides sound prompts for doing interval exercises. The goal of this project is to prevent a user from needing to look at a clock while performing an interval workout and be able to perform a long series of exercises without having to think hard about what comes next. To achieve this, this program can process a long sequence of exercises that one would like to perform and generates text-to-speech prompts and time allotments to perform these exercises.

The following parameters are customizable
- Spoken exercise prompts (e.g. 'jumping jacks' or 'push ups') (automated by Google Text-to-Speech)  
- Background mp3 music  
- Exercise and rest interval timing  

The output mp3 describes which exercise is next, and will play music for the period that is specified. The example file, [`sample_30_10.mp3`](https://github.com/frongk/interval-workout-music/raw/master/sample_30_10.mp3)  plays music for 30 seconds for performing an exercise and is silent for 10 seconds for rest and prepping for next exercise. The [sample file](https://github.com/frongk/interval-workout-music/raw/master/sample_30_10.mp3) was generated using a clip of the audio from this youtube [video](https://www.youtube.com/watch?v=qmY5PGazrcI).

## Dependencies
[`pydub`](https://github.com/jiaaro/pydub) - this is a great api btw  
`gTTS`  
`ffmpeg`  
