


from chord import Chord
import numpy as np
import pandas as pd
import itertools
from ast import literal_eval





#Removes the dictionary and stores as a list
def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        return sorted(names)

    return []





df = pd.read_csv(r"tmdb_5000_movies.csv") # Importing the dataset
data = pd.DataFrame(df,columns=['genres']) # taking only required columns


genres = data['genres'].apply(literal_eval)#Safely evaluate an expression node or a string containing a Python literal 
genres = genres[genres.str.len() > 0] # Remove empty strings


genres = genres.apply(get_list) #Calling the Function


genres = [list(itertools.combinations(i,2)) for i in genres] #Commbines 2 genres  to form a matrix


genres = list(itertools.chain.from_iterable((i, i[::-1]) for c_ in genres for i in c_)) #Creates 2 columns with genres


matrix = pd.pivot_table(pd.DataFrame(genres), index=0, columns=1, aggfunc="size", fill_value=0).values.tolist() #Creating  a matrix


names = np.unique(genres).tolist() #taking a list of unique genres


colors = ["#e6194B", "#3cb44b", "#ffe119", "#4363d8", "#f58231",
    "#911eb4", "#42d4f4", "#f032e6", "#bfef45", "#fabebe",
    "#469990", "#e6beff", "#9A6324", "#fffac8", "#800000",
    "#aaffc3", "#a9a9a9", "#ffd8b1", "#000075", "#a9a9a9",];





Chord(matrix, names, colors=colors, wrap_labels=False, margin=50).to_html()  #output

