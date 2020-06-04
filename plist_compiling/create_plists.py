#!/usr/bin/env python3

import plistlib

from shortcuts import shortcuts
from markdown_it_emoji import markdown_it_emojis

if __name__ == "__main__":

    markdown_it_emojis_expanded = []
    for shortcut, emoji in markdown_it_emojis.items():
        d = {'phrase': emoji, 'shortcut': f":{shortcut}:"}
        markdown_it_emojis_expanded.append(d)

    with open('../markdown-it-emoji_check_before_commit.plist', 'wb') as f:
        # https://docs.python.org/3/library/plistlib.html#plistlib.dump
        plistlib.dump(markdown_it_emojis_expanded, f, fmt=plistlib.FMT_XML, sort_keys=False, skipkeys=False)

    shortcuts_expanded = []
    for markdown_emoji_shortcut, shortcut_array in shortcuts.items():
        emoji = markdown_it_emojis[markdown_emoji_shortcut]
        for shortcut in shortcut_array:
            d = {'phrase': emoji, 'shortcut': shortcut}
            shortcuts_expanded.append(d)

    with open('../shortcuts_check_before_commit.plist', 'wb') as f:
        # https://docs.python.org/3/library/plistlib.html#plistlib.dump
        plistlib.dump(shortcuts_expanded, f, fmt=plistlib.FMT_XML, sort_keys=False, skipkeys=False)
