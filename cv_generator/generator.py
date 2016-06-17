import os
from os.path import join as pjoin
import tempfile
import pathlib
import subprocess as sp
import shutil as sh

import jinja2
import yaml

LATEX_JINJA_PARAMS = dict(
    block_start_string=r'\BLOCK{',
    block_end_string='}',
    variable_start_string=r'\VAR{',
    variable_end_string='}',
    comment_start_string=r'\#{',
    comment_end_string='}',
    line_statement_prefix='%%',
    line_comment_prefix='%#',
    trim_blocks=True,
    autoescape=False,
)

def process(configuration, data_dir, template_dir):
    loader = jinja2.FileSystemLoader(os.path.abspath(template_dir))
    env = jinja2.Environment(loader=loader, **LATEX_JINJA_PARAMS)
    data = _load_data(data_dir)

    latex_config = configuration.get('latex', {})
    latex_program = latex_config.get('program', 'latex')
    latex_texfile = latex_config.get('root', 'index.tex')
    latex_format = latex_config.get('format', 'dvi')

    template_root = pathlib.Path(template_dir)
    with tempfile.TemporaryDirectory(prefix='cv_generator') as result_dir:
        for template_path in template_root.iterdir():
            if template_path.suffix != '.tex' or template_path.name.startswith('.'):
                continue
            template = env.get_template(template_path.name)
            result_path = pjoin(result_dir, template_path.name)
            with open(result_path, 'w') as resfile:
                resfile.write(template.render(**data))
            sp.call([
                latex_program, '-output-directory', result_dir,
                pjoin(result_dir, latex_texfile)
            ])
            sh.copy(
                pjoin(
                    result_dir,
                    latex_texfile.replace('.tex', '.' + latex_format)
                ),
                os.getcwd()
            )


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
