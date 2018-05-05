# OTP Key Extractor

This script lets you extract various keys from a dumped Wii U OTP, as outlined on [the WiiUBrew site](http://wiiubrew.org/wiki/Hardware/OTP).
----------------------------------------

### How to use it:

 * Extract your OTP to your SD card by using the following:
	* [OTP2SD](https://github.com/dimok789/otp2sd_dumper) (for a less complete OTP dump)
 	* [hexCFW](https://github.com/hexkyz/hexFW) (for an OTP with two extra keys, which were previously inaccessible.)
         * This is done via getting access to boot1... Which I'm unable to explain on WHY it works.
	 	* No, we don't have the boot1 key. Yet. This dumps the OTP without the boot1 decryption key.
 * Download the script to a directory.
 * Copy the resulting OTP.bin to the directory containing the OTPKeySplitter.py script.
 	* If you forget to do so or put it in the wrong place before running the script - It will let you know where to put it.
 * Install pycrypto somehow. Like `sudo pip install pycrypto` or `sudo pip3 install pycrypto` or however else.
 * Run the script using Python 3.
 	* This can likely be done by running `python3 OTPKeySplitter.py`
 * Use a hex editor to copy out your keys OR grab the key directly from the Keys.txt file.
 	* If you want to use the hex editor technique, I personally would suggest using [HxD](https://mh-nexus.de/en/hxd/) on Windows, or [Bless](http://home.gna.org/bless) on Linux distros.

### BIG thanks goes to (in no particular order):

 * Dimok, for the original [OTP2SD](https://github.com/dimok789/otp2sd_dumper) homebrew that started me on this
 	* For the unofficial GBATemp thread: [Click Here](http://gbatemp.net/threads/otp2sd-by-dimok.447353/)
 * The WiiUBrew team that got the list up in the first place.
 * Audiosurf for helping shorten the script itself in quite a few places.
 * My friends that I've complained about this to.
 	* Especially those that were great help with helping keep me sane and sanity check me when I needed it!
 * Thank you dogcow for giving me the missing `binascii.hexlify(variable).decode('utf-8')` hint that I needed for writing the keys to a text file!
