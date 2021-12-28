############################### USING PATH ###########################
#Text = open('PATH_NAME', 'r')
#texts =  Text.read() #this line is to import all the text in the file from the path

#####################################################################

############## OR USING A STRING OF TEXT 
texts ="Business owners across the country, built hotels and residencies to serve the accommodation needs of a wide range of persons from travelers to family members and even young students. At the beginning, these inns only offered basic services, but as time went by and demand for short-term accommodation grew, the hotel owners became prepared to provide guests with more facilities. Since then, the hotel industry expanded further as people were willing to pay more for better quality services. This industry has always striven to fulfil the changing demands of the society and has developed into an essential part of the economy. Today, travelers can find different types of accommodation based on their budget, from cheap bed and breakfasts, to luxurious 5-star hotels. Hotel Management can be defined as the organizing, monitoring and controlling of resources in order to ensure the running of a hotel in any due time." 

############## HERE every single special characters are replaced with NOTHING

replaced_text = texts.replace(",","")

replaced_text = replaced_text.replace(".","")

replaced_text = replaced_text.replace("-","")

print(replaced_text)


print(" REPLACED ===========================================================================================")
replaced_text = replaced_text.lower() #all texts are converted to lower case
split_texts = replaced_text.split() #here all texts are separated individually no matter the if they repeated
print(split_texts)

print("===========================================================================================")
word_dic = {}

for word in split_texts:
    word_dic[word] = word_dic.get(word, 0) + 1 #here the words will be added in the dictionary as a key and if it is repeated the value is incremented

print(word_dic)

print("===========================================================================================")
word_freq = []

for key,value in word_dic.items():
    word_freq.append((value,key)) #here, the key and value are swapped for eazy sorting

print(word_freq)

print("===========================================================================================")
word_freq.sort(reverse=True)

print(word_freq)
print("===========================================================================================")