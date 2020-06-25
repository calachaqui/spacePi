from setuptools import setup

NAME = "pyubx"
VERSION = "0.1"
REQS = [
    "pyserial==3.*",
]

LINKS = []

setup(
    name=NAME,
    version=VERSION,
    install_requires=REQS,
    dependency_links=LINKS,
    description="Python3 module for interfacing with U-blox GPS devices.",
    author_email="william@williamflynt.com",
    url="https://github.com/williamflynt/pyUblox",
    keywords=["uBlox", "ublox", "ubx", "pyubx", "pyublox"],
    packages=['.', 'UBX'],
    include_package_data=True,
    long_description=""" """
)