import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello! {get_author_name(message.author)}')
    if message.content.startswith('$help'):
        await message.channel.send(f'Hi! {get_author_name(message.author)}\n'
                                   f'Этот бот пока умеет только здаровться \n'
                                   f'Команды бота начинаются с $')


@client.event
async def on_member_join(member):
    mention = member.mention  # mention user
    guild = member.guild  # guild == server
    # await member.create_dm()
    # await member.dm_channel.send(f"welcome{guild}")
    embed = discord.Embed(
        title="***New Member***",
        colour=0x47bfbd,
        description=f"Добро пожаловать в наш маленький уголок {mention}"
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name=member.name, icon_url=member.avatar_url)
    embed.set_footer(text=guild, icon_url=guild.icon_url)

    channel = discord.utils.get(guild.channels, id=int("761583725800587291"))
    await channel.send(embed=embed)


@client.event
async def on_member_leave(member):
    guild = member.guild  # guild == server
    await member.create_dm()
    await member.dm_channel.send(f"Жаль конечно что ты ушел с {guild}")


def get_author_name(_name):
    r_name = str(_name)
    return r_name[: str(r_name).find('#')]


client.run('ODIxNjY4NjM4NDc3MjU0NjU2.YFHEjQ.Z8KPaSTldRnpRf8w-l0msSGO_os')
