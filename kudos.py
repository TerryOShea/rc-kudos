import zulip
import time
import re

client = zulip.Client(config_file=".zuliprc")

def kudos_handler(messages):
    for message in messages:
        recipients, message_body, is_anonymous, is_private = process_md_message(message['content'])
        for recipient in recipients:
            personal_message = message_body
            # Add a Congratulations at the beginning and tag the person
            personal_message = f":congratulations: Contragulations @**{recipient}**, you received a **Kudo**\n\n" + personal_message

            # Add the from at the end
            if not is_anonymous:
                personal_message = personal_message + f"\n\nfrom {message['sender_full_name']}"

            print(f"\nMessage {message_body} was sent to {recipient}")
            send_kudo(recipient, personal_message, is_private)

    mark_read([message['id'] for message in messages])


def send_kudo(recipient, message_body, is_private):
    if not is_private:
        request = {
            "type": "stream",
            "to": "kudos",
            "subject": recipient,
            "content": message_body,
        }
    else:
        request = {
            "type": "private",
            "to": recipient, # FIXME this fails because we do not have the email
            "content": message_body,
        }

    result = client.send_message(request)


def get_messages():
    request = {
        "use_first_unread_anchor": True,
        "num_before": 0,
        "num_after": 8,
        "apply_markdown": False,
        "narrow": [{"operator": "is", "operand": "mentioned"}],
    }

    result = client.get_messages(request)

    if result['found_newest'] and result['messages']:
        kudos_handler(result['messages'])


def process_md_message(message):
    is_anonymous = False
    is_private = False

    # Get all the mentions
    # @**name of the person**
    mentions = re.findall('(@\*\*(.*?)\*\*)', message)

    # Clean up the message removing the mentions
    for md_mention, mention in mentions:
        message = message.replace(md_mention, '')

    # is_anonymous
    if message.find('--anon') >= 0:
        message = message.replace('--anon', '')
        is_anonymous = True

    if message.find('--private') >= 0:
        message = message.replace('--private', '')
        is_private = True

    # Remove extra whitespaces from mentions or any other place
    message.strip()

    # Filter the mention to the bot
    mentions = [mention for md_mention, mention in mentions if mention != 'Test-Kudos']

    # return the recipients and message
    return (mentions, message, is_anonymous, is_private)


def mark_read(message_ids):
    if message_ids:
        request = {
            'messages': message_ids,
            'op': 'add',
            'flag': 'read'
        }

        result = client.update_message_flags(request)

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
