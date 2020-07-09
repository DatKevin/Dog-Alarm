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
    if "@dogalarm" in update.message.text:    
        message = update.message.text
        message = message.replace("@dogalarm ", "")
        username = update.message.chat.username

        # For Logging
        print("Timer Started!")
        print("Message: ", message)
        print("From: ", username)
        print(update.message)

        #Checks what numbers are available
        timer = [int(num) for num in message.split() if num.isdigit()]
        if timer:
            timer = timer[0]
            if "remind me " in message or "Remind me " in message:
                message = message.replace("remind me ", "")            
                message = message.replace("Remind me ", "")
            if "minute" in message:
                timer *= 60
            if "hour" in message:
                timer *= 3600
            print("Time: ", timer)
            update.message.reply_text(f"Okay, will remind you {message}")
            time.sleep(timer)
            update.message.reply_text(f"Hey @{username}, reminding you to {message}")
            print("Message Sent!")
        else:
            update.message.reply_text("Sorry, no time was specified")


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    # Insert Bot Token Here
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatch = updater.dispatcher

    # on different commands - answer in Telegram
    dispatch.add_handler(CommandHandler("start", start))
    dispatch.add_handler(CommandHandler("help", help_command))

    # on noncommand, activates the timer Telegram
    dispatch.add_handler(MessageHandler(Filters.text, timer))


    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
