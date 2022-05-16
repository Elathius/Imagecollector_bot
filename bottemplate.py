#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
from credentials import TELEAUTHKEY
import logging
import requests
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from server import API_URL



# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


##############################################################
API_URL = f'https://api.telegram.org/bot{TELEAUTHKEY}' + '/{method_name}'
##############################################################



##Exec 1
def send_local_file(file_path):
    print("exec sendlocalfile")
    f = open(file_path, 'rb')
    file_bytes = f.read()
    f.close()
    response = {
        'document': (f.name, file_bytes)
    }
    method_name = 'sendDocument'
    return sendfile(method_name, response)

##Exec 2
def sendfile(method_name, params):
    print("exec sendfile")
    if method_name == 'sendDocument':
        document = params['document']
        del params['document']
        r = requests.post(url=API_URL.format(method_name=method_name), params=params, files={'document': document})
        print("Doc detected")
        print(requests.post(url=API_URL.format(method_name=method_name), params=params, files={'document': document}))
        print(r.status_code)
    else:
        r = requests.post(url=API_URL.format(method_name=method_name), params=params)
        print("No Doc detected")
        print(r.status_code)
    return r.status_code == 200


##############################################################
def collect(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    print("exec 1")
    update.message.reply_text('Collecting your images!')
    print("exec 2")
    print(send_local_file('Ziparchx.zip'))
    print("exec 3")
##############################################################




def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(TELEAUTHKEY)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("collect", collect))
    dispatcher.add_handler(CommandHandler("sendfile", sendfile))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()