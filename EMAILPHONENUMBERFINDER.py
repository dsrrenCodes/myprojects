import re, pyperclip

#email regex
emailRegex=re.compile(r'''(
[a-zA-Z0-9._%+-]+  #first 
@ #@
[a-zA-Z0-9.-]+ #domain
\.
com


)''', re.VERBOSE)

#Phone regex number in SG Context
phoneRegex=re.compile(r'\+65\s\d{8}')

#find matches in copied text
matches=[]
copied= pyperclip.paste()
for group in emailRegex.findall(copied):
    matches.append(group  )

for group in phoneRegex.findall(copied):
    matches.append(group)

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
    


    