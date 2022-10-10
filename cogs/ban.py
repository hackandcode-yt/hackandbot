from discord.ext import commands
import models.models as models
import discord
from cogs.settings import log_channel, embed_thumbnail, mod_role_name


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *, reason):
        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f'{user.mention} wurde von {ctx.author.mention} gebannt für: {reason}')
        try:
            logs = commands.get_channel(log_channel)
            await logs.send(f"{user.mention} wurde von {ctx.author.mention} gebannt für: {reason}")
        except:
            pass
        await ctx.message.add_reaction('\U00002705')
        embed = discord.Embed(
            title="Du wurdest gebannt", color=0x00ff00)
        embed.set_thumbnail(
            url=embed_thumbnail)
        embed.add_field(name=f"Du wurdest auf {ctx.guild.name} gebannt von:",
                        value=ctx.author.mention)
        embed.add_field(name="Grund für den Ban:", value=reason)
        await user.send(embed=embed)
        ban = models.Ban(
            user_id=str(user.id), reporter_id=ctx.author.id, reason=reason)
        with models.Session() as session:
            session.add(ban)
            session.commit()


def setup(client):
    client.add_cog(Ban(client))
    print('Fun cog loaded')
