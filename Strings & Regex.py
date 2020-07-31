import re
s = 'Did you know...\n\n... that the first discovered fossil of the dinosaur Weewarrasaurus was noted for\nbeing preserved in green-blue opal?\n\n... that the golden-headed cisticola (pictured) has been described as the "finest tailor of all birds"?\n\n... that the rhythm of the call of the fulvous owl has been likened to Morse code?'

x = re.sub(r'know...','know:',s)
x2 = re.sub(r'....that',':that',x)
print('***Task 1:\n\n',x2)

xa = re.sub(r'\n',' ',s)
print('\n\n***Task 2:\n\n',xa)

xb = re.sub(r'know....','know:',s)
xbb = re.sub(r'....that','*that',xb)
xbbb= re.sub(r'\n\n','\n',xbb)
print('\n\n***Task 3:\n\n',xbbb)

s.title()
print('\n\n***Task 4:\n\n',s.title())
