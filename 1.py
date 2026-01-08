import struct
import os
from ctypes import *

GENERIC_READ          = 0x80000000
GENERIC_WRITE         = 0x40000000
OPEN_EXISTING         = 0x00000003
FILE_ATTRIBUTE_NORMAL = 0x00000080

NULL = None

def main():

  kernel32 = windll.kernel32
  hHEVD = kernel32.CreateFileA(b"\\\\.\\HackSysExtremeVulnerableDriver",
                               (GENERIC_READ | GENERIC_WRITE),
                               0x00,
                               NULL,
                               OPEN_EXISTING,
                               FILE_ATTRIBUTE_NORMAL,
                               NULL)
  if (hHEVD == -1):
    print("[-] Failed to get a handle on HackSysExtremeVulnerableDriver\n")
    exit(-1)

  buffer = "wetw0rk"

  print("[*] Calling control code 0x222003")
  kernel32.DeviceIoControl(hHEVD,
                           0x222003,
                           buffer,
                           len(buffer),
                           NULL,
                           0x00,
                           byref(c_ulong()),
                           NULL)

main()
