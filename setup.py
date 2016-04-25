#basic set up and table create

#function to create summary table for displaying basic menu for selecting
def create_summary_dict(index_line1,words_table):
    summary_1=dict()
    for category in index_line1:
        if category!= 'Sport' and category!= 'Discipline' and category!= 'Event':
            summary_1[category]=[]
            index_of_category=index_line1.index(category)
            for line in words_table:
                if line[index_of_category] not in summary_1[category]:
                    summary_1[category].append(line[index_of_category])
        elif category=='Sport':
            summary_1[category]={}
            index_of_sport=index_line1.index('Sport')
            index_of_discipline=index_line1.index('Discipline')
            index_of_event=index_line1.index('Event')
            for line in words_table:
                if line[index_of_sport] not in summary_1[category]:
                    summary_1[category][line[index_of_sport]]={}
                if line[index_of_discipline] not in summary_1[category][line[index_of_sport]]:
                    summary_1[category][line[index_of_sport]][line[index_of_discipline]]=[]
                if line[index_of_event] not in summary_1[category][line[index_of_sport]][line[index_of_discipline]]:
                    summary_1[category][line[index_of_sport]][line[index_of_discipline]].append(line[index_of_event])
        else:
            pass
    return summary_1

#function to sort order in summary table for better displaying
def sort_summary(summary_1):
    for cat in summary_1:
        if cat=='Sport':
            for sport in summary_1[cat]:
                for disp in summary_1[cat][sport]:
                    summary_1[cat][sport][disp].sort()
        else:
            summary_1[cat].sort()
    return summary_1

#function to displaying menu for selecting
def print_menu(a):
    for item in a:
        print(a.index(item),item)

#function to create a list of keys in dictionary
def list_keys(dicts):
    names=list(dicts.keys())
    names.sort()
    return names

#function to add choice if not already in the choice list
def add_if_not_in(a,b):
    if a not in b:
        b.append(a)

#clean choice list
def clean_table(levels):
    cleaned_levels=[]
    for item in levels:
        if item!=[] and item !={}:
            cleaned_levels.append(item)
    return cleaned_levels

