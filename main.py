import os
import discord
from discord.ext import commands
from discord.ui import Button, View

from myserver import server_on

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ฟังก์ชันเมื่อผู้ใช้กดปุ่มรับยศ
class RankView(View):
    @discord.ui.button(label="รับยศ", style=discord.ButtonStyle.green)
    async def assign_rank(self, interaction: discord.Interaction, button: Button):
        role = discord.utils.get(interaction.guild.roles, name="พลเรือน | Civilian")  # ชื่อยศที่ต้องการมอบ
        if role:
            await interaction.user.add_roles(role)
            await interaction.response.send_message(f"คุณได้รับยศ {role.name} เรียบร้อยแล้ว!", ephemeral=True)
        else:
            await interaction.response.send_message("ไม่พบยศที่ต้องการมอบ", ephemeral=True)

# คำสั่งสำหรับสร้างปุ่มรับยศ
@bot.command()
async def rank(ctx):
    view = RankView()
    await ctx.send("กดปุ่มเพื่อรับยศ!", view=view)

# เริ่มบอท

server_on()

bot.run(os.getenv('TOKEN'))
