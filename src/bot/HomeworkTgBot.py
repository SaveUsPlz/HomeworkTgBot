import telebot


class HomeworkTgBot:

    def __init__(self) -> None:
        self.bot = telebot.TeleBot('1339112927:AAFO2IsDIdjUYSXU4I_T8hEOneu5mOiL9YM')

        @self.bot.message_handler(commands=["start"])
        def _process_command_start(message):
            self.start_message(message)
        super().__init__()

    def start_message(self, message):
        self.bot.send_message(message.chat.id, 'Привет')

    def start(self):
        self.bot.polling()
