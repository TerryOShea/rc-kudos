class MyBotHandler(object):
    '''
    Use this bot to give kudos to fellow Recurse Center community members.
    '''

    def usage(self):
        return '''[FILL THIS IN]'''

    def handle_message(self, message, bot_handler):
        # add your code here
        bot_handler.send_reply(message, "Thanks for the message!")

handler_class = MyBotHandler
