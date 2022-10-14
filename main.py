# A program what will read midi file and converts it to a list of frequencies and duration.
import mido

# Open the midi file
mid = mido.MidiFile('music.mid')

# Edit this value to shift the pitch of the song.
# 1 means shift one key up, -1 means shift one key down.
# While 12 means shift one octave up, -12 means shift one octave down.
key = 12

freq_final = ""
delay_final = ""

for msg in mid:
    if not msg.is_meta and msg.type == 'note_on' and msg.velocity == 0:
        delay = round(msg.time*1000)
        delay_final = f"{delay_final}{delay}, "

for msg in mid:
    if not msg.is_meta and msg.type == 'note_on' and msg.velocity != 0:
        freq = round(440 * 2**((msg.note + key - 69)/12))
        freq_final = f"{freq_final}{freq}, "

print(delay_final)
print(freq_final)