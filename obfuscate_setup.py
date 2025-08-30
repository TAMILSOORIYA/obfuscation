from setuptools import setup
from Cython.Build import cythonize
import os

BASE_DIR = os.path.dirname(__file__)

def list_py_files(base_dir):
    py_files = []
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith(".py") and not f.startswith("__init__"):
                py_files.append(os.path.join(root, f))
    return py_files

setup(
    name="my_fastapi_app",
    ext_modules=cythonize(
        list_py_files(BASE_DIR),  # replace with your folder name
        compiler_directives={"language_level": "3"},
    ),
    zip_safe=False,
)
