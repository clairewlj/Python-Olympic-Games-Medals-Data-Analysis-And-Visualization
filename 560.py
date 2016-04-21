with open("Olympics1.csv") as f:
    words_lines=f.readlines()
words_table=[]

#create table of data
for line in words_lines:
    line=line.strip()
    words_table.append(line.split(';'))

#clean data: removing extra rows
index_line1=words_table[0]
words_table=words_table[1:-3]

#create lists/dicts for information displaying
summary=dict()
for category in index_line1:
    summary[category]=[]
    index_of_category=index_line1.index(category)
    for line in words_table:
        if line[index_of_category] not in summary[category]:
            summary[category].append(line[index_of_category])

#create dict of dict ... to store data in order
medals_by_year={}
for year in summary["Year"]:
    medals_by_year[year]={}
    for line in words_table:
        if line[0]==year:
            if 'Sport' not in medals_by_year[year]:
                medals_by_year[year]['Sport']={}
            medals_by_year[year]['City']=line[1]
            if line[2] not in medals_by_year[year]['Sport']:
                medals_by_year[year]['Sport'][line[2]]={}
            if line[3] not in medals_by_year[year]['Sport'][line[2]]:
                medals_by_year[year]['Sport'][line[2]][line[3]]={}
            if line[4] not in medals_by_year[year]['Sport'][line[2]][line[3]]:
                medals_by_year[year]['Sport'][line[2]][line[3]][line[4]]={}
            if line[5] not in medals_by_year[year]['Sport'][line[2]][line[3]][line[4]]:
                medals_by_year[year]['Sport'][line[2]][line[3]][line[4]][line[5]]={}
            if line[6] not in medals_by_year[year]['Sport'][line[2]][line[3]][line[4]][line[5]]:
                medals_by_year[year]['Sport'][line[2]][line[3]][line[4]][line[5]][line[6]]=line[7]

#create functions to list unique values of each variable
def unique(var_index,index_line,data_summary):
    return summary[index_line[var_index]]

#display background information of the dataset
print("This data set consists of information about medals of Olympic Games. Below are the variables included:")

#display asked information
while True:
    levels=[]
    for i in range(8):
        levels.append([])
    while True:
        print("No.","Variable")
        for var in index_line1:
            print(index_line1.index(var),var)
        input_level1=input("Please enter a number to select. Enter q to quit search and print result: ")
        if input_level1=="q" or input_level1=="Q":
            break
        else:
            try:
                input_level1=int(input_level1)
                level1_name=index_line1[input_level1]
                print("****")
                for item in unique(input_level1,index_line1,summary):
                    print(unique(int(input_level1),index_line1,summary).index(item),item)
                input_level2=input("Please enter the number of one specific type and further select. Enter q to quit search and print result: ")
                if input_level2=="q" or input_level2=="Q":
                    break
                else:
                    try:
                        input_level2=int(input_level2)
                        levels[input_level1].append(summary[level1_name][input_level2])
                    except:
                        print("Invalid Input. Please enter again")
            except:
                print("Invalid input. Please try again.")
    break

#display choice
print("\nYou have chosen:")
i=0
while i<=7:
    item=levels[i]
    if item==[]:
        print(index_line1[i],": ","NA")
    else:
        if len(item)==1:
            print(index_line1[i],": ",item[0])
        else:
            delimeter=', '
            item2=delimeter.join(item)
            print(index_line1[i],":",item2)
    i=i+1

#clean choice list
cleaned_levels=[]
for item in levels:
    if item!=[]:
        cleaned_levels.append(item)

#select result rows
result_rows=[]
for line in words_table:
    values=[]
    for item in cleaned_levels:
        item_not_in_line=[]
        for value in item:
            value_not_in_line=value in line
            item_not_in_line.append(value_not_in_line)
        values.append(any(item_not_in_line))
    if all(values):
        result_rows.append(line)


#print result
print("\nSelected data:")
delimeter2=' '
print(delimeter2.join(index_line1))
for row in result_rows:
    print(delimeter2.join(row))