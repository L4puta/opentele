import pathlib
from setuptools import setup


setup(
    name="opentele",
    version="1.15.2",
    license="MIT",
    description="A Python Telegram API Library for converting between tdata and telethon sessions, with built-in official Telegram APIs.",
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/thedemons/opentele",
    author="thedemons",
    author_email="thedemons@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Development Status :: 5 - Production/Stable",
    ],
    keywords=[
        "tdata",
        "tdesktop",
        "telegram",
        "telethon",
        "opentele",
    ],
    include_package_data=True,
    packages=[
        "opentele",
        "opentele.td",
        "opentele.tl",
    ],
    package_dir={
        "opentele": "src"
    },
    install_requires=[
        "pyqt6",
        "telethon",
        "tgcrypto",
    ]
)
