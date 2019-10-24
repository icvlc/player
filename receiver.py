from serial import Serial
from gtts import gTTS
from winmm import play

port = 'COM3'
ser = Serial(port, timeout=0.5)
buf = b''

while True:
  data = ser.read()
  if not data:
    continue

  print(f'\rbuffer: {str(buf).ljust(80)}', end='')

  if data == b'\n':
    msg = buf.decode()
    tts = gTTS(text=msg, lang='ko')
    tts.save('out.mp3')
    play('out.mp3')
    buf = b''
  elif data != b'\r':
    buf += data
