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
        process_messages(result['messages'])

def process_messages(messages):
    for message in messages:
        # TODO Get the format and send_kudo
        print('The message: ')
        print(message)

    mark_read([message['id'] for message in messages])

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

if __name__ == "__main__":
    while True:
        get_messages()
        time.sleep(5)
