# CreatedBy : Aswin Joseph Raj


from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram import Update
import telegram
from telegram import KeyboardButton, ReplyKeyboardMarkup

# Create a list of buttons
button_list = [
    KeyboardButton("stupid"),
    KeyboardButton("fat"),
    KeyboardButton("dumb"),
]

# Create a keyboard markup with the list of buttons
reply_markup = ReplyKeyboardMarkup(
    [button_list], resize_keyboard=True, one_time_keyboard=True)

# Send a message with the keyboard markup
# telegram.Bot.send_message(chat_id=update.message.chat_id,
#                  text="Choose a button:", reply_markup=reply_markup)

# Create a list of buttons
button_list = [
    KeyboardButton("stupid"),
    KeyboardButton("fat"),
    KeyboardButton("dumb"),
]

# Create a keyboard markup with the list of buttons
reply_markup = ReplyKeyboardMarkup(
    [button_list], resize_keyboard=True, one_time_keyboard=True)

# Send a message with the keyboard markup
# telegram.Bot.send_message(chat_id=update.message.chat_id, text="Choose a button:", reply_markup=reply_markup)


# Define a callback function to handle button clicks

def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    button = query.data

    # Send the appropriate joke based on the button clicked
    if button == "stupid":
        context.bot.send_message(
            chat_id=query.message.chat_id, text="Why did the tomato turn red? Because it saw the salad dressing!")
    elif button == "fat":
        context.bot.send_message(
            chat_id=query.message.chat_id, text="Why did the gym close down? It just didn't work out!")
    elif button == "dumb":
        context.bot.send_message(
            chat_id=query.message.chat_id, text="Why did the computer go to the doctor? Because it had a virus!")


updater = Updater(token='YOUR_TELEGRAM_BOT_TOKEN', use_context=True)

# get the dispatcher instance
dispatcher = updater.dispatcher

# Register the callback function to handle button clicks
dispatcher.add_handler(CallbackQueryHandler(button_click))


# Define a callback function to handle button clicks

def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    button = query.data

    # Send the appropriate joke based on the button clicked
    if button == "stupid":
        context.bot.send_message(
            chat_id=query.message.chat_id, text="Why did the tomato turn red? Because it saw the salad dressing!")
    elif button == "fat":
        context.bot.send_message(
            chat_id=query.message.chat_id, text="Why did the gym close down? It just didn't work out!")
    elif button == "dumb":
        context.bot.send_message(
            chat_id=query.message.chat_id, text="Why did the computer go to the doctor? Because it had a virus!")


# Register the callback function to handle button clicks
dispatcher.add_handler(CallbackQueryHandler(button_click))

# Make sure to replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
