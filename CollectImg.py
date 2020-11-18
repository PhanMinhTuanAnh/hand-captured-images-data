import cv2
import os
import time
import uuid

IMAGES_PATH = "collect-images45"
labels = ['write1', 'write2', 'write3', 'wait', 'stop', 'back', 'check']
number_imgs = 10
i = 0
for label in labels:
    cap = cv2.VideoCapture(0)
    codec = 0x47504A4D  # MJPG
    cap.set(cv2.CAP_PROP_FPS, 30.0)
    cap.set(cv2.CAP_PROP_FOURCC, codec)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    print("Collecting images for {}".format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        imagename = os.path.join(IMAGES_PATH + "/" + label + "." + "{}.jpg".format(str(81+imgnum)))
        # imagename = os.path.join(IMAGES_PATH + "/" + "multi" + "." + "{}.jpg".format(str(306+i)))
        i = i + 1
        print(imagename)
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) and 0xFF == ord('q'):
            break

    cap.release()