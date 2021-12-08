import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!')
client.remove_command('help')

# Words
hello_words = ['привет', 'hi', 'здарова', 'hello']
bad_words = ['Фрост тварь', 'быть Фростом не круто',
             'ты не крутой Фрост', 'Фросты твари!'
            ]


@client.event
async def on_ready():
    print('Я родился')


@client.event
async def on_member_join(member):
    channel = client.get_channel(773937441727316001)
    role = discord.utils.get(member.guilds.roles, id=774268671550816256)
    await member.add_roles(role)
    await channel.send('работает')

# !hello


@client.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Привет от Фроста){author}')

# !echo


@client.command()
async def echo(ctx, *, message):
    await ctx.send(message)

# !clear Чистка чата


@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount+1)

# !kick кик игрока


@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason='Гнев Фроста'):
    await ctx.channel.purge(limit=1)

    await member.kick(reason=reason)
    await ctx.send(f'Бог в гневе и выкинул с олимпа { member.mention }')

# !ban Бан игрока


@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member: discord.Member, *, reason='Наверное ты и сам догадываешься'):
    await ctx.channel.purge(limit=1)

    await member.ban(reason=reason)
    await ctx.send(f'Фрост сегодня злой,он забанил{ member.mention }')

# !unban разбанить игрока


@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    await ctx.channel.purge(limit=1)
    banned_users = await ctx.guild.bans()
    for ban_entry in banned_users:
        user = ban_entry.user
        await ctx.guild.unban(user)
        await ctx.send(f'Фрост сегодня добрый , он простил {user.mention}')
        return

# !user_mute Замутить пользователя


@client.command()
@commands.has_permissions(administrator=True)
async def user_mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='холоп(mute)')
    await member.add_roles(mute_role)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='Царь')
    await member.remove_roles(mute_role)
    await ctx.send(f'Фрост забрал право голоса у {member.mention}')

# !user_unmute Замутить пользователя


@client.command()
@commands.has_permissions(administrator=True)
async def user_unmute(ctx, member: discord.Member):
    await ctx.channel.purge(limit=1)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='Царь')
    await member.add_roles(mute_role)
    mute_role = discord.utils.get(ctx.message.guild.roles, name='холоп(mute)')
    await member.remove_roles(mute_role)
    await ctx.send(f'Фрост вернул право голоса {member.mention}')

# !help Список команд


@client.command()
async def help(ctx):
    await ctx.send('Команды бота:\n'
                   '!hello - Поздороваться с ботом\n'
                   '!echo - эхо\n'
                   '!clear [количество сообщений+1] - Стереть сообщения\n'
                   '!kick - Кикнуть кого-либо (Использование только Администраторами)\n'
                   '!ban - Забанить кого-либо (Использование только Администраторами)\n'
                   '!unban - Разбанить кого-либо (Использование только Администраторами)\n'
                   '!user_mute - Замутить кого-либо (Использование только Администраторами)\n'
                   '!user_unmute - Размутить кого-либо (Использование только Администраторами)\n'


# Connect

token = open('token.txt', 'r').readline()

client.run(token)


# @client.event


# async def on_message( message ):
# msg = message.content.lower()
# if msg in hello_words:
# await message.channel.send( 'Здравствуй' )
