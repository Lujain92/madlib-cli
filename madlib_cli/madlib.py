import re
def read_template(f):
    with open(f) as file:
        content=file.read()
        return content


def parse_template(file):
    empty_content=re.sub(r"\{.*?\}","{}",file)
    res=re.findall(r"\{.*?\}",file)
    new_list=[]
    for x in res :
        y=x[1:-1]
        new_list.append(y)
    return(empty_content,tuple(new_list))
    
    



    

def merge(content,value):
    x=content.format(*value)
    with open("assets/dark_and_stormy_night_template_copy.txt","wt") as f2:
        f2.write(x)
    return x    



