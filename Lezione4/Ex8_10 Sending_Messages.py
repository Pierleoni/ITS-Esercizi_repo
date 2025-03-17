list_message:list[str] = ["Hello, World", "Hey There", "How are you?", "How do you do?"]

def send_messages(list_message:list) ->list[str]:
    sent_message = []
    while list_message:
        messaggio=list_message.pop()
        sent_message.append(messaggio)
    print(sent_message)

send_messages(list_message)






