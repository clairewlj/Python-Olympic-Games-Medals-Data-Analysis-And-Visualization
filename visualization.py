from ranking import count_total_metals
from setup import *
import matplotlib.pyplot as plt

def line_graph(summary_for_view,words_table):
    print_menu(summary_for_view['NOC'])
    NOC_1=input("Please enter the index of the first NOC.")
    try:
        NOC1_to_plot=summary_for_view['NOC'][int(NOC_1)]
        NOC_2=input("Please enter the index of the second NOC.")
        try:
            #calculate total medals
            NOC2_to_plot=summary_for_view['NOC'][int(NOC_2)]
            x_line=[]
            y_line_1=[]
            y_line_2=[]
            for year in summary_for_view['Year']:
                x_line.append(year)
                year_count_1=0
                year_count_2=0
                for line in words_table:
                    if line[0]==year and line[7]==NOC1_to_plot:
                        year_count_1+=1
                    elif line[0]==year and line[7]==NOC2_to_plot:
                        year_count_2+=1
                y_line_1.append(year_count_1)
                y_line_2.append(year_count_2)

            #plot line graph
            plt.plot(x_line,y_line_1,marker="o",linestyle='--',color='m',label=NOC1_to_plot)
            plt.plot(x_line,y_line_2,marker="*",linestyle='-.',color='c',label=NOC2_to_plot)
            plt.xlabel('Year')
            plt.ylabel('Total Medals')
            title_NOC="Medals won by "+NOC1_to_plot+" & "+NOC2_to_plot
            plt.title(title_NOC)
            plt.legend()
            plot_name=title_NOC+".png"
            plt.savefig(plot_name)
        except:
            print("Invalid input. Please enter again.")
    except:
        print("Invalid input. Please enter again.")

def bar_graph(summary_for_view,words_table):
    while True:
        print_menu(summary_for_view['Year'])
        second_step=input("Please the index of one specific year. The graph will be saved under current directory.")
        try:
            second_step=int(second_step)
            #create the table of selected data and count the number of total medals and each type of medal
            bar_plot_data=[]
            for line in words_table:
                if line[0]==summary_for_view['Year'][second_step]:
                    bar_plot_data.append(line)
            count_total_metals(bar_plot_data,3)
            break
        except:
            print("Invalid input. Please enter again.")