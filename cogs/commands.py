import discord
from discord.ext import commands
import platform

import cogs._json

class Commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Commands Cog has been loaded\n-----")

    @commands.command()
    async def stats(self, ctx):
        """
        A usefull command that displays bot statistics.
        """
        version_of_python = platform.python_version()
        dpy_version = discord.__version__
        server_count = len(self.bot.guilds)
        member_count = len(set(self.bot.get_all_members()))

        embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='\uFEFF', colour=ctx.author.colour, timestamp=ctx.message.created_at)


        embed.add_field(name='Python Version:', value = version_of_python)
        embed.add_field(name='Discord.Py Version', value=dpy_version)
        embed.add_field(name='Total Guilds:', value=str(server_count))
        embed.add_field(name='Total Users:', value=str(member_count))

        embed.set_footer(text=f"Carpe Noctem | {self.bot.user.name}")
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Commands(bot))
