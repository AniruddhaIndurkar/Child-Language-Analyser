'''
Name : Aniruddha Indurkar

We make a few assumptions regarding the task:
1. The ENNI Dataset folder in the working directory
2. The ENNI Dataset folder contains 2 folders named TD and SLI
3. These folders combined contain 20 files for SLI and TD kept in the format "TD-XX.txt" or "SLI-XX.txt"
4. re and os modules are already installed
5. Instead of retaining [*m:+ed], I replaced it by [*] to make it easier and similarly for [*m]

All the references for the code have been cited in the documentation
'''

#Importing the 'Re' for regular expressions
import re
#Using the OS import library to find out the OS system name, list of files in the directory and to make directories
from os import name,listdir,makedirs,getcwd

if name=='posix':

    input_path=str(getcwd())+"/ENNI Dataset/"

if name=='nt':

    input_path=str(getcwd())+"\\ENNI Dataset\\"

# we make use of the below two lists for validation
TD = ['TD-1.txt', 'TD-2.txt', 'TD-3.txt', 'TD-4.txt', 'TD-5.txt', 'TD-6.txt', 'TD-7.txt', 'TD-8.txt', 'TD-9.txt',
      'TD-10.txt']
SLI = ['SLI-1.txt', 'SLI-2.txt', 'SLI-3.txt', 'SLI-4.txt', 'SLI-5.txt', 'SLI-6.txt', 'SLI-7.txt', 'SLI-8.txt',
       'SLI-9.txt', 'SLI-10.txt']

def pre_process(path,file):

    '''
    Function to preprocess the files and extract the required data and save it in the same directory.
    :param path: Path in which the TD and SLI folders are stored.
    :param file: Name of the file
    :return: prints the name of the file that was written
    '''

    #We initiate a few empty lists in order to store the data
    extract = []
    dt = []

    output=""

    #we split into two conditions depending on the system used
    if name=="posix":
        #If the file is SLI then start open and put the data in the list called extract
        if file[0]=='S':
            output=path + "SLI_cleaned/" + file

            with open(path + "SLI/" + file, 'r') as myfile:
                extract = myfile.readlines()
            myfile.close()

        #If the file is TD then start open and put the data in the list called extract
        if file[0]=='T':
            output=path + "TD_cleaned/" + file

            with open(path + "TD/" + file, 'r') as myfile:
                extract = myfile.readlines()
            myfile.close()

    #Do the similar function for windows OS
    if name=="nt":

        if file[0]=='T':
            output = path + "TD_cleaned\\" + file

            with open(path + "TD\\" + file, 'r') as myfile:
                extract = myfile.readlines()
            myfile.close()
        if file[0]=='S':
            output = path + "SLI_cleaned\\" + file

            with open(path + "SLI\\" + file, 'r') as myfile:
                extract = myfile.readlines()
            myfile.close()

    #We perform the tasks on each sentence of the extract by extracting only the child transcripts
    for sentence in extract:
        i = extract.index(sentence)

        if sentence[:4] == "*CHI":
            j = 1

            #We create a while loop in order to append the next lines till we get %mor as this is recognised pattern
            #in all the files
            while extract[i + j][:4] != "%mor":
                sentence = sentence + extract[i + j].strip()
                j += 1

            #Append the extract and store it in the list dt
            dt.append(sentence[5:].strip())

    data = []

    # perform task a
    for sentence in dt:

        #We first remove all the characters that do not begin with '[/' or '[*' . post this the characters can contain
        #anything in between
        sentence = re.sub(r'\[[^/*][\w\s\W]*?\]', "", sentence)

        #Then we remove only '(..)' or '(...)'
        sentence = re.sub(r'\(\.{2,}\)', "", sentence)

        #We then substiture [* m: +ed] to [*] for simplifying (Grammatical errors)
        sentence = re.sub(r'\[\* m\]',"[*]",sentence)
        sentence = re.sub(r'\[\* m:\+ed\]',"[*]",sentence)

        #These sentences are appended to the list
        data.append(sentence)



    #We perform task b,c & d and initiate a list of retainers and special characters that need to be replaced
    txt = []
    retainers = ["[//]", "[/]", "[*]", "(.)"]
    special = ["<", ">", "(", ")"]

    for sentence in data:

        line = []

        #In this case we split the sentences into single words separated by spaces and then perform replace of character
        for word in sentence.split():

            if word[0] == "[" or word == "(.)":

                if word in retainers:
                    line.append(word)
                else:
                    pass

            #The words with prefixes are not appended
            elif word[0] == "&" or word[0] == "+":
                pass

            elif word[0] == '(' and word[1] != '.':

                #removing infixes of '(' or ')'
                if word[len(word) - 1] == ")":

                    for i in special:
                        word = word.replace(i, "")

                    line.append(word[:len(word) - 1])
                else:

                    for i in special:
                        word = word.replace(i, "")

                    line.append(word[:len(word)])

            elif word[0] != '(' and word[len(word) - 1] == ')':
                # remove suffix
                line.append(word[:len(word) - 1])

            else:

                # remove infix
                for char in special:
                    word = word.replace(char, "")

                line.append(word)

        line = " ".join(line)

        #This txt list contains the data processed in the required format
        txt.append(line)

    #Here the output takes in the output string made from the path provided to the function
    with open(output, "w+") as f:
        for i in txt:
            f.write(i + "\n")

    f.close()

    return(print("File {} written successfully".format(file)))


def appender(list_files,check_list):
    '''

    :param list_files: list of files are taken
    :param check_list: validation file list
    :return: returns the list after validating with the validation file list
    '''

    file = []

    for i in list_files:

        if i in check_list:
            file.append(i)

        else:
            pass

    print("==========================================")
    print('There are {} files'.format(len(file)))
    print(file)
    print("==========================================")
    return file

def harmoniser(path):
    '''

    :param path: provide the path of the working directory
    :return: True or False
    '''

    #We initiate a few variables required for validation and file checks
    pathTD = path + "TD"
    pathSLI = path + "SLI"
    try:
        filename_TD = listdir(pathTD)
    except:
        print('Please check the path again as it does not exist')

    try:
        filename_SLI = listdir(pathSLI)
    except:
        print('Please check the path again as it does not exist')

    file_TD=appender(filename_TD,TD)
    file_SLI= appender(filename_SLI,SLI)

    #Make seperate directories for SLI and TD cleaned files
    try:
        makedirs(pathTD + "_cleaned")
    except:
        pass

    try:
        makedirs(pathSLI + "_cleaned")
    except:
        pass

    #If there are 10 files then proceed with the hamronisation
    if set(file_TD)==set(TD) and set(file_SLI)==set(SLI):

        #Preprocess if the things are good
        for i in file_TD:
            pre_process(path, i)

        for i in file_SLI:
            pre_process(path, i)
        print("=================================================")
        print("\nThe harmonisation was successful")
        return False

    else:
        print("\nCheck the files again and check the user input path")
        return True

#Integrated the functions in the structure in order to complete the loop in case there is something wrong
def structure():
    '''
    Function to integrate the task 1
    :return:Returns nothing
    '''
    try:
        harmoniser(input_path)
        print("The task 1 was completed successfully")
        print("=================================================")
    except:
        print("The task 1 was unsuccessful")
        print("=================================================")

if __name__ =='__main__':
    structure()

