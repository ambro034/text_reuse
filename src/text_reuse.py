import pandas as pd

from IPython.display import HTML as html_print
from IPython.display import display

import re

import numpy as np

###################
### Definitions ###
###################

### Identify Reuse ###

def id_reuse(str1,str2,l):

  new1 = str1.lower().split()
  new2 = str2.lower().split()

  #print(new1)
  #print(new2)

  long_answer = []

  for i in range(0,len(new1)-1):
    for j in range(0,len(new2)-1):
      ans = []
      if new1[i]==new2[j]:
        n=i
        m=j
        while new1[n]==new2[m]:

          ans.append(new1[n])
          if n<len(new1)-1 and m<len(new2)-1:
            n+=1
            m+=1
          else:
            break


      if len(ans)>=len(long_answer):
        long_answer = list(ans)

  if len(long_answer) >= l:
    return" ".join(long_answer)


### Print in Color ###

from IPython.display import HTML as html_print
from IPython.display import display

def cstr(s, color='black'):
    return "<text style=color:{}>{}</text>".format(color, s)

def print_color(t):
    display(html_print(' '.join([cstr(ti, color=ci) for ti,ci in t])))

### ONE LOOP ####

def reuse_loops(str1,str2,l):

  m_str1 = str1.lower()
  m_str1 = re.sub('([.,!?()-])', r' \1 ', m_str1)
  m_str2 = str2.lower()
  m_str2 = re.sub('([.,!?()-])', r' \1 ', m_str2)

  ##################
  # First Split

  # Get reused phrase
  reuse = id_reuse(m_str1,m_str2,l)

  # split phrases string #1
  new_str = []
  try:
    str1_pre = m_str1.find(reuse)
    new_str.append((str1_pre, 'green'))
  except IndexError:
    False
  new_str.append((reuse,'black'))
  try:
    str1_post = m_str1.split(reuse)[1]
    new_str.append((str1_post, 'green'))
  except IndexError:
    False
  #print(new_str)

  # split phrases string #2
  old_str = []
  try:
    str2_pre = m_str2.split(reuse)[0]
    old_str.append((str2_pre, 'red'))
  except IndexError:
    False
  old_str.append((reuse,'black'))
  try:
    str2_post = m_str2.split(reuse)[1]
    old_str.append((str2_post, 'red'))
  except IndexError:
    False
  #print(old_str[1][1])

  #####################
  # Additional Splits

  for x in range(len(new_str)):
    if new_str[x][1] != 'black':
      for y in range(len(old_str)):
        if old_str[y][1] != 'black':
          #print('x is:', x)
          #print('str x is:', new_str[x][0])
          #print('y is:', y)
          #print('str y is:', old_str[y][0])
          reuse_a = id_reuse(new_str[x][0],old_str[y][0],l)
          if reuse_a == None:
            continue
          else:
            print('reuse_a is:', reuse_a)

            # split phrases string #1
            g = x
            m_str_1_a = new_str[x][0]
            new_str.pop(x)

            try:
              str1_pre = m_str_1_a.split(reuse_a)[0]
              new_str.insert(g,(str1_pre, 'green'))
            except IndexError:
              False
            new_str.insert(g+1,(reuse_a,'black'))
            try:
              str1_post = m_str_1_a.split(reuse_a)[1]
              new_str.insert(g+2,(str1_post, 'green'))
            except IndexError:
              False

            print(new_str)

            # split phrases string #2
            g = x
            m_str_2_a = old_str[x][0]
            old_str.pop(x)

            try:
              str2_pre = m_str_2_a.split(reuse_a)[0]
              old_str.insert(g,(str2_pre, 'red'))
            except IndexError:
              False
            old_str.insert(g+1,(reuse_a,'black'))
            try:
              str2_post = m_str_2_a.split(reuse_a)[1]
              old_str.insert(g+2,(str2_post, 'red'))
            except IndexError:
              False

            print(old_str)


  #####################
  # PRINT
  print('New Language:')
  print_color((new_str))

  print('Old Language:')
  print_color((old_str))


