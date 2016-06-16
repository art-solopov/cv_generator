import click
import configparser

from cv_generator.generator import process

@click.command()
@click.option('--config', default='cv_generation.ini', help='Configuration file')
@click.argument('templatedir')
@click.argument('datadir')
def generate(config_file, template_dir, data_dir):
    cfg = configparser.ConfigParser().read(config_file)
    process(configuration=cfg, data_dir=data_dir, template_dir=template_dir)
