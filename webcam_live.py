import cv2 as cv2

cam_port = 1
webcam = cv2.VideoCapture(cam_port, cv2.CAP_DSHOW)

while True:
    ret,frame = webcam.read()

    if ret==True:
        cv2.imshow(f"Cam {cam_port +1} Live", frame)
        key = cv2.waitKey(1)
        if key==ord("q"):
            break
    else:
        print(f"Cam {cam_port +1} not detected")
        break

webcam.release()
cv2.destroyAllWindows()
