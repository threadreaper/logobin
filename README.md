# logobin  

### A simple command line utility for working with logo.bin files for Android head units based on the ac8227l SoC.  
  
This utility is made to simplify the process of extracting the MediaTek header from a logo.bin file or adding it 
to an image file you want to use as your boot screen.  All the units I've seen need a 1024x600 pixel bitmap image
in 8-bit RGB color.

To install:  
  
Clone this git repository, and from the top-level directory (where setup.py is):

	pip3 install .

Alternatively, you can get the package from PyPi using:

	pip3 install logobin

Once installed, the logobin utility should be available from the command line.  Example:

	logobin -u logo.bin

Help is available from the command line with the -h or --help option, but basic usage is as follows:  
  
	-c (file)             Test a file for the presence of a valid header.
	-u (logo.bin file)    Unpack logo.bin to a header and image file.
	-p [(header file) (image file) (optional: filename)]	Pack header and image into a flashable binfile.If not given, filename defaults to logo.bin

### Using logobin as a module:  
  
If you'd like to use this script as a module in some other code, it exposes the following methods:  
  
	check(these_bytes):		*Accepts a list of bytes as input, and tests to see if they start with a valid header.*
	logo_bin_pack(header, bmp, filename):	*Accepts an MTK header, a bitmap file and an optional output filename as input.   Packs a logo.bin file.   If not given, filename defaults to logo.bin*  
	logo_bin_unpack(binfile):	*Accepts a logo.bin with a valid MTK header as input, and unpacks it, producing header.bin and logo.bmp*

Questions or comments can be directed to threadreaper@gmail.com.  Pull requests are welcome if you discover any issues.

	Copyright [2020] [Michael Podrybau]

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

	http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or 
	implied.  See the License for the specific language governing 
	permissions and limitations under the License.