import os
from glob import glob
from setuptools import setup

package_name = 'unityros_launch'

setup(
    # Other parameters ...
    data_files=[
        # ... Other data files
        # Include all launch files.
        (os.path.join('share', package_name), glob('launch/unityros.launch.py'))
    ]
)
