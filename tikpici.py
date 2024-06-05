import os
from pytube import YouTube
import yt_dlp
from colorama import init, Fore, Style

init()

def print_purple(text):
    print(f"{Fore.MAGENTA}{text}{Style.RESET_ALL}")

def save_directory(directory):
    with open("directory.txt", "w") as file:
        file.write(directory)

def load_directory():
    try:
        with open("directory.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return None

def clear_screen():
    
    os.system('cls' if os.name == 'nt' else 'clear')

def download_youtube_video(url, directory):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_stream.download(directory)
        print_purple("YouTube baixado com sucesso!")
    except Exception as e:
        print_purple(f"Erro ao fazer o download: {e}")

def download_twitter_video(url, directory):
    try:
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
            'quiet': True,  
            'no_warnings': True 
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print_purple("Twitter baixado com sucesso!")
    except Exception as e:
        print_purple(f"Erro ao fazer o download: {e}")

def download_tiktok_video(url, directory):
    try:
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegVideoRemuxer',
                'preferedformat': 'mp4',
            }],
            'ffmpeg_location': '/path/to/ffmpeg',  
            'quiet': True,  
            'no_warnings': True  
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print_purple("TikTok baixado com sucesso!")
    except Exception as e:
        print_purple(f"Erro ao fazer o download: {e}")

def main():
    saved_directory = load_directory()
    if saved_directory:
        directory = saved_directory
    else:
        directory = input(Fore.MAGENTA + "Caminho da pasta que irá salvar os vídeos: " + Style.RESET_ALL)
        save_directory(directory)

    ascii_art = """
             .
            .n                   .                 .                  n.
      .   .dP                  dP                   9b                 9b.    .
     4    qXb         .       dX                     Xb       .        dXp     t
    dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
    9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
     9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
      `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
        `9XXXXXXXXXXXP' `9XX'          `98v8P'          `XXP' `9XXXXXXXXXXXP'
            ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                            )b.  .dbo.dP'`v'`9b.odb.  .dX(
                          ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                         dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                        dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                        9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                         `'      9XXXXXX(   )XXXXXXP      `'
                                  XXXX X.`v'.X XXXX
                                  XP^X'`b   d'`X^XX
                                  X. 9  `   '  P )X
                                  `b  `       '  d'
                                   `             '    
    """

    while True:
        clear_screen()  
        print_purple(ascii_art)  

        url = input(Fore.MAGENTA + "Insira a URL (ou digite 'sair' para encerrar): " + Style.RESET_ALL)
        if url.lower() == 'sair':
            print_purple("Encerrando o programa. Até logo!")
            break

        print_purple("Downloading...")

        if "youtube.com" in url:
            download_youtube_video(url, directory)
        elif "twitter.com" in url:
            download_twitter_video(url, directory)
        elif "tiktok.com" in url:
            download_tiktok_video(url, directory)
        else:
            print_purple("URL inválida!")

if __name__ == "__main__":
    main()
