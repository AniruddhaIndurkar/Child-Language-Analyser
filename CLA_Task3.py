"""
Name: Aniruddha Indurkar

We make use of pandas to make use of dataframe. Matplotlib is used for graphs and numpy is used for manipulations to
dataframe.
Once the task 3 script is run the visualisation images will be saved inside the folder ENNI Dataset.
Assumptions made:
1. Two objects if SLI and TD class have been made in task 2 and they are imported.
2. 6 visualisation plots of the statistics are saved in the same working directory.
3. Numpy, pandas and matplotlib are already installed
4. Task 1 and task 2 have been completed successfully
5. We assume that Matplotlib, numpy and pandas module is successful and we are running the scripts after installation.

All the references for the code are cited in the document
"""

from task2_29389429 import TD_class,SLI_class,input_path

#for using a data frame and plotting we use pandas and matplotlib respectively
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


#We create a new list from the objects SLI and TD lists in order to obtain a joint data set for the class
data=[TD_class.data_list,SLI_class.data_list]

class task3():

    def __init__(self,data):

        #Create column names
        self.labels=['Transcript','No. of Repititions','No. of Grammatical Errors','No. of Retraces',\
                     'No. of Pauses','Size of Vocabulary','Length of Transcripts']

        #Create an empty Data Frame
        df = pd.DataFrame()

        #We append the two lists for SLI and TD to form a data frame
        #Reference to the below line of code is cited in the document
        for i in data:

            df = df.append(pd.DataFrame(i, columns=self.labels)).reset_index(drop=True)

        #Appended data frame is stored for the class three instance
        self.data_frame = df

        #Append a column using values from the file name to attach to a particular group
        self.data_frame['Group'] = np.where(self.data_frame.Transcript.str[0] == 'S', 'SLI', 'TD')

    def __str__(self):

        #In order to display all the columns in print we use option_context function
        #Reference for the below line of code is cited in the document
        with pd.option_context('display.max_rows', None, 'display.max_columns', None) as printframe:
            print(self.data_frame)

        return str(printframe)

    def compute_average(self):


        #We group the data frame according to the SLI and TD group and calculate the mean
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            print(self.data_frame.groupby(['Group']).mean())

        return self.data_frame.groupby(['Group']).mean()

    def visualisation_statistics(self):

        #We reshape the data by transposing in order to visualise the statistics from a data frame
        vis_data = self.data_frame.groupby(['Group']).mean().T

        #Run the visualisation and save it to a file inside the current working directory
        for i in range(vis_data.shape[0]):

            #to create a new plot everytime
            plt.figure(i)

            #plotting the bar graph
            plt.bar([0, 1], [vis_data.iloc[i, 0], vis_data.iloc[i, 1]], color=["b", "g"])

            #rename the xlabels
            #refeence to the below line of code is cited in the document
            plt.xticks([0,1],['SLI','TD'])

            #giving title
            plt.title(str(vis_data.index[i]))

            #values of the bars put as labels
            #Reference for below line of code is cited in the document
            plt.text(0, vis_data.iloc[i, 0] + 0.5, vis_data.iloc[i, 0])
            plt.text(1, vis_data.iloc[i, 1] + 0.5, vis_data.iloc[i, 1])

            #saving the file
            plt.savefig(input_path+str(vis_data.index[i]) + ".png", format='png')

            print("\nVisualisation {} saved successfully in the directory".format(vis_data.index[i]))


if __name__=="__main__":
    t3=task3(data)
    print(t3)
    t3.compute_average()
    t3.visualisation_statistics()
