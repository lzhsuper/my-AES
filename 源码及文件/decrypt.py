import base64
import sys
sys.path.append("C:\ProgramData\Anaconda3\Lib\site-packages")
from Crypto.Cipher import AES

message = sys.argv[1]
def decrypt(message):
    key = str.encode('iUeHTJbIvclcm2Fr')
    aes = AES.new(key, AES.MODE_ECB)
    unpad = lambda date: date[0:-ord(date[-1])]
    res = base64.decodebytes(message.encode("utf8"))
    msg = aes.decrypt(res).decode("utf8")
    result = unpad(msg)
    print(result)
    return result
decrypt(message)
