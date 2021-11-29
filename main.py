from pytube import YouTube
import os 

#CRIAÇÃO DO DIRETÓRIO CASO O MESMO NÃO EXISTA
def criaDiretorio (vDir):
    if os.path.isdir(vDir) == False:
        try: 
            os.mkdir(vDir) #CRIAÇÃO DO DIRETÓRIO
        except OSError as error: 
            print(f'Erro => {error}')
            return False
        else:
            return True
    else:
        return True  

def youTubeDownloader(vURL):
    vDir = 'temp/'
    criaDiretorio(vDir)

    vVideo = YouTube(vURL)
    print(f'Baixando o Vídeo: {vVideo.title}') 
    #print(vVideo.thumbnail_url) 

    vVideo = vVideo.streams.get_highest_resolution() #set stream resolution
    vVideoDownload = vVideo.download(output_path=vDir) #Download video
    
    return vVideoDownload


vUrl = input("Informe a URL do Vídeo que deseja baixar: \n")

if vUrl != '':
    try:
        vVideoDownload = youTubeDownloader(vUrl)
    except Exception as error:
        print('ERRO => '+error)
    else:
        vVideoBaixado = vVideoDownload.replace("/",'\\')
        print(f'Vídeo baixado com sucesso!\n\n{vVideoBaixado}')
        os.startfile(vVideoDownload.replace("/",'\\'))


    


#https://www.youtube.com/watch?v=gomDSZaay3E
