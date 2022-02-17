import moviepy.editor as mp
import argparse

parser = argparse.ArgumentParser(description='Extract audios from video.')
parser.add_argument('--video', help='Your video file name')
parser.add_argument('--audio', help='Your exported autio file name.')
args = parser.parse_args()
print("import video: ", args.video, "Output audio: ", args.audio)

mc_clip = mp.VideoFileClip(args.video)

#Extracting the audio

mc_clip.audio.write_audiofile(args.audio)

