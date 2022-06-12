import cv2

def setup():
    vid = cv2.VideoCapture(0)
    if not vid.isOpened():
        raise IOError("Cannot open webcam")
    while (True):
        ret, cam = vid.read()
    # cv2.namedWindow('displaymywindows', cv2.WINDOW_NORMAL)
    # CV_cat = cv2.imread("./test/WIN_20220611_19_45_33_Pro.jpg")
    # cv2.imshow('displaymywindows', CV_cat)
    # cv2.waitKey(0)

def capture(cap):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
