user_dict:dict[str, int] = {
    "nome": input("Inserire il Nome:"), 
    "ruolo": input("Inserire il Ruolo:").lower(), 
    "età": int(input("Inserire l'età:"))
}

match user_dict:
    case {"ruolo": "admin"}:
        print("Accesso completo a tutte le funzionalità.")
    case {"ruolo": "moderatore"}:
        print(f"Salve {user_dict['nome']}! Può gestire i contenuti ma non modificare le impostazioni.")
    case {"ruolo": "utente", "età": age} if age >= 18:
        print("Accesso standard a tutti i servizi.")
    case {"ruolo": "utente", "età": age} if age < 18:
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case {"ruolo": "ospite"}:
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Ruolo non riconosciuto! Accesso Negato!")

