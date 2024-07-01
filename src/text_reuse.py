import pandas as pd

from IPython.display import HTML as html_print
from IPython.display import display

import re

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

  clean_data = pd.DataFrame(columns = ['Statement ID','New_Text','Added', 'Reused', 'Terminated', 'Old_Text'])

  for x in range(len(data)):

    id_num = data.iloc[x][id]
    new = data.iloc[x][new_year]
    old = data.iloc[x][old_year]

    new_str, old_str = reuse_loops2(new,old,l)

    added = ""
    reuse = ""
    removed = ""

    for x in range(len(new_str)):
      if new_str[x][1] != 'black':
        if added != "":
          added = " ".join([added, "[...]"])
        added = " ".join([added, new_str[x][0]])
      else:
        if reuse != "":
          reuse = " ".join([reuse, "[...]"])
        reuse = " ".join([reuse, new_str[x][0]])

    for x in range(len(old_str)):
      if old_str[x][1] != 'black':
        if removed != "":
          removed = " ".join([removed, "[...]"])
        removed = " ".join([removed, old_str[x][0]])

    clean_data = clean_data._append({'Statement ID':id_num,'New_Text':new,'Added':added, 'Reused':reuse, 'Terminated':removed, 'Old_Text':old},ignore_index=True)
  return clean_data

##############
### Set Up ###
##############

### Dataset Construction ###

def construct_dataset(data,id,new_year,old_year): # data to load, position of the id column, position of the new_year column, position of the old_year column

  dataset = pd.DataFrame({'Statement ID' : [],
                         'New_Year' : [],
                         'Old_Year' : []})

  dataset['Statement ID']=data.iloc[:, id].apply(int)
  dataset['New_Year']=data.iloc[:, new_year].apply(str)
  dataset['Old_Year']=data.iloc[:, old_year].apply(str)

  return dataset[['Statement ID','New_Year','Old_Year']]
