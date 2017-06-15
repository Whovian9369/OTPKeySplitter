# OTP Key Extractor

**This is a test and development branch for python3 use.**
----------------------------------------

This script lets you extract various keys from a dumped Wii U OTP, as outlined on [the WiiUBrew site](http://wiiubrew.org/wiki/Hardware/OTP).

----------------------------------------

### How to use it:

 * Extract your OTP to your SD card by using [OTP2SD](https://github.com/dimok789/otp2sd_dumper)
 * Copy the resulting OTP.bin to a folder called "OTP"
 	* If you forget to do so or put it in the wrong place before running the script - It will create the folder then let you know where to put it.
 * Install pycrypto somehow. Like `sudo pip install pycrypto` or `sudo pip3 install pycrypto` or however else.
 * Download the script to a folder.
 * Put the extracted OTP from step 1 into the folder holding the script.
 * Run the script using Python 3.
 	* This can likely be done by running `python3 OTPKeySplitter.py`
 * Use a hex editor to copy out your keys.
 	* I personally would suggest using [HxD](https://mh-nexus.de/en/hxd/) on Windows, or [Bless](http://home.gna.org/bless) on Linux distros.

### BIG thanks goes to (in no particular order):

 * Dimok, for the original [OTP2SD](https://github.com/dimok789/otp2sd_dumper) homebrew that started me on this
 	* For the unofficial GBATemp thread: [Click Here](http://gbatemp.net/threads/otp2sd-by-dimok.447353/)
 * The WiiUBru team that got the list up in the first place, and the ones that put up with my complaining about writing this.
 * vmgoose for code contributions, like pushing the keys as hex to a file.
 * Audiosurf for helping shorten the script itself in quite a few places.
 * Truedread for supplying an OTP.bin for me to test with.
 * Anyone else that cares enough to nag me about it in the WiiUBru IRC.
 * My friends that I've complained about this to, that aren't in the WiiUBru IRC.
