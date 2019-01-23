class KudosHandler(object):
    '''
    Use this bot to give kudos to your fellow community members.
    '''

    def usage(self):
        # TODO: fill this in
        return '''[FILL THIS IN]'''

    def parse_message(self, message):
        # TODO: get sender, receiver, optional message
        # TODO: if there's receiver, error message
        return {
            'sender': 'Terry',
            'receiver': 'Michelle',
            'message': 'Great work!',
            'private': False,
        }

    def handle_message(self, message, bot_handler):
        parsed_message = self.parse_message(message)
        #bot_handler.send_reply(message, "Thanks for the message!")
        bot_handler.send_message(dict(
            type='stream',
            to='397 Bridge',
            subject='kudos',
            content=f"Congratulations to {parsed_message['receiver']}!",
        ))

handler_class = KudosHandler
