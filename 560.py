from helper import *

with open("Olympics2.csv") as f:
    words_lines=f.readlines()
words_table=[]

#create table of data
for line in words_lines:
    line=line.strip()
    words_table.append(line.split(';'))

#clean data: removing extra rows
index_line1=words_table[0]
index_line2=[]
for cat in index_line1:
    if cat!='Discipline' and cat!= 'Event':
        index_line2.append(cat)
words_table=words_table[1:]

#create lists/dicts for information displaying
summary_1=create_summary_table(index_line1,words_table)

#sort the values following alphabet order in the lists in summary_1
summary_1=sort_summary(summary_1)

#display background information of the data set
while True:
    print("This data set consists of information about medals of Olympic Games. Below are the variables included:")
    #display asked information
    levels=[]
    for i in range(6):
        if i != 2:
            levels.append([])
        else:
            levels.append({})
    all_select=select_level1(words_table,summary_1,index_line2,levels)

    #display choice
    if all_select!=[]:
        pass
    else:
        print("\nYou have chosen:")
        i=0
        while i<=5:
            item=levels[i]
            if item==[]:
                print(index_line2[i],": ","NA")
            elif item=={}:
                print(index_line2[i],": ","NA")
            else:
                if i != 2:
                    if len(item)==1:
                        print(index_line2[i],": ",item[0])
                    else:
                        print(index_line2[i],": ",', '.join(item))
                else:
                    print("Sport: ")
                    sport_chosen=list_keys(levels[2])
                    for sport in sport_chosen:
                        print("  ",sport,": ",)
                        discipline_chosen=list_keys(levels[2][sport])
                        for disp in discipline_chosen:
                            if len(levels[2][sport][disp])==1:
                                print("    ",disp,": ",levels[2][sport][disp][0])
                            else:
                                events_chosen=', '.join(levels[2][sport][disp])
                                print("    ",disp,": ",events_chosen)
            i=i+1

    #clean choice list
    cleaned_levels=clean_table(levels)

    #select result rows
    result_rows=[]
    for line in words_table:
        values=[]
        for item in cleaned_levels:
            if type(item)==type([]):
                item_in_line=[]
                for value in item:
                    value_in_line=value in line
                    item_in_line.append(value_in_line)
                values.append(any(item_in_line))
            else:
                sport_in_line=False
                sport_in_line=[]
                for sport in item:
                    if line[2]==sport:
                        for disp in item[sport]:
                            if line[3]==disp:
                                if line[4] in item[sport][disp]:
                                    sport_in_line=True
                values.append(sport_in_line)
        if all(values):
            result_rows.append(line)

    #print result
    print("\nSelected data:")
    if all_select!=[]:
        for row in all_select:
            print(' '.join(row))
        print("**"*20)
        print("Total:",len(all_select),"lines.")
        print("**"*20)
    else:
        print(' '.join(index_line1))
        for row in result_rows:
            print(' '.join(row))
        print("**"*20)
        print("Total:",len(result_rows),"lines.")
        print("**"*20)