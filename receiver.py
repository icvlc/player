import sys

from serial import Serial
from gtts import gTTS
from winmm import play

ser = Serial('COM3', timeout=0.5)
buf = b''
msg = ''

while True:
    print(f'\rmsg: {msg.ljust(40)}', end='')
    sys.stdout.flush()

    data = ser.read()
    if not data:
        continue

    try:
        msg = buf.decode()
    except UnicodeDecodeError:
        pass

    if data == b'\n':
        try:
            msg = buf.decode()
        except UnicodeDecodeError:
            print('\nIgnoring...')
            buf = b''
            msg = ''
        else:
            print()

        tts = gTTS(text=msg, lang='ko')
        tts.save('out.mp3')
        play('out.mp3')

        buf = b''
        msg = ''
    elif data != b'\r':
        buf += data
