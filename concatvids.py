#!/usr/bin/env python3

import argparse
import os
import subprocess
from pathlib import Path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import webbrowser
from time import sleep

SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def youtube_authenticate():
    config_path = Path.home() / ".config" / "concatvids" / "client_secrets.json"
    
    if not config_path.exists():
        print(f"\n🔒 Credenciais do YouTube não encontradas em:\n  {config_path}\n")
        print("Para usar o upload, siga estes passos:\n")
        print("1. Acesse o Google Cloud Console:")
        print("   https://console.cloud.google.com/apis/credentials")
        print("2. Crie um projeto e ative a API 'YouTube Data API v3'")
        print("3. Crie credenciais do tipo 'OAuth - aplicativo de área de trabalho'")
        print("4. Baixe o arquivo JSON e salve como:")
        print(f"   {config_path}")
        print("\nAbrindo o navegador para facilitar...\n")

        try:
            os.makedirs(config_path.parent, exist_ok=True)
        except Exception as e:
            print(f"❌ Erro ao criar diretório: {e}")
            exit(1)

        webbrowser.open("https://console.cloud.google.com/apis/credentials")
        sleep(2)
        exit(1)

    flow = InstalledAppFlow.from_client_secrets_file(str(config_path), SCOPES)
    creds = flow.run_local_server(port=8080)
    return build('youtube', 'v3', credentials=creds)

def upload_video(youtube, video_path, title, description, tags):
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': '22'
        },
        'status': {
            'privacyStatus': 'unlisted',
            'selfDeclaredMadeForKids': False
        }
    }

    media = MediaFileUpload(
        video_path,
        chunksize=-1,
        resumable=True,
        mimetype='video/*'
    )

    request = youtube.videos().insert(
        part=','.join(body.keys()),
        body=body,
        media_body=media
    )

    print("Iniciando upload para o YouTube...")
    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Progresso: {int(status.progress() * 100)}%")

    print(f"✅ Upload finalizado! ID do vídeo: {response['id']}")
    return response['id']

def main():
    parser = argparse.ArgumentParser(description="Concatena vídeos MP4 usando ffmpeg e (opcionalmente) envia para o YouTube.")
    parser.add_argument("-o", "--output", default="output.mp4", help="Nome do arquivo de saída (padrão: output.mp4)")
    parser.add_argument("--ext", default="mp4", help="Extensão dos arquivos (padrão: mp4)")
    parser.add_argument("--upload", action="store_true", help="Se ativado, envia o vídeo final para o YouTube")
    parser.add_argument("--title", help="Título do vídeo no YouTube")
    parser.add_argument("--description", help="Descrição do vídeo no YouTube")
    parser.add_argument("--tags", nargs='*', help="Lista de tags (separadas por espaço)")

    args = parser.parse_args()
    ext = args.ext.lower()
    arquivos = sorted(Path(".").glob(f"*.{ext}"), key=lambda x: x.stat().st_mtime)

    if not arquivos:
        print(f"Nenhum arquivo .{ext} encontrado no diretório atual.")
        return

    with open("filelist.txt", "w", encoding="utf-8") as f:
        for arquivo in arquivos:
            f.write(f"file '{arquivo.name}'\n")

    cmd = [
        "ffmpeg", "-f", "concat", "-safe", "0",
        "-i", "filelist.txt", "-c", "copy", args.output
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f"🎞️ Vídeos concatenados com sucesso: {args.output}")
    except subprocess.CalledProcessError:
        print("❌ Erro ao executar ffmpeg.")
        return

    if args.upload:
        youtube = youtube_authenticate()
        title = args.title or input("Título do vídeo: ")
        description = args.description or input("Descrição: ")
        tags = args.tags or input("Tags (separadas por vírgula): ").split(',')
        upload_video(youtube, args.output, title, description, tags)

if __name__ == "__main__":
    main()
