import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DATA_DIR = os.path.join(PROJECT_ROOT, 'data')

GOOD_DATA = os.path.join(DATA_DIR, 'good')

BAD_DATA = os.path.join(DATA_DIR, 'bad')

VECTOR_DATA = os.path.join(GOOD_DATA, 'vector')

RASTER_DATA = os.path.join(GOOD_DATA, 'raster')

METADATA_DIR = os.path.join(PROJECT_ROOT, 'metadata')

GOOD_METADATA = os.path.join(METADATA_DIR, 'good')
