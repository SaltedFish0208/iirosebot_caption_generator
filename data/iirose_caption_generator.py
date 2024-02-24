import requests

from loguru import logger
from API.api_message import at_user
from API.api_iirose import APIIirose  # 大部分接口都在这里
from globals.globals import GlobalVal  # 一些全局变量 now_room_id 是机器人当前所在的房间标识，websocket是ws链接，请勿更改其他参数防止出bug，也不要去监听ws，websockets库只允许一个接收流
from API.api_get_config import get_master_id  # 用于获取配置文件中主人的唯一标识
from API.decorator.command import on_command, MessageType  # 注册指令装饰器和消息类型Enmu

API = APIIirose()  # 吧class定义到变量就不会要求输入self了（虽然我都带了装饰器没有要self的 直接用APIIirose也不是不可以 习惯了

cpddapi = 'https://api.xingzhige.com/API/cp_generate/?'
chpapi = 'https://api.shadiao.pro/chp'
pyqapi = 'https://api.shadiao.pro/pyq'
djtapi = 'https://api.shadiao.pro/du'
kfcapi = 'https://api.shadiao.pro/kfc'

@on_command('>cp短打 ', True, command_type=[MessageType.room_chat, MessageType.private_chat])  # substring可输入布朗类型也可以是列表，用于取左侧的消息，第二个参数为数字类，框架会取这个数字的左侧，如果发送的消息=左侧这几个数字的消息就会执行此函数，函数需要有两个参数，第二个参数会返回去除指令的消息
async def cpdd(Message, text):
    para = text.split(" ")
    response = requests.post(f'{cpddapi}g={para[0]}&s={para[1]}').json()
    await API.send_msg(Message, f'{response["data"]["msg"]}')

@on_command('>彩虹屁', False, command_type=[MessageType.room_chat, MessageType.private_chat])  # substring可输入布朗类型也可以是列表，用于取左侧的消息，第二个参数为数字类，框架会取这个数字的左侧，如果发送的消息=左侧这几个数字的消息就会执行此函数，函数需要有两个参数，第二个参数会返回去除指令的消息
async def chp(Message):
    response = requests.get(chpapi).json()
    await API.send_msg(Message, f'{response["data"]["text"]}')

@on_command('>朋友圈文案', False, command_type=[MessageType.room_chat, MessageType.private_chat])  # substring可输入布朗类型也可以是列表，用于取左侧的消息，第二个参数为数字类，框架会取这个数字的左侧，如果发送的消息=左侧这几个数字的消息就会执行此函数，函数需要有两个参数，第二个参数会返回去除指令的消息
async def pyq(Message):
    response = requests.get(pyqapi).json()
    await API.send_msg(Message, f'{response["data"]["text"]}')

@on_command('>毒鸡汤', False, command_type=[MessageType.room_chat, MessageType.private_chat])  # substring可输入布朗类型也可以是列表，用于取左侧的消息，第二个参数为数字类，框架会取这个数字的左侧，如果发送的消息=左侧这几个数字的消息就会执行此函数，函数需要有两个参数，第二个参数会返回去除指令的消息
async def djt(Message):
    response = requests.get(djtapi).json()
    await API.send_msg(Message, f'{response["data"]["text"]}')

@on_command('>疯狂星期四', False, command_type=[MessageType.room_chat, MessageType.private_chat])  # substring可输入布朗类型也可以是列表，用于取左侧的消息，第二个参数为数字类，框架会取这个数字的左侧，如果发送的消息=左侧这几个数字的消息就会执行此函数，函数需要有两个参数，第二个参数会返回去除指令的消息
async def kfc(Message):
    response = requests.get(kfcapi).json()
    await API.send_msg(Message, f'{response["data"]["text"]}')