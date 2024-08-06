from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
import os
import config

def create_video(audio_file, trends):
    # Define a duração total do vídeo
    video_duration = 8 * 60  # 8 minutos

    # Carrega o vídeo de introdução e fechamento
    intro_clip = VideoFileClip('assets/intro.mp4').subclip(0, 5)  
    outro_clip = VideoFileClip('assets/outro.mp4').subclip(0, 5) 

    # Gera clipes de texto baseados nas tendências
    trend_clips = []
    for trend in trends:
        text_clip = TextClip(trend['title'], fontsize=24, color='white', bg_color='black', size=(640, 480))
        text_clip = text_clip.set_duration(60)  # Cada tendência dura 1 minuto
        trend_clips.append(text_clip)

    # Concatenar todos os clipes
    video_clips = [intro_clip] + trend_clips + [outro_clip]
    video = concatenate_videoclips(video_clips)

    # Ajustar o áudio
    audio = AudioFileClip(audio_file)
    audio = audio.set_duration(video.duration)
    video = video.set_audio(audio)

    # Salvar o vídeo final
    output_file = os.path.join(config.DOWNLOADS_PATH, 'anime_trends_video.mp4')
    video.write_videofile(output_file, codec='libx264', audio_codec='aac')

    print(f"Vídeo salvo em {output_file}")
