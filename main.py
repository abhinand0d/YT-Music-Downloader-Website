import streamlit as st
import youtube_dl as yd
import time
import os

url = 'https://yt-downloader-by-abhi.herokuapp.com/Music'
if os.path.exists('Music'):
    print("Path Exist")
else:
    os.mkdir('Music')
    print("Created the path")

st.title("Youtube Music Downloader - Heroku")


input = st.text_input("Enter Youtube URL Here:")

def download_to_client():
    global get_title
    st.markdown('### Download Mp3 ###')
    # st.markdown('<a href="'+url+'/'+get_title+'.mp3" download>Download'+get_title+'</a>',unsafe_allow_html=True )
    st.audio("Music/Music"+str(timea)+".mp3")
    st.markdown('Click and Hold the Audio file and save the audio in case of android in case of PC please use three dot and choose download')
    st.text('Please Rename the file after installation as I haven;t found any solutions for that')


def download():
    global get_title,timea
    timea = time.time()
    ymdl_opts = {}

    with yd.YoutubeDL(ymdl_opts) as yddl:
        meta = yddl.extract_info(input, download=False) 
        get_title = meta['title']

    ydl_ops = {
    'outtmpl':'Music/Music'+str(timea)+'.%(ext)s',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    }
    
    def download_vid():
        with yd.YoutubeDL(ydl_ops) as ydl:
            ydl.download([zxt])
            

    zxt = input.strip()
    download_vid()
    print(get_title+".mp3")
    download_to_client()
    



if st.button("Stream/Download Audio"):
    download()
    
