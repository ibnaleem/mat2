```
 _____ _____ _____ ___ 
|     |  _  |_   _|_  |  Keep you data,
| | | |     | | | |  _|     trash your meta!
|_|_|_|__|__| |_| |___|
                       
```

[![pipeline status](https://0xacab.org/jvoisin/mat2/badges/master/pipeline.svg)](https://0xacab.org/jvoisin/mat2/commits/master)
[![coverage report](https://0xacab.org/jvoisin/mat2/badges/master/coverage.svg)](https://0xacab.org/jvoisin/mat2/commits/master)

This software is currently in **beta**, please don't use it for anything
critical.

# Metadata and privacy

Metadata consist of information that characterizes data.                                             
Metadata are used to provide documentation for data products.                                        
In essence, metadata answer who, what, when, where, why, and how about                               
every facet of the data that are being documented.                                                   

Metadata within a file can tell a lot about you.                                                     
Cameras record data about when a picture was taken and what                                          
camera was used. Office documents like PDF or Office automatically adds                              
author and company information to documents and spreadsheets.                                        
Maybe you don't want to disclose those information on the web. 

This is precisely the job of MAT2: getting rid, as much as possible, of
metadata.

# Requirements

- `python3-mutagen` for audio support
- `python3-gi-cairo` and `gir1.2-poppler-0.18` for PDF support
- `gir1.2-gdkpixbuf-2.0` for images support
- `libimage-exiftool-perl` for everything else

Please note that MAT2 requires at least Python3.5, meaning that it
doesn't run on [Debian Jessie](Stretc://packages.debian.org/jessie/python3),

# Running the testsuite

```bash
$ python3 -m unittest discover -v
```

# Supported formats

```bash
$ python3 ./main.py -l
```

# Related softwares

- The first iteration of [MAT](http://mat.boum.org)
- [Exiftool](https://sno.phy.queensu.ca/~phil/exiftool/mat)
- [pdf-redact-tools](https://github.com/firstlookmedia/pdf-redact-tools), that
	tries to deal with *printer dots* too.
- [pdfparanoia](https://github.com/kanzure/pdfparanoia), that removes
	watermarks from PDF.

# License

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Copyright 2018 Julien (jvoisin) Voisin <julien.voisin+mat2@dustri.org>

# Thanks

MAT2 wouldn't existe without:

- the Google Summer of Code,
- the fine people from the Tails project
- friends

Many thanks to them!

