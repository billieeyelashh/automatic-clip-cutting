import os 
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Path to cut videos

path = "yvonne_bar_"
RESOLUTION = (720, 1280)
ENABLE_TRANSITION = True
TRANSITION_FILE_PATH = "/yvonne_bar_/2021-03-01_19-16-45_UTC.mp4"
RESIZE_TRANSITION = True
REZISE_CLIPS = True

def get_clip_paths(path: str) -> list:
    return [
            os.path.join(path, file) for file in os.listdir(path) if file.endswith(".mp4")

        ]

def add_clip(path: str, rezise: bool = True) -> VideoFileClip:
    return VideoFileClip(path, target_resolution=RESOLUTION if rezise else None)

def render(path: str) -> None:
    
    video = []
    number = 0 

    clips = get_clip_paths(path)

    for clip in clips:
        if ENABLE_TRANSITION and not (number == 0 or number == len(clips)):
            video.append(add_clip(TRANSITION_FILE_PATH, REZISE_TRANSITION))
        
        video.append(add_clip(clip))
    

    number += 1


    del clip
    
    
    #Create Final Clip

    final = concatenate_videoclips(video, method="compose")
    final.write_videofile("rendered.mp4")

    for clip in video:
        clip.close()

    final.close()

    del final 
    del clips
    del video



render(path)
