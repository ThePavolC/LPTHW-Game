try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Game',
    'author': 'Pavol Celuch',
    'url': 'https://github.com/ThePavolC/LPTHW-Game',
    'download_url': 'https://github.com/ThePavolC/LPTHW-Game',
    'author_email': 'ThePavolC@users.noreply.github.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['game'],
    'scripts': [],
    'name': 'game'
}

setup(**config)