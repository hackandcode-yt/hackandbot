from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def bring(self, ctx, type: str):
        if type == 'coffee':
            await ctx.send(f'here is your coffee {ctx.author.mention}! \U00002615')
        elif type == 'tea':
            await ctx.send(f'here is your tea {ctx.author.mention}! \U0001F375')
        elif type == 'water':
            await ctx.send(f'here is your water {ctx.author.mention}! \U0001F4A6')
        elif type == 'mate':
            await ctx.send(f'here is your mate {ctx.author.mention}! \U0001F9C9')
        else:
            await ctx.send(f'{ctx.author.mention} you have to choose between coffee, tea, water and mate')
        await ctx.message.add_reaction('\U00002705')


def setup(client):
    client.add_cog(Fun(client))
    print('Fun cog loaded')
