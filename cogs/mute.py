from discord.ext import commands
import models.models as models
import discord
from cogs.settings import mute_channel, log_channel, mute_role_name, embed_thumbnail, mod_role_name


class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, user: discord.Member, *, reason):
        mute_role = discord.utils.get(user.guild.roles, name=mute_role_name)
        await user.add_roles(mute_role)

        await ctx.send(f'{user.mention} wurde von {ctx.author.mention} gemuted für: {reason}')
        try:
            logs = commands.get_channel(log_channel)
            await logs.send(f"{user.mention} wurde von {ctx.author.mention} gemuted für: {reason}")
        except:
            pass
        await ctx.message.add_reaction('\U00002705')
        embed = discord.Embed(
            title="Du wurdest gemuted", color=0x00ff00)
        embed.set_thumbnail(
            url=embed_thumbnail)
        embed.add_field(name=f"Du wurdest auf {ctx.guild.name} gemuted von:",
                        value=ctx.author.mention)
        embed.add_field(name="Grund für den Mute:", value=reason)
        embed.add_field(
            name="Einspruch?", value="Ein Einspruch ist jederzeit möglich, melde dich hierfür bei einem **@sudoer** "
                                     "oder **@root**", inline=False)
        await user.send(embed=embed)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, user: discord.Member, *, reason):
        mute_role = discord.utils.get(user.guild.roles, name=mute_role_name)
        await user.remove_roles(mute_role)

        await ctx.send(f'{user.mention} wurde von {ctx.author.mention} entmuted')
        try:
            logs = commands.get_channel(log_channel)
            await logs.send(f"{user.mention} wurde von {ctx.author.mention} entmuted")
        except:
            pass
        await ctx.message.add_reaction('\U00002705')
        embed = discord.Embed(
            title="Dein Mute wurde aufgehoben!", color=0x00ff00)
        embed.set_thumbnail(
            url=embed_thumbnail)
        embed.add_field(name=f"Dein Mute auf {ctx.guild.name} wurde aufgehoben von: ",
                        value=ctx.author.mention)
        await user.send(embed=embed)


def setup(client):
    client.add_cog(Mute(client))
    print('Mute cog loaded')
