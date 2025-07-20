from setuptools import setup

setup(
    name="concatvids",
    version="0.1",
    py_modules=["concatvids"],
    entry_points={
        "console_scripts": [
            "concatvids=concatvids:main",
        ],
    },
)
