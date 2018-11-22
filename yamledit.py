#!/usr/bin/python
import glob
import yaml
from yaml import CLoader as Loader, CDumper as Dumper
from pathlib import Path
import click
import os
from os.path import join as pjoin, basename, dirname, exists, splitext
import logging




@click.command(help="\b Edit yaml fields")
@click.option('--path', '-p', required=True, help="Read the yamls from this path",
              type=click.Path(exists=True, readable=True))
def main(path):
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
    yaml_path = os.path.abspath(path)
    count = 0
    for path, subdirs, files in os.walk(yaml_path):
        for fname in files:
            if fname.endswith('.yaml'):
                f_name = os.path.join(path, fname)
                logging.info("Reading %s", (f_name))
                count = count + 1
                with open(f_name) as fl:
                    meta = yaml.load(fl, Loader=Loader)

                # bands = meta['image']['bands']
                # meta['image']['bands'] = fix_s3(bands, folder, base)
                meta['extent']['center_dt'] = '2000-01-01T00:00:00'

                meta['extent']['from_dt'] = '2000-01-01T00:00:00'
                print(meta)
                with open(f_name, 'w') as fl:
                    yaml.dump(meta, fl, default_flow_style=False, Dumper=Dumper)
                logging.info("Writing Yaml to %s, %i", basename(f_name), count)


if __name__ == "__main__":
    main()





