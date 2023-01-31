captains = {
    "Picard" : "The next Generation",
    "Riker"  : "The next Generation",
    "Janeway": "Voyager",
    "Kirk":    "The Original Series",
    "Sisko":   "Deep Space Nine",
}

# print(captains["Picard"])
# print(captains["Riker"])
# print(captains["Janeway"])
# print(captains["Kirk"])
# print(captains["Sisko"])

# for captain in captains:
#     print(captain)
    
for captain in captains:
    print(captain, captains[captain], sep=", ")