from tkinter import *
from Analyze_Behavioural_Data import classifier, cv
import browserhistory as bh
import webbrowser
import numpy as np
import matplotlib.pyplot as plt

def graph():

    #### getting the value for entertainment and studies
    dict = bh.get_browserhistory()
    bh.write_browserhistory_csv()

    list1 = list(dict.values())
    res = [item for t in list1 for item in t]
    history_list = [item for t in res for item in t]
    # print(history_list)

    i = 1
    final_list = []
    while i < len(history_list):
        final_list.append(history_list[i])
        i += 3

    entertainment = 0
    study = 0
    predict_res = 0
    feed_list = []
    for item in final_list:
        feed_list.append(item)
        feed_list1 = cv.transform(feed_list).toarray()
        predict_res = int(classifier.predict(feed_list1))
        # print(type(predict_res))
        if predict_res == 0:
            entertainment += 1
        else:
            study += 1
        feed_list.clear()


    ### Setting the Graph
    courses = ['Entertainment', 'Studies']
    values = [entertainment, study]

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(courses, values, color='blue',
            width=0.2)

    plt.xlabel("CATEGORIES")
    plt.ylabel("FREQUENCY")
    plt.title("USER HISTORY ANALYSIS")
    plt.show()


def GO():
    webbrowser.open('https://colab.research.google.com/drive/1x67Pj3b9D7eRJcYHC8x96HWXnLFcYNHY')

def manual_feed():
    # print("button clicked", string_data.get())
    new = []
    new.append(string_data.get())
    new = cv.transform(new).toarray()
    # print(type(new))
    custom_predict = classifier.predict(new)
    if custom_predict == 0:
        result_label.config(text = "Intreseted in Entertainment")
    else:
        result_label.config(text="Intreseted in Education and Studies")


def automatic_feed():
    dict = bh.get_browserhistory()
    bh.write_browserhistory_csv()

    list1 = list(dict.values())
    res = [item for t in list1 for item in t]
    history_list = [item for t in res for item in t]
    # print(history_list)

    i = 1
    final_list = []
    while i < len(history_list):
        final_list.append(history_list[i])
        i += 3

    ## Final_list contains my latest chrome history
    # print(final_list)

    entertainment = 0
    study = 0
    predict_res = 0
    feed_list = []
    for item in final_list:
        feed_list.append(item)
        feed_list1 = cv.transform(feed_list).toarray()
        predict_res = int(classifier.predict(feed_list1))
        # print(type(predict_res))
        if predict_res == 0:
            entertainment += 1
        else:
            study += 1
        feed_list.clear()
    if(entertainment > study):
        result_label.config(text = "User more Inclined towards Fun")
    else:
        result_label.config(text="User more Inclined towards Study")



root = Tk()
root.title('BANKAI')
root.geometry('800x500')
root.minsize(800, 500)
root.maxsize(800, 500)
# pic=PhotoImage(file='mario.png')

# my_label = Label(root, image=pic)
# my_label.place(x=0, y=0, relwidth=1, relheight=1)

# my_text = Label(text="ANALYSE YOUR HISTORY",font=("monotype 35 bold"), fg="black", bg = "orange", relief=SUNKEN, borderwidth=5)
# my_text.pack(pady=12)

################## VARIABLES ################

string_data = StringVar()

#############################################

## for manual feeding
manual = Label( text='ENTER ANY STRING BELOW', font= ('Times',20, "bold"), padx = 5, pady = 10)
manual.pack(pady=7, fill=X)

manual_entry = Entry(textvariable=string_data, font = ('Arial',20))
manual_entry.pack(pady=10)
## button to execture the function
B1 = Button(root, text = "      RESULT     ", font = ('Times 12 bold'), padx=5, pady=10,fg="black", relief=SUNKEN, borderwidth= 3, command = manual_feed)
B1.config(compound='center')
B1.pack(pady=7)


## Shows result for manual feed
result_label = Label(text = '',font = ('Times 14 bold'),  borderwidth=10, relief=GROOVE)
result_label.pack()


## For automatic history collection
B2 = Button(root, text = "    AUTOMATIC  ", font = ('Times 12 bold'), padx=5, pady=10,fg="black",  relief=SUNKEN, borderwidth= 4, command = automatic_feed)
B2.pack(pady=7)

B3 = Button(root, text = "CODE", font = ('Times 12 bold'), padx=5, pady=10,fg="black", relief=SUNKEN, borderwidth= 4,
            command = GO)
B3.pack(pady=7)

B4 = Button(root, text = "GRAPH", font = ('Times 12 bold'), padx=5, pady=10,fg="black",  relief=SUNKEN, borderwidth= 4,
            command = graph)
B4.pack(pady=7, anchor = W)

# ## to show result for automatic feed
# result_label_auto = Label(font = ('Arial 10 bold'),  borderwidth=10)
# result_label_auto.grid(row = 1, column = 3)


root.mainloop()

























