import logging
import os
import asyncio
from asyncio.subprocess import Process
from shlex import split
from html import escape
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN: str = os.getenv("BOT_TOKEN")
MSG_LENGTH_LIMIT = 2 ** 12
SANDBOX_USER='bot'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher3
bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

COMMANDS = ['sed', 'grep', 'cut', 'tr', 'tail', 'head', 'uniq', 'sort', 'awk']


@dp.message_handler(regexp=f'^({"|".join(COMMANDS)})')
async def cmd_handler(message: types.Message):
    if message.reply_to_message:
        input_text = message.reply_to_message.text.encode('utf-8')
    else:
        input_text = b''

    cmdline = message.text
    proc = await asyncio.create_subprocess_exec("su", SANDBOX_USER, "-c", f"/usr/src/app/sandbox.sh {cmdline}",
                                                stdout=asyncio.subprocess.PIPE,
                                                stderr=asyncio.subprocess.PIPE,
                                                stdin=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate(input_text)

    # Telegram message length limit
    if len(stdout) >= MSG_LENGTH_LIMIT:
        stdout = b"Output is too long"
    if len(stderr) >= MSG_LENGTH_LIMIT:
        stderr = b"Error is too long"

    if stderr:
        await message.reply(f'<pre>{escape(stderr.decode("utf-8", errors="ignore"))}</pre>')
    elif stdout:
        if message.reply_to_message:
            await message.reply_to_message.reply(escape(stdout.decode("utf-8", errors="ignore")))
        else:
            await message.reply(escape(stdout.decode('utf-8', errors='ignore')))
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
I am stream editor bot. I can evaluate best Unix stream processing utilities in chat.
Just add me in your group and learn how to use Unix stream editors.

<b>Usage:</b>

<i>command args</i>, where command is one of my supported commands.

Reply on any message to use it as command input.

Now I support: """ + ', '.join(COMMANDS))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
