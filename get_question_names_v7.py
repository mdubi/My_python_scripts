import re
fname = raw_input("Enter file name: ")
fh = open(fname)
zmienne_output = open('nazwy_pytan.txt', 'wb')
line_as_list =list()
for line in fh:
    if len(line)>0 :
        line_as_list = line.split()
        if len(line_as_list)>1:
            #print line_as_list
            first_word = line_as_list[0]
            is_letter_first = re.match('[a-zA-Z]', first_word[0])
            if '.' in first_word[2:5] and '.' in first_word[-1] and is_letter_first :
                zmienne_output.write(first_word)
                zmienne_output.write('\n')
                #print first_word
            else:
                continue
zmienne_output.close()
fh2 = open('nazwy_pytan.txt') #warto dodac jeszcze deduplikacje nazw zmiennych
zmienne_output2 = open('nazwy_pytan_raport.txt', 'wb')
d = dict()
count_qst = 0
for line in fh2:
    count_qst += 1 #warto by bylo dodac inteligentne pomijanie naglowkow w wyliczeniach
    variable = line.strip()
    if variable not in d:
        d[variable] = 1
    else:
        d[variable] = d[variable] + 1
import operator
sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
reported_str = 'Liczba wszystkich pytan i naglowkow w kwestionariuszu: '+ str(count_qst)
zmienne_output2.write(reported_str) #do zastanowienia czy nie dodac informacji o liczbie stron w HTMLu
zmienne_output2.write('\n')
for obj in sorted_d :
    reported_variable = str(obj).strip('(').strip(')').strip('\'').replace('\',',' count =')
    zmienne_output2.write(reported_variable)
    zmienne_output2.write('\n')
zmienne_output2.close()


