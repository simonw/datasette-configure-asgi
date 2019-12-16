from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-configure-asgi",
    description="Datasette plugin for configuring arbitrary ASGI middleware",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-configure-asgi",
    license="Apache License, Version 2.0",
    version=VERSION,
    entry_points={"datasette": ["configure_asgi = datasette_configure_asgi"]},
    py_modules=["datasette_configure_asgi"],
    extras_require={
        "test": ["pytest", "pytest-asyncio", "asgiref==3.1.2", "datasette"]
    },
)
