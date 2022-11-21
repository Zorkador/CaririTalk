from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Uncomment the following lines to enable verbose logging
import logging
logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot('Terminal')

trainer = ListTrainer(bot)

trainer.train([
    'How are you?',
    'I am good.',
    'That is good to hear.',
    'Thank you',
    'You are welcome.',
])

print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input("Você: ")

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break