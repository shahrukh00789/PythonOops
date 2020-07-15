class father:
    swimmer = True

class son(father):
    play_cricket = True
    swimmer = False

class grandson(son):
    play_videogame = True
    play_cricket = False

shahabuddin = father()
asif = son()
xavien = grandson()

print(shahabuddin.swimmer)
print(asif.swimmer)
print(asif.play_cricket)
print(xavien.swimmer)
print(xavien.play_cricket)
print(xavien.play_videogame)