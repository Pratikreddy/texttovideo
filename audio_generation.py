# voice_creation.py
from gtts import gTTS
from pydub import AudioSegment
import os
from moviepy.editor import AudioFileClip

def generate_audio_clips(segments, temp_audio_dir):
    audio_clips = []
    for idx, segment in enumerate(segments):
        text = segment.get(f'text_{idx+1}', '')
        audio_filename = os.path.join(temp_audio_dir, f'audio{idx}.mp3')
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(audio_filename)
        audio_clip = AudioSegment.from_mp3(audio_filename)
        # Apply the speed change to the audio clip
        sped_up_audio = audio_clip.speedup(playback_speed=1.5)
        audio_clips.append(sped_up_audio)
    # Concatenate all sped up audio clips
    final_audio = sum(audio_clips)
    final_audio.export(os.path.join(temp_audio_dir, 'final_audio.mp3'), format='mp3')
    return AudioFileClip(os.path.join(temp_audio_dir, 'final_audio.mp3'))