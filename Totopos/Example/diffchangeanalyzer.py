import sys

source_F = open(str(sys.argv[1]),'r')
diff_l = []

for number in source_F.readlines():
    diff_l.append(float(number.strip('\n')))

index = 0
analyze_l = []
a = b = c = d = e = f = g = h = i = j = k = 0

for number in diff_l:

    if 0 < number <= 10 : a += 1
    elif 10 < number <= 20 : b += 1
    elif 20 < number <= 30 : c += 1
    elif 30 < number <= 40 : d += 1
    elif 40 < number <= 50 : e += 1
    elif 50 < number <= 60 : f += 1
    elif 60 < number <= 70 : g += 1
    elif 70 < number <= 80 : h += 1
    elif 80 < number <= 90 : i += 1
    elif 90 < number <= 100 : j += 1
    else: k += 1

    if index != 0 and index % 100 == 0:
        analyze_l.append([a,b,c,d,e,f,g,h,i,j,k])
        a = b = c = d = e = f = g = h = i = j = k = 0

    index +=1

print analyze_l

output_F = open('outputdiff.txt' , 'w')

for analyze in analyze_l:
    towrite = str(analyze).strip('[')
    towrite = str(analyze).strip(']')
    towrite = towrite + '\n'
    output_F.write(towrite)

output_F.close()

