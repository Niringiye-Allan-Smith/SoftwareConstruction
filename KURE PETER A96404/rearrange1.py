import re
def rearrange_name(name):
    result = re.search(r"^([\w .]*),([\w .]*)$")
    if result == None:
        return name
    return "{}{}".format(result[2], result[1])