class KudosHandler(object):
    '''
    Use this bot to give kudos to your fellow community members.
    '''

    def usage(self):
        # TODO: fill this in
        return '''[FILL THIS IN]'''

    def handle_message(self, message, bot_handler):
        bot_handler.send_reply(message, "Thanks for the message!")

handler_class = KudosHandler
