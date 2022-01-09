mergedInput = open('distribution_final/gu.txt', 'r')

lines = [line.strip() for line in mergedInput.readlines()]

step = 180
start = 0

for i in range(6):
    splitFileLines = lines[start : start+step]
    
    splitFile = open('distribution_final/input_files/input'+str(i)+'.txt', 'w')
    for line in splitFileLines:
        splitFile.write(line+'\n')
    
    start = start + step
    if i==2 : step = 113

