import json
out = []

with open("DevDiscord.txt", 'r') as file:
    arr = file.readlines()
    for i in range(len(arr)):
        if arr[i].startswith('#') or arr[i].startswith("| Name") or arr[i].startswith("| -") or arr[i].startswith('\n'):
            continue
        out.append(arr[i])


to_return = []
for i in out:
    temp = i.split("|")

    def format_link(link):
        link = link.split("(")
        return link[1].replace(")", "")
    a = {
        "name": temp[1].strip(" "),
        "link": format_link(temp[2].strip(" ")),
        "description": temp[3].strip(" ")
    }
    to_return.append(a)

with open('out.json', 'w') as out_file:
    json.dump(to_return, out_file)
