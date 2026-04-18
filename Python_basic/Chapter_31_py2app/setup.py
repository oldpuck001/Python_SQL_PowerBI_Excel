from setuptools import setup
import py2app

APP = ['text_editor.py']
OPTIONS = {
    'argv_emulation': True,
		'packages': ['tkinter'],
}

setup(
    app = APP,
    options = {'py2app': OPTIONS},
    setup_requires = ['py2app'],
)