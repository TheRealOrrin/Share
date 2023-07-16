family = [
    { "lineage" : "brother", "name" : "Toep", "age" : 49, "partner" : "Linda"},
    { "lineage" : "mother" , "name" : "Teep", "age" : 68, "partner" : "Tom"},
    { "lineage" : "father" , "name" : "Pap",  "age" : 76, "partner" : "Tineke" }
]

for member in family:
    print(member["lineage"], member["name"], member["age"], member["partner"], sep = ", ")