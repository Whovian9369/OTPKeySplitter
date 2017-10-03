#!/usr/bin/env python3
import os, sys, zlib, binascii
import codecs
from Crypto.Cipher import AES

otpbin = os.path.abspath("otp.bin")
if not os.path.exists(otpbin):
    print("Put the otp.bin into this folder please!")
    sys.exit(1)
keytxt = open('Keys.txt', 'a')
#Thank you Audiosurf for the initial folder creation help.
#Mine was way too messy originally!

x = "Output/"
k = " - Wii U Bank"
outputfol = [x, x+"00 - Wii Bank" , x+"01"+k, x+"02"+k, x+"03"+k, x+"04 - Wii U NG Bank", x+"05 - Wii U Certificate Bank" , x+"06 - Wii Certificate Bank", x+"07 - Misc Bank"]
for f in outputfol:
	if not os.path.exists(f):
		os.makedirs(f)

#Other Variables that will be used later down the line:
out0 = x+"00 - Wii Bank"+"/"
out1 = x+"01"+k+"/"
out2 = x+"02"+k+"/"
out3 = x+"03"+k+"/"
out4 = x+"04 - Wii U NG Bank/"
out5 = x+"05 - Wii U Certificate Bank/"
out6 = x+"06 - Wii Certificate Bank/"
out7 = x+"07 - Misc Bank/"
#End other variables

#prepare keys
#Thanks FIX94 for this code snippet from the iosuhax
#fw.img grabber in his IOSUHax fork.
#For the source of this code, see:
#https://github.com/FIX94/iosuhax/blob/master/bin/getfwimg.py

if os.path.exists(otpbin):
    with open(otpbin,'rb') as f:
        print("Key extraction time!")

        # First, vWii.

        f.seek(0x000)
        wii_boot1_sha1 = f.read(20)
        f.seek(0x014)
        wii_common_key = f.read(16)
        f.seek(0x024)
        wii_ng_id = f.read(4)
        f.seek(0x028)
        wii_ng_priv_key = f.read(29)
        f.seek(0x044)
        wii_nand_hmac = f.read(20)
        f.seek(0x058)
        wii_nand_key = f.read(16)
        f.seek(0x068)
        wii_rng_key = f.read(16)
        f.seek(0x078)
        wii_unknown01_padding = f.read(8)
#Wiki switches to Bank 1 (Wii U) right here. See #L78 // 0x300 begins Bank 6. 

        f.seek(0x300)
        wii_root_cert_ms_id_0x00000002 = f.read(4)
        f.seek(0x304)
        wii_root_cert_ca_id_0x00000001 = f.read(4)
        f.seek(0x308)
        wii_root_cert_ng_key_id = f.read(4)
        f.seek(0x30C)
        wii_root_cert_ng_signature = f.read(60)
        f.seek(0x348)
        wii_korean_key = f.read(16)
        f.seek(0x358)
        wii_unknown02_unused = f.read(8)
        f.seek(0x360)
        wii_private_nss_device_cert_key = f.read(32)
        
