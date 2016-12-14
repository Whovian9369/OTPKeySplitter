#!/user/bin/env python2
import os, sys, zlib, binascii
import codecs
from Crypto.Cipher import AES


otpbinpath = os.path.abspath("OTP/otp.bin")

#Thank you Audiosurf for:

x = "Output/"
k = " - Wii U Bank"
outputfol = [x, x+"01 - Wii Bank", x+"02"+k, x+"03"+k, x+"04"+k, x+"05"+k, x+"06 - Wii SEEPROM Bank", x+"07 - Misc Bank"]
for f in outputfol:
	if not os.path.exists(f):
		os.makedirs(f)

#End Audiosurf's amazing and super useful contribution!

#prepare keys
#Thanks FIX94 for this code snippet from the iosuhax
#fw.img grabber in his IOSUHax Branch.
#For the source of this code, see:
# https://github.com/FIX94/iosuhax/blob/master/bin/getfwimg.py

if os.path.exists(otpbinpath):
    with open(otpbinpath,'rb') as f:
        print("Key extraction time!")

        # First, vWii.

        f.seek(0x000)
        vwii_boot1_sha1 = binascii.hexlify(f.read(20))
        f.seek(0x014)
        vwii_commonkey = binascii.hexlify(f.read(16))
        f.seek(0x024)
        vwii_ng_id = binascii.hexlify(f.read(4))
        f.seek(0x028)
        vwii_ng_priv_key = binascii.hexlify(f.read(29))
        f.seek(0x044)
        vwii_nand_hmac = binascii.hexlify(f.read(20))
        f.seek(0x058)
        vwii_nand_key = binascii.hexlify(f.read(16))
        f.seek(0x068)
        vwii_rng = binascii.hexlify(f.read(16))
        f.seek(0x078)
        vwii_unknown = binascii.hexlify(f.read(8))
        f.seek(0x220)
        possibly_vwii_ng_private_key = binascii.hexlify(f.read(32))
        
        # vWii SEEPROM Bank
        
        f.seek(0x300)
        old_wii_seeprom_cert = binascii.hexlify(f.read(96))
        f.seek(0x360)
        old_wii_seeprom_sig = binascii.hexlify(f.read(32))
        

        # The Wii U is next

        f.seek(0x90)
        starbuck_ancast_key = binascii.hexlify(f.read(16))
        f.seek(0xA0)
        wiiu_seeprom_key = binascii.hexlify(f.read(16))
        f.seek(0x150)
        wiiu_xor = binascii.hexlify(f.read(16))
        f.seek(0x160)
        wiiu_rng_key = binascii.hexlify(f.read(16))
        f.seek(0x260)
        wiiu_rng_seed = binascii.hexlify(f.read(16))
        f.seek(0x21C)
        wiiu_usb_key_seed_u32 = binascii.hexlify(f.read(4))
        f.seek(0x08C)
        unknown_00010000 = binascii.hexlify(f.read(4))

        
        
        # MISC

        f.seek(0x380)
        boot1_locked_unknown_01 = binascii.hexlify(f.read(32))
        f.seek(0x3A0)
        boot1_key_locked_by_b0 = binascii.hexlify(f.read(16))
        f.seek(0x3B0)
        boot0_locked_unused_01 = binascii.hexlify(f.read(16))
        f.seek(0x3C0)
        misc_empty = binascii.hexlify(f.read(16))
        f.seek(0x3E0)
        misc_unknown = binascii.hexlify(f.read(16))
        f.seek(0x3F0)
        ascii_tag = binascii.hexlify(f.read(12))
        f.seek(0x3FC)
        jtag_status = binascii.hexlify(f.read(4))

else:
    if not os.path.exists("OTP"):
        os.makedirs("OTP")
    print("Put the otp.bin into the OTP folder please!")
    sys.exit(1)

##################################################################
#Some actual key extraction. No output to a file yet, though.
print("\nvWii_boot1_sha1:")
print(vwii_boot1_sha1)
print("\nvWii Common Key:")
print(vwii_commonkey)
print("\nStarbuck Ancast Key:")
print(starbuck_ancast_key)
print("\nWii U Common Key:")
print(wiiu_common_key)
print("\nWii U SEEPROM Key:")
print(wiiu_seeprom)
print("\nWii U XOR:")
print(wiiu_xor)
print("\nWii U RNG:")
print(wiiu_rng)
#
##################################################################

wiiu_common_key = codecs.decode(wiiu_common_key, 'hex')
starbuck_ancast_key = codecs.decode(starbuck_ancast_key, 'hex')

if zlib.crc32(wiiu_common_key) & 0xffffffff != 0x7a2160de:
    print("wiiu_common_key is wrong")
    sys.exit(1)

if zlib.crc32(starbuck_ancast_key) & 0xffffffff != 0xe6e36a34:
    print("starbuck_ancast_key is wrong")
    sys.exit(1)
