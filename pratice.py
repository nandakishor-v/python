# import required libraries 
import pandas as pd 
import re 

# creating Dataframe with 
# name and their comments 


df = pd.DataFrame({ 
	'Name' : ['Akash', 'Ashish', 'Ayush', 
			'Diksha' , 'Radhika'], 
	
	'Comments': ['Hey! Akash how r u' , 
				'Why are you asking this to me?' , 
				'Today, what we are going to do.' , 
				'No plans for today why?' , 
				'Wedding plans, what are you saying?']}, 
	
	columns = ['Name', 'Comments'] 
	) 

# show the Dataframe 
print(df)
# define a function for extracting 
# the punctuations 
def check_find_punctuations(text): 
	
	# regular expression containing 
	# all punctuation 
	result = re.findall(r'[!"\$%&\'()*+,\-.\/:;=#@?\[\\\]^_`{|}~]*', 
						text) 
	
	# form a string 
	string = "".join(result) 
	
	# list of strings return 
	return list(string) 
	
# creating new column name 
# as a punctuation_used and 
# applying user defined function 
# on each rows of Comments column 
df['punctuation_used'] = df['Comments'].apply( 
						lambda x : check_find_punctuations(x) 
						) 

# show the Dataframe 
print(df)
