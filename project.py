# license: https://github.com/Joey5729/ATLA-Line-Visualization/blob/master/LICENSE

import os
import chord
# credit to Dr. Shahin Rostami, creator of the chord package
# https://github.com/shahinrostami/chord

def main():

    # retrieve list of episode files
    fileList = os.listdir('episodes/')
    lineList = []
    
    # extract the lines from files in episode list
    for f in fileList:
        with open('episodes/' + f) as fOb:
            for line in fOb:
                lineList.append(line.strip())

    # set up the lists used
    codeList =  ['a',       'k',        's',        't',        'z',        'i',        'az',       'o',        'm',        'ty',       'su']
    names =     ['Aang',    'Katara',   'Sokka',    'Toph',     'Zuko',     'Iroh',     'Azula',    'Ozai',     'Mai',      'Ty Lee',   'Suki']
    colorList = ['#fff81f', '#6eddff',  '#1690b5',  '#0dd610',  '#ff0000',  '#ffaa00',  '#590069',  '#804f00',  '#1c0000',  '#ed009a',  '#80ff00']

    matrix = [
[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],
    ]

    # parse over the list of lines, filling the matrix
    for line in lineList:
        chars = line.split(',')
        matrix[codeList.index(chars[0])][codeList.index(chars[1])] += 1
        matrix[codeList.index(chars[1])][codeList.index(chars[0])] += 1

    # yay we're done

    #printMatrix(matrix, names)
    chord.Chord(matrix, names, wrap_labels = 0, colors = colorList).to_html()

# debug function

def printMatrix(matrix, names):
    
    print(end = '\t')

    for name in names:
        print(name,  end = '\t')
    
    print()

    for y in matrix:
        print(names[matrix.index(y)], end = '\t')
        for x in y:
            print (x, end = '\t')
        print()
        
# very important
main()