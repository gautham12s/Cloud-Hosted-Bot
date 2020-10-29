import discord
from discord.ext import commands

r = input("Enter Todays Day Order")










dyorder = {1:"9-10(Physics),11-12(Maths),2-330(Maths)",2:"9-1040(English),12-1(Physics),1-2(Maths),2-330(Physics Lab)",3:"11-12(Eng),1-2(EEE),2-330(EG Lab)",4:"9-1040(EEE),1-2(Physics),2-330(EEE Lab)",5:"9-1040(EG),11-12(EEE),1-2(Eng),2-330(Yoga)",6:"9-1040(Prof Skills),230-330(COI)"}

client = commands.Bot(command_prefix="!>")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def dayorder(ctx):
    await ctx.send(r)

@client.command()
async def dy1(ctx):
    await ctx.send(dyorder[1])
@client.command()
async def dy2(ctx):
    await ctx.send(dyorder[2])
@client.command()
async def dy3(ctx):
    await ctx.send(dyorder[3])
@client.command()
async def dy4(ctx):
    await ctx.send(dyorder[4])
@client.command()
async def dy5(ctx):
    await ctx.send(dyorder[5])
@client.command()
async def dy6(ctx):
    await ctx.send(dyorder[6])


client.run("NzcwNTAzMDYxNDk1MzQ5MjUw.X5eg5Q.LUzGTc_MF01r5ipDAndCijUCkyI")
