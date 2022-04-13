import os
import fnmatch
import sys


class Conversor:
    def __init__(self, ext) -> None:
        self.ext = ext
        self._codec_video = '-c:v libx264'
        self._crf = '-crf 23'
        self._preset = '-preset ultrafast'
        self._codec_audio = '-c:a aac'
        self._bitrate_audio = '-b:a 320k'
        self._debug = '-ss 00:00:00 -to 00:00:00'

    @property
    def codec_video(self):
        return self._codec_video

    @property
    def crf(self):
        return self._crf

    @property
    def preset(self):
        return self._preset

    @property
    def codec_audio(self):
        return self._codec_audio

    @property
    def bitrate_audio(self):
        return self._bitrate_audio

    @property
    def debug(self):
        return self._debug

    def comando(self):
        if sys.platform == 'linux':
            self.command = 'ffmpeg'
        else:
            self.command = 'C:\Python\\ffmpeg\\ffmpeg.exe'

    def folder(self):
        try:
            self.path_or = os.mkdir('D:\\Arquivos\\Video_entrada')
            self.path_fn = os.mkdir('D:\\Arquivos\\Video_saida')
        except:
            self.path_or = 'D:\\Arquivos\\Video_entrada'
            self.path_fn = 'D:\\Arquivos\\Video_saida'

    def converte(self):
        for root, folders, files in os.walk(self.path_or):
            for file in files:
                if not fnmatch.fnmatch(file, "*.mp4" or "*.mkv"):
                    continue

                path_complete = os.path.join(root, file)
                file_name, file_ext = os.path.splitext(file)

                arquivo_saida = f'{self.path_fn}\{file}_NOVO.{self.ext}'

                self.exec = f'{self.command} -i "{path_complete}" {self.codec_video} {self.crf} {self.preset} ' \
                    f'{self.codec_audio} {self.bitrate_audio} "{arquivo_saida}"'
                os.system(self.exec)

    def exec_class(self):
        self.comando()
        self.folder()
        self.converte()


if __name__ == '__main__':
    teste = Conversor(input('Digite pra qual tipo de arquivo será'
                            'convertido, EX: mkv, mp4: '))
    teste.exec_class()
