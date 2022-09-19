from discord.ext import commands
from cogs.settings import youtube_link, insta_link, discord_link, github_link, tiktok_link, twitter_link, twitch_link

class Social(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def yt(self, ctx):
        if youtube_link != '':
            await ctx.send(youtube_link)

    @commands.command()
    async def invite(self, ctx):
        if discord_link != '':
            await ctx.send(discord_link)

    @commands.command()
    async def github(self, ctx):
        if github_link != '':
            await ctx.send(github_link)

    @commands.command()
    async def insta(self, ctx):
        if insta_link != '':
            await ctx.send(insta_link)

    @commands.command()
    async def tiktok(self, ctx):
        if tiktok_link != '':
            await ctx.send(tiktok_link)

    @commands.command()
    async def twitter(self, ctx):
        if tiktok_link != '':
            await ctx.send(twitter_link)

    @commands.command()
    async def twitch(self, ctx):
        if twitch_link != '':
            await ctx.send(twitch_link)



def setup(client):
    client.add_cog(Social(client))
    print('Social cog loaded')
