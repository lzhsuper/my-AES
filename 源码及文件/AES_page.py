import tkinter
import sys
import base64
from Crypto.Cipher import AES
from tkinter import messagebox
import json


class EncryptDate:
    def __init__(self, key):
        self.key = str.encode(key)  # 初始化密钥
        self.length = AES.block_size  # 初始化数据块大小
        self.aes = AES.new(self.key, AES.MODE_ECB)  # 初始化AES,ECB模式的实例
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]
        # pad / unpad

    def pad(self, text):
        '''
        #填充函数，使被加密数据的字节码长度是block_size的整数倍
        '''
        count = len(text.encode('utf-8'))
        add = self.length - (count % self.length)
        entext = text + (chr(add) * add)
        return entext

    def encrypt(self, encrData):  # 加密函数
        res = self.aes.encrypt(self.pad(encrData).encode("utf8"))
        msg = str(base64.b64encode(res), encoding="utf8")
        return msg

    def decrypt(self, decrData):  # 解密函数
        res = base64.decodebytes(decrData.encode("utf8"))
        msg = self.aes.decrypt(res).decode("utf8")
        return self.unpad(msg)


def message():
    if len(entry_m.get('0.0', tkinter.END)) == 0 and len(entry_k.get()) == 0:
        messagebox.showinfo(title='error', message='请输入需解密内容！')
    elif len(entry_m.get('0.0', tkinter.END)) == 0 and len(entry_k.get()) != 0:
        messagebox.showinfo(title='error', message='请输入需解密内容！')
    elif len(entry_m.get('0.0', tkinter.END)) != 0 and len(entry_k.get()) == 0 and v.get() in (1, 2):
        messagebox.showinfo(title='error', message='请输入所需密钥！')
    elif len(entry_k.get()) not in (16, 24, 32) and v.get() in (1, 2):
        messagebox.showinfo(title='error', message='请输入16位key！')
    else:
        try:
            if v.get() == 1:
                text.delete(0.0, tkinter.END)
                message = EncryptDate(entry_k.get())
                message_result = message.encrypt(entry_m.get('0.0', tkinter.END))
                text.insert(0.0, message_result)
                result = message_result
                return result
            elif v.get() == 2:
                text.delete(0.0, tkinter.END)
                message = EncryptDate(entry_k.get())
                message_result = message.decrypt(entry_m.get('0.0', tkinter.END))
                text.insert(0.0, message_result)
                result = message_result
                return result
            elif v.get() == 3:
                text.delete(0.0, tkinter.END)
                key_old = EncryptDate('')
                key_result = key_old.decrypt('=')
                result = EncryptDate(key_result)
                message_result = result.encrypt(entry_m.get('0.0', tkinter.END))
                text.insert(0.0, message_result)
                result = message_result
                return result
            elif v.get() == 4:
                text.delete(0.0, tkinter.END)
                key_old = EncryptDate('')
                key_result = key_old.decrypt('=')
                result = EncryptDate(key_result)
                message_result = result.decrypt(entry_m.get('0.0', tkinter.END))
                text.insert(0.0, message_result)
                result = message_result
                return result
            elif v.get() == 5:
                text.delete(0.0, tkinter.END)
                key_old = EncryptDate('')
                key_result = key_old.decrypt('=')
                result = EncryptDate(key_result)
                message_result = result.encrypt(entry_m.get('0.0', tkinter.END))
                text.insert(0.0, message_result)
                result = message_result
                return result
            elif v.get() == 6:
                text.delete(0.0, tkinter.END)
                key_old = EncryptDate('')
                key_result = key_old.decrypt('=')
                result = EncryptDate(key_result)
                message_result = result.decrypt(entry_m.get('0.0', tkinter.END))
                text.insert(0.0, message_result)
                result = message_result
                return result
        except:
            messagebox.showinfo(title='error', message='请确保输入内容正确！')


def get_json():
    null = None
    result = message()
    try:
        result = eval(result)
        result = json.dumps(result, sort_keys=False, indent=2,ensure_ascii=False)
        text.delete(0.0, tkinter.END)
        text.insert(0.0, result)
    except:
        messagebox.showinfo(title='error', message='该数据不符合格式转换条件！')


def clear_key():
    entry_m.delete(1.0, tkinter.END)


def clear_text():
    text.delete(1.0, tkinter.END)


# def zhanshi():
#     if v.get() in (3, 4):
#         return tkinter.DISABLED
#     elif v.get() in (1, 2):
#         return tkinter.NORMAL
window = tkinter.Tk()
window.minsize(800, 600)
# window.maxsize(800, 600)
window.title('加解密专用程序')
cen_x = (1920 - 800) / 2
cen_y = (1080 - 600) / 2
size_xy = '%dx%d+%d+%d' % (800, 600, cen_x, cen_y)
window.geometry(size_xy)

v = tkinter.IntVar()
v.set(1)

lable = tkinter.Label(window, text='message :', width=10, height=2).place(x=-4, y=0)
lable1 = tkinter.Label(window, text='key(16 bit) :', width=10, height=2).place(x=0, y=121)
lable3 = tkinter.Label(window, text='result :', width=10, height=2).place(x=-13, y=160)

entry_m = tkinter.Text(window, bd=4, width=100, height=1.5)
entry_m.place(x=75, y=10)
entry_k = tkinter.Entry(window, bd=4, width=100)
entry_k.place(x=75, y=130)

rad = tkinter.Radiobutton(window, text='加密', variable=v, value=1)
rad.place(x=90, y=58)
rad1 = tkinter.Radiobutton(window, text='解密', variable=v, value=2)
rad1.place(x=160, y=58)
rad3 = tkinter.Radiobutton(window, text='Two b默认加密', variable=v, value=3)
rad3.place(x=230, y=58)
rad4 = tkinter.Radiobutton(window, text='Two b默认解密', variable=v, value=4)
rad4.place(x=355, y=58)
rad5 = tkinter.Radiobutton(window, text='Two c默认加密', variable=v, value=5)
rad5.place(x=90, y=90)
rad6 = tkinter.Radiobutton(window, text='Two c默认解密', variable=v, value=6)
rad6.place(x=230, y=90)

button = tkinter.Button(window, text='清空', width=15, height=1, bd=4, command=lambda: clear_key())
button.place(x=660, y=48)
button1 = tkinter.Button(window, text='确定', width=15, height=1, bd=4, command=lambda: message())
button1.place(x=500, y=48)
button2 = tkinter.Button(window, text='清空', width=10, height=1, bd=4, command=lambda: clear_text())
button2.place(x=693, y=174)
button3 = tkinter.Button(window, text='json格式', width=10, height=1, bd=4, command=lambda: get_json())
button3.place(x=693, y=234)

text = tkinter.Text(window, width=85, height=30, bd=2)
text.place(x=75, y=175)

window.mainloop()
