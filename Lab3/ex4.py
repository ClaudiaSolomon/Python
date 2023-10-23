# 4
def build_xml_element(tag, continut, **dictionar):
    sir = "<" + tag + " "
    for pereche in dictionar.items():
        sir += pereche[0]+"=\""+pereche[1]+"\\ \" "
    sir += ">" + continut
    return sir


print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))
