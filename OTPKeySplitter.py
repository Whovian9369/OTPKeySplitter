#!/usr/bin/env python2
import os, sys, zlib, binascii
import codecs
from Crypto.Cipher import AES


otpbinpath = os.path.abspath("OTP/otp.bin")

#Thank you Audiosurf for the initial folder creation help.
#Mine was way too messy originally!

x = "Output/"
k = " - Wii U Bank"
outputfol = [x, x+"00 - Wii Bank" , x+"01"+k, x+"02"+k, x+"03"+k, x+"04"+k, x+"05"+k , x+"06 - Wii SEEPROM Bank", x+"07 - Misc Bank"]
for f in outputfol:
	if not os.path.exists(f):
		os.makedirs(f)

#Other Variables that will be used later down the line:
out0 = x+"00 - Wii Bank"+"/"
out1 = x+"01"+k+"/"
out2 = x+"02"+k+"/"
out3 = x+"03"+k+"/"
out4 = x+"04"+k+"/"
out5 = x+"05"+k+"/"
out6 = x+"06 - Wii SEEPROM Bank/"
out7 = x+"07 - Misc Bank/"
#wiiu = "Wii U "
#vwii = "vWii "

#End other variables

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
        vwii_common_key = binascii.hexlify(f.read(16))
        f.seek(0x024)
        vwii_ng_id = binascii.hexlify(f.read(4))
        f.seek(0x028)
        vwii_ng_priv_key = binascii.hexlify(f.read(29))
        f.seek(0x044)
        vwii_nand_hmac = binascii.hexlify(f.read(20))
        f.seek(0x058)
        vwii_nand_key = binascii.hexlify(f.read(16))
        f.seek(0x068)
        vwii_rng_key = binascii.hexlify(f.read(16))
        f.seek(0x078)
        vwii_unknown = binascii.hexlify(f.read(8))
        f.seek(0x220)
        possible_vwii_ng_private_key = binascii.hexlify(f.read(32))
        
        # vWii SEEPROM Bank
        
        f.seek(0x300)
        old_wii_seeprom_cert = binascii.hexlify(f.read(96))
        f.seek(0x360)
        old_wii_seeprom_sig = binascii.hexlify(f.read(32))
        

        # The Wii U is next
        
        f.seek(0x080)
        security_level_flag = binascii.hexlify(f.read(4))
        f.seek(0x084)
        some_iostrength_config_flag = binascii.hexlify(f.read(4))
        f.seek(0x088)
        seeprom_manual_clk_pulse_length = binascii.hexlify(f.read(4))
        f.seek(0x08C)
        unknown_00010000 = binascii.hexlify(f.read(4))
        f.seek(0x90)
        starbuck_ancast_key = binascii.hexlify(f.read(16))
        f.seek(0xA0)
        wiiu_seeprom_key = binascii.hexlify(f.read(16))
        f.seek(0x0B0)
        unknown_01 = binascii.hexlify(f.read(16))
        f.seek(0x0C0)
        unknown_02 = binascii.hexlify(f.read(16))
        f.seek(0x0E0)
        wiiu_common_key = binascii.hexlify(f.read(16))
        f.seek(0x0F0)
        unknown_03 = binascii.hexlify(f.read(16))
        f.seek(0x100)
        unknown_04 = binascii.hexlify(f.read(16))
        f.seek(0x110)
        unknown_05 = binascii.hexlify(f.read(16))
        f.seek(0x120)        
        encrypt_decrypt_ssl_rsa_key = binascii.hexlify(f.read(16))
        f.seek(0x130)
        usb_storage_key_seed_encryption_key = binascii.hexlify(f.read(16))
        f.seek(0x140)
        unknown_06 = binascii.hexlify(f.read(16))        
        f.seek(0x150)
        wiiu_xor_key = binascii.hexlify(f.read(16))
        f.seek(0x160)
        wiiu_rng_key = binascii.hexlify(f.read(16))
        f.seek(0x170)
        wiiu_slc_nand_key = binascii.hexlify(f.read(16))
        f.seek(0x180)
        wiiu_mlc_emmc_key = binascii.hexlify(f.read(16))
        f.seek(0x190)
        seeprom_devkit_key_decryption_key = binascii.hexlify(f.read(16))
        f.seek(0x1A0)
        encryption_key_for_drh_wlan_data = binascii.hexlify(f.read(16))
        f.seek(0x1B0)
        unknown_07 = binascii.hexlify(f.read(48))
        f.seek(0x1E0)
        wiiu_slc_nand_hmac = binascii.hexlify(f.read(20))
        f.seek(0x1F4)
        unknown_08 = binascii.hexlify(f.read(12))
        f.seek(0x200)
        unknown_09 = binascii.hexlify(f.read(16))
        f.seek(0x210)
        unknown_10 = binascii.hexlify(f.read(12))
        f.seek(0x21C)
        wiiu_usb_key_seed_u32 = binascii.hexlify(f.read(4))
        f.seek(0x240)
        unknown_11 = binascii.hexlify(f.read(32))        
        f.seek(0x260)
        wiiu_rng_seed = binascii.hexlify(f.read(16))
        f.seek(0x270)
        unknown_12 = binascii.hexlify(f.read(16))
        f.seek(0x280)
        possible_wiiu_and_vwii_root_ca_version = binascii.hexlify(f.read(4))
        f.seek(0x284)
        possible_wiiu_and_vwii_root_ca_ms = binascii.hexlify(f.read(4))
        f.seek(0x288)
        unknown_13 = binascii.hexlify(f.read(4))
        f.seek(0x28C)
        possible_wiiu_and_vwii_root_ca_signature = binascii.hexlify(f.read(64))
        f.seek(0x2CC)
        unknown_14 = binascii.hexlify(f.read(20))
        f.seek(0x2E0)
        unknown_15_locked_by_boot1 = binascii.hexlify(f.read(32))
        
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

