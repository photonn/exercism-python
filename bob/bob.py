import re
def response(hey_bob):
    answers = [
        (r"^(?![a-z])[A-Z ,.]+[\?]$","Calm down, I know what I'm doing!"),
        (r"[A-Z]+[\!]","Whoa, chill out!"),
        (r"[A-Z]+$","Whoa, chill out!"),
        (r"[\?]$|[\?][ ]+$","Sure."),
        (r"^\s+$|^$","Fine. Be that way!")
    ]
    for pattern, value in answers:
        if re.search(pattern, hey_bob):
            return value
    return "Whatever."