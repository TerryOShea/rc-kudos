from flask import Flask
import zulip
app = Flask(__name__)

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
        "narrow": [{"operator": "is:mentioned", "operand": "KudosBot"}],
    }
    result = client.get_messages(request)
    print(result)

if name == "__main__":
    get_messages()
