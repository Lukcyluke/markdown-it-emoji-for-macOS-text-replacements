#!/usr/bin/env python3

import plistlib
import sys

from shortcuts import shortcuts
from markdown_it_emoji import markdown_it_emojis

"""
    This script can be used to remove the added markdown emoji shortcuts from the text substitutions.
    Just export the text substitutions, like explained in the README.md, and run this script in the file.
    If a second file is given, it will export to it.
"""

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print(f"usage: {__file__} <exported.plist> [<output.plist>]")
        exit(1)

    with open(sys.argv[1], 'rb') as f:
        text_replacements = plistlib.load(f)

    for shortcut, emoji in markdown_it_emojis.items():
        d = {'phrase': emoji, 'shortcut': f":{shortcut}:"}
        text_replacements.remove(d)

    for markdown_emoji_shortcut, shortcut_array in shortcuts.items():
        emoji = markdown_it_emojis[markdown_emoji_shortcut]
        for shortcut in shortcut_array:
            d = {'phrase': emoji, 'shortcut': shortcut}
            text_replacements.remove(d)

    if len(sys.argv) < 3:
        print(text_replacements)  # as plist file content
        exit(0)
    else:
        # dump into third arg
        with open(sys.argv[2], 'wb') as f:
            # https://docs.python.org/3/library/plistlib.html#plistlib.dump
            plistlib.dump(text_replacements, f, fmt=plistlib.FMT_XML, sort_keys=False, skipkeys=False)
