from tkinter import *
import pandas as pd
import numpy as np
import seaborn as sb
from scipy import stats
import matplotlib.pyplot as plt

root = Tk()
root.geometry("1600x900")

def CHECK():
    data_1 = entry_1.get()
    data_2 = entry_2.get()
    data_3 = entry_3.get()
    data_4 = entry_4.get()
    data_5 = entry_5.get()
    data_6 = entry_6.get()
    data_7 = entry_7.get()
    data_8 = entry_8.get()
    data_9 = entry_9.get()
    data_10 = entry_10.get()

    df = pd.DataFrame({'SNo':[1,2,3,4,5,6,7,8,9,10],'Data':[data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8, data_9, data_10]})

    X = df.iloc[:,:-1].values
    Y = df.iloc[:,1].values

    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, random_state = 0, test_size = 0.5)

    from sklearn.linear_model import LinearRegression
    reg = LinearRegression()

    reg.fit(X_train, Y_train)
    Y_predict = reg.predict(X_test)

    Y_predict_val = reg.predict(np.array(11).reshape(1,1))
    # print(Y_predict_val)

    r2_score = reg.score(X_train,Y_train)
    # print(r2_score)
    accuracy = r2_score * 100



    predicted_value_label = Label(root, text = f"The predicted value from the data is {Y_predict_val}\nAccuracy --> {accuracy}%", font = ('Corbel 20 bold underline'))
    predicted_value_label.place(x = 600, y = 650)

    plt.scatter(X, Y, color = 'red', label = "Scatter data")
    plt.title('Plot of the Entered Data')
    plt.xlabel('SNo')
    plt.ylabel('Entered Data')
    plt.show()
# --------------------------------------------------------------------------------------------------------------------------
Title_Label = Label(root, text = "Machine Learning Prediction Model - By Sparsh", font = ('Algerian 25 bold underline'))
Title_Label.pack()

entry_label_1 = Label(root, text = "Data 1", font = ('Bahnschrift 15'))
entry_label_1.place(x = 700, y = 95)

entry_1 = Entry(root, width = 25)
entry_1.place(x = 770, y = 100)

entry_label_2 = Label(root, text = "Data 2", font = ('Bahnschrift 15'))
entry_label_2.place(x = 700, y = 145)

entry_2 = Entry(root, width = 25)
entry_2.place(x = 770, y = 150)

entry_label_3 = Label(root, text = "Data 3", font = ('Bahnschrift 15'))
entry_label_3.place(x = 700, y = 195)

entry_3 = Entry(root, width = 25)
entry_3.place(x = 770, y = 200)
#
entry_label_4 = Label(root, text = "Data 4", font = ('Bahnschrift 15'))
entry_label_4.place(x = 700, y = 245)

entry_4 = Entry(root, width = 25)
entry_4.place(x = 770, y = 250)
#
entry_label_5 = Label(root, text = "Data 5", font = ('Bahnschrift 15'))
entry_label_5.place(x = 700, y = 295)

entry_5 = Entry(root, width = 25)
entry_5.place(x = 770, y = 300)

entry_label_6 = Label(root, text = "Data 6", font = ('Bahnschrift 15'))
entry_label_6.place(x = 700, y = 345)

entry_6 = Entry(root, width = 25)
entry_6.place(x = 770, y = 350)

entry_label_7 = Label(root, text = "Data 7", font = ('Bahnschrift 15'))
entry_label_7.place(x = 700, y = 395)

entry_7 = Entry(root, width = 25)
entry_7.place(x = 770, y = 400)

entry_label_8 = Label(root, text = "Data 8", font = ('Bahnschrift 15'))
entry_label_8.place(x = 700, y = 445)

entry_8 = Entry(root, width = 25)
entry_8.place(x = 770, y = 450)

entry_label_9 = Label(root, text = "Data 9", font = ('Bahnschrift 15'))
entry_label_9.place(x = 700, y = 495)

entry_9 = Entry(root, width = 25)
entry_9.place(x = 770, y = 500)

entry_label_10 = Label(root, text = "Data 10", font = ('Bahnschrift 15'))
entry_label_10.place(x = 700, y = 545)

entry_10 = Entry(root, width = 25)
entry_10.place(x = 770, y = 550)

check_button = Button(root, text = "CHECK", bg = 'black', fg = 'white', activebackground = 'yellow', font = ('Bahnschrift 15 bold'), command = CHECK)
check_button.place(x = 770, y = 600)

root.mainloop()
