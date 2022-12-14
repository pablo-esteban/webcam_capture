
# Webcam Capture
A python script for capturing screenshots from a USB webcam.  
- Flexible number of USB webcams
- Overlays Campaign ID and Timestamp info
- No on-site configuration required
- Can be run by Windows Task Scheduler


## Authors
- Github [@liam.heff](https://github.com/liam-heff-wood)
- Mail [liam.heffernan](mailto:liam.heffernan@woodplc.com?subject=Python%20Webcam%20Capture)


## Features
- Reads `webcam.config` from `C:\Lidar\Settings`
- Creates output folder
- Searches `campaign_path` and reads the most recent file and extracts `key_word`
- Captures image from webcams in sequential order
- Overlays `key_word` and Timestamp info onto image
- Writes execution log to output folder


## webcam.config
| Parameter       | Type     | Description                                            |
|:----------------| :------- |:-------------------------------------------------------|
| `cam_ports`     | `string` | List of port numbers to search for a USB webcam device |
| `campaign_path` | `string` | Location of lidar campaign files                       |
| `key_word `     | `string` | Value in settings file to search for                   |
| `path_out`      | `string` | Location of saved images and log file                  |


## Run via CMD
Create an environment with Python 3.9, OpenCV, Pyinstaller & Pyinstaller_versionfile.    
Copy `webcam.config` file to `C:\Lidar\Settings` folder.  
Run the following commands.

```bash
  (base) conda env create -n webcam python=3.9
  (base) conda activate webcam
  (webcam) conda install -c conda-forge opencv pyinstaller
  (webcam) pip install pyinstaller_versionfile
  (webcam) cd `...\webcam_capture\webcam`
  (webcam) python main.py
```

## webcam.log
Example of expected log outputs showing successful and error outputs.  

```bash
2022-10-26 14:05:06.587 Cam 1 image saved
2022-10-26 14:05:12.285 Cam 2 image saved
2022-10-26 14:05:20.805 Cam 1 image saved
2022-10-26 14:05:20.807 Cam 2 not detected
```

## Build .exe for deployment
Update relevant details in the `version_file_builder.py` and execute to make the `version.txt` file required for the pyinstaller .exe build. 
```bash
(base) conda activate webcam
(webcam) cd `...\webcam_capture\webcam`
(webcam) pyinstaller main.spec
```

## Deploy on lidar
- Copy `webcam.config` file to `C:\Lidar\Settings` folder
- Copy `webcam_capture.exe` to `C:\Lidar\Software` folder
- Create task in Windows Task Scheduler to run at desired frequency
- Create GoodSync task to sync `output_folder` to data server on a daily basis

## Roadmap
- **Build live image capture**
