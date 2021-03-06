#!/usr/bin/python

# A python script to automatically extract .po files from tarballs (.gz, .bz2, .xz and .zip)

# Usage: python poextract.py

# Author: Nilamdyuti Goswami <nilamdyuti@gmail.com>

## This library is free software; you can redistribute it and/or
## modify it under the terms of the GNU Lesser General Public
## License as published by the Free Software Foundation; either
## version 2.1 of the License, or (at your option) any later version.
##
## This library is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## Lesser General Public License for more details.
##
## You should have received a copy of the GNU Lesser General Public
## License along with this library.  If not, see
## <http://www.gnu.org/licenses/>.

import os
import sys

def extract():
    try:
        directory = raw_input('\n\x1b[31mEnter the directory path: \x1b[0m')
        stime = str(os.popen("date").read())
        print('\n\x1b[32mStarted on %s\n\x1b[0m' % stime)
        tarball_path_names = os.popen("find %s \( -name '*.gz' -o -name '*.bz2' -o -name '*.xz' -o -name '*.zip' \) | sort | uniq" % directory).read().splitlines()
        print('\x1b[32mExtracting po files...\n\x1b[0m')
        for lines in tarball_path_names:
            modpath = os.path.dirname(lines)
            os.system("mkdir -p extracted/%s" % modpath)
            if os.path.basename(lines).endswith(".gz"):
                command = "tar zxf %s -k -C extracted/%s '*.po'" % (lines, modpath) + ">/dev/null 2>&1"
            elif os.path.basename(lines).endswith(".bz2"):
                command = "tar jxf %s -k -C extracted/%s '*.po'" % (lines, modpath) + ">/dev/null 2>&1"
            elif os.path.basename(lines).endswith(".xz"):
                command = "tar Jxf %s -k -C extracted/%s '*.po'" % (lines, modpath) + ">/dev/null 2>&1"
            else:
                command = "unzip -n %s -d extracted/%s '*.po'" % (lines, modpath) + ">/dev/null 2>&1"
	    output = os.system(command)
	    if output > 0:
		os.system("echo 'Error: %s' >> poextract.log " % lines)
        print('\x1b[32mSuccessfully extracted all .po files!\n\x1b[0m')
        etime = str(os.popen("date").read())
        print('\n\x1b[32mCompleted on %s\n\x1b[0m' % etime)
        tsize = str(os.popen("du -ch extracted | grep total").read())
        print('\n\x1b[32mSize of extracted data: %s\n\x1b[0m' % tsize)
    except KeyboardInterrupt:
        print('\n\n\x1b[32mExiting on user interrupt!\n\x1b[0m')
        sys.exit()
def main():
    extract()
if __name__ == '__main__':
    main()
