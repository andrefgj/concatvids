#!/usr/bin/env python3

import argparse
import os
import subprocess
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Concatena vídeos MP4 usando ffmpeg.")
    parser.add_argument("-o", "--output", default="output.mp4", help="Nome do arquivo de saída (padrão: output.mp4)")
    parser.add_argument("--ext", default="mp4", help="Extensão dos arquivos (padrão: mp4)")
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
        print(f"Vídeos concatenados com sucesso: {args.output}")
    except subprocess.CalledProcessError:
        print("Erro ao executar ffmpeg.")

if __name__ == "__main__":
    main()
