import re

file = open('chat.txt','r',encoding='utf-8')
input = file.readlines()

pattern=re.compile(r'^20\d\d/\d\d/\d\d')
nextfilename='yyyy-mm-dd'

end=0
top=1
for line in input:
    match = re.search(pattern, line)
    if match:
        with open('out/'+nextfilename, 'w+') as f:
            out = input[top:end]
            for item in out:
                f.write("%s"%item)
            nextfilename=match.group(0).replace('/','-')
            top=end
    end=end+1

if(top != end +1):
    with open('out/'+nextfilename, 'w+') as f:
        out = input[top:end]
        for item in out:
            f.write("%s"%item)


