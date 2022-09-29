import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))


if env('USE_MYSQL', default=True):
    import pymysql
    pymysql.install_as_MySQLdb()
