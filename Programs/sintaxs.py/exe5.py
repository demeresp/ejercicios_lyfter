total_notes = int(input("Digit the total of notes:", ))

notes = []
unapproved = []
approved = []
counter = 0

while counter < total_notes:
        note = int(input("Digit your note:",))
        notes.append(note)
        counter = counter + 1
for note in notes:
        if note < 70:
            unapproved.append(note)
        else:
            approved.append(note)

print("The total of approved notes is:", len(approved))
print("The total of non-approved notes is:", len(unapproved))

if len(approved) == 0:
    prom_approv = 0
else:prom_approv = sum(approved) / len(approved)

if len(unapproved) == 0:
    prom_unapprov = 0
else: prom_unapprov = sum(unapproved) / len(unapproved)
averag_total = sum(notes) / total_notes

print("The approval average is:", prom_approv)
print("The non-aproval average is:", prom_unapprov)
print("The total average is:", averag_total)