# Wii U
        
        f.seek(0x080)
        security_level_flag = f.read(4)
        f.seek(0x084)
        iostrength_config_flag = f.read(4)
        f.seek(0x088)
        seeprom_manual_clk_pulse_length = f.read(4)
        f.seek(0x08C)
        SigType_00010000 = f.read(4)
        f.seek(0x090)
        wiiu_starbuck_ancast_key = f.read(16)
        f.seek(0x0A0)
        wiiu_seeprom_key = f.read(16)
        f.seek(0x0B0)
        unknown_01_unused = f.read(16)
        f.seek(0x0C0)
        unknown_02_unused = f.read(16)
        f.seek(0x0D0)
        vwii_common_key = f.read(16)
        f.seek(0x0E0)
        wiiu_common_key = f.read(16)
        f.seek(0x0F0)
        unknown_03_unused = f.read(16)
        f.seek(0x100)
        unknown_04_unused = f.read(16)
        f.seek(0x110)
        unknown_05_unused = f.read(16)
        f.seek(0x120)        
        encrypt_decrypt_ssl_rsa_key = f.read(16)
        f.seek(0x130)
        usb_storage_key_seed_encryption_key = f.read(16)
        f.seek(0x140)
        unknown_06 = f.read(16)        
        f.seek(0x150)
        wiiu_xor_key = f.read(16)
        f.seek(0x160)
        wiiu_rng_key = f.read(16)
        f.seek(0x170)
        wiiu_slc_nand_key = f.read(16)
        f.seek(0x180)
        wiiu_mlc_emmc_key = f.read(16)
        f.seek(0x190)
        encrypt_decrypt_shdd_key = f.read(16)
        f.seek(0x1A0)
        encryption_key_for_drh_wlan_data = f.read(16)
        f.seek(0x1B0)
        unknown_07_unused = f.read(48)
        f.seek(0x1E0)
        wiiu_slc_nand_hmac = f.read(20)
        f.seek(0x1F4)
        unknown_08_padding = f.read(12)
        f.seek(0x200)
        unknown_09_unused = f.read(16)
        f.seek(0x210)
        unknown_10_unused = f.read(12)
        f.seek(0x21C)
        wiiu_ng_id = f.read(4)
        f.seek(0x220)
        wiiu_ng_private_key = f.read(32)
        f.seek(0x240)
        wiiu_private_nss_device_cert_key = f.read(32)        
        f.seek(0x260)
        wiiu_otp_rng_seed = f.read(16)
        f.seek(0x270)
        unknown_12_unused = f.read(16)
        f.seek(0x280)
        wiiu_root_cert_ms_id_0x00000012 = f.read(4)
        f.seek(0x284)
        wiiu_root_cert_ca_id_0x00000003 = f.read(4)
        f.seek(0x288)
        wiiu_root_cert_ng_key_id = f.read(4)
        f.seek(0x28C)
        wiiu_root_cert_ng_signature = f.read(64)
        f.seek(0x2C8)
        unknown_14_unused = f.read(20)
        f.seek(0x2E0)
        unknown_15_locked_by_boot1 = f.read(32)
        
        # MISC

        f.seek(0x380)
        boot1_locked_unknown_01 = f.read(32)
        f.seek(0x3A0)
        boot1_key_locked_by_b0 = f.read(16)
        f.seek(0x3B0)
        boot0_locked_unused_01 = f.read(16)
        f.seek(0x3C0)
        misc_empty1 = f.read(32)
        f.seek(0x3E0)
        misc_empty2 = f.read(4)
        f.seek(0x3E4)
        otp_version_and_revision = f.read(4)
        f.seek(0x3E8)
        otp_date_code = f.read(8) 
        f.seek(0x3F0)
        otp_version_name_string = f.read(8)
        f.seek(0x3F8)
        misc_empty3 = f.read(4)
        f.seek(0x3FC)
        jtag_status = f.read(4)

else:
    print("Put the otp.bin into this folder please!")
    print("If you got here without the file there... Darn you.")
    sys.exit(1)

#Output to files. This will be messy.
#Probably way messier than above.
#vWii

 # 0. Wii Bank

targetfol=out0
keytxt.write("(Most of) vWii:\n\n")

name="01. Wii boot1 SHA-1 hash"
fi = open(targetfol+name+".bin", "wb")
fi.write(wii_boot1_sha1)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wii_boot1_sha1).decode('utf-8')+"\n")

name="02. Wii common key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wii_common_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wii_common_key).decode('utf-8')+"\n")

name="03. Wii NG ID"
fi = open(targetfol+name+".bin", "wb")
fi.write(wii_ng_id)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wii_ng_id).decode('utf-8')+"\n")

name="04. Wii NG private key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wii_ng_priv_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wii_ng_priv_key).decode('utf-8')+"\n")

name="05. Wii NAND HMAC (overlaps with NG private key)"
fi = open(targetfol+name+".bin", "wb")
fi.write(wii_nand_hmac)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wii_nand_hmac).decode('utf-8')+"\n")

name="06. Wii NAND key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wii_nand_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wii_nand_key).decode('utf-8')+"\n")

name="07. Wii RNG key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wii_rng_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wii_rng_key).decode('utf-8')+"\n")

name="08. Unknown (Padding)"
fi = open(targetfol+name+".bin", "wb")
fi.write(wii_unknown01_padding)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wii_unknown01_padding).decode('utf-8')+"\n")

