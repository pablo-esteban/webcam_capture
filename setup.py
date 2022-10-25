from distutils.core import setup

setup(
    name='webcam capture',
    version='1.0',
    description='Utility to automate USB webcam screenshots.',
    url='https://github.com/liam-heff-wood/webcam_capture.git',
    author='Liam Heffernan',
    author_email='liam.heffernan@woodplc.com',
    license='Wood Group Internal',
    packages=['', 'webcam'],
    package_dir={'': 'webcam'},
    install_requires=['OpenCV']
)
