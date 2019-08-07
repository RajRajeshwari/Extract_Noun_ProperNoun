#packages used
import os
import re

#files used
n_ind = open('index.noun','r').readlines()
n_data = open('data.noun','r').readlines()
noun_dic = open('NounGlosses.dic','w')
proper_nouns = open('ProperNounGloss.dic','w')

#variables and their content
indices = list() # to store the gloss indices of the keyword
meaning = list() # to store the glosses of the keyword
Proper_n_indices = list() # to store the indices of all the proper nouns

#temporary variables used in the code and there uses:
    # i,j - is the iterator 
    # temp - is a list which stores the values from the split operation based on space on each line of data.noun file, we need the first index of the temp to be stored in the 'indices' list
    # temp1 - is a list which stores the values from the split operation based on '|'. The part of the string after '|' is the gloss of the word and is stored in the 'meaning' list
    # tem_split - split operation is again performed on temp1[0] to find all the proper nouns and store the indices of those words in 'Proper_n_indices' list
   
for i1 in range(0,len(n_data)): 
    temp = n_data[i1].split(' ')
    temp1 = n_data[i1].split('|')
    tem_split = temp1[0].split(' ')
    if tem_split[4].isupper():
        Proper_n_indices.append(tem_split[0])
    elif not tem_split[4].islower() and not tem_split[4].isupper():
        Proper_n_indices.append(tem_split[0])
    elif bool(re.search(r'\d', tem_split[4])):
        Proper_n_indices.append(tem_split[0])
    indices.append(temp[0])
    meaning.append(temp1[1])

for i in range(0,len(n_ind)): 
    temp2 = n_ind[i].split(' ')
    temp2[0] = re.sub('\._','.',temp2[0])
    temp2[0] = re.sub('_',' ',temp2[0])
    senses = int(temp2[2])
    if temp2[-senses-2] not in Proper_n_indices:
        noun_dic.write(temp2[0]+'\n')
    else:
        proper_nouns.write(temp2[0]+'\n')
    for j in range(senses,0,-1):
        if temp2[-j-2] not in Proper_n_indices:
            if temp2[-j-2] in indices:
                gloss_ind = indices.index(temp2[-j-2])
                meaning[gloss_ind] = meaning[gloss_ind].lstrip()
                meaning[gloss_ind] = meaning[gloss_ind].replace('\n','')
                meaning[gloss_ind] = re.sub(r'\".*\"|\"','',meaning[gloss_ind])
                noun_dic.write(meaning[gloss_ind].rstrip()+"\n")
        else:
            gloss_ind = indices.index(temp2[-j-2])
            meaning[gloss_ind] = meaning[gloss_ind].lstrip()
            meaning[gloss_ind] = meaning[gloss_ind].replace('\n','')
            meaning[gloss_ind] = re.sub(r'\".*\"|\"','',meaning[gloss_ind])
            proper_nouns.write(meaning[gloss_ind].rstrip()+"\n")

noun_dic.close()
proper_nouns.close()
