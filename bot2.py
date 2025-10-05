from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

WELCOME_MESSAGE = "🌩 NUMBER VIP HACK  🌩\n\n07 Club Annie vip TEAM\n\n⚡️NEW  UPDATED  𝗩𝗘𝗥𝗦𝗜𝗢𝗡  ⚡️\n\n🎉 𝗛𝗼𝘄 𝗧𝗼 𝗨𝘀𝗲 :- \n\n✅ 𝗖𝗿𝗲𝗮𝘁𝗲 𝗔 𝗡𝗲𝘄 𝗔𝗰𝗰𝗼𝘂𝗻𝘁.\n✅ 𝗗𝗲𝗽𝗼𝘀𝗶𝘁 𝗠𝗼𝗻𝗲𝘆 200 /-  💲\n✅ 𝗨𝘀𝗲 𝗛𝗮𝗰𝗸 𝗔𝗻𝗱 𝗘𝗮𝗿𝗻. 😎👍\n       \n\n🎉  𝐇𝐀𝐂𝐊 𝐔𝐏𝐃𝐀𝐓𝐄𝐃 🤯\n\n📈💥 99% UNDER 3 LEVEL 💥📈\n    \nhttps://07club2.com/#/register?invitationCode=56565100020\n\nVip Group link :\n\nhttps://t.me/+chFrKxwDAthmZDRl"

async def handle_join_request(update, context):
    u = update.chat_join_request.from_user
    c = update.chat_join_request.chat
    try:
        await context.bot.approve_chat_join_request(c.id, u.id)
        await context.bot.send_message(u.id, f"Hello Darling ❤️ {u.first_name or 'Friend'} and welcome to Annie's Channel!")
        if os.path.exists("ANNIE SURESHOT VIP_1.1.apk"):
            await context.bot.send_document(u.id, open("ANNIE SURESHOT VIP_1.1.apk", 'rb'), caption=WELCOME_MESSAGE)
        else:
            await context.bot.send_message(u.id, WELCOME_MESSAGE)
    except:
        pass

# Initialize Telegram bot
app = ApplicationBuilder().token(os.getenv('BOT_TOKEN')).build()
app.add_handler(ChatJoinRequestHandler(handle_join_request))

# Start Telegram bot
if __name__ == '__main__':
    app.run_polling()
