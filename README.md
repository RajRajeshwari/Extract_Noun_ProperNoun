# Extract_Noun_ProperNoun

Code to extract and create separate files for all the nouns and proper nouns, along with all their glosses present in 
the WordNet dictionary created by Princeton University.
This code was developed as a part of my internship assignment at Anusaaraka lab, IIIT Hyderabad. 
The data.noun and index.noun files are slightly modified. 
These files can be found in your local machine (after installing WordNet browser) at the given location:
  /usr/share/wordnet
The output files produced can be used in NLP or related fields.

For developers:
  The code can be changed to print in the format you require. The program is properly commented for your ease.
  data.noun and index.noun - data files
  NounProperNoun.py - code file
To run the code:
   Place the data.noun and index.noun files in the same directory as the code. 
   python NounProperNoun.py  
After code execution we get two output files:
  NounGlosses.dic - all the nouns along with all possible senses/glosses
  ProperNounGloss.dic - all the proper nouns with all possible senses/glosses
  
If you directly want the output files, it can be found under the names- NounGlosses.dic and ProperNounGloss.dic respectively.
