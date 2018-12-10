"""
Name: Aniruddha Indurkar

In this task , we make a following assumptions according to the requirements in task 3:
1. Objects in class for task 2 are only to view the data for print function in this class
2. I created a separate list in order for the class in-order to pass it onto task 3 as a list.
3. All the objects and functions required from task1 are imported into this module
4. We make use of os library to deal with cleaned files
5. Name function from os is used to identify the system used (posix,nt)

All the references for the code are given in the documentation

"""

#Requirement from task 1 and os library
from task1_29389429 import input_path,TD,SLI,appender
from os import listdir,name

#We take the path from the users for the directory where we stored the cleaned data
path=input_path

#Class defined for task2
class task2():

    def __init__(self):

        self.length = 0
        self.size = 0
        self.reps = 0
        self.retrace = 0
        self.errors = 0
        self.pause = 0
        self.file = []
        self.data_list=[]

    def __str__(self):

        #in order to print we use the print formatter
        print_statistics = ""
        print_statistics += "Length of Transcript: {}\n".format(self.length) + \
                            "No. of Retraces: {}\n".format(self.retrace) \
             + "No. of Repetitions: {}\nGrammatical errors:{}\nPauses: {}".format(self.reps, self.errors, self.pause) \
             + "\nSize of vocabulary: {}".format(self.size)

        return print_statistics

    def analyse_script(self, cleaned_file,file_name):

        extract = cleaned_file.readlines()

        file=[]

        #Defined to separate them from the vocabulary
        punctuations = ["?", ".", "!", "(.)", "[//]", "[/]", "[*]", ",", ":", ";", "$", '%']
        file_set = set()

        for each in extract:

            file.append(each.split())

        for each in file:

            for i in each:
                self.file.append(i)

        a = 0
        #We create a set in order to remove the duplicate elements to get the size of vocabulary
        for each in self.file:

            if each not in punctuations:
                file_set.add(each)
                a +=1

        #list to append each file data separately
        file_list = []

        # we append this list to the class in order to save data for each iteration
        file_list.append(file_name[:len(file_name)-4])
        file_list.append(self.file.count("[/]"))
        file_list.append(self.file.count("[*]"))
        file_list.append(self.file.count("[//]"))
        file_list.append(self.file.count("(.)"))
        file_list.append(len(file_set))
        file_list.append(self.file.count(".") + self.file.count("?") + self.file.count("!"))

        #Collated data statistitics
        self.data_list.append(file_list)

        self.length += self.file.count(".") + self.file.count("?") + self.file.count("!")

        self.reps += self.file.count("[/]")

        self.retrace += self.file.count("[//]")

        self.pause += self.file.count("(.)")

        self.errors += self.file.count("[*]")

        self.size += len(file_set)

        self.file=[]

#We give the path of the new cleaned folder
pathTD = path + "TD_cleaned"
pathSLI = path + "SLI_cleaned"

#Below line of code is used to get the filenames from the directory and pass it to the task3().Analyser()
try:
    filename_TD = listdir(pathTD)
except:
    print('Please check the path again as it does not exist')

try:
    filename_SLI = listdir(pathSLI)
except:
    print('Please check the path again it does not exist')

file_TD = appender(filename_TD,TD)
file_SLI = appender(filename_SLI,SLI)


SLI_class = task2()
TD_class = task2()


if name=='posix':
    for  i in file_TD:

        with open(pathTD+'/' + i, 'r') as myfile:


            TD_class.analyse_script(myfile,i)
        myfile.close()

    for i in file_SLI:

        with open(pathSLI+'/' + i, 'r') as myfile:

            SLI_class.analyse_script(myfile,i)
        myfile.close()

if name == 'nt':
    for i in file_TD:

        with open(pathTD + '\\' + i, 'r') as myfile:
            TD_class.analyse_script(myfile, i)

        myfile.close()

    for i in file_SLI:

        with open(pathSLI + '\\' + i, 'r') as myfile:
            SLI_class.analyse_script(myfile, i)

        myfile.close()


if __name__=='__main__':

    print('==================================')
    print("TD")
    print('==================================')
    print(TD_class)
    print("==================================")
    print("SLI")
    print('==================================')
    print(SLI_class)
    print('==================================')
