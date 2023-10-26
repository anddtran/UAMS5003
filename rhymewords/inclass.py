import pandas as pd

#reverse function 
def reverse(x): 
    reversed_word = x[::-1]
    return reversed_word

#access dataframe['RWORDS'] row, match it to y, give the matching row in 'RFREQ' column
def find_frequency(data, y): 
    frequency = data[data['RWORDS'] == y]['RFREQ']
    return frequency.values[0] #return the value only

if __name__ == '__main__':
    #access dataframe using dataframe[column_name] and make a list of column 0
    data = pd.read_excel('bag_of_words.xlsx')
    rwords = list(data['RWORDS']) 
    unique_words = list(set(rwords))

    reverse_words = [reverse(word) for word in unique_words]
    sorted_words = sorted(reverse_words)
    rhyme_words = [reverse(word) for word in sorted_words]
    frequency_reorder = [find_frequency(data, x) for x in rhyme_words]

    dataframe = pd.DataFrame({'rhyme_words': rhyme_words, 'frequency_reorder': frequency_reorder}) #create dataframe

    #outputs to xlsx file without the index column from the dataframe
    file_path = './output.xlsx'
    dataframe.to_excel(file_path, index=False, engine='openpyxl') 
    print(dataframe)