# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 07:15:40 2021

@author: C0624150
"""

import os


audios_ext = ['.mp3', '.wav', '.flac']
videos_ext = ['.mp4', '.mov', '.avi']
imagens_ext = ['.jpg', '.jpeg', '.png']
documentos_ext = ['.txt', '.log', '.pdf', '.docx']
powerpoint_ext = ['.ppt', '.pptx']
zip_ext = ['.zip']
python_ext = ['.py']

# pegando a extensão do arquivo para determinar o tipo
def pegar_extensao(nome):
    index = nome.rfind('.')
    return nome[index:]

def organizar(diretorio):
    AUDIO_DIR = os.path.join(diretorio, "audios")
    IMAGENS_DIR = os.path.join(diretorio, "imagens")
    DOCS_DIR = os.path.join(diretorio, "documentos")
    VIDEOS_DIR = os.path.join(diretorio, "videos")
    PPT_DIR = os.path.join(diretorio, "powerpoint")
    ZIP_DIR = os.path.join(diretorio, "zips")
    PYTHON_DIR = os.path.join(diretorio, "python")
    OUTROS_DIR = os.path.join(diretorio, "outros")
    
    # criando pastas: imagens, audios, documentos, videos, outros
    if not os.path.isdir(AUDIO_DIR):
        os.mkdir(AUDIO_DIR)
    if not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    if not os.path.isdir(PPT_DIR):
        os.mkdir(PPT_DIR)
    if not os.path.isdir(ZIP_DIR):
        os.mkdir(ZIP_DIR)
    if not os.path.isdir(PYTHON_DIR):
        os.mkdir(PYTHON_DIR)
    if not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)
       
     
     
     
    nomes_arquivos = os.listdir(diretorio)
    nova_pasta = ''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio, arquivo)):
            # extensão do arquivo com letras minusculas
            extensao = str.lower(pegar_extensao(arquivo))
            print(arquivo, extensao)
            if extensao in audios_ext:
                nova_pasta = AUDIO_DIR
            elif extensao in imagens_ext:
                nova_pasta = IMAGENS_DIR
            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR
            elif extensao in documentos_ext:
                nova_pasta = DOCS_DIR
            elif extensao in powerpoint_ext:
                nova_pasta = PPT_DIR
            elif extensao in zip_ext:
                nova_pasta = ZIP_DIR
            else:
                nova_pasta = OUTROS_DIR
            #move o arquivo para a pasta correspondente
            velho = os.path.join(diretorio, arquivo)
            novo = os.path.join(nova_pasta, arquivo)
            os.rename(velho, novo)    
            print('Moveu:', velho, "->", novo)    
        
if __name__ == '__main__':
   
    organizar('downloads')
            
            
            
            
            
            
            
            
            