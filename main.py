import re
count = 0
software =[]
lines = 0

pattern = re.compile("software", re.IGNORECASE)
with open("D:\project.txt","rt") as file_info:
    for file_line in file_info:
        lines+=1
        if pattern.search(file_line)!=None:
            software.append((lines,file_line.rstrip('\n')))
    for answer in software:
        count+=1
        with open("software.txt","a") as file_answer:
            file_answer.writelines(str(count)+" :")
            file_answer.writelines(answer[1]+'\n')

