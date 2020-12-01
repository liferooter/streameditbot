import logging
import os
import asyncio
from shlex import split
from html import escape
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN: str = os.getenv("BOT_TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher3
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

COMMANDS = ['sed', 'grep', 'cut', 'tr', 'tail', 'head', 'uniq', 'sort', 'awk']

CMD_PREFIX = ["env", "-i", "PATH=/bin:/usr/bin", "timeout", "2"]


@dp.message_handler(regexp="||".join(COMMANDS))
async def cmd_handler(message: types.Message):
    if not message.reply_to_message:
        await message.reply("You should reply on message to process it")
        return

    cmdline = split(message.text)
    proc = await asyncio.create_subprocess_exec(*CMD_PREFIX, *cmdline,
                                                stdout=asyncio.subprocess.PIPE,
                                                stderr=asyncio.subprocess.PIPE,
                                                stdin=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate(input=message.reply_to_message.text.encode('utf-8'),)
    if stderr:
        await message.reply(f'<pre>{escape(stderr.decode("utf-8", errors="ignore"))}</pre>')
    elif stdout:
        await message.reply_to_message.reply(escape(stdout.decode("utf-8", errors="ignore")))
    else:
        await message.reply("<pre>Output is empty...</pre>")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This is a handler for `/help` and `/start` commands
    :param message:
    :return:
    """
    await message.reply("""Hi!
I am stream editor bot. I can evaluate best Unix stream processing utilities on messages.
Just add me in your group and learn how to use Unix stream editors.

<b>Usage:</b>

Reply on any message: /command <i>args</i>, where command is one of my supported commands.

Now I support: """ + ', '.join(COMMANDS))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
