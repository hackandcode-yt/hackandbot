from discord.ext import commands


async def create_voice_channel(guild, channel_name, user_limit=None):
    await guild.create_voice_channel(
        channel_name, category=get_category_by_name(guild, "Voice"), user_limit=user_limit)
    return get_channel_by_name(guild, channel_name)


def get_channel_by_name(guild, channel_name):
    channel = None
    for c in guild.channels:
        if c.name == channel_name:
            channel = c
            break
    return channel


def get_category_by_name(guild, category_name):
    category = None
    for c in guild.categories:
        if c.name == category_name:
            category = c
            break
    return category