#Output to files. This will be messy.
#Probably way messier than above.
#vWii

 # 0. Wii Bank

target=out0+"01. Wii boot1 SHA-1 hash.bin"
fi = open(target, "wb")
fi.write(vwii_boot1_sha1.decode("hex"))
fi.close()

target=out0+"02. Wii common key.bin"
fi = open(target, "wb")
fi.write(vwii_common_key.decode("hex"))
fi.close()

target=out0+"03. Wii NG ID.bin"
fi = open(target, "wb")
fi.write(vwii_ng_id.decode("hex"))
fi.close()

target=out0+"04. Wii NG private key.bin"
fi = open(target, "wb")
fi.write(vwii_ng_priv_key.decode("hex"))
fi.close()

target=out0+"05. Wii NAND HMAC (overlaps with NG private key).bin"
fi = open(target, "wb")
fi.write(vwii_nand_hmac.decode("hex"))
fi.close()

target=out0+"06. Wii NAND key.bin"
fi = open(target, "wb")
fi.write(vwii_nand_key.decode("hex"))
fi.close()

target=out0+"07. Wii RNG key.bin"
fi = open(target, "wb")
fi.write(vwii_rng_key.decode("hex"))
fi.close()

target=out0+"08. Unknown.bin"
fi = open(target, "wb")
fi.write(vwii_unknown.decode("hex"))
fi.close()


# Wii U

 # 1. Wii U Bank

target=out1+"01. Security level flag.bin"
fi = open(target, "wb")
fi.write(security_level_flag.decode("hex"))
fi.close()

target=out1+"02. Some flag for IOStrength configurations.bin"
fi = open(target, "wb")
fi.write(some_iostrength_config_flag.decode("hex"))
fi.close()

target=out1+"03. Pulse length for SEEPROM manual CLK.bin"
fi = open(target, "wb")
fi.write(seeprom_manual_clk_pulse_length.decode("hex"))
fi.close()

target=out1+"04. Unknown (0x00010000).bin"
fi = open(target, "wb")
fi.write(unknown_00010000.decode("hex"))
fi.close()

target=out1+"05. Wii U Starbuck ancast key.bin"
fi = open(target, "wb")
fi.write(starbuck_ancast_key.decode("hex"))
fi.close()

target=out1+"06. Wii U SEEPROM key.bin"
fi = open(target, "wb")
fi.write(wiiu_seeprom_key.decode("hex"))
fi.close()

target=out1+"07. Unknown (01).bin"
fi = open(target, "wb")
fi.write(unknown_01.decode("hex"))
fi.close()

target=out1+"08. Unknown (02).bin"
fi = open(target, "wb")
fi.write(unknown_02.decode("hex"))
fi.close()

target=out1+"09. vWii common key.bin"
fi = open(target, "wb")
fi.write(vwii_common_key.decode("hex"))
fi.close()

target=out1+"10. Wii U Common Key.bin"
fi = open(target, "wb")
fi.write(wiiu_common_key.decode("hex"))
fi.close()

target=out1+"11. Unknown (03).bin"
fi = open(target, "wb")
fi.write(unknown_03.decode("hex"))
fi.close()

 # 2. Wii U Bank

target=out2+"01. Unknown (04).bin"
fi = open(target, "wb")
fi.write(unknown_04.decode("hex"))
fi.close()

target=out2+"02. Unknown (05).bin"
fi = open(target, "wb")
fi.write(unknown_05.decode("hex"))
fi.close()

target=out2+"03. Key to encrypt or decrypt SSL RSA key.bin"
fi = open(target, "wb")
fi.write(encrypt_decrypt_ssl_rsa_key.decode("hex"))
fi.close()

target=out2+"04. Key to encrypt seeds for USB storage keys.bin"
fi = open(target, "wb")
fi.write(usb_storage_key_seed_encryption_key.decode("hex"))
fi.close()

target=out2+"05. Unknown (06).bin"
fi = open(target, "wb")
fi.write(unknown_06.decode("hex"))
fi.close()

target=out2+"06. Wii U XOR key.bin"
fi = open(target, "wb")
fi.write(wiiu_xor_key.decode("hex"))
fi.close()

target=out2+"07. Wii U RNG key.bin"
fi = open(target, "wb")
fi.write(wiiu_rng_key.decode("hex"))
fi.close()

