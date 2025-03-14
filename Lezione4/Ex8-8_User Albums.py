def make_album(name_artist:str, title_album:str, number_songs:int = None) ->str:
    music_album:dict[str] = {"Artist": name_artist, "Album": title_album, "Number of the songs": number_songs}
    return music_album


while True:
    
    print("\nEnter an album's artist and title:")
    print("Type \"Esc\" to quit")
    risposta:str = input("Vuoi inserire il nome dell'artista e il nome dell'Album?")
    if risposta =="Si" or risposta.lower() == "si":
        art_name = input("Insert the name of the artist:")
        t_name = input("Insert the title of the album:")
    else:
        break

music_data = make_album(art_name, t_name)
print(music_data)