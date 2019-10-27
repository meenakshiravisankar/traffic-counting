import cv2
import os

def get_fps(path_to_video) :
    """
    Computes fps given the path of the video
    ----------
    Parameters
    ----------
    path_to_video - path to the mp4 file
    -------
    Returns
    -------
    fps - frames per second
    """
    video = cv2.VideoCapture(path_to_video)    
    fps = video.get(cv2.CAP_PROP_FPS)
    video.release()
    return fps

def get_total_frames(path_to_video) :
    """
    Computes fps given the path of the video
    ----------
    Parameters
    ----------
    path_to_video - path to the mp4 file
    -------
    Returns
    -------
    frames - total frames in the video
    """
    video = cv2.VideoCapture(path_to_video)    
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    video.release()
    return frames

def display_video(path_to_video) : 
    """
    Displays video
    ----------
    Parameters
    ----------
    path_to_video - path to the mp4 file
    -------
    Returns
    -------
    NA
    """
    video = cv2.VideoCapture(path_to_video)
    while(video.isOpened()) :
        _ , frame = video.read()        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        fps = get_fps(path_to_video)
        wait_ms = int(1000/fps)

        if cv2.waitKey(wait_ms) & 0xFF == ord('q') :
            break
    video.release()
    cv2.destroyAllWindows()

def extract_images(path_to_video, path_to_images) :
    """
    Extract images from video
    ----------
    Parameters
    ----------
    path_to_video - path to the mp4 file
    path_to_images - path to the directory to save images
    -------
    Returns
    -------
    NA
    """
    count = 0    
    if not os.path.exists(path_to_images):
        os.makedirs(path_to_images)
    video = cv2.VideoCapture(path_to_video)
    while(video.isOpened()) :
        ret, frame = video.read()
        if not ret :
            break       
        image_name = str(count)+".jpg"
        cv2.imwrite(os.path.join(path_to_images, image_name), frame)
        count+=1
    video.release()
    

path_to_video = "../files/videos/1569843500.mp4"
path_to_images = "../files/images"

# extract_images(path_to_video, path_to_images)
