#-*- coding: utf-8 -*-

digits = ['૦', '૧', '૨', '૩', '૪', '૫', '૬', '૭', '૮', '૯']

vowels = ['અ', 'આ', 'ઇ', 'ઈ', 'ઉ', 'ઊ', 'ઋ', 'ૠ', 'એ', 'ઐ', 'ઓ', 'ઔ']

# 'ઌ', 'ૡ', 'ૃ', 'ૄ'  'ઁ',  'ં' , 'ઃ', '્'

consonants = ['ક', 'ખ', 'ગ', 'ઘ', 'ઙ',
              'ચ', 'છ', 'જ', 'ઝ', 'ઞ',
              'ટ', 'ઠ', 'ડ', 'ઢ', 'ણ',
              'ત', 'થ', 'દ', 'ધ', 'ન',
              'પ', 'ફ', 'બ', 'ભ', 'મ',
              'ય', 'ર', 'લ', 'ળ', 'વ', 
              'શ', 'ષ', 'સ', 'હ']

complex_consonants = ['ક', 'ખ', 'ઙ', 'છ', 'જ', 'ઝ', 'ઞ',
                      'ટ', 'ઠ', 'ઢ', 'ણ', 'ફ', 'બ', 'ભ',
                      'ય', 'લ', 'ળ', 'શ', 'ષ', 'સ', 'હ']

simple_consonants = list(set(consonants) - set(complex_consonants)) + list(set(complex_consonants) - set(consonants))

maatras = ['ા', 'િ', 'ી', 'ુ', 'ૂ', 'ે', 'ૈ', 'ો', 'ૌ']

print('Digits = '+str(len(digits)) + ' (All Simple)')
print('Vowels = '+str(len(vowels)) + ' (All Complex)')
print('Consonants = '+str(len(consonants)) + ' (Simple '+str(len(simple_consonants)) + ' Complex '+str(len(complex_consonants)) + ')')
print('Maatras = '+str(len(maatras)))

spaceFileName = '/home/pika/Desktop/TIFR/YOLO-AppV2.0/TRDG/trdg/gu_dict/distribution_final_363/space_363.names'

file = open(spaceFileName, 'w') 

for v in vowels:
    file.write(v)
    file.write('\n')

for c in complex_consonants:
    file.write(c)
    file.write('\n')

for c in complex_consonants:
    for m in maatras:
        file.write(''.join([c, m]))
        file.write('\n')

for c in simple_consonants:
    file.write(c)
    file.write('\n')

for c in simple_consonants:
    for m in maatras:
        file.write(''.join([c, m]))
        file.write('\n')

for d in digits:
    file.write(d)
    file.write('\n')

file.write('Space\n')

file = open(spaceFileName, 'r')

lines = file.readlines()
print()
print("Total = " + str(len(lines)))
c, s = 0, 0
for line in lines:
    if line[0] in complex_consonants or line[0] in vowels:
        c+=1
    elif line.strip() == 'Space':
        continue
    else:
        s+=1

flag = False
for line in lines[0:222]:
    if line[0] in complex_consonants or line[0] in vowels:
        flag = True
    else:
        flag = False

print("Complex = " + str(c))
print("Simple = " + str(s))
print("Space = " + str(1))
print()
print('Complex lies only in 0 : 222 - '+str(flag))




