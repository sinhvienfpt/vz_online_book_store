import pandas as pd

df = pd.read_csv('D:\\PROGRAMS\\vz_BOOKSTORE\DATA\Raw_CSVs\\books.csv')

#Get author df
author_col = df['Authors']
author_set = set()

for i in range(len(author_col)):
    authors_list = author_col[i][2:].split(',')
    for author in authors_list:
        author = author.strip()
        author_set.add(author)

author_df = pd.DataFrame(author_set, columns=['Author'])
author_df = author_df[1:]
author_df.to_csv('D:\\PROGRAMS\\vz_BOOKSTORE\DATA\CSVs\\Authors.csv', index=True)
