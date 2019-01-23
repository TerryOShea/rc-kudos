import zulip
import time

client = zulip.Client(config_file=".zuliprc")



def send_kudo():
    # TODO: verify against list of users and handles
    # TODO: pull info from parameters: recipient, public/private/anonymous
    request = {
        "type": "stream",
        "to": "kudos",
        "subject": "Terry O'Shea",
        "content": "Great work today, terrykoshea@gmail.com!",
    }
    result = client.send_message(request)
    print(result)

def get_messages():
    request = {
        "use_first_unread_anchor": True,
        "num_before": 0,
        "num_after": 8,
        "narrow": [{"operator": "is", "operand": "mentioned"}],
    }
    result = client.get_messages(request)
    if result['found_newest']:
        for message in result['messages']:
            process_message(message)
        mark_read([message['id'] for message in result['messages']])

def process_message(messages):
    # TODO Get the format and send_kudo
    print('The message: ')
    print(message)
    # Find the user mentioned, probably with soup search for the second span with class="user-mention"

    # Get the kudo message, stripping the mentions and the flag inside the paragraph

    # Get the anonymous flag '--anonymous'


def mark_read(message_ids):
    if message_ids:
        request = {
            'messages': message_ids,
            'op': 'add',
            'flag': 'read'
        }
        result = client.update_message_flags(request)
        print('Marked as read? ')
        print(result)


"""
    SAMPLE MESSAGE RESULT:
    {
        'found_oldest': True, 
        'found_newest': True, 
        'msg': '', 
        'result': 'success', 
        'history_limited': False, 
        'anchor': 156721588, 
        'messages': [{
            'subject': 'hello', 
            'sender_id': 198461, 
            'type': 'stream', 
            'timestamp': 1548274892, 
            'flags': ['mentioned'], 
            'display_recipient': 'kudos', 
            'reactions': [], 
            'subject_links': [], 
            'recipient_id': 289417, 
            'content': '<p><span class="user-mention" data-user-id="200653">@Test-Kudos</span> iws thiasdfas</p>', 
            'sender_full_name': "Michelle Torres (W2'19)", 
            'sender_realm_str': 'recurse', 
            'sender_email': 'hola@michelletorres.mx', 
            'id': 156721588, 
            'is_me_message': False, 
            'stream_id': 182659, 
            'avatar_url': 'https://secure.gravatar.com/avatar/ab772058030721ef1c85f4d7692609dc?d=identicon&version=1', 
            'sender_short_name': 'hola', 
            'client': 'website', 
            'submessages': [], 
            'content_type': 'text/html'
        }], 
        'found_anchor': True
    }
"""


if __name__ == "__main__":
    while True:
        get_messages()
        time.sleep(5)
