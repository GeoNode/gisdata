=======================================
gis-data - Sample data for GIS packages
=======================================

Sometimes you need sample raster and vector data for your python applications.

Sometimes you need bad data for your corner test cases. (No projections, NaN values).

This library provides both.

Installation
============

The latest release can be installed using::

    pip install gisdata

Usage
=====

Get the absolute path to the the sample data from python::

>>> from gisdata import GIS_DATA
>>> print GIS_DATA
'/usr/lib/python2.6/site-packages/gisdata/data'
>>> from gisdata import BAD_DATA
>>> print BAD_DATA
'/usr/lib/python2.6/site-packages/gisdata/data/bad'
>>> from gisdata import GOOD_DATA
>>> print GOOD_DATA
'/usr/lib/python2.6/site-packages/gisdata/data/good'

Known Issues
============

 * Vector data does not have sld files
 * There is no sample raster data
 * No xml files with metadata
 * No .keywords fils for machine tags
