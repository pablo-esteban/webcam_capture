import pyinstaller_versionfile

pyinstaller_versionfile.create_versionfile(
    output_file="version.txt",
    version="1.0.0",
    company_name="Wood Group",
    file_description='Lidar Webcam Capture',
    internal_name='Lidar Webcam Capture',
    legal_copyright='© Wood Group. All rights reserved',
    original_filename='webcam_capture_x64.exe',
    product_name='Lidar Webcam Capture',
)