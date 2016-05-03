import jinja2
import yaml
import os

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
