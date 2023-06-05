
import codecs

term = 'ter' + str(input("Ingrese nombre del Terminal a traducir:       ter"))

with codecs.open(r'Terminales Traducidas\{}'.format(term), 'r', encoding='ansi') as fin:
    file_content = fin.read()



with codecs.open(r'Terminales Traducidas\{}.txt'.format(term), 'x', encoding='macroman') as fout:    
    fout.write(file_content)