### IDENTIFY ALL REUSE ###

def reuse_loops2(str1,str2,l):

  ##################
  # Pre Processing

  m_str1 = str1.lower()
  m_str1 = re.sub('([a-zA-Z.,;!?()-])([.,;!?()-])', r'\1 \2', m_str1) #  !()-[]{};:'"\,<>./?@#$%^&*_~
  m_str1 = re.sub('([.,;!?()-])([a-zA-Z])', r'\1 \2', m_str1)
  m_str2 = str2.lower()
  m_str2 = re.sub('([a-zA-Z.,;!?()-])([.,;!?()-])', r'\1 \2', m_str2)
  m_str2 = re.sub('([.,;!?()-])([a-zA-Z])', r'\1 \2', m_str2)

  ##################
  # First Split

  # Get reused phrase
  reuse = id_reuse(m_str1,m_str2,l)


  if reuse != None:

    # split phrases string #1
    new_str = []
    try:
      str1_pre = m_str1.split(reuse)[0]
      #print(m_str1.split(reuse))
      new_str.append((str1_pre, 'green'))
    except IndexError:
      False
    new_str.append((reuse,'black'))
    try:
      str1_post = m_str1.split(reuse)[1]
      new_str.append((str1_post, 'green'))
    except IndexError:
      False
    #print(new_str)

    # split phrases string #2
    old_str = []
    try:
      str2_pre = m_str2.split(reuse)[0]
      old_str.append((str2_pre, 'red'))
    except IndexError:
      False
    old_str.append((reuse,'black'))
    try:
      str2_post = m_str2.split(reuse)[1]
      old_str.append((str2_post, 'red'))
    except IndexError:
      False
    #print(old_str[1][1])

    #####################
    # Additional Splits
    s = -1
    for s in range(round(int((len(m_str1.split()))/(l)),0)):

      #print('####')
      #print(s)
      #print(new_str)
      #print(old_str)

      s+=1

      for x in range(len(new_str)):
        if new_str[x][1] != 'black':
          for y in range(len(old_str)):
            if old_str[y][1] != 'black':
              #print('x is:', x)
              #print('str x is:', new_str[x][0])
              #print('y is:', y)
              #print('str y is:', old_str[y][0])
              reuse_a = id_reuse(new_str[x][0],old_str[y][0],l)
              if reuse_a == None:
                #print('reuse_a is: NONE')
                continue
              else:
                #print('reuse_a is:', reuse_a)

                # split phrases string #1
                g = x
                #print('g is:', g)
                m_str_1_a = new_str[g][0]
                #print(new_str[g][0])
                #print(m_str_1_a.split(reuse_a))
                new_str.pop(g)

                try:
                  str1_pre = m_str_1_a.split(reuse_a)[0]
                  #print(g, (str1_pre, 'green'))
                  new_str.insert(g,(str1_pre, 'green'))
                except IndexError:
                  False
                new_str.insert(g+1,(reuse_a,'black'))
                #print(g+1, (reuse_a,'black'))
                try:
                  str1_post = m_str_1_a.split(reuse_a)[1]
                  new_str.insert(g+2,(str1_post, 'green'))
                  #print(g+2, (str1_post, 'green'))
                except IndexError:
                  False

                #print(new_str)

                # split phrases string #2
                w = y
                #print('w is:', w)
                m_str_2_a = old_str[w][0]
                old_str.pop(w)

                try:
                  str2_pre = m_str_2_a.split(reuse_a)[0]
                  old_str.insert(w,(str2_pre, 'red'))
                except IndexError:
                  False
                old_str.insert(w+1,(reuse_a,'black'))
                try:
                  str2_post = m_str_2_a.split(reuse_a)[1]
                  old_str.insert(w+2,(str2_post, 'red'))
                except IndexError:
                  False

              #print(old_str)

  else:
    new_str = []
    new_str.append((m_str1, 'green'))

    old_str = []
    old_str.append((m_str2, 'red'))


  #####################
  return new_str, old_str


  
