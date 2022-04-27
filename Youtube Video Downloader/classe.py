'''
Por enquanto, este programa não funciona devido a problemas na lib do pytube.
'''
import fnmatch
import os
import shutil
from pytube import YouTube
from sys import platform
from pathlib import Path
# Será criada uma classe que recebe a URL do vídeo;
# Será criada uma classe que salva o arquivo de vídeo;
# Será criada uma classe que converte o vídeo.


class DownloadVideo:
    pass


class SaveFile:
    pass


class VideoConverter:
    pass


if __name__ == '__main__':
    teste = 'https://www.youtube.com/watch?v=fi0NxuDUuv4'

    yt = YouTube(teste)
    print(yt.streams)
