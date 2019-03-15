#!/usr/bin/python
import glob
from os.path import basename
import yaml
from yaml import CLoader as Loader, CDumper as Dumper
from pathlib import Path
import click
import os 

CURRENT_PATH = '/g/data/u46/users/hr8696/'
def fix_path(band):
   file_n= basename(band)
   return file_n.split(".")[0]
   

@click.command()
@click.argument('folder')
def main(folder):
    print('in and out of {}'.format(CURRENT_PATH + folder))
    in_folder = CURRENT_PATH + folder
   # out_folder = CURRENT_PATH + folder
    in_dir = os.path.abspath(in_folder)
    print(in_dir)
    files = [filename for filename in glob.glob(in_dir + "/**/*.yaml",recursive=True)]
    print(files)
    for filename in files:
        print('processing {}'.format(basename(filename)))

        with open(filename) as fl:
            meta = yaml.load(fl, Loader=Loader)

        
        meta['image']['bands']['wofs']['path'] = fix_path(filename) + ".tif"
        meta['lineage']['source_datasets'] ={}

        with open(filename, 'w') as fl:
            yaml.dump(meta, fl, default_flow_style=False, Dumper=Dumper)

main()



