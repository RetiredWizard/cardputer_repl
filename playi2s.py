# 
# Files that have been converted as follows have been tested
# Other formats may work.....
#

"""Audio Format                          : PCM
Format settings                          : Little / Signed
Codec ID                                 : 1
Duration                                 : 4 min 5 s
Bit rate mode                            : Constant
Bit rate                                 : 128 kb/s
Channel(s)                               : 1 channel
Sampling rate                            : 8 000 Hz
Bit depth                                : 16 bits
Stream size                              : 3.75 MiB (100%)
"""


import board
try:
    import bitbangio
except:
    import busio as bitbangio
try:
    import adafruit_sdcard
except:
    pass
try:
    from pydos_ui import Pydos_ui
except:
    from supervisor import runtime as Pydos_ui

import digitalio
import storage
import audiocore
import audiobusio
fname = input("Filename:")
try:
    if "SD_SCK" in dir(board):
        spi = bitbangio.SPI(board.SD_SCK,board.SD_MOSI,board.SD_MISO)
    else:
        spi = bitbangio.SPI(board.SCK,board.MOSI,board.MISO)

    if "SD_CS" in dir(board):
        cs = digitalio.DigitalInOut(board.SD_CS)
    elif "SDCARD_CS" in dir(board):
        cs = digitalio.DigitalInOut(board.SDCARD_CS)
    else:
        cs = digitalio.DigitalInOut(board.CS)

    sd = adafruit_sdcard.SDCard(spi,cs)
    vfs = storage.VfsFat(sd)
    storage.mount(vfs,'/sd')
    print('SD card mounted on /sd')
except:
    pass
f = open(fname, "rb")
wav = audiocore.WaveFile(f)
if 'I2S_BIT_CLOCK' in dir(board):
    a = audiobusio.I2SOut(board.I2S_BIT_CLOCK, board.I2S_WORD_SELECT, board.I2S_DATA)
elif 'SPEAKER_SCK' in dir(board):
    a = audiobusio.I2SOut(board.SPEAKER_SCK, board.SPEAKER_WS, board.SPEAKER_DOUT)
else:
    print('No I2S pins defined on the board')

print("Press Q to quit")
try:
    a.play(wav)
    cmnd = ""
    while cmnd.upper() != "Q":
        if Pydos_ui.serial_bytes_available():
            cmnd = Pydos_ui.read_keyboard(1)
            if cmnd in "qQ":
                break
except:
    pass
f.close()
a.deinit()
