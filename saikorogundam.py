from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
import gspread
import discord
import numpy as np
from parse import parse
import argparse



def dice(dice_size):
    return np.random.randint(1, int(dice_size))

def simple_dice(dice_size, dice_num):
    dice_val = np.array([], dtype=np.int64)
    for i in range(dice_num):
        dice_val = np.append(dice_val, dice(dice_size))
    msg = 'dice: ' + str(np.sum(dice_val)) + ' = ' + str(dice_val)
    return msg


client = discord.Client()
client_id = 'your id'


@client.event
async def on_ready():
    print('Logged in')
    print('-----')

@client.event
async def on_message(message):
    # 開始ワード
    if message.content.startswith('roll'):
        print('-----')
        # 送り主がBotではないか
        if client.user != message.author:
            info = parse('roll {}d{}', message.content)
            if info:
                if info[1].isdecimal() and info[0].isdecimal():
                    dice_num = int(info[0])
                    dice_size = int(info[1])

                    m = simple_dice(dice_size, dice_num)
                   
                    # メッセージが送られてきたチャンネルへメッセージを送ります
                    await message.channel.send(m)


client.run(client_id)