################
### OUT PUTS ###
################

### Single Color ###

def reuse_color_coded(str1,str2,l):
  new_str, old_str = reuse_loops2(str1,str2,l)

  # PRINT
  print('New Language:')
  print_color((new_str))

  print('Old Language:')
  print_color((old_str))

#### Multiple Color ###

def reuse_color_coded_dataset(data,id,new_year,old_year,l):

  for x in range(len(data)):

    id_num = data.iloc[x][id]
    new = data.iloc[x][new_year]
    old = data.iloc[x][old_year]

    new_str, old_str = reuse_loops2(new,old,l)

    # PRINT
    print('Statement ID:', id_num)
    print('New Language:')
    print_color((new_str))

    print('Old Language:')
    print_color((old_str))
    print('')

### Dataset to Dataset ###

def reuse_dataset_to_dataset(data,id,new_year,old_year,l):

  ny = data.columns[new_year]
  oy = data.columns[old_year]

  nt = ny+'_Text'
  ntw = ny+'_Text_WC'

  na = ny+'_Added'
  naw = ny+'_Added_WC'
  nr = ny+'_Reused'
  nrw = ny+'_Reused_WC'
  nter = ny+'_Terminated'
  nterw = ny+'_Terminated_WC'

  ot = oy+'_Text'
  otw = oy+'_Text_WC'

  rmnt = ny+'_New_Ratio_of_Match'
  rmot = ny+'_Old_Ratio_of_Match'
  njs = ny+'Jaccard_Similarity'

  clean_data = pd.DataFrame(columns = ['Statement ID', nt, ntw, na, naw, nr, nrw, nter, nterw, ot, otw, rmnt, rmot, njs])

  for x in range(len(data)):

    id_num = data.iloc[x][id]
    new = data.iloc[x][new_year]
    old = data.iloc[x][old_year]

    new_str, old_str = reuse_loops2(new,old,l)

    added = ""
    added2 = ""
    reuse = ""
    reuse2 = ""
    removed = ""
    removed2 = ""

    # Reused text

    for x in range(len(new_str)):
      if new_str[x][1] != 'black':
        if added != "":
          added = " ".join([added, "[...]"])
        added = " ".join([added, new_str[x][0]])
        added2 = " ".join([added2, new_str[x][0]])
      else:
        if reuse != "":
          reuse = " ".join([reuse, "[...]"])
        reuse = " ".join([reuse, new_str[x][0]])
        reuse2 = " ".join([reuse2, new_str[x][0]])

    for x in range(len(old_str)):
      if old_str[x][1] != 'black':
        if removed != "":
          removed = " ".join([removed, "[...]"])
        removed = " ".join([removed, old_str[x][0]])
        removed2 = " ".join([removed2, old_str[x][0]])

    # Counts

    if new != "" and new != "nan":
      new_wc = len(re.findall(r'\w+', new))
    else:
      new_wc = 0

    if added2 != "" and added2 != "nan":
      added_wc = len(re.findall(r'\w+', added2))
    else:
      added_wc = 0

    if reuse2 != "" and reuse2 != "nan":
      reuse_wc = len(re.findall(r'\w+', reuse2))
    else:
      reuse_wc = 0

    if removed2 != "" and removed2 != "nan":
      removed_wc = len(re.findall(r'\w+', removed2))
    else:
      removed_wc = 0

    if old != "" and old != "nan":
      old_wc = len(re.findall(r'\w+', old))
    else:
      old_wc = 0

    # Reuse Calculations

    if new_wc != 0:
      rom_new = reuse_wc/new_wc
    else:
      rom_new = 0
    if old_wc != 0:
      rom_old = reuse_wc/old_wc
    else:
      rom_old = 0

    if new_wc == 0 and old_wc == 0 :
      jac_sim = 0
    else:
      jac_sim = reuse_wc/(new_wc + old_wc)

    clean_data = clean_data._append({'Statement ID':id_num,nt:new,ntw: new_wc, na:added, naw: added_wc, nr:reuse, nrw: reuse_wc, nter:removed, nterw: removed_wc, ot:old, otw: old_wc, rmnt: rom_new, rmot: rom_old, njs: jac_sim},ignore_index=True)
  return clean_data

