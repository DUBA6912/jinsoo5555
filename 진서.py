import asyncio
import discord

client = discord.Client()

# 복사해 둔 토큰을 your_token에 넣어줍니당
token = "NzY0MjcxMzA4NjAyMzQzNDU1.X4D1Hw.LFn0yM9yE0yigpiB388t0yojmCQ"

# 봇이 구동되었을 때 동작되는 코드
@client.event
async def on_ready():
    print("로그인 된 봇:") #화면에 봇의 아이디, 닉네임이 출력되는 코드
    print(client.user.name)
    print(client.user.id)
    print("===========")
    
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("시작하는 중...")
    await client.change_presence(status=discord.Status.online, activity=game)
    while True:
        game = discord.Game("안녕하세요? 챗봇입니다")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("아직 베타 테스트 중이예요~")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(3)
# 디스코드에는 현재 본인이 어떤 게임을 플레이하는지 보여주는 기능이 있습니다.
# 이 기능을 사용하여 봇의 상태를 간단하게 출력해줄 수 있습니다.
        


# 봇이 새로운 메시지를 수신했을때 동작되는 코드입니다.
@client.event
async def on_message(message):
    if message.author.bot: #만약 메시지를 보낸사람이 봇일 경우에는
        return None #동작하지 않고 무시합니다.

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content.startswith('!안녕'):
        channel = message.channel
        await channel.send('안녕하세요? 진서봇은 일꾼입니다!')


    if message.content.startswith('!진서'):
        channel = message.channel
        await channel.send('진서:BUG')

