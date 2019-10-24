import uuid
from ctypes import c_buffer, windll

def play(path):
  def _send_command(command):
    ret_buf = c_buffer(255)
    ret_code = int(windll.winmm.mciSendStringA(command.encode('cp949'), ret_buf, 254, 0))
    if ret_code:
      err_buf = c_buffer(255)
      windll.winmm.mciGetErrorStringA(ret_code, err_buf, 254)
      raise RuntimeError(err_buf.value.decode('cp949'))
    return ret_buf.value.decode()

  alias = uuid.uuid4()
  _send_command(f'open "{path}" alias "{alias}" wait')
  _send_command(f'set "{alias}" time format milliseconds wait')
  duration = int(_send_command(f'status "{alias}" length wait'))
  _send_command(f'play "{alias}" from 0 to {duration} wait')
  _send_command(f'close "{alias}" wait')
