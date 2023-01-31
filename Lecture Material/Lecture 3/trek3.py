captains = [
    {"name": "Picard","Series" : "The next Generation", "Ship": "Enterprise D" },
    {"name":"Riker","Series"  : "The next Generation", "Ship": "Titan"},
    {"name":"Janeway","Series": "Voyager", "Ship": "Voyager"},
    {"name":"Kirk","Series":    "The Original Series","Ship": "Enterprise A" },
    {"name":"Sisko", "Series":   "Deep Space Nine", "Ship": "Defiant"},
]

for captain in captains:
    print(captain["name"], captain["Series"], captain["Ship"], sep = ", ")