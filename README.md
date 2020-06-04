# markdown-it-emoji for macOS text replacements

Uses this property lists to use the markdown-it-emoji phrases in your macOS keyboard.
If you sync your text replacements, you can also use them iOS.

## Installation

1. Make a backup of your text replacements (see also: [Back up and share text replacements on Mac - Apple Support](https://support.apple.com/guide/mac-help/back-up-and-share-text-replacements-on-mac-mchl2a7bd795/mac "Back up and share text replacements on Mac - Apple Support"))
![Export drag'n'drop animation](images/export_drag_n_drop.gif "Drag the selected replacements from the Text pane to the desktop.")
2. Download the `.plist` files to a convenient location
3. On your Mac, choose Apple menu <img src="https://help.apple.com/assets/5E3B07AD680CE24F6D211AD5/5E3B07B2680CE24F6D211AE3/en_US/e043ddf1a45711e13f0b30612db65e21.png" alt="" height="15" width="13" originalimagename="SharedGlobalArt/IL_AppleLogo.png"> > System Preferences > Keyboard > Text
4. Drag the `.plist` files from its location to the Text pane
![Import drag'n'drop animation](images/import_drag_n_drop.gif "Drag the `.plist` files from its location to the Text pane")
* It could be useful to turn off [ ] Correct Spelling automatically

## Compiling the `.plist` files

You can recompile the files, if needed with the provided Python script.
To do so:

* Update `markdown_it_emoji.py` and `shortcuts.py`
* Run `create_plists.py` from within `plist_compiling/`