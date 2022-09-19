from discord.ext import commands
import models.models as models
import discord
from cogs.settings import log_channel, embed_thumbnail, mod_role_name, verify_role_name


class Verify(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role(mod_role_name)
    async def verify(self, ctx, user: discord.Member):
        verify_role = discord.utils.get(user.guild.roles, name=verify_role_name)
        await user.add_roles(verify_role)
        await ctx.send(f'{user.mention} wurde von {ctx.author.mention} verifiziert.')
        try:
            logs = commands.get_channel(log_channel)
            await logs.send(f"{user.mention} wurde von {ctx.author.mention} verifiziert")
        except:
            pass
        await ctx.message.add_reaction('\U00002705')
        embed = discord.Embed(
            title="Du wurdest verifiziert", color=0x00ff00)
        embed.set_thumbnail(
            url=embed_thumbnail)
        embed.add_field(name=f"Du wurdest auf {ctx.guild.name} verifiziert von:",
                        value=ctx.author.mention)
        await user.send(embed=embed)
        warn = models.Verify(
            user_id=str(user.id), mod_id=ctx.author.id)
        with models.Session() as session:
            session.add(warn)
            session.commit()


def setup(client):
    client.add_cog(Verify(client))
    print('Verify cog loaded')
