import discord
from discord.ext import commands
import cogs.utils
from cogs.settings import voice_channel_id, voice_role_name, use_voice_role, use_user_voice, voice_category_name

# TODO send join and leave messages into voice threads


class Voice(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        voice_role = discord.utils.get(member.guild.roles, name=voice_role_name)
        if member.bot:
            return

        if not before.channel:
            if use_voice_role:
                await member.add_roles(voice_role)
            print(f'{member.name} hat den channel betreten')

        if before.channel and not after.channel:
            if use_voice_role:
                await member.remove_roles(voice_role)
            print(f'{member.name} hat den channel verlassen')

        if use_user_voice:
            if after.channel is not None:
                if after.channel.id == voice_channel_id:
                    channel = await cogs.utils.create_voice_channel(after.channel.guild,
                                                                    f'{member.name}s Talk')
                    if channel is not None:
                        await member.move_to(channel)

            if before.channel is not None:
                if before.channel.category.id == cogs.utils.get_category_by_name(before.channel.guild, voice_category_name).id:
                    print(before.channel.id)
                    if len(before.channel.members) == 0 and before.channel.id != voice_channel_id:
                        await before.channel.delete()


def setup(client):
    client.add_cog(Voice(client))
    print('Voice cog loaded')
