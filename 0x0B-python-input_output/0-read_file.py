#!/usr/bin/python3
# 0-read_file.py
# Nicholas M Mwanza <nicholasmuindi25@gmail.com>
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
