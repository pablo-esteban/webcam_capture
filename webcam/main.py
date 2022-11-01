import sys
import logging
import cv2 as ocv
from glob import glob
from configparser import ConfigParser
from datetime import datetime
from pathlib import Path


def get_config(config_file, section):
    config_dict = {}
    settings = config_file.options(section)
    for val in settings:
        try:
            config_dict[val] = config_file.get(section, val)
            if config_dict[val] == -1:
                logging.info(f"skip: {val}")
        except:
            logging.info(f"exception on {val}!")
            config_dict[val] = None
            raise
    return config_dict


def img_cap(port):
    # init webcam
    cam = ocv.VideoCapture(port, ocv.CAP_DSHOW)
    cam.set(ocv.CAP_PROP_FRAME_WIDTH, 1920)
    cam.set(ocv.CAP_PROP_FRAME_HEIGHT, 1080)

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


def get_campaign(campaign_path, key_word):
    # get most recent campaign file
    f_path = str(campaign_path) + '\\' + '**' + '\\' + '*.txt'
    file_list = glob(f_path, recursive=True)
    campaign_file = file_list[-1]

    with open(campaign_file, 'r') as campaign_file:
        settings = campaign_file.readlines()

        for line in settings:
            # find campaign id line
            if line.find(key_word) != -1:
                campaign_name = line.split(':')[1]

    return campaign_name


def run_log(path_out):
    f_name = f"webcam.log"
    f_path = path_out / f_name
    logging.basicConfig(level='INFO',
                        format='%(asctime)s.%(msecs)03d %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=f_path,
                        filemode='a')


if __name__ == '__main__':
    # read config
    webcam_config = Path(r"C:\Lidar\System\webcam.config")

    if Path.exists(webcam_config):
        config_file = ConfigParser()
        config_file.read(webcam_config)
    else:
        sys.exit(f'Error: "{webcam_config}" not found')

    # get inputs
    cam_ports = get_config(config_file, 'Files')['cam_ports']
    campaign_file = Path(get_config(config_file, 'Files')['campaign_path'])
    key_word = get_config(config_file, 'Files')['key_word']
    path_out = Path(get_config(config_file, 'Files')['path_out'])

    # make output dir
    Path.mkdir(path_out, parents=True, exist_ok=True)

    # setup logging
    run_log(path_out)

    # get campaign ID
    if Path.exists(campaign_file):
        campaign_name = get_campaign(campaign_file, key_word).rstrip()
    else:
        logging.info(f'Error: "{campaign_file}" not found')
        sys.exit(f'Error: "{campaign_file}" not found')

    # capture images
    if len(cam_ports) >= 1:
        for port in cam_ports:
            result, image = img_cap(int(port))

            if result:
                now = datetime.now().strftime('%Y%m%d_%H%M%S')
                fig_name = f'{campaign_name}_{now}_Cam{int(port) + 1}.png'
                file_path = path_out / fig_name
                img_save(image, fig_name, file_path)
                logging.info(f'Cam {int(port) + 1} image saved')
            else:
                logging.info(f"Cam {int(port) + 1} not detected")
    else:
        logging.info(f'Error: No cam ports found in webcam.config')
        sys.exit(f'Error: No cam ports found in webcam.config')
