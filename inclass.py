import pandas as pd

#access dataframe using dataframe[column_name] and make a list of column 0
data = pd.read_excel('bag_of_words.xlsx')
rwords = list(data['RWORDS']) 

#reverse function 
def reverse(x): 
    reversed_word = x[::-1]
    return reversed_word

#access dataframe['RWORDS'] row, match it to y, give the matching row in 'RFREQ' column
def find_frequency(data, y): 
    frequency = data[data['RWORDS'] == y]['RFREQ']
    return frequency.values[0] #return the value only

reverse_words = [reverse(word) for word in rwords]
sorted_words = sorted(reverse_words)
rhyme_words = [reverse(word) for word in sorted_words]
frequency_reorder = [find_frequency(data, x) for x in rhyme_words]

dataframe = pd.DataFrame() #create empty dataframe
dataframe['rhyme_words'] = rhyme_words #dataframe column 0
dataframe['frequency_reorder'] = frequency_reorder #dataframe column 1

#outputs to xlsx file without the index column from the dataframe
file_path = '/Users/andrewtran/Documents/pycharm/5003/output.xlsx'
dataframe.to_excel(file_path, index=False, engine='openpyxl') 
print(dataframe)