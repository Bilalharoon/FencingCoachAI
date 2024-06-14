from pytube import YouTube
import mediapipe as mp
import cv2
import numpy as np

mp_pose = mp.solutions.pose
mp_drawing_styles = mp.solutions.drawing_styles
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(enable_segmentation=True, static_image_mode=True, min_detection_confidence=0.5, model_complexity=2)

def parse_vidoes():
    with open('./video_links.txt', 'r') as file:
        text = file.read()
        links = text.split('\n')
        return links
def download_youtube_video(url, file_name):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(filename=file_name)



def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

def get_fencers(frames):
    pose_landmarks = []
    for frame in frames:
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)
        
        pose_landmarks.append(results.pose_landmarks)
    return pose_landmarks
video_name = 'video.mp4'


if __name__ == '__main__':
    time_stamp = '2:50'
    start_frame = 5000
    # Yes I could make it look prettier but I am tired of doing this calculation by hand
    test_frame = int(round(((int(time_stamp.split(':')[0])*60+int(time_stamp.split(':')[1])) * 30) - start_frame, -1) /10)
    print(test_frame)
    # links = parse_vidoes()
    # download_youtube_video(links[0],video_name)
    frames = extract_frames(video_name)[start_frame::10]
    fencer_pose = get_fencers(frames)
    image = cv2.cvtColor(frames[test_frame], cv2.COLOR_BGR2RGB)
    print(fencer_pose[test_frame])
    mp_drawing.draw_landmarks(
            image,
            fencer_pose[test_frame],
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
        )
    try:
        while True:
            cv2.imshow('MediaPip Pose', image)
            if cv2.waitKey(0) & 0xFF == ord('q'):
                break
    except KeyboardInterrupt:
        print("keyboard interrupted")
