import os
import discord
from discord.ext import commands

from myserver import server_on

# สร้าง instance ของ bot
intents = discord.Intents.default()
intents.message_content = True  # เปิดใช้งาน intent ที่จำเป็น
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="-", intents=intents)

# ฟังก์ชันเมื่อมีการส่งข้อความ
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # บอทไม่ทำงานกับข้อความของตัวเอง

    # ตรวจสอบว่าข้อความเริ่มต้นด้วย 'รับยศ'
    if message.content.startswith("รับยศ"):
        role_name = message.content[6:].strip()  # ตัดคำว่า 'รับยศ' และเก็บชื่อยศ
        guild = message.guild
        role = discord.utils.get(guild.roles, name=role_name)  # ค้นหายศตามชื่อ

        if role:
            # เพิ่มยศให้ผู้ใช้
            await message.author.add_roles(role)
            # แจ้งผู้ใช้ว่าได้รับยศแล้ว (ลบข้อความนี้ภายหลัง)
            await message.channel.send(f"คุณ {message.author.mention} ได้รับยศ {role.name} แล้ว!", delete_after=5)
        else:
            # แจ้งว่าหายศไม่พบ (ลบข้อความนี้ภายหลัง)
            await message.channel.send(f"ไม่พบยศ {role_name}", delete_after=5)

        # ลบข้อความของผู้ใช้
        await message.delete()

# เริ่มรันบอท

server_on()

bot.run(os.getenv('TOKEN'))
