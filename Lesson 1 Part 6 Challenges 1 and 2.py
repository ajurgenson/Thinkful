#Challenge 1 - Change

import collections
population_dict = collections.defaultdict(int)

with open('/Users/AJurgenson/Thinkful/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
	header = next(inputFile)
	for line in inputFile:
		line = line.rstrip().split(',')
		line[5] = int(line[5])
		line[6] = float(line[6])
		change = (line[6] - line[5])
		if line[1] == 'Total National Population':
			print line[0], line[5], line[6], change
			list = [line[5],line[6],change]
			newList = str(list)
			population_dict[line[0]] = newList

with open('change_population.csv','w') as outputFile:
	outputFile.write('continent,2010_population,2100_population,change\n')

	for k,v in population_dict.iteritems():
		newV = v.replace("[","")
		newV = newV.replace("]","")
		outputFile.write(k + ',' + str(newV) + '\n')

#Challenge 2 - Density

import collections
population_dict = collections.defaultdict(int)

with open('/Users/AJurgenson/Thinkful/lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
	header = next(inputFile)
	for line in inputFile:
		line = line.rstrip().split(',')
		line[5] = int(line[5])
		line[7] = float(line[7])
		density = (line[5] / line[7])
		if line[1] == 'Total National Population':
			print line[0], line[5], line[7], density
			list = [line[5],line[7],density]
			newList = str(list)
			population_dict[line[0]] = newList

with open('density_population.csv','w') as outputFile:
	outputFile.write('continent,2010_population,land_area,density\n')

	for k,v in population_dict.iteritems():
		newV = v.replace("[","")
		newV = newV.replace("]","")
		outputFile.write(k + ',' + str(newV) + '\n')