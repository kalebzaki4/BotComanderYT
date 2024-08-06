from googleapiclient.discovery import build
from script_generator import generate_script
from tts import generate_voiceover
from video_creator import create_video
import config

def get_youtube_trends():
    # Configura e constrói o serviço YouTube
    youtube = build('youtube', 'v3', developerKey=config.YOUTUBE_API_KEY)

    # Faz a requisição para a API
    request = youtube.videos().list(
        part='snippet',
        chart='mostPopular',
        regionCode='BR',
        videoCategoryId='1',  # Categoria de Filmes e Animação
        maxResults=5
    )

    response = request.execute()

    trends = []
    for item in response['items']:
        trends.append({
            'title': item['snippet']['title'],
            'description': item['snippet']['description'],
            'url': f"https://www.youtube.com/watch?v={item['id']}"
        })

    return trends

def main():
    # Busca as tendências de animes no YouTube Brasil
    trends = get_youtube_trends()

    # Gera o roteiro do vídeo
    script = generate_script(trends)

    # Gera a narração em áudio
    audio_file = generate_voiceover(script)

    # Cria o vídeo com base no roteiro e narração
    create_video(audio_file, trends)

if __name__ == "__main__":
    main()
