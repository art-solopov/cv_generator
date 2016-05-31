import jinja2
import yaml
import os
import pathlib

LATEX_JINJA_PARAMS = dict(
    block_start_string='\BLOCK{',
    block_end_string='}',
    variable_start_string='\VAR{',
    variable_end_string='}',
    comment_start_string='\#{',
    comment_end_string='}',
    line_statement_prefix='%%',
    line_comment_prefix='%#',
    trim_blocks=True,
    autoescape=False,
)

TEMPLATES = ['cv.tex']

def process(configuration, data_dir, template_dir):
    loader = jinja2.FileSystemLoader(os.path.abspath(template_dir))
    env = jinja2.Environment(loader=loader, **LATEX_JINJA_PARAMS)
    data = _load_data(data_dir)

def _load_data(data_dir):
    data = {}
    data_root = pathlib.Path(data_dir)
    data_paths = [x for x in data_root.iterdir()
                  if x.suffix == '.yml' or x.suffix == '.yaml']
    for path in data_paths:
        with open(str(path), 'r') as df:
            file_data = yaml.load(df)
            data[path.stem] = file_data

    return data
