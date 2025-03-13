# Dichiaro la lista fuori dalla funzione
list_message:list[str] = ["Hello, World", "Hey There", "How are you?", "How do you do?"]

# dichiaro la funzione show_message() e definisco il parametro posizionale message
def show_messages(message:list) ->None:
    # Uso un ciclo for per cui per ogni elemento presente nella lista message, dichiaro la variabile msg che punta a una stringa formattata dpve vengono presi i singoli elementi della lista message
    for elem in message:
        msg= f" The list contains this elements: {elem}"
        # stampo in output la variabile msg
        print(msg)
    

# chiamo la funzione show_message() e gli passo come argomento la lista list_message
show_messages(list_message)


