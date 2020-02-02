from pydub import AudioSegment
from gtts import gTTS
from io import BytesIO
import os

# INTERVAL SPACES
WORK_INTERVAL = 30*1000
REST_INTERVAL = 10*1000

# WORKOUT PLAN
WORKOUT = [
   'jumping jacks',
   'push ups',
   'sit ups',
   'wall sit',
   'burpees',
   'forward lunges',
   'chair dips',
   'forward plank',
   'left side plank',
   'right side plank',
   'leg lifts'
]

# REPETITION NUMBER
REP_NO = len(WORKOUT)

# IMPORT SOUND FILES
START_PULSE_FILE = 'audio_files/b5_marimba.wav'
MIDPOINT_PULSE_FILE = 'audio_files/g4_xylo.wav'
END_PULSE_FILE = 'audio_files/g2_marimba.wav'

# BACKGROUND MUSIC
MUSIC_FILE = 'audio_files/Coucou Anne.mp3'

TEMP_MP3 = 'audio_files/tmp.mp3'


class SoundSet():

    def __init__(self):
        self.load_pulse()
        self.load_music()
        self.generate_exercise_speech()

    def load_pulse(self):
        self.start_pulse = AudioSegment.from_wav(START_PULSE_FILE)[:1500]
        self.mid_pulse = AudioSegment.from_wav(MIDPOINT_PULSE_FILE)[:1500]
        self.end_pulse = AudioSegment.from_wav(END_PULSE_FILE)[:1500]

    def load_music(self):
        if MUSIC_FILE is not None:
            self.music = AudioSegment.from_file(MUSIC_FILE, format='mp3')[30000:] - 20
        else:
            self.music = None
        
    def generate_exercise_speech(self):
        self.workout_list = []
        for item in WORKOUT:
            self.workout_list.append(self._gtts_make_speech(item))

    def _gtts_make_speech(self, phrase):
        # mp3_temp = BytesIO() # Not sure why this doesn't work
        
        tts = gTTS(phrase, lang='en')
        tts.save(TEMP_MP3)
        output =  AudioSegment.from_file(TEMP_MP3, format='mp3')
        os.remove(TEMP_MP3)
        return output


class TrackMaker():

    def __init__(self):
        self.sounds = SoundSet()
        self.work_interval = WORK_INTERVAL
        self.rest_interval = REST_INTERVAL

    def generate(self, output_file_name):
        workout = AudioSegment.silent(2000)
        for workout_item in self.sounds.workout_list:
            workout_unit =  self.make_rest(workout_item) + self.make_work()
            workout += workout_unit

        workout.export(output_file_name, format="mp3")
        
    def make_work(self):
        half_work = WORK_INTERVAL//2
        start_silence_dur = half_work - len(self.sounds.start_pulse)
        start = self.sounds.start_pulse + AudioSegment.silent(start_silence_dur)

        mid_silence_dur = half_work - len(self.sounds.mid_pulse)
        mid = self.sounds.mid_pulse + AudioSegment.silent(mid_silence_dur)

        output = start + mid
        if self.sounds.music is not None:
           output = output.overlay(
               self.sounds.music 
           )
     
        return output

    def make_rest(self, workout_instruction):
        rest_silence_dur = REST_INTERVAL - len(workout_instruction) - len(self.sounds.end_pulse)
        rest = self.sounds.end_pulse + workout_instruction + AudioSegment.silent(rest_silence_dur)

        return rest

if __name__ == "__main__":
    track = TrackMaker()
    track.generate('test.mp3')
