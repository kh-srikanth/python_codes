book = {}
book["srikanth"] = {
    "Name": "srikanth khandavalli",
    "Address": "16-42-10, NGO's Colony",
    "Phone": 9491419809
}
book["Mounica"] = {
    "Name": "Mounca kommu",
    "Address": "16-10, Attili",
    "Phone": 7207508522
}

import json
s = '[' + json.dumps(book) + ']'
print(s)

with open("C://Users//PC//Documents//book.json", "w") as f:
    f.write(s)