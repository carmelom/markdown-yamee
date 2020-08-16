from setuptools import setup

VERSION = '0.0.1'
BASE_CVS_URL = 'https://github.com/carmelom/markdown-yamee'

setup(
    name='yamee',
    packages=['yamee',],
    version=VERSION,
    author='Carmelo Mordini',
    author_email='carmelo.mordini@gmail.com',
    url=BASE_CVS_URL,
    download_url='{}/tarball/{}'.format(BASE_CVS_URL, VERSION),
    test_suite='tests',
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        'markdown.extensions': [
            'yamee = yamee.yamee:EmojiExtension']
    },
)
