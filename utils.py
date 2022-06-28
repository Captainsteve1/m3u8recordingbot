import os
from pytz import timezone 
from datetime import datetime
import json
from urllib.request import urlopen, Request
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser

import subprocess



class config:
    AUTH_USERS = [5521710836 , 1451257129 , 1451257129]
    ADMIN_USERS = [5521710836 , 1451257129 , 1451257129]
    LINK_JSON = "https://gist.githubusercontent.com/Captainsteve1/21fb755cd48557486f4d79166f72c8fe/raw/b88b6aa2e9cc09ba135be73429390f66bf5ff24a/Steve.json"




def get_width_height(filepath):
    metadata = extractMetadata(createParser(filepath))
    if metadata.has("width") and metadata.has("height"):
      return metadata.get("width"), metadata.get("height")
    else:
      return 1280, 720




def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element) + " "
    return result.rstrip()


def getMsgfromUser(msg):
    msg.pop(0)
    query = ""
    for i in msg:
        query += i + " "
    return query.rstrip()


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2 ** 10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def get_duration(filepath):
    metadata = extractMetadata(createParser(filepath))
    if metadata.has("duration"):
        return metadata.get('duration')
    else:
        return 0









def audioListTitle(data):
  string = ""
  for i in data:
    string += f'{(i)}-' 
  return string[:-1]   









def multi_rip(client, message, streamUrl, channel, recordingDuration, language, ripType, ripQuality, fileTitle):
    user_id = message.from_user.id
    ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%d-%m-%Y [%H-%M-%S]')
    video_opts = 'ffmpeg -reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -i'
    video_opts_2 = '-to'
    video_opts_3 = '-map 0:v:0 -map 0:a'
    filename = f'[Conan76] {channel} - {fileTitle} - {ind_time} [{ripQuality}] [x264] {ripType} [{language}].mkv'
    cmd = video_opts.split() + [streamUrl] + video_opts_2.split() + [recordingDuration] + video_opts_3.split() + [filename]
    # process = Popen(cmd, stdout=PIPE, stderr=PIPE)
    # stdout, stderr = process.communicate()
    subprocess.run(cmd)

    return filename    
