from discord.ext import commands
import models.models as models
import discord
from cogs.settings import report_channel, log_channel, embed_thumbnail


class Report(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def report(self, ctx, user: discord.Member, *, reason):
        await ctx.send(f'{user.mention} wurde von {ctx.author.mention} reported für: {reason}')
        try:
            logs = commands.get_channel(log_channel)
            warn = commands.get_channel(report_channel)
            await logs.send(f"{user.mention} wurde von {ctx.author.mention} reported für: {reason}")
            await warn.send(f"{user.mention} wurde von {ctx.author.mention} reported für: {reason}")
        except:
            pass
        await ctx.message.add_reaction('\U00002705')
        embed = discord.Embed(
            title="Du wurdest reported", color=0x00ff00)
        embed.set_thumbnail(
            url=embed_thumbnail)
        embed.add_field(name=f"Du wurdest auf {ctx.guild.name} reported von:",
                        value=ctx.author.mention)
        embed.add_field(name="Grund des Reports:", value=reason)
        embed.add_field(
            name="Einspruch?",
            value="Ein Einspruch ist jederzeit möglich, melde dich hierfür bei einem **@sudoer** oder **@root**",
            inline=False)
        await user.send(embed=embed)
        report = models.Report(
            user_id=str(user.id), reporter_id=ctx.author.id, reason=reason)
        with models.Session() as session:
            session.add(report)
            session.commit()


def setup(client):
    client.add_cog(Report(client))
    print('Report cog loaded')
