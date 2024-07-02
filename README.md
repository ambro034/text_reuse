# text_reuse
## Python functions for evaluating the reuse of text.

This package evaluates the differences between two policy statements returning the statements data inline with the conceptualization of policy evolution in Ambrose et al., 2024.  Given this conceptualization, policy evolution observed in text can be (1) reused (i.e., no change observed between documents {black output text}), (2) added (i.e., added text observed between documents {green output text}), or (3) terminated (i.e., removed text observed between documents {red output text}). While this can happen at the whole statement level, it can also be observed as calibration or intra-statement changes. text_reuse is capable of evaluating evolution at the statement and intra-statement levels. 

## Getting Started

These instructions will outline installation, a description of the functions, as well as identify examples.

# Table of Contents
1. [Installing](#Installing)
2. [Functions](#Functions)
   - [Practical Reuse Functions](#Practical-Reuse-Functions)
   - [Data Construction](#Data-Construction)
   - [Additional Reuse Functions](#Additional-Reuse-Functions)
3. [Examples](#Examples)
4. [Other Stuff](#Built-With)

### Installing

All of the functions that are identified below can be installed and imported given the code below:

    !pip install "git+https://github.com/ambro034/text_reuse.git"
    import text_reuse as tr

## Functions

### Practical Reuse Functions

#### reuse_color_coded
This is a function returns two statements, color-coded based on their reuse; where, black text is 'reused' between the two statements, green text is 'added' between statement #1 and statement #2, and red text is 'terminated' between statement #1 and statement #2. Statement #1 is assumed to temporally proceed statement #2. 

    reuse_color_coded(str1,str2,l)

Where:
  - *str1* is the first string of text passed to the function
  - *str2* is the second string of text passed to the function
  - *l* is the minimum n-gram length the function is observing (i.e., l = 2, two-word chucks)

#### reuse_color_coded_dataset
This is a function returns pairs of statements from a dataframe, color-coded based on their reuse; where, black text is 'reused' between the two statements, green text is 'added' between statement #1 and statement #2, and red text is 'terminated' between statement #1 and statement #2. Statement #1 is assumed to temporally proceed statement #2.

    reuse_color_coded_dataset(data,id,new_year,old_year,l)

Where:
  - *data* is the name of the dataframe
  - *id* is the column position for Statement IDs in the dataframe
  - *new_year* is the column position for Statement #1 in the dataframe
  - *old_year* is the column position for Statement #2 in the dataframe
  - *l* is the minimum n-gram length the function is observing (i.e., l = 2, two-word chucks)

#### reuse_dataset_to_dataset
This is a function returns pairs of statements from a dataframe, to a new dataframe representing the new statement, the added text, the reused test, the terminated text, and the old statement. For the added text, the reused test, the terminated text -- text is reported sequentially, so '[...]' are inserted where text is not sequentually relevent.

    reuse_color_coded_dataset(data,id,new_year,old_year,l)

Where:
  - *data* is the name of the dataframe
  - *id* is the column position for Statement IDs in the dataframe
  - *new_year* is the column position for Statement #1 in the dataframe
  - *old_year* is the column position for Statement #2 in the dataframe
  - *l* is the minimum n-gram length the function is observing (i.e., l = 2, two-word chucks)


### Data Construction

A function to added with dataframe construction.

#### construct_dataset
This is a function that takes a variably framed dataframe and conforms it to the structure useful in the above functions.

    construct_dataset(data,id,new_year,old_year)

Where:
  - *data* is the name of the dataframe
  - *id* is the column position for Statement IDs in the dataframe
  - *new_year* is the column position for Statement #1 in the dataframe
  - *old_year* is the column position for Statement #2 in the dataframe
    

### Additional Reuse Functions

These functions are nested into the 'practical functions above, but can be used indamendently if needed.

#### id_reuse
This is a function that identifies the longest stretch of words that are shared between to statements passed to the function. This function optimizes (i.e., finds the longest stretch of words), but does not return all reused words if there are two or more chuncks of text that are reused. 

    id_reuse(str1,str2,l)

Where:
  - *str1* is the first string of text passed to the function
  - *str2* is the second string of text passed to the function
  - *l* is the minimum n-gram length the function is observing (i.e., l = 2, two-word chucks)

#### reuse_loops2
This is a function that identifies all stretchs of words that are shared between to statements passed to the function. This function first optimizes (i.e., finds the longest stretch of words), loops through the text untill all text chuncks of size *l* are found. 

    reuse_loops2(str1,str2,l)

Where:
  - *str1* is the first string of text passed to the function
  - *str2* is the second string of text passed to the function
  - *l* is the minimum n-gram length the function is observing (i.e., l = 2, two-word chucks)

### Examples

    # Set Up
    !pip install "git+https://github.com/ambro034/text_reuse.git"
    import text_reuse as tr
    import pandas as pd
    
    # Load Data
    data = pd.read_csv(fake_data.csv, encoding='cp1252')
    data.info()

    # Two Statements from Strings
    s1 = "In this case, the public utilities commission shall consult with the energy commission in calculating market prices and establishing other renewable portfolio standard policies--for this is the right thing."
    s2 = "The public utilities commission shall consult with the energy commission in establishing renewable portfolio standard policies, but this is the right thing."

    tr.id_reuse(s1,s2,2)

    tr.reuse_color_coded(s1,s2,2)

    # Construct Data
    mydata = tr.construct_dataset(data,0,1,2)

    #Run Dataframe to Dataframe
    tr.reuse_dataset_to_dataset(mydata,0,2,1,2)

    
## Built With

  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used
    for the Code of Conduct
  - [Creative Commons](https://creativecommons.org/) - Used to choose
    the license

## Authors

  - **Graham Ambrose** - 
    [ambro034](https://github.com/ambro034/)


## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

## Acknowledgments

  - People
  
