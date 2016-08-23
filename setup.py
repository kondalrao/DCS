try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'DCS',
    'author': 'Kondal Rao Komaragiri',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'kondal04@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['DCS'],
    'scripts': [],
    'name': 'DCS'
}

setup(**config)