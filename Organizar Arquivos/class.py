import os
import shutil


"""Extensões para detectar para onde os arquivos irão"""
ext_texto = ('.pdf', '.docx', '.txt')
ext_program = ('.exe', '.msi')
ext_compress = ('.rar', '.zip', '.7z')
ext_music = ('.mp3')
ext_video = ('.mp4', '.mkv')
ext_imagem = ('.jpeg', '.jpg', '.png')

"""Diretório original, mude para o seu"""
dir_original = 'D:\\Downloads'

"""Novos diretórios, coloque aqui para onde cada arquivo vai
   seguindo a ordem:
   1-Documentos
   2-Programas
   3-Arquivos ZIP
   4-Musicas
   5-Videos
   6-Imagens
"""
new_dirs = {1: 'D:\\Arquivos\\Documents', 2: 'D:\\Arquivos\\Programs',
            3: 'D:\\Arquivos\\Compressed', 4: 'D:\\Arquivos\\Music',
            5: 'D:\\Arquivos\\Video', 6: 'D:\\Arquivos\\Imagens'}


class Organizador:
    '''Classe que irá fazer todo o trabalho de mover os arquivos'''
    conta = 0
    
    def __init__(self, dir_original: str, new_dir: dict, type_tex=None, type_program=None,
                 type_compress=None, type_music=None, 
                 type_video=None, type_imagem=None) -> None:
        '''Método construtor, aqui os type estão em None por que
           você pode ou não mover alguns arquivos, se você quiser.
           Se deseja especificar apenas quais serão os tipos de arquivos
           coloque dentro do objeto que você irá criar:
           Ex: você quer que documentos e imagens sejam movidos?
           Coloque:
           obj_test = Organizador(dir_original, new_dirs, type_tex=ext_texto,
           type_imagem=ext_imagem)'''
        
        self._dir_original = dir_original
        self._new_dir = new_dir
        self.type_tex = type_tex
        self.type_program = type_program
        self.type_compress = type_compress
        self.type_music = type_music
        self.type_video = type_video
        self.type_imagem = type_imagem
        
    @property
    def dir_original(self):
        return self._dir_original
    
    @dir_original.setter
    def dir_original(self, valor) -> str:
        if not isinstance(valor, str):
            raise TypeError('O diretório precisa ser em STRING.')

        return valor
    
    @property
    def new_dir(self):
        return self._new_dir
    
    @new_dir.setter
    def new_dir(self, valor):
        if not isinstance(valor, tuple):
            raise TypeError('Os novos diretórios precisam estar em uma tupla.')
        
        return self._new_dir
    
    def move_doc(self):
        '''Método que irá mover os documentos'''
        if self.type_tex:
            for root, dirs, files in os.walk(self.dir_original):
                for file in files:
                    old_file_path = os.path.join(self.dir_original, file)
                    new_file_path = os.path.join(self.new_dir[1], file)
                    file_wth_ext, ext = os.path.splitext(file)
                    
                    if ext in self.type_tex:
                        self.conta += 1
                        shutil.move(old_file_path, new_file_path)
        else: pass

    def move_program(self):
        '''Método que irá mover os programas'''
        if self.type_program:
            for root, dirs, files in os.walk(self.dir_original):
                for file in files:
                    old_file_path = os.path.join(self.dir_original, file)
                    new_file_path = os.path.join(self.new_dir[2], file)
                    file_wth_ext, ext = os.path.splitext(file)
                    
                    if ext in self.type_program:
                        self.conta += 1
                        shutil.move(old_file_path, new_file_path)
        else: pass
        
    def move_compress(self):
        '''Método que irá mover os arquivos zipados'''
        if self.type_compress:
            for root, dirs, files in os.walk(self.dir_original):
                for file in files:
                    old_file_path = os.path.join(self.dir_original, file)
                    new_file_path = os.path.join(self.new_dir[3], file)
                    file_wth_ext, ext = os.path.splitext(file)
                    
                    if ext in self.type_compress:
                        self.conta += 1
                        shutil.move(old_file_path, new_file_path)
        else: pass
    
    def move_music(self):
        '''Método que irá mover as músicas'''
        if self.type_music:
            for root, dirs, files in os.walk(self.dir_original):
                for file in files:
                    old_file_path = os.path.join(self.dir_original, file)
                    new_file_path = os.path.join(self.new_dir[4], file)
                    file_wth_ext, ext = os.path.splitext(file)
                    
                    if ext in self.type_music:
                        self.conta += 1
                        shutil.move(old_file_path, new_file_path)
        else: pass
        
    def move_video(self):
        '''Método que irá mover os vídeos'''
        if self.type_video:
            for root, dirs, files in os.walk(self.dir_original):
                for file in files:
                    old_file_path = os.path.join(self.dir_original, file)
                    new_file_path = os.path.join(self.new_dir[5], file)
                    file_wth_ext, ext = os.path.splitext(file)
                    
                    if ext in self.type_video:
                        self.conta += 1
                        shutil.move(old_file_path, new_file_path)
        else: pass
        
    def move_imagem(self):
        '''Método que irá mover as imagens'''
        if self.type_imagem:
            for root, dirs, files in os.walk(self.dir_original):
                for file in files:
                    old_file_path = os.path.join(self.dir_original, file)
                    new_file_path = os.path.join(self.new_dir[6], file)
                    file_wth_ext, ext = os.path.splitext(file)
                    
                    if ext in self.type_imagem:
                        self.conta += 1
                        shutil.move(old_file_path, new_file_path)
        else: pass
        
    def exec_class(self):
        '''Método que irá executar toda a classe e 
        indicar quantos arquivos serão movidos'''
        self.move_doc()
        self.move_program()
        self.move_compress()
        self.move_music()
        self.move_video()
        self.move_imagem()
        if not self.conta:
            print('Não há nenhum arquivo para mover.')
            return
        
        print(f'{self.conta} arquivo(s) movido(s) com sucesso!')
    


if __name__ == '__main__':
    teste = Organizador(dir_original, new_dirs, ext_texto, ext_program, 
                        ext_compress, ext_music, ext_video, ext_imagem)
    teste.exec_class()
