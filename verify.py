from logging import error
import discord
from discord.ext import tasks
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import random


import os
intents = discord.Intents(messages=True, guilds=True, members=True)


client = commands.Bot(command_prefix='--', intents=intents,status=discord.Status.dnd)

dudey = random.randrange(10000,200000)
channel = client.get_channel(881574176392097832)



@client.event
async def on_member_join(member):
    ema = discord.Embed(title=f"Welcome {member.name} To Your Server Name",description=f"""Before Entering The Code Please Read rules First
    **Your Code: {dudey}**""",colour=discord.Color(random.randint(0x000000, 0xFFFFFF)))
    ema.add_field(name="Invite Rewards",value="""There are no invite rewards as the server is on maintainance""",inline=False)
    ema.add_field(name="Available Services",value="""Server Is Under Maintainance""",inline=False)
    ema.set_footer(text=f"{member.id}",icon_url=member.avatar_url)
    ema.set_thumbnail(url='thumbnailurl')
    rolie = member.guild.get_role(881576796578017350)
    await member.add_roles(rolie,reason=None)
    cannel = client.get_channel(881574176392097832)
    await cannel.send(f"{member.mention} type the code given in your dm you can get the code again by typing ``resend``",delete_after=15)
    try:
        await member.send(embed=ema)
        await member.send("Invite Your Friends!")
    except discord.Forbidden:
        channel = client.get_channel(881574176392097832)
        await channel.send("I can't seem to dm you Maybe Your dms are closed, type ``resend`` if you have your dms unlocked now",delete_after=15)


@client.event
async def on_message(message):
    member = message.author
    if message.author.bot:
        return
    
    if message.channel.id == 881574176392097832:
        if "resend" in message.content:
            await message.delete()
            await member.send(f"This is your code: {dudey} ")


    if str(dudey) in message.content:
        await message.delete()
        
        ger = member.guild.get_role(881574216468676639)
        rlie = member.guild.get_role(881576796578017350)
        await member.add_roles(ger,reason=None)
        await member.remove_roles(rlie,reason=None)

        embed = discord.Embed(color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embed.add_field(name=f"𝙎𝙚𝙧𝙫𝙚𝙧 𝙍𝙪𝙡𝙚𝙨",value="Bot is under maintainance ")
        embed.add_field(name=f"𝙎𝙚𝙧𝙫𝙚𝙧 𝙐𝙥𝙙𝙖𝙩𝙚𝙨",value="Bot is under maintainance ")
        embed.set_author(icon_url=member.avatar_url,name=f"{member.name}#{member.discriminator} 𝙔𝙤𝙪 𝘼𝙧𝙚 𝙉𝙤𝙬 𝙑𝙚𝙧𝙞𝙛𝙞𝙚𝙙")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Member ID: {member.id}")
        channel = client.get_channel(881573119003873291)
        await channel.send(member.mention)
        await channel.send(embed=embed)
        return
    else:    
        if message.channel.id == 881574176392097832:
            await message.delete()
            await message.channel.send("The Code Seems to be incorrect",delete_after=2)


client.run("Your Token")
