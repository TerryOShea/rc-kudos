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

if __name__ == "__main__":
    while True:
        get_messages()
        time.sleep(5)
