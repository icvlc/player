from serial import Serial
from gtts import gTTS
from winmm import play

ser = Serial('COM3', timeout=0.5)
buf = b''

while True:
    b = ser.read()
    if not b:
        continue
    print(f'\rbuffer: {str(buf).ljust(80)}', end='')
    if b == b'\n':
        msg = buf.decode()
        r = gTTS(text=msg, lang='ko')
        r.save('out.mp3')
        play('out.mp3')
        buf = b''
    elif b != b'\r':
        buf += b
