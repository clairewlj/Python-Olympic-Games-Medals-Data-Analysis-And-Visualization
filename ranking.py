#module for ranking
from setup import *
import numpy as np
import matplotlib.pyplot as plt

#ask user to select subtypes of selected types for ranking
def select_subtype(choice_1,summary_for_ranking,rank_choices):
    choice_1=int(choice_1)
    while True:
        print_menu(summary_for_ranking[choice_1])
        choice_2=input("Please enter the index of one type, or enter a to select all types and return to the previous menu, or enter q to stop selecting and return to previous menu: ")
        if choice_2=="q" or choice_2=="Q":
            break
        elif choice_2=="a" or choice_2=="A":
            rank_choices[choice_1]=summary_for_ranking[choice_1]
            break
        else:
            try:
                choice_2=int(choice_2)
                add_if_not_in(summary_for_ranking[choice_1][choice_2],rank_choices[choice_1])
            except:
                print("Invalid Input. Please enter again.")
        print("**"*20)
    return rank_choices

#ask user to select types for ranking
def select_ranking_types(rank_row_names,summary_for_ranking):
    #create list of lists to store choices
    rank_choices=[]
    for i in range(4):
        rank_choices.append([])
    while True:
        print_menu(rank_row_names)
        print("**"*20)
        choice_1=input("Please enter the index of one variable for further selecting, or enter a to select all variables and quit search, or enter q to quit searching directly: ")
        if choice_1=="q" or choice_1=="Q":
            break
        elif choice_1=="a" or choice_1=="A":
            for i in range(4):
                rank_choices[i]=summary_for_ranking[i]
            break
        else:
            try:
                rank_choices=select_subtype(choice_1,summary_for_ranking,rank_choices)
            except:
                print("Invalid Input. Please enter again.")
        print("**"*20)
    return rank_choices

#print selected ranking data
def print_selected_ranking(rank_choices,rank_row_names):
    print("********************\nYou have chosen:")
    for i in range(4):
        if rank_choices[i]==[]:
            print(rank_row_names[i],": NA")
        else:
            if len(rank_choices[i])==1:
                print(rank_row_names[i],":",rank_choices[i][0])
            else:
                print(rank_row_names[i],":",", ".join(rank_choices[i]))
    print("**"*20)

#select data rows based on user's choices
def select_ranking_data(rank_choices,words_table):
    #clean choices list and create list of empty lists prepared for selecting data rows in next step
    cleaned_choices=[]
    for i in range(4):
        if rank_choices[i]!=[]:
            cleaned_choices.append(rank_choices[i])

    #select related data and create a new table
    selected_table=[]
    for line in words_table:
        value_choices=[]
        for choice in cleaned_choices:
            choice_in_row=[]
            for item in choice:
                item_in_row=item in line
                choice_in_row.append(item_in_row)
            value_choices.append(any(choice_in_row))
        if all(value_choices):
            selected_table.append(line)
    return selected_table

#printing selected data
def print_ranking_data(index_line1,selected_table):
    print("Selected data:")
    print("**"*20)
    print(' '.join(index_line1))
    for row in selected_table:
        print(' '.join(row))
    print("**"*20)

#function to count numbers of medals and print formatted ranking
def count_total_metals(selected_table,num):
    NOC_rank={}
    medals=["Total","Gold","Silver","Bronze"]
    for line in selected_table:
        if line[7] not in NOC_rank:
            NOC_rank[line[7]]=[]
            for i in range(4):
                NOC_rank[line[7]].append(0)
            NOC_rank[line[7]][0]=1
            NOC_rank[line[7]][medals.index(line[6])]=1
        else:
            NOC_rank[line[7]][0]+=1
            NOC_rank[line[7]][medals.index(line[6])]+=1

    rank_rows=[]
    i=0
    for NOC in NOC_rank:
        rank_rows.append([])
        rank_rows[i].append(NOC)
        for medal in NOC_rank[NOC]:
            rank_rows[i].append(medal)
        i+=1
    while True:
        print("**"*20)
        if num==1:
            print_menu(medals)
            view_input=input("Please enter the index of one ranking criterion and view the result, or enter q to quit:")
            if view_input=="q" or view_input=="Q":
                break
            else:
                try:
                    view_input=int(view_input)
                    rank_rows.sort(key=lambda x: x[view_input+1],reverse=True)
                    print("**"*20)
                    print("NOC","Total","Gold","Silver","Bronze")
                    #for printing out correctly: all integers need to be transfered to string
                    newlist=[]
                    for i in range(len(rank_rows)):
                        newlist.append([])
                        for item in rank_rows[i]:
                            newlist[i].append(str(item))
                    for line in newlist:
                        print(' '.join(line))
                except:
                    print("Invalid input. Please enter again.")
        elif num==3:
            #ask user to show bar chart of total/gold/silver/bronze
            print_menu(medals)
            third_step=input("Please enter the index of the specific medal to plot a bar chart related, or enter q to quit: ")
            if third_step=="q" or third_step=="Q":
                break
            else:
                try:
                    third_step=int(third_step)
                    rank_rows.sort(key=lambda x: x[third_step+1],reverse=True)
                    newlist=rank_rows[0:10]
                    #plot a bar chart
                    data_for_plot=[]
                    plot_names=[]
                    for NOC in newlist:
                        data_for_plot.append(int(NOC[third_step+1]))
                        plot_names.append(NOC[0])
                    plot_names=tuple(plot_names)

                    y_pos=np.arange(10)
                    y_label=medals[third_step]
                    bar_width=0.5
                    plot_title="Top 10 NOC Of "+y_label
                    plt.bar(y_pos,data_for_plot,bar_width,alpha=0.5,color='b')
                    plt.ylabel(y_label)
                    plt.xlabel("NOC")
                    plt.title(plot_title)
                    plt.xticks(y_pos+0.2,plot_names)

                    plot_name=plot_title+".png"
                    plt.savefig(plot_name)
                except:
                    print("Invalid input. Please enter again.")
                print("**"*20)