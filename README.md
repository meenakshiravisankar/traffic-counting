# TRAFFIC ANALYSIS WITH TRAFFIC CAMERA

1. Vehicles count for each lane
2. Pedestrians in either direction
3. Video time of entry of road user

The given dataset has 4953 frames at ~10fps with (width,height) = (1280,720)

### TODO
- [x] Extract images from video
- [x] Detect all types of vehicles in the video
- [x] Counting vehicles
- [x] Pedestrian detection
- [ ] Track pedestrians over crossing and count them
- [ ] Stabilize the count of vehicles
- [x] Add time information

### FAILURE CASES
1. Occluding vehicles
2. Vehicle is too fast
3. Sometimes bicycles

### USAGE
**Dependencies**
1. Opencv (version>3)
2. Keras
3. Tensorflow gpu (version<2)
4. Numpy
5. Tesseract-ocr
6. Numba
7. Skimage
   
Install tesseract for OCR
```
sudo add-apt-repository ppa:alex-p/tesseract-ocr
sudo apt-get update
sudo apt install tesseract-ocr libtesseract-dev
```

Perform object detection for both vehicles and pedestrians. Maintain count when entering, present and moving out of the frame. Assumption is that the traffic flow is in horizontal direction and a zebra crossing is along vertical.
```
git clone git@github.com:meenakshiravisankar/keras-yolo3.git
cd keras-yolo3
wget https://pjreddie.com/media/files/yolov3.weights
python3 convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
```
To run
```
python3 yolo_video.py --input <path-to-video>
```

The above generates a video with detection and counts traffic participants. It also generates log file with the time at which they are counted. The computation for object detection is ~0.23s per frame.

### OTHER IDEAS
1. Lane classification - adapt with different places 
2. Tracking

### CREDITS
1. Yolov3 - [link](https://github.com/pjreddie/darknet)
2. Keras-yolo3 - [link](https://github.com/meenakshiravisankar/keras-yolo3)