##############
### Set Up ###
##############

### Dataset Construction ###

def construct_dataset(data,id,new_year,new_year_num,old_year,old_year_num): # data to load, position of the id column, position of the new_year column, position of the old_year column

  nyn = 'y_'+ str(new_year_num)
  oyn = 'y_'+ str(old_year_num)

  dataset = pd.DataFrame({'Statement ID' : [],
                         nyn : [],
                         oyn : []})
  
  if id != False:

    dataset['Statement ID']=data.iloc[:, id].apply(int)
    dataset[nyn]=data.iloc[:, new_year].apply(str)
    dataset[oyn]=data.iloc[:, old_year].apply(str)
  
  else:
    dataset['Statement ID']= range(len(data))
    dataset[nyn]=data.iloc[:, new_year].apply(str)
    dataset[oyn]=data.iloc[:, old_year].apply(str)

  return dataset[['Statement ID',nyn,oyn]]



### IDENTIFY SENTENCES ###

# -*- coding: utf-8 -*-
import re
alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|Prof|Capt|Cpt|Lt|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov|edu|me)"
digits = "([0-9])"
multiple_dots = r'\.{2,}'

def split_into_sentences(text: str) -> list[str]:
    """
    Split the text into sentences.

    If the text contains substrings "<prd>" or "<stop>", they would lead
    to incorrect splitting because they are used as markers for splitting.

    :param text: text to be split into sentences
    :type text: str

    :return: list of sentences
    :rtype: list[str]
    """
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    text = re.sub(digits + "[.]" + digits,"\\1<prd>\\2",text)
    text = re.sub(multiple_dots, lambda match: "<prd>" * len(match.group(0)) + "<stop>", text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = [s.strip() for s in sentences]
    if sentences and not sentences[-1]: sentences = sentences[:-1]
    return sentences

### TEXT STRINGS TO DATAFRAME ###

def reuse_lists_to_dataset(new_year,old_year,l):

  clean_data = pd.DataFrame(columns = ['New ID','New_Text','New_Text_WC','Added','Added_WC', 'Reused', 'Reused_WC', 'Terminated', 'Terminated_WC', 'Old ID', 'Old_Text', 'Old_Text_WC', 'Ratio_of_Match_IN_NEW', 'Ratio_of_Match_FROM_OLD','Jaccard_Similarity'])

# converst to a list of sentences if not already a list
  if isinstance(new_year, list):
    new_year = new_year
  elif isinstance(new_year, str):
    new_year = split_into_sentences(new_year)

  if isinstance(old_year, list):
    old_year = old_year
  elif isinstance(old_year, str):
    old_year = split_into_sentences(old_year)

  new_year.append(" ")
  old_year.append(" ")

  for x in range(len(new_year)):
    id_new = x
    new = new_year[x]
    for y in range(len(old_year)):
      id_old = y
      old = old_year[y]

      new_str, old_str = reuse_loops2(new,old,l)

      added = ""
      added2 = ""
      reuse = ""
      reuse2 = ""
      removed = ""
      removed2 = ""

      # Reused text

      for t in range(len(new_str)):
        if new_str[t][1] != 'black':
          if added != "":
            added = " ".join([added, "[...]"])
          added = " ".join([added, new_str[t][0]])
          added2 = " ".join([added2, new_str[t][0]])
        else:
          if reuse != "":
            reuse = " ".join([reuse, "[...]"])
          reuse = " ".join([reuse, new_str[t][0]])
          reuse2 = " ".join([reuse2, new_str[t][0]])

      for w in range(len(old_str)):
        if old_str[w][1] != 'black':
          if removed != "":
            removed = " ".join([removed, "[...]"])
          removed = " ".join([removed, old_str[w][0]])
          removed2 = " ".join([removed2, old_str[w][0]])

        # Counts

      if new != "" and new != "nan":
        new_wc = len(re.findall(r'\w+', new))
      else:
        new_wc = 0

      if added2 != "" and added2 != "nan":
        added_wc = len(re.findall(r'\w+', added2))
      else:
        added_wc = 0

      if reuse2 != "" and reuse2 != "nan":
        reuse_wc = len(re.findall(r'\w+', reuse2))
      else:
        reuse_wc = 0

      if removed2 != "" and removed2 != "nan":
        removed_wc = len(re.findall(r'\w+', removed2))
      else:
        removed_wc = 0

      if old != "" and old != "nan":
        old_wc = len(re.findall(r'\w+', old))
      else:
        old_wc = 0

      # Reuse Calculations

      if new_wc != 0:
        rom_new = reuse_wc/new_wc
      else:
        rom_new = 0
      if old_wc != 0:
        rom_old = reuse_wc/old_wc
      else:
        rom_old = 0

      if new_wc == 0 and old_wc == 0 :
        jac_sim = 0
      else:
        jac_sim = reuse_wc/(new_wc + old_wc)


      clean_data = clean_data._append({'New ID':id_new,'New_Text':new,'New_Text_WC': new_wc,'Added':added,'Added_WC': added_wc, 'Reused':reuse,'Reused_WC': reuse_wc, 'Terminated':removed,'Terminated_WC': removed_wc, 'Old ID':id_old, 'Old_Text':old, 'Old_Text_WC': old_wc, 'Ratio_of_Match_IN_NEW': rom_new, 'Ratio_of_Match_FROM_OLD': rom_old,'Jaccard_Similarity': jac_sim},ignore_index=True)
  return clean_data

### TEXT OVER TIME ###

def text_over_time(new_year,old_year,l,thresh):
  dataframe = reuse_lists_to_dataset(new_year,old_year,l)

  t_new = dataframe['New ID'].max()
  t_old = dataframe['Old ID'].max()

  best_matches = pd.DataFrame(data = None, columns= dataframe.columns)
  matches = pd.DataFrame(data = None, columns= best_matches.columns)

  perfect_match = dataframe.loc[dataframe['Jaccard_Similarity'] == 0.5]
  #print(perfect_match)

  observed_new = list(perfect_match['New ID'])
  #print(observed_new)

  observed_old = list(perfect_match['Old ID'])
  #print(observed_old)

  # Best Match
  num_bm = 0
  for x in range(t_new):
    if x not in observed_new:
      new_lower = 0
      new_upper = t_new
      for y in range(x+1):
        l = (x-y)
        if l in observed_new:
          new_lower = l
          break

        for z in range((t_new+1)-x):
          u = (x+z)
          if u in observed_new:
            new_upper = u
            break

      if new_lower in observed_new:
        old_lower = perfect_match.loc[perfect_match['New ID'] == new_lower, 'Old ID'].iloc[0]
      else:
        old_lower = 0

      if new_upper in observed_new:
        old_upper = perfect_match.loc[perfect_match['New ID'] == new_upper, 'Old ID'].iloc[0]
      else:
        old_upper = t_old

      #print('new_lower: ', new_lower)
      #print('new_upper: ', new_upper)
      #print('old_lower: ', old_lower)
      #print('old_upper: ', old_upper)

      best_match = dataframe.loc[(dataframe['New ID'] == x) &
       (dataframe['Old ID'] > int(old_lower)) &
        (dataframe['Old ID'] < int(old_upper)) &
         (dataframe['Jaccard_Similarity'] > float(thresh))]

      if len(best_match) > 0:
        num_bm = num_bm + 1
        #print(num_bm)
        best_matches = pd.concat([best_matches, best_match])

  best_matches['Jaccard_Similarity'] = best_matches['Jaccard_Similarity'].astype(float)

  for q in range(num_bm):
    if len(best_matches) == 0:
      break
    else:
      bJS = best_matches['Jaccard_Similarity'].max()
      best_row = dataframe.loc[(dataframe['Jaccard_Similarity'] == bJS)]
      perfect_match = pd.concat([perfect_match, best_row])

      best_matches = best_matches.loc[(best_matches['New ID'] != best_row.iloc[0]['New ID'])]
      observed_new.append(best_row.iloc[0]['New ID'])
      #print(observed_new)

      best_matches = best_matches.loc[(best_matches['Old ID'] != best_row.iloc[0]['Old ID'])]
      observed_old.append(best_row.iloc[0]['Old ID'])
      #print(observed_old)

  # Added and Terminated

  no_match = dataframe.loc[(~dataframe['New ID'].isin(observed_new)) & (dataframe['Old_Text_WC'] == 0) & (dataframe['New_Text_WC'] != 0 )]
  perfect_match = pd.concat([perfect_match, no_match])
  no_match = dataframe.loc[(~dataframe['Old ID'].isin(observed_old)) & (dataframe['New_Text_WC'] == 0) & (dataframe['Old_Text_WC'] != 0 )]
  perfect_match = pd.concat([perfect_match, no_match])

  perfect_match.loc[(perfect_match['New_Text_WC'] == 0), "New ID"] = None
  perfect_match.loc[(perfect_match['Old_Text_WC'] == 0), "Old ID"] = None
  perfect_match = perfect_match.assign(order_new=perfect_match['New ID'])
  perfect_match = perfect_match.assign(order_old=perfect_match['Old ID'])

  perfect_match = perfect_match.reset_index(drop=True)

  for b in range(len(perfect_match)):
    if perfect_match['order_new'].iloc[b] == None:
      num = perfect_match['order_old'].iloc[b] - 1
      index = perfect_match.index[perfect_match.order_old == num][0]
      perfect_match.at[b, 'order_new'] = perfect_match['order_new'].iloc[index]

  for g in range(len(perfect_match)):
    if perfect_match['order_old'].iloc[g] == None:
      num = perfect_match['order_new'].iloc[g] - 1
      index = perfect_match.index[perfect_match.order_new == num][0]
      perfect_match.at[g, 'order_old'] = perfect_match['order_old'].iloc[index]

  perfect_match['order'] = perfect_match['order_new'] + perfect_match['order_old']

  # Sort
  perfect_match = perfect_match.sort_values(by=['order']) #.sort_values(by=['Old ID'])

  perfect_match = perfect_match.reset_index(drop=True)

  return perfect_match


### TEXT ONLY OVER TIME ###

def text_only_over_time(new_year,old_year,l,thresh):
  dataframe = reuse_lists_to_dataset(new_year,old_year,l)

  t_new = dataframe['New ID'].max()
  t_old = dataframe['Old ID'].max()

  best_matches = pd.DataFrame(data = None, columns= dataframe.columns)
  matches = pd.DataFrame(data = None, columns= best_matches.columns)

  perfect_match = dataframe.loc[dataframe['Jaccard_Similarity'] == 0.5]
  #print(perfect_match)

  observed_new = list(perfect_match['New ID'])
  #print(observed_new)

  observed_old = list(perfect_match['Old ID'])
  #print(observed_old)

  # Best Match
  num_bm = 0
  for x in range(t_new):
    if x not in observed_new:
      new_lower = 0
      new_upper = t_new
      for y in range(x+1):
        l = (x-y)
        if l in observed_new:
          new_lower = l
          break

        for z in range((t_new+1)-x):
          u = (x+z)
          if u in observed_new:
            new_upper = u
            break

      if new_lower in observed_new:
        old_lower = perfect_match.loc[perfect_match['New ID'] == new_lower, 'Old ID'].iloc[0]
      else:
        old_lower = 0

      if new_upper in observed_new:
        old_upper = perfect_match.loc[perfect_match['New ID'] == new_upper, 'Old ID'].iloc[0]
      else:
        old_upper = t_old

      #print('new_lower: ', new_lower)
      #print('new_upper: ', new_upper)
      #print('old_lower: ', old_lower)
      #print('old_upper: ', old_upper)

      best_match = dataframe.loc[(dataframe['New ID'] == x) &
       (dataframe['Old ID'] > int(old_lower)) &
        (dataframe['Old ID'] < int(old_upper)) &
         (dataframe['Jaccard_Similarity'] > float(thresh))]

      if len(best_match) > 0:
        num_bm = num_bm + 1
        best_matches = pd.concat([best_matches, best_match])

  best_matches['Jaccard_Similarity'] = best_matches['Jaccard_Similarity'].astype(float)

  for q in range(num_bm):
    bJS = best_matches['Jaccard_Similarity'].max()
    best_row = dataframe.loc[(dataframe['Jaccard_Similarity'] == bJS)]
    perfect_match = pd.concat([perfect_match, best_row])

    best_matches = best_matches.loc[(best_matches['New ID'] != best_row.iloc[0]['New ID'])]
    observed_new.append(best_row.iloc[0]['New ID'])
    #print(observed_new)

    best_matches = best_matches.loc[(best_matches['Old ID'] != best_row.iloc[0]['Old ID'])]
    observed_old.append(best_row.iloc[0]['Old ID'])
    #print(observed_old)

  # Added and Terminated


  no_match = dataframe.loc[(~dataframe['New ID'].isin(observed_new)) & (dataframe['Old_Text_WC'] == 0) & (dataframe['New_Text_WC'] != 0 )]
  perfect_match = pd.concat([perfect_match, no_match])
  no_match = dataframe.loc[(~dataframe['Old ID'].isin(observed_old)) & (dataframe['New_Text_WC'] == 0) & (dataframe['Old_Text_WC'] != 0 )]
  perfect_match = pd.concat([perfect_match, no_match])

  perfect_match.loc[(perfect_match['New_Text_WC'] == 0), "New ID"] = None
  perfect_match.loc[(perfect_match['Old_Text_WC'] == 0), "Old ID"] = None
  perfect_match = perfect_match.assign(order_new=perfect_match['New ID'])
  perfect_match = perfect_match.assign(order_old=perfect_match['Old ID'])

  perfect_match = perfect_match.reset_index(drop=True)

  for b in range(len(perfect_match)):
    if perfect_match['order_new'].iloc[b] == None:
      num = perfect_match['order_old'].iloc[b] - 1
      index = perfect_match.index[perfect_match.order_old == num][0]
      perfect_match.at[b, 'order_new'] = perfect_match['order_new'].iloc[index]

  for g in range(len(perfect_match)):
    if perfect_match['order_old'].iloc[g] == None:
      num = perfect_match['order_new'].iloc[g] - 1
      index = perfect_match.index[perfect_match.order_new == num][0]
      perfect_match.at[g, 'order_old'] = perfect_match['order_old'].iloc[index]

  perfect_match['order'] = perfect_match['order_new'] + perfect_match['order_old']


  # Sort
  perfect_match = perfect_match.sort_values(by=['order']) #.sort_values(by=['Old ID'])

  perfect_match = perfect_match.loc[:,['New ID', 'New_Text','Added', 'Reused','Terminated','Old ID','Old_Text']]

  perfect_match = perfect_match.reset_index(drop=True)

  return perfect_match

### MERGE DATAFRAMES ###

def merge_over_time(new_df,old_df):

  if len(new_df.columns) != len(old_df.columns):
    print("Error: input dataframes are not the same size")
    print("new_df: ", len(new_df.columns), "columns")
    print("old_df: ", len(old_df.columns), "columns")
    return None

  else:

    if len(new_df.columns) == 7:
      old_position = 12
    else:
      old_position = 27

    matched_df = pd.DataFrame(data = None, columns= [])
    empty = pd.DataFrame(data = None, columns= new_df.columns)
    old_ID2 = list(old_df['Old ID'])
    #print(old_ID2)
    for x in range(len(new_df)):
      ID1 = new_df['Old ID'].iloc[x]
      #print(ID1)
      if isinstance(ID1, int):
        df1 = new_df.loc[(new_df['Old ID'] == ID1)].reset_index(drop=True)
        df2 = old_df.loc[(old_df['New ID'] == ID1)].reset_index(drop=True)
        matched = pd.concat([df1, df2], axis=1)
        matched_df =  pd.concat([matched_df, matched])
        index = old_df.index[old_df['New ID'] == ID1][0]
        index2 = old_df.iloc[index]['Old ID']
        old_ID2.remove(index2)

      else:
        df1 = new_df.loc[(new_df.index.isin([x]))].reset_index(drop=True)
        matched = pd.concat([df1,empty], axis=1)
        matched_df = pd.concat([matched_df, matched])
        matched_df.reset_index(drop=True)
      if len(old_ID2) != 0:
        #print(matched_df.iloc[x][old_position])
        if matched_df.iloc[x,old_position] > min(old_ID2):
          nones = [l for l in old_ID2 if l < matched_df.iloc[x,old_position]]
          for n in nones:
            df2 = old_df.loc[(old_df['Old ID'] == n)].reset_index(drop=True)
            matched = pd.concat([empty,df2], axis=1)
            first_matched_df = matched_df.iloc[:-1 , :]
            last_matched_df = matched_df.iloc[-1: , :]
            matched_df =  pd.concat([first_matched_df, matched, last_matched_df])
            matched_df.reset_index(drop=True, inplace=True)
            old_ID2.remove(n)
            #print(old_ID2)


  matched_df.reset_index(drop=True, inplace=True)
  return matched_df

### STRAINGHT MERGE ####
def straight_merge(new_df,old_df):

  n_suf = "_"+new_df.columns[1][:6]
  o_suf = "_"+old_df.columns[1][:6]
  
  matched_df = new_df.join(old_df.drop(old_df.columns[1], axis=1), lsuffix=n_suf, rsuffix=o_suf)
  
  return matched_df

### STRAINGHT MERGE Text Only ####
def straight_merge_text_only(new_df,old_df):

  small_new_df = new_df.iloc[:, [0,1,3,5,7]]
  small_old_df = old_df.iloc[:, [1,3,5,7,9]]

  n_suf = "_"+new_df.columns[1][:6]
  o_suf = "_"+old_df.columns[1][:6]

  matched_df = small_new_df.join(small_old_df, lsuffix=n_suf, rsuffix=o_suf)

  return matched_df
  
### UPLOAD FROM GOOGLE DRIVE ####

def data_from_GD(file_name,tab_name):

  # mount
  from google.colab import auth
  auth.authenticate_user()

  import gspread
  from google.auth import default
  creds, _ = default()

  gc = gspread.authorize(creds)

  # real code
  worksheet = gc.open(file_name).worksheet(tab_name)

  # get_all_values gives a list of rows.
  rows = worksheet.get_all_values()

  import pandas as pd
  df_name = pd.DataFrame.from_records(rows)

  df_name.columns = df_name.iloc[0]  # Set the first row as header
  df_name = df_name[1:]  # Remove the first row from the data

  # Reset the index (optional)
  df_name.reset_index(drop=True, inplace=True)

  return df_name
  
