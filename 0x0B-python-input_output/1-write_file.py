#!/usr/bin/python3
"""file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8.

    Args:
        filename (str): The name of the file.
        text (str): The text to write.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
