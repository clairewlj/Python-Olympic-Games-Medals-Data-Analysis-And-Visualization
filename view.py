#module for seleting functions
from setup import *

#create list to store user's choices for further data selecting
def create_levels():
    levels=[]
    for i in range(6):
        if i != 2:
            levels.append([])
        else:
            levels.append({})
    return levels

#function to select sport/non-sport variable
def select_level1(words_table,summary_1,index_line2,levels):
    all_select=[]
    while True:
        print("No.","Variable")
        print_menu(index_line2)
        input_level1=input("Please enter the index of the variable for further selecting, enter 'a' to select all data and quit search, or enter q to directly quit search: ")
        if input_level1=="q" or input_level1=="Q":
            break
        elif input_level1=="a" or input_level1=="A":
            all_select=words_table
            break
        else:
            try:
                input_level1=int(input_level1)
                if input_level1!=2:
                    while True:
                        level1_name=index_line2[input_level1]
                        print("**"*20)
                        print_menu(summary_1[level1_name])
                        input_level2=input("Please enter the index of one specific type for further selecting, or enter 'a' to select all and return to previous menu, or enter q to quit search and return to previous menu: ")
                        if input_level2=="q" or input_level2=="Q":
                            break
                        elif input_level2=="a" or input_level2=="A":
                            levels[input_level1]=summary_1[level1_name]
                            break
                        else:
                            try:
                                print("**"*20)
                                input_level2=int(input_level2)
                                add_if_not_in(summary_1[level1_name][input_level2],levels[input_level1])
                            except:
                                print("Invalid Input. Please enter again")
                else:
                    while True:
                        #create a list of keys in sport
                        sport_names=list_keys(summary_1['Sport'])
                        print("**"*20)
                        print_menu(sport_names)
                        input_level2=input("Please enter the index of one specific type of sport for further selecting. Enter 'a' to select all and return to previous menu, or enter q to select none and return to previous menu: ")
                        if input_level2=="q" or input_level2=="Q":
                            break
                        elif input_level2=="a" or input_level2=="A":
                            levels[input_level1]=summary_1['Sport']
                            break
                        else:
                            try:
                                input_level2=int(input_level2)
                                sport_name=sport_names[input_level2]
                                #create a list of keys in discipline
                                discipline_names=list_keys(summary_1['Sport'][sport_name])
                                select_discipline(input_level1,levels,summary_1,discipline_names,sport_name)
                            except:
                                print("Invalid Input. Please enter again.")
                        print("**"*20)
            except:
                print("Invalid input. Please try again.")
        print("**"*20)
    return all_select

#function to select discipline in sport
def select_discipline(input_level1,levels,summary_1,discipline_names,sport_name):
    while True:
        print("**"*20)
        print_menu(discipline_names)
        input_level3=input("Please enter the index of one specific discipline for further selecting. Enter 'a' to select all and return to the previous menu, or enter q to select none and return to previous menu: ")
        if input_level3=="q" or input_level3=="Q":
            break
        else:
            if sport_name not in levels[input_level1]:
                levels[input_level1][sport_name]={}
            if input_level3=="a" or input_level3=="A":
                levels[input_level1][sport_name]=summary_1['Sport'][sport_name]
                break
            try:
                print("**"*20)
                input_level3=int(input_level3)
                discipline_name=discipline_names[input_level3]
                #create a list of keys of events in discipline
                event_names=summary_1['Sport'][sport_name][discipline_name]
                select_event(input_level1,levels,summary_1,event_names,discipline_name,sport_name)
            except:
                print("Invalid Input. Please enter again.")
        print("**"*20)

#function to select event in discipline
def select_event(input_level1,levels,summary_1,event_names,discipline_name,sport_name):
    while True:
        print("**"*20)
        print_menu(event_names)
        input_level4=input("Please enter the index of one specific event to view. Enter 'a' to select all and return to the previous menu, or enter q to select none and return to previous menu: ")
        if input_level4=="q" or input_level4=="Q":
            break
        else:
            if discipline_name not in levels[input_level1][sport_name]:
                levels[input_level1][sport_name][discipline_name]=[]
            if input_level4=="a" or input_level4=="A":
                levels[input_level1][sport_name][discipline_name]=summary_1['Sport'][sport_name][discipline_name]
                break
            try:
                input_level4=int(input_level4)
                event_name=event_names[input_level4]
                add_if_not_in(event_name,levels[input_level1][sport_name][discipline_name])
            except:
                print("Invalid Input. Please enter again.")
        print("**"*20)

#display choices
def display_selected_choices(all_select,levels,index_line2):
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

#extracting data rows based on user's choices
def select_result_rows(words_table,cleaned_levels):
    result_rows=[]
    for line in words_table:
        values=[]
        for item in cleaned_levels:
            if type(item)==type([]): #choices not related to sport types
                item_in_line=[]
                for value in item:
                    value_in_line=value in line
                    item_in_line.append(value_in_line)
                values.append(any(item_in_line))
            else: #choices related to sport types
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
    return result_rows

#print selected data
def print_selected_data(all_select,index_line1,result_rows):
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