keytxt.write("\n------------------------------------------------")

# Wii U
keytxt.write("\n\n*(Mostly) Wii U:\n")
keytxt.write("\n	1. Wii U Bank\n")
 # 1. Wii U Bank

targetfol=out1

name="01. Security level flag"
fi = open(targetfol+name+".bin", "wb")
fi.write(security_level_flag)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(security_level_flag).decode('utf-8')+"\n")

name="02. Some flag for IOStrength configurations"
fi = open(targetfol+name+".bin", "wb")
fi.write(iostrength_config_flag)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(iostrength_config_flag).decode('utf-8')+"\n")

name="03. Pulse length for SEEPROM manual CLK"
fi = open(targetfol+name+".bin", "wb")
fi.write(seeprom_manual_clk_pulse_length)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(seeprom_manual_clk_pulse_length).decode('utf-8')+"\n")

name="04. Seems_To_Be_A_Sig_Type_(0x00010000)"
fi = open(targetfol+name+".bin", "wb")
fi.write(SigType_00010000)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(SigType_00010000).decode('utf-8')+"\n")

name="05. Wii U Starbuck ancast key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_starbuck_ancast_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_starbuck_ancast_key).decode('utf-8')+"\n")

name="06. Wii U SEEPROM key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_seeprom_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_seeprom_key).decode('utf-8')+"\n")

name="07. Unknown (01)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_01_unused)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_01_unused).decode('utf-8')+"\n")

name="08. Unknown (02)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_02_unused)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_02_unused).decode('utf-8')+"\n")

name="09. vWii common key"
fi = open(targetfol+name+".bin", "wb")
fi.write(vwii_common_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(vwii_common_key).decode('utf-8')+"\n")

name="10. Wii U Common Key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_common_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_common_key).decode('utf-8')+"\n")

name="11. Unknown (03)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_03_unused)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_03_unused).decode('utf-8')+"\n")

 # 2. Wii U Bank
keytxt.write("\n	2. Wii U Bank\n")

targetfol=out2

name="01. Unknown (04)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_04_unused)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_04_unused).decode('utf-8')+"\n")

name="02. Unknown (05)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_05_unused)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_05_unused).decode('utf-8')+"\n")

name="03. Key to encrypt or decrypt SSL RSA key"
fi = open(targetfol+name+".bin", "wb")
fi.write(encrypt_decrypt_ssl_rsa_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(encrypt_decrypt_ssl_rsa_key).decode('utf-8')+"\n")

name="04. Key to encrypt seeds for USB storage keys"
fi = open(targetfol+name+".bin", "wb")
fi.write(usb_storage_key_seed_encryption_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(usb_storage_key_seed_encryption_key).decode('utf-8')+"\n")

name="05. Unknown (06)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_06)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_06).decode('utf-8')+"\n")

name="06. Wii U XOR key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_xor_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_xor_key).decode('utf-8')+"\n")

name="07. Wii U RNG key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_rng_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_rng_key).decode('utf-8')+"\n")

name="08. Wii U SLC (NAND) key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_slc_nand_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_slc_nand_key).decode('utf-8')+"\n")

 # 3. Wii U Bank
keytxt.write("\n	3. Wii U Bank\n")

targetfol=out3

name="01. Wii U MLC (eMMC) key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_mlc_emmc_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_mlc_emmc_key).decode('utf-8')+"\n")

name="02.  Key to encrypt and decrypt SHDD key"
fi = open(targetfol+name+".bin", "wb")
fi.write(encrypt_decrypt_shdd_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(encrypt_decrypt_shdd_key).decode('utf-8')+"\n")

name="03. Key to encrypt DRH WLAN data"
fi = open(targetfol+name+".bin", "wb")
fi.write(encryption_key_for_drh_wlan_data)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(encryption_key_for_drh_wlan_data).decode('utf-8')+"\n")

name="04. Unknown (07)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_07_unused)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_07_unused).decode('utf-8')+"\n")

name="05. Wii U SLC (NAND) HMAC"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_slc_nand_hmac)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_slc_nand_hmac).decode('utf-8')+"\n")

name="06. Unknown (08 - Padding)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_08_padding)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_08_padding).decode('utf-8')+"\n")

 # 4. Wii U Bank
