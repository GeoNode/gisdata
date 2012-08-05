import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

def all_dirs(location):
    output = []
    for path, dirs, files in os.walk(location):
        for d in dirs:
            item = os.path.join(path, d, '*')
            # Get rid of the first 'gisdata'
            valid_dir = os.sep.join(item.split(os.sep)[1:])
            output.append(valid_dir)
    return output


setup(
    name="gisdata",
    version="0.4.2",
    author="ingenieroariel",
    author_email="ingenieroariel@gmail.com",
    description="Sample data and metadata for GIS packages",
    long_description=(read('README')),
    # Full list of classifiers can be found at:
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License'
    ],
    license="BSD",
    keywords="gis",
    url='https://github.com/GeoNode/gisdata',
    packages=['gisdata',],
    package_data={'gisdata': all_dirs('gisdata'),},
    zip_safe=False,
)
