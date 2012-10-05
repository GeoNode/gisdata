import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

def all_dirs(location):
    output = []
    for root, dirs, files in os.walk(location):
        if len(files) > 0 and root != location and 'README.txt' not in files:
            data_path = os.path.join(root, '*')

            # Get rid of the first 'gisdata'
            valid_dir = os.sep.join(data_path.split(os.sep)[1:])
            output.append(valid_dir)
    return output

setup(
    name="gisdata",
    version="0.5.4",
    author="ingenieroariel",
    author_email="ingenieroariel@gmail.com",
    description="Sample data and metadata for GIS packages",
    long_description=(read('README')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    license="BSD",
    keywords="gis",
    url='https://github.com/GeoNode/gisdata',
    packages=['gisdata',],
    package_data={'gisdata': all_dirs('gisdata'),},
    zip_safe=False,
)
