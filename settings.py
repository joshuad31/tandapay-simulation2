import os

_cur_dir = os.path.dirname(os.path.realpath(__file__))

DB_DIR = os.path.join(_cur_dir, 'databases')
FILE_SYSTEM = '1 System Database.xlsx'
FILE_USER = '2 User Database.xlsx'

ROOT_DIR = os.path.expanduser('~/.tandapay')
os.makedirs(ROOT_DIR, exist_ok=True)

RESULT_DIR = os.path.join(_cur_dir, 'result')
os.makedirs(RESULT_DIR, exist_ok=True)

MIN_VARIABLES = {
    'ev': [30, 1000, 0, 0, 0, 0, 2, 0, 0],
    'pv': [1, 1, 1, 1, 1, 1]
}
MAX_VARIABLES = {
    'ev': [130, 1000, 100, 50, 50, 100, 4, 5, 100],
    'pv': [50, 25, 100, 25, 100, 25]
}

try:
    from local_settings import *
except ImportError:
    pass
