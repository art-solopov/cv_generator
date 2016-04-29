from setuptools import setup, find_packages

setup(
    name='CV generator',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'Jinja2 >=2.8, <3',
        'click >=6, <7',
        'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'cv_generator = cv_generator.cmd:generate'
        ]
    },
    test_suite='tests'
)

