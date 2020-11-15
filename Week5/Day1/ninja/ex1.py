class Phone:
    def __init__(self, number):
        self.number = number
        self.call_history = []
        self.messages = []
    def call(self, other_phone):
        self.call_history.append(other_phone)
    def show_call_history(self):
        print(f"Your recent calls are{self.call_history}")
    def send_message(self, to, sender, content):
        message = {"to":to,
        "sender": sender,
        "content": content}
    # def show_outgoing_messages(self):
    #     print(self.message)

    