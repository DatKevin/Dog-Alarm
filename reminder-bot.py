import logging
import schedule
import time
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def timer(update, context):
    """Echo the user message."""
    #update.message.text is the input 
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    timer = []
    for n in update.message.text:
        if n in numbers:
            timer.append(n)
    if timer:
        timer = int("".join(timer))
        update.message.reply_text(f"Okay, will remind in {timer}")
        wait_time = float(timer)
        time.sleep(wait_time)
        update.message.reply_text("Here's the reminder!")
    else:
        update.message.reply_text("Sorry, no time was specified")


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("953051145:AAElkgFrnYZ01tElx-7zpvDjMHHOkaQPmvQ", use_context=True)

    # Get the dispatcher to register handlers
    dispatch = updater.dispatcher

    # on different commands - answer in Telegram
    dispatch.add_handler(CommandHandler("start", start))
    dispatch.add_handler(CommandHandler("help", help_command))

    # on noncommand, activates the timer Telegram
    #dispatch.add_handler(MessageHandler(Filters.text, echo))
    dispatch.add_handler(MessageHandler(Filters.text, timer))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
