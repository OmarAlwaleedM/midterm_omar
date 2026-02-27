# Question 8 — Mutable vs Immutable

# EXPLANATION:
# Mutable means you can change it in place. A list is mutable — you can
# add, remove, or change items inside it without creating a new list.
#
# Immutable means you cannot change it in place. A string is immutable —
# if you want to change even one character, you have to build a whole new string.
#
# Analogy: A list is like a playlist on Spotify — you can swap songs,
# remove one, or add a new one and it's still the same playlist.
# A string is like a song that's already been released — you can't change
# a lyric in it. If you want different words, you have to release a new song.

# --- Code showing the difference ---

# LIST is mutable — we can change it directly
playlist = ["Drake", "Kanye", "Travis"]
print(playlist)            # ["Drake", "Kanye", "Travis"]
playlist[1] = "Kendrick"   # swap Kanye for Kendrick, no problem
print(playlist)            # ["Drake", "Kendrick", "Travis"]
playlist.append("Future")  # add a new song at the end
print(playlist)            # ["Drake", "Kendrick", "Travis", "Future"]

# STRING is immutable — we CANNOT change it directly
song = "Hello"
print(song)        # Hello
# song[0] = "J"    # ERROR! 'str' object does not support item assignment
song = "J" + song[1:]  # have to build a brand new string
print(song)        # Jello
