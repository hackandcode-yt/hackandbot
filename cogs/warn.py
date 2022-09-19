from discord.ext import commands
import models.models as models
import discord
from cogs.settings import warn_channel, log_channel, embed_thumbnail, mod_role_name


class Warn(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, user: discord.Member, *, reason):
        await ctx.send(f'{user.mention} wurde von {ctx.author.mention} verwarnt für: {reason}')
        try:
            logs = commands.get_channel(log_channel)
            warn = commands.get_channel(warn_channel)
            await logs.send(f"{user.mention} wurde von {ctx.author.mention} verwarnt für: {reason}")
            await warn.send(f"{user.mention} wurde von {ctx.author.mention} verwarnt für: {reason}")
        except:
            pass
        await ctx.message.add_reaction('\U00002705')
        embed = discord.Embed(
            title="Du wurdest verwarnt", color=0x00ff00)
        embed.set_thumbnail(
            url=embed_thumbnail)
        embed.add_field(name=f"Du wurdest auf {ctx.guild.name} verwarnt von:",
                        value=ctx.author.mention)
        embed.add_field(name="Grund der Verwarnung:", value=reason)
        embed.add_field(
            name="Einspruch?", value="Ein Einspruch ist jederzeit möglich, melde dich hierfür bei einem **@sudoer** "
                                     "oder **@root**", inline=False)
        await user.send(embed=embed)
        warn = models.Warn(
            user_id=str(user.id), mod_id=ctx.author.id, reason=reason)
        with models.Session() as session:
            session.add(warn)
            session.commit()


def setup(client):
    client.add_cog(Warn(client))
    print('Warn cog loaded')
