# OTP Splitter

To my knowledge, this only works on the Linux command line at the moment. If you test this on a Windows python2 instance, please do let me know.

This script lets you extract various keys from a dumped Wii U OTP, as outlined on [the WiiUBrew site](http://wiiubrew.org/wiki/Hardware/OTP).

This should be a 100% legal way to get copies of these keys FOR YOUR PERSONAL USE!

This is my first "real" experiment in Python and Hexadecimal, so it's not super pretty to read or look at. And it's QUITE long.

Please do feel free to throw Pull Requests at me to fix any mistakes that you think I have made, or to shorten the script.

### How to use:

 * Extract your OTP to your SD card by using [OTP2SD](https://github.com/dimok789/otp2sd_dumper)
 * Copy the resulting OTP.bin to a folder called "OTP"
 	* If you forget to do so or put it in the wrong place before running the script - It will create the folder then let you know where to put it.
 * Install pycrypto somehow on Windows (I couldn't find decent documentation on that, sorry), or `sudo pip install pycrypto` (or however else you know/prefer) on Linux.
 * Download the script to a folder, and make a folder called "OTP" in the same folder.
 * Put the extracted OTP from step 1 into the OTP folder
 * Run the script using Python 2
 	* On various Linux distributions, this can likely be done by running `python2 OTPKeySplitter.py`
 * Use a hex editor to copy out your keys.
 	* I personally would suggest using [HxD](https://mh-nexus.de/en/hxd/) (on Windows), or [Bless](http://home.gna.org/bless) (on various Linux distros) to achieve this.

### BIG thanks goes to (in order of when I remembered their name):

 * Dimok, for the original [OTP2SD](https://github.com/dimok789/otp2sd_dumper) homebrew that started me on this
 	* For the unofficial GBATemp thread: [Click Here](http://gbatemp.net/threads/otp2sd-by-dimok.447353/)
 * The WiiUBru team that got the list up in the first place, and the ones that put up with my complaining about writing this.
 * vmgoose for code contributions, like pushing the keys as hex to a file.
 * Audiosurf for helping shorten the script itself in quite a few places.
 * Truedread for supplying an OTP.bin for me to test with.
 * Anyone else that cares enough to nag me about it in the WiiUBru IRC.
 * My friends that I've complained about this to, that aren't in the WiiUBru IRC.
