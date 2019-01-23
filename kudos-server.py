import zulip
import time

client = zulip.Client(config_file=".zuliprc")



"""
@app.route("/kudos")
def send_kudo():
    # TODO: get token from coffee chatters
    # TODO: verify against list of users and handles
    # TODO: pull info from parameters: recipient, public/private/anonymous
    # TODO: These are not public routes 
    request = {
        "type": "stream",
        "to": "kudos",
        "subject": "Terry O'Shea",
        "content": "Great work today, terrykoshea@gmail.com!",
    }
    result = client.send_message(request)
    print(result)
"""

def get_messages():
    request = {
        "use_first_unread_anchor": True,
        "num_before": 4,
        "num_after": 8,
        "narrow": [{"operator": "is", "operand": "mentioned"}],
    }
    result = client.get_messages(request)
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
