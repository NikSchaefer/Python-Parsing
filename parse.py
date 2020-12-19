import json


def purge(string):
    return string.replace(" ", "")


def delete_lines(lines):  # returns array of lines with not essential lines removed
    return_array = []
    for i in range(len(lines)):
        if not ("|---|" in lines[i] or "API | " in lines[i] or "**[" in lines[i] or lines[i] == "\n"):
            return_array.append(lines[i].replace("\n", ""))
    return return_array


def to_categories(array):
    out = []
    content = []
    names = []
    for i in range(len(array)):
        if "###" in array[i]:
            names.append(array[i].replace("#", ""))
            to_return = {
                "name": names[len(names) - 2],
                "content": content
            }
            out.append(to_return)
            content = []
        else:
            split = array[i].split('|')
            name_split = split[1].split("]")
            link = name_split[1].replace("(", "")
            to_add = {
                "name": purge(name_split[0].replace("[", "")),
                "link": purge(link.replace(")", "")),
                "description": split[2],
                "Auth": purge(split[3]),
                'HTTPS': purge(split[4]),
            }
            content.append(to_add)
    return out[1:]


def main():
    with open('apis.txt', 'r') as f:
        lines = f.readlines()
        f.close()

    deleted = delete_lines(lines)
    out = to_categories(deleted)

    with open('target.json', 'w') as w:
        json.dump(out, w)


if __name__ == "__main__":
    main()
