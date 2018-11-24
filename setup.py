import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='sshauthproxy',
    version='0.1',
    py_modules=['sshauthproxy'],

    entry_points={
        'console_scripts': [
            'sshauthproxy = sshauthproxy:main',
        ],
    },

    author='quantum',
    author_email='quantum2048@gmail.com',
    url='https://github.com/quantum5/sshauthproxy',
    description='SSH AuthorizedKeysCommand proxy: publish your SSH authorized_keys from '
                'an existing AuthorizedKeysCommand',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='AGPLv3',
    keywords='ssh public-key proxy authorized_keys',
    install_requires=['tornado'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: System :: Systems Administration :: Authentication/Directory',
        'Topic :: Utilities',
    ],
)

