
# Webcam Capture
A python script for capturing screenshots from a USB webcam.  
- Flexible number of USB webcams
- Overlays Campaign ID and Timestamp info
- No custom configuration required


## Authors
- Github [@liam.heff](https://github.com/liam-heff-wood)
- Mail [liam.heffernan](mailto:liam.heffernan@woodplc.com?subject=Python%20Webcam%20Capture)


## Features
- Reads `webcam.config` from `C:\Lidar\Settings`
- Creates output folder
- Reads lidar `settings_file` file and extracts `key_word`
- Captures image from webcams in sequential order
- Overlays `key_word` and Timestamp info onto image
- Writes execution log to output folder


## webcam.config
| Parameter      | Type     | Description                                            |
| :------------- | :------- | :----------------------------------------------------  |
| `cam_ports`    | `string` | List of port numbers to search for a USB webcam device |
| `settings_file`| `string` | Location of lidar settings file                        |
| `key_word `    | `string` | Value in settings file to search for                   |
| `path_out`     | `string` | Location of saved images and log file                  |


## Run via CMD
Create an environment with Python 3.9+, OpenCV and Pyinstaller.  
Run the following commands.

```bash
  conda env create -n webcam python=3.9
  conda install -c conda-forge opencv pyinstaller
  conda activate webcam
  cd `project` folder
  python main.py
```
