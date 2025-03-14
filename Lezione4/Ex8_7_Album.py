def make_album(name_artist:str, title_album:str, number_songs:int = None) ->str:
    music_album:dict[str] = {"Artist": name_artist, "Album": title_album, "Number of the songs": number_songs}
    return music_album

music_data = make_album("Motorhead", "Ace of spades")
print(music_data)

music_data = make_album("Iron Maiden", "The number of the beast")
print(music_data)

music_data = make_album("Leftover Crack", "Fuck World Trade")
print(music_data)

music_data = make_album("Choking Victim", "No Gods/No Managers", 14 )
print(music_data)
