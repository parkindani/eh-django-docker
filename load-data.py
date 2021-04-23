import os
import django
import requests
import csv
import math
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
# Get the base directory
basepath = Path()
basedir = str(basepath.cwd())
# Load the environment variables
envars = basepath.cwd() / '.env'
load_dotenv(envars)

from xml.etree import ElementTree as ET

os.environ["DJANGO_SETTINGS_MODULE"] = 'elderlyhome.settings'
django.setup()

from homes.models import Home



