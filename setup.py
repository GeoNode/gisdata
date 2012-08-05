import os
from distutils.core import setup

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

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
    package_data={'gisdata': ['data/good/vector/*',
                              'data/good/raster/*',
                              'data/bad/*',
                              'data/good/time/*',
                              ]},
    zip_safe=False,
)
