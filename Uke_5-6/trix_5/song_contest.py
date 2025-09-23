def les_song_contest(filnavn):
    årene = []
    landene = []

    for linje in open(filnavn):
        linje = linje.strip()
        kolonner = linje.split()
        år = kolonner[0]
        land = kolonner[1]
        årene.append(år)
        landene.append(land)
    
    song_contest = {}
    song_contest["år"] = årene
    song_contest["land"] = landene

    return song_contest
print(les_song_contest("song_contest.txt"))