keytxt.write("\n	4. Wii U Bank\n")

targetfol=out4

name="01. Unknown (09)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_09_unused)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_09_unused).decode('utf-8')+"\n")

name="02. Unknown (10)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_10_unused)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_10_unused).decode('utf-8')+"\n")

name="03. Wii U NG ID"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_ng_id)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_ng_id).decode('utf-8')+"\n")

name="04. Wii U NG Private Key"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_ng_private_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_ng_private_key).decode('utf-8')+"\n")

name="05. Wii U private key for NSS device certificate"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_private_nss_device_cert_key)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_private_nss_device_cert_key).decode('utf-8')+"\n")

name="06. Wii U RNG seed (only the first 0x04 bytes are used)"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_otp_rng_seed)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_otp_rng_seed).decode('utf-8')+"\n")

name="07. Unknown (12)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_12_unused)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_12_unused).decode('utf-8')+"\n")

# 5. Wii U Bank
keytxt.write("\n	5. Wii U Bank\n")

targetfol=out5

name="01. Wii U root certificate MS ID"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_root_cert_ms_id_0x00000012)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_root_cert_ms_id_0x00000012).decode('utf-8')+"\n")

name="02. Wii U root certificate CA ID"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_root_cert_ca_id_0x00000003)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_root_cert_ca_id_0x00000003).decode('utf-8')+"\n")

name="03.  Wii U root certificate NG key ID"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_root_cert_ng_key_id)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_root_cert_ng_key_id).decode('utf-8')+"\n")

name="04. Wii U root certificate NG signature"
fi = open(targetfol+name+".bin", "wb")
fi.write(wiiu_root_cert_ng_signature)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(wiiu_root_cert_ng_signature).decode('utf-8')+"\n")

name="04. Unknown (14 - Unused)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_14_unused)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_14_unused).decode('utf-8')+"\n")

name="05. Unknown (locked out by boot1)"
fi = open(targetfol+name+".bin", "wb")
fi.write(unknown_15_locked_by_boot1)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(unknown_15_locked_by_boot1).decode('utf-8')+"\n")

# 7. Misc Bank
keytxt.write("\n	7. Wii U Bank\n")

targetfol=out7

name="01. Unknown (locked by boot1)"
fi = open(targetfol+name+".bin", "wb")
fi.write(boot1_locked_unknown_01)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(boot1_locked_unknown_01).decode('utf-8')+"\n")

name="02. boot1 key (locked by boot0)"
fi = open(targetfol+name+".bin", "wb")
fi.write(boot1_key_locked_by_b0)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(boot1_key_locked_by_b0).decode('utf-8')+"\n")

name="03. Unknown (locked out by boot0, not used)"
fi = open(targetfol+name+".bin", "wb")
fi.write(boot0_locked_unused_01)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(boot0_locked_unused_01).decode('utf-8')+"\n")

name="04. Empty 1"
fi = open(targetfol+name+".bin", "wb")
fi.write(misc_empty1)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(misc_empty1).decode('utf-8')+"\n")

name="05. Empty 2"
fi = open(targetfol+name+".bin", "wb")
fi.write(misc_empty2)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(misc_empty2).decode('utf-8')+"\n")

name="06. OTP Version and Revision"
fi = open(targetfol+name+".bin", "wb")
fi.write(otp_date_code)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(otp_date_code).decode('utf-8')+"\n")

name="07. OTP Date Code"
fi = open(targetfol+name+".bin", "wb")
fi.write(otp_version_and_revision)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(otp_version_and_revision).decode('utf-8')+"\n")

name="08. OTP Version Name String"
fi = open(targetfol+name+".bin", "wb")
fi.write(otp_version_name_string)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(otp_version_name_string).decode('utf-8')+"\n")

name="09. Empty 3"
fi = open(targetfol+name+".bin", "wb")
fi.write(misc_empty3)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(misc_empty3).decode('utf-8')+"\n")

name="10. JTAG status"
fi = open(targetfol+name+".bin", "wb")
fi.write(jtag_status)
fi.close()
keytxt.write("\n"+name+": " + binascii.hexlify(jtag_status).decode('utf-8')+"\n")
#End file output