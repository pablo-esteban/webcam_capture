import logging
import cv2 as ocv
from datetime import datetime
from pathlib import Path

# input variables
cam_ports = [0, 1]
settings_file = r'C:\Lidar\System\settings.txt'
key_word = 'Campaign ID ='
path_out = Path(r'C:\Lidar\Webcam')


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


def get_campaign(settings_file, key_word):
    # open settings file, read each line
    with open(settings_file, 'r') as settings_file:
        settings = settings_file.readlines()

        for line in settings:
            # find campaign id line
            if line.find(key_word) != -1:
                line_str = line.split('"')
                
    return line_str[1]


def run_log(path_out):
    f_name = f"webcam.log"
    f_path = path_out / f_name
    logging.basicConfig(level='INFO',
                        format='%(asctime)s.%(msecs)03d %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=f_path,
                        filemode='a')


if __name__ == '__main__':
    # make output dir
    Path.mkdir(path_out, parents=True, exist_ok=True)

    # setup logging
    run_log(path_out)

    # get campaign ID
    campaign_name = get_campaign(settings_file, key_word)

    for port in cam_ports:
        result, image = img_cap(port)

        if result:
            now = datetime.now().strftime('%Y%m%d_%H%M%S')
            fig_name = f'{campaign_name}_{now}_Cam{port + 1}.png'
            file_path = path_out / fig_name
            img_save(image, fig_name, file_path)
            logging.info(f'Cam {port + 1} image saved')
        else:
            logging.info(f"Cam {port + 1} not detected")
