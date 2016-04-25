from view import *
from ranking import *
from visualization import *

#ask user for choice of fine and open file
filenum=input("There are two files including data about medals of Olympic Games. Please enter 1 to view data about Winter Olympic Games, or enter 2 to view data about Summer Olympic Games: ")
while True:
    if int(filenum)==1:
        filename="Olympics1.csv"
        break
    elif int(filenum)==2:
        filename="Olympics2.csv"
        break
    else:
        print("Invalid input. Please enter again.")
with open(filename) as f:
    words_lines=f.readlines()

#create table of data
words_table=[]
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

#create lists/dicts for information displaying, and create summary list as index for ranking
summary_for_view=create_summary_dict(index_line1,words_table)
summary_for_ranking=[summary_for_view['Year'],list_keys(summary_for_view['Sport']),summary_for_view['Event gender'],summary_for_view['Medal']]

#sort the values following alphabet order in the lists in summary_for_view
summary_for_view=sort_summary(summary_for_view)

#display background information of the data set
while True:
    first_step=input("This data set consists of information about medals of Olympic Games. Enter 1 to view rankings of all countries on medals winning by year/sport/gender/medal. Enter 2 to select and view detailed data by year/city/sport/discipline/event/gender/medal/NOC. Enter 3 to view bar charts/line graphs: ")
    print("**"*20)
#if user choose to view ranking
    if int(first_step)==1:
        rank_row_names=['Year','Sport','Gender','Medal']

        #ask for user's choices to select data for ranking
        rank_choices=select_ranking_types(rank_row_names,summary_for_ranking)

        #print choices
        print_selected_ranking(rank_choices,rank_row_names)

        #re-start if choose nothing to rank
        if all(rank_choices):
            continue
        #select data rows based on user's choices
        selected_table=select_ranking_data(rank_choices,words_table)

        #printing selected data
        print_ranking_data(index_line1,selected_table)

        #print formatted ranking
        count_total_metals(selected_table,1)

        #print bar chart of top 10 NOC

#if user choose to view detailed data
    elif int(first_step)==2:

        #create list to store user's choices for further data selecting
        levels=create_levels()

        #ask user to select types of data interested in
        all_select=select_level1(words_table,summary_for_view,index_line2,levels)

        #display user's choices
        display_selected_choices(all_select,levels,index_line2)

        #clean choice list for extracting data rows out of original table
        cleaned_levels=clean_table(levels)

        #select result rows
        result_rows=select_result_rows(words_table,cleaned_levels)

        #print result
        print_selected_data(all_select,index_line1,result_rows)
    elif int(first_step)==3:
        #ask user whether view line graph or bar chart

        second_step=input("View line graph of medals won by two NOC over history, enter 1. View top 10 NOC win most medals in one specific year, enter 2:")

        #if line graph
        if int(second_step)==1:
            line_graph(summary_for_view,words_table)

        #if bar chart
        elif int(second_step)==2:
            bar_graph(summary_for_view,words_table)

        else:
            print("Invalid input. Please enter again.")
    else:
        print("Invalid Input. Please enter again.")
    print("**"*20)