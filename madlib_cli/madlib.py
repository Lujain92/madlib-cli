import re
#welcome function
def welcome():
    print("welcome to my mdlib")

#the file name
f="assets/make_me_a_video_game_template.txt"

#read function
def read_template(f):
    with open(f) as file:
        content=file.read()
        return content
  
file=read_template(f)

#parse function
def parse_template(file):
    empty_content=re.sub(r"\{.*?\}","{}",file)
    res=re.findall(r"\{.*?\}",file)
    new_list=[]
    for x in res :
        y=x[1:-1]
        new_list.append(y)
    return(empty_content,tuple(new_list))
    
content=parse_template(file)[0]  
value_empty=parse_template(file)[1]

#user input
def user_input():
    tuple_new=[]
    for item in value_empty:
        i=input(f"{item} : ")
        tuple_new.append(i)
    return(tuple(tuple_new))

value=user_input()

#merge function
def merge(content,value):

    x=content.format(*value)
    with open("assets/make_me_a_video_game_template_copy.txt","wt") as f2:
        f2.write(x)
    return x    




welcome()
merging_done=merge(content,value)
print(merging_done)