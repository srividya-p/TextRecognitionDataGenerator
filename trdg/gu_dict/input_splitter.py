# mergedInput = open('distribution_final_11/gu.txt', 'r')
mergedInput = open('distribution_final_363/gu.txt', 'r')

lines = [line.strip() for line in mergedInput.readlines()]

# step = 180
step = 6334
start = 0

for i in range(6):
    splitFileLines = lines[start : start+step]
    
    # splitFile = open('distribution_final_11/input_files/input'+str(i)+'.txt', 'w')
    splitFile = open('distribution_final_363/input_files/input'+str(i)+'.txt', 'w')
    for line in splitFileLines:
        splitFile.write(line+'\n')
    
    start = start + step
    if i==2 : step = 4000

