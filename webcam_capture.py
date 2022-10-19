import cv2 as ocv
from datetime import datetime
from pathlib import Path

cam_ports = [0, 1]
now = datetime.now().strftime('%Y%m%d_%H%M%S')
path_out = Path(r'C:\Users\liam.heffernan\OneDrive - Wood PLC\Photos\webcam_capture')


def img_cap(port):
    # init webcam
    cam = ocv.VideoCapture(port, ocv.CAP_DSHOW)
    cam.set(ocv.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(ocv.CAP_PROP_FRAME_HEIGHT, 720)

    # capture image
    result, image = cam.read()

    # close webcam
    cam.release()

    return result, image


def img_save(image, fig_name, file_path):
    # overlay text on captured image
    new_fig = ocv.putText(img=image,
                          text=fig_name[:-4],
                          org=(5, 25),
                          fontFace=ocv.FONT_HERSHEY_SIMPLEX,
                          fontScale=1,
                          color=(0, 0, 0),
                          thickness=2,
                          )
    # save to file                        
    ocv.imwrite(str(file_path), new_fig)


for port in cam_ports:
    fig_name = f'EA1_A10_{now}_Cam{port + 1}.png'
    file_path = path_out / fig_name

    result, image = img_cap(port)

    if result:
        img_save(image, fig_name, file_path)
    else:
        print(f"Cam {port + 1} not detected")
