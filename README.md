## Overview

A dictionary converted from [EDICT2](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) for Mozc.

Thanks to the Electronic Dictionary Research and Development Group.

## License

mozcdic-ut-edict2.txt: [Creative Commons Attribution-ShareAlike Licence (V4.0)](https://www.edrdg.org/edrdg/licence.html)

Source code: Apache License, Version 2.0

## Usage

Add the dictionary to dictionary00.txt and build Mozc as usual.

```
tar xf mozcdic-ut-*.txt.tar.bz2
cat mozcdic-ut-*.txt >> ../mozc-master/src/data/dictionary_oss/dictionary00.txt
```

To modify the costs for words or merge multiple UT dictionaries into one, use this tool:

[merge-ut-dictionaries](https://github.com/utuhiro78/merge-ut-dictionaries)

## Update this dictionary with the latest stuff

Requirement(s): python-jaconv

```
cd src/
sh make.sh
```

[HOME](http://linuxplayers.g1.xrea.com/mozc-ut.html)
