import subprocess

# avrdude_path = r"C:\Program Files (x86)\Arduino\hardware\tools\avr\bin\avrdude.exe"
# config_path = r"C:\Program Files (x86)\Arduino\hardware\tools\avr\etc\avrdude.conf"
avrdude_path = r"yourpath"
config_path =  r"yourpath"
port = "COM11"
output_file = "leo_firmware.hex"

command = [
    avrdude_path,
    "-C", config_path,
    "-c", "stk500v1",  # Changed from "avrisp"
        #-c is the programmer chip (testing device)
    "-p", "m32u4",
        #-p is part number, this is the avr microcontroller connected to programmer
        # chip of device under test
    "-P", port,
    "-b", "19200",     # Change back to 19200
    "-U", f"flash:r:{output_file}:i"
]

try:
    result = subprocess.run(command, capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    
    if result.returncode == 0:
        print(f"\nFirmware successfully extracted to {output_file}")
    else:
        print(f"\nError: Command failed with return code {result.returncode}")
        
except Exception as e:
    print(f"Error executing command: {e}")