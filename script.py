import csv
import os
import shutil

from collections import defaultdict
from datetime import datetime
from decimal import Decimal


def process_csv(filename):
    source_file=filename
    output_file_name=f'{filename.split("/")[-1]}'
    # output_file_name=f'{output_file_name.split(".")[0]}_checked_{str(datetime.now())}.csv'
    destination_file=os.path.join('output', output_file_name)
    if os.path.isfile(source_file):
        shutil.copy(source_file, destination_file)

    return destination_file
