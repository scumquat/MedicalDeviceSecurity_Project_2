from intelhex import IntelHex

ih = IntelHex("leo_firmware.hex")
ih.tobinfile("leo_firmware.bin")
print("Converted to binary!")