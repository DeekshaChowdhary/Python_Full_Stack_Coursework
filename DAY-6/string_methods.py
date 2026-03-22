#1.case conversion methods

"deeksha".upper()
'DEEKSHA'

'DEEKSHA'.lower()
'deeksha'

'deek'.capitalize()
'Deek'

'Deeksha chowdhary'.title()
'Deeksha Chowdhary'

'DeekSha'.swapcase()
'dEEKsHA'

'deeksha'.casefold()
'deeksha'

'DEEKSHA'.casefold()
'deeksha'

'Deeksha'.casefold()
'deeksha'


#2.Alignment & Formatting

'deek'.center(4,"*")
'deek'

'deek'.center(8,"*")
'**deek**'

'deek'.ljust(6,'&')
'deek&&'

'deek'.rjust(6,'&')
'&&deek'

'deek'.zfill(5)
'0deek'


#3.search & find methods

'deek'.find("1")
-1

'deek'.find("1")
-1

'deek'.find("d")
0

'deek'.rfind("e")
2

'deek'.rfind("e")
1

'deek'.index("d")
0

'deek'.index('s')
ValueError: substring not found

'deek'.rindex("k")
3

'deeksha'.count("e")
2


#4.string testing methods

'deeksha'.startswith('dee')
True

'deeksha'.endswith('sha')
True

'deek'.isalpha()
True

'deek1'.isalnum()
True

"deek".islower()
True

'DEEK'.isupper()
True

" ".isspace()
True

"Deek Sha".istitle()
True

"var1".isidentifier()
True

10.isliteral()
SyntaxError: invalid syntax


#5.Replace & modify methods:

"deeksha".replace("sha","deek")
'deekdeek'

'deeksha'.translate(str.maketrans("d","x"))
'xeeksha'

'deeksha'.maketrans("deek","sha")
{100: 115, 101: 104, 101: 97, 107: 97}


#6.splitting & joining methods

"d,e,e,k".split(",")
['d', 'e', 'e', 'k']

"d,e,e,k".rsplit(",", 1)
['d,e,e', 'k']

"Deek\nSha".splitlines()
['Deek', 'Sha']

" ".join(["Hello", "world"])
'Hello world'

"deek-sha".partition("-")
('deek', '-', 'sha')

"deek-sha".rpartition("-")
('deek', '-', 'sha')


#7.whitespace & trimming methods

"  deek  ".strip()
'deek'

"--deek".lstrip()
'--deek'

"--deek".lstrip("-")
'deek'

"deek--".rstrip("-")
'deek'


#8.encoding & decoding:

"deek".encode("utf-8")
b'deek'

b"deek".decode("utf-8")
'deek'