target=out2+"08. Wii U SLC (NAND) key.bin"
fi = open(target, "wb")
fi.write(wiiu_slc_nand_key.decode("hex"))
fi.close()

 # 3. Wii U Bank

target=out3+"01. Wii U MLC (eMMC) key.bin"
fi = open(target, "wb")
fi.write(wiiu_mlc_emmc_key.decode("hex"))
fi.close()

target=out3+"02. Key to decrypt SEEPROM devkit key.bin"
fi = open(target, "wb")
fi.write(seeprom_devkit_key_decryption_key.decode("hex"))
fi.close()

target=out3+"03. Key to encrypt DRH WLAN data.bin"
fi = open(target, "wb")
fi.write(encryption_key_for_drh_wlan_data.decode("hex"))
fi.close()

target=out3+"04. Unknown (07).bin"
fi = open(target, "wb")
fi.write(unknown_07.decode("hex"))
fi.close()

target=out3+"05. Wii U SLC (NAND) HMAC.bin"
fi = open(target, "wb")
fi.write(wiiu_slc_nand_hmac.decode("hex"))
fi.close()

target=out3+"06. Unknown (08).bin"
fi = open(target, "wb")
fi.write(unknown_08.decode("hex"))
fi.close()

 # 4. Wii U Bank
target=out4+"01. Unknown (09).bin"
fi = open(target, "wb")
fi.write(unknown_09.decode("hex"))
fi.close()

target=out4+"02. Unknown (10).bin"
fi = open(target, "wb")
fi.write(unknown_10.decode("hex"))
fi.close()

target=out4+"03. The USB key seed in SEEPROM must start with this u32.bin"
fi = open(target, "wb")
fi.write(wiiu_usb_key_seed_u32.decode("hex"))
fi.close()

target=out4+"04. vWii NG private key?.bin"
fi = open(target, "wb")
fi.write(possible_vwii_ng_private_key.decode("hex"))
fi.close()

target=out4+"05. Unknown (11).bin"
fi = open(target, "wb")
fi.write(unknown_11.decode("hex"))
fi.close()

target=out4+"06. Wii U RNG seed (only the first 0x04 bytes are used).bin"
fi = open(target, "wb")
fi.write(wiiu_rng_seed.decode("hex"))
fi.close()

target=out4+"07. Unknown (12).bin"
fi = open(target, "wb")
fi.write(unknown_12.decode("hex"))
fi.close()

 # 5. Wii U Bank
target=out5+"01. Wii U and vWii Root-CA version (0x00000012)?.bin"
fi = open(target, "wb")
fi.write(possible_wiiu_and_vwii_root_ca_version.decode("hex"))
fi.close()

target=out5+"02. Wii U and vWii Root-CA MS (0x00000003)?.bin"
fi = open(target, "wb")
fi.write(possible_wiiu_and_vwii_root_ca_ms.decode("hex"))
fi.close()

target=out5+"03. Unknown (13).bin"
fi = open(target, "wb")
fi.write(unknown_13.decode("hex"))
fi.close()

target=out5+"04. Wii U and vWii Root-CA signature?.bin"
fi = open(target, "wb")
fi.write(possible_wiiu_and_vwii_root_ca_signature.decode("hex"))
fi.close()

target=out5+"04. Unknown (14).bin"
fi = open(target, "wb")
fi.write(unknown_14.decode("hex"))
fi.close()

target=out5+"05. Unknown (locked out by boot1).bin"
fi = open(target, "wb")
fi.write(unknown_15_locked_by_boot1.decode("hex"))
fi.close()

# 6. Wii SEEPROM Bank

target=out6+"01. Old Wii SEEPROM certificate data.bin"
fi = open(target, "wb")
fi.write(old_wii_seeprom_cert.decode("hex"))
fi.close()

target=out6+"02. Old Wii SEEPROM signature?.bin"
fi = open(target, "wb")
fi.write(old_wii_seeprom_sig.decode("hex"))
fi.close()

# 7. Misc Bank

target=out7+"01. Unknown (locked by boot1).bin"
fi = open(target, "wb")
fi.write(boot1_locked_unknown_01.decode("hex"))
fi.close()

target=out7+"02. boot1 key (locked by boot0).bin"
fi = open(target, "wb")
fi.write(boot1_key_locked_by_b0.decode("hex"))
fi.close()

target=out7+"03. Unknown (locked out by boot0, not used).bin"
fi = open(target, "wb")
fi.write(boot0_locked_unused_01.decode("hex"))
fi.close()

target=out7+"04. Empty.bin"
fi = open(target, "wb")
fi.write(misc_empty.decode("hex"))
fi.close()

target=out7+"05. Unknown.bin"
fi = open(target, "wb")
fi.write(misc_unknown.decode("hex"))
fi.close()

target=out7+"06. ASCII tag (unknown meaning).bin"
fi = open(target, "wb")
fi.write(ascii_tag.decode("hex"))
fi.close()

target=out7+"07. JTAG status.bin"
fi = open(target, "wb")
fi.write(jtag_status.decode("hex"))
fi.close()
#End file output
