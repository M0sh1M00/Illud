from setuptools import setup
MODULES = ["pygame", "random", "contextlib"]
GAME = ["Illud.py"]
DATA =  [("",["images"]),("",["audio"]),("",["mytitle"])]
OPTIONS = {'argv_emulation': False,"iconfile":"mytitle/title.icns","includes":MODULES,"packages":"pygame"}

setup(
    app = GAME,
    data_files = DATA,
    options = {"py2app":OPTIONS},
    setup_requires = ["py2app"]


    )
