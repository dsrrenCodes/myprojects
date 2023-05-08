import re , pyperclip
#date regex
dateRegex=re.compile(r'''(
(\d\d) #day
\/ #/
(\d\d) #month
\/ #/
(\d\d\d\d) #year



)''',re.VERBOSE)
match=[]
copied=pyperclip.paste()
for groups in dateRegex.findall(copied):
    day=groups[1]
    month=groups[2]
    year=groups[3]
    
    if day >'30':
        print("Invalid day")
    if month >'12':
        print("Invalid month")
    if year>'999':
        print("Invalid year")
    else:
        lol = '/'.join([groups[1], groups[2], groups[3]])
        match.append(lol)
if len(match) > 0:
    pyperclip.copy('\n'.join(match))
    print('Copied to clipboard:')
    print('\n'.join(match))
    


    