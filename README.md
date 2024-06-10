# text_reuse
## Python functions for evaluating the reuse of text.

One Paragraph of the project description

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Installing

All of the functions that are identified below can be installed and imported given the code below:

    !pip install "git+https://github.com/ambro034/text_reuse.git"
    import text_reuse as tr

## Practical Reuse Functions

### reuse_color_coded
This is a function returns two statements, color-coded based on their reuse; where, black text is 'reused' between the two statements, green text is 'added' between statement #1 and statement #2, and red text is 'terminated' between statement #1 and statement #2. Statement #1 is assumed to temporally proceed statement #2. 

    reuse_color_coded(str1,str2,l)

Where:
  - *str1* is the first string of text passed to the function
  - *str2* is the second string of text passed to the function
  - *l* is the minimum n-gram length the function is observing (i.e., l = 2, two-word chucks)

### reuse_color_coded_dataset
This is a function returns pairs of statements from a dataframe, color-coded based on their reuse; where, black text is 'reused' between the two statements, green text is 'added' between statement #1 and statement #2, and red text is 'terminated' between statement #1 and statement #2. Statement #1 is assumed to temporally proceed statement #2.

    reuse_color_coded_dataset(data,id,new_year,old_year,l)

Where:
  - *data* is the name of the dataframe
  - *id* is the column position for Statement IDs in the dataframe
  - *new_year* is the column position for Statement #1 in the dataframe
  - *old_year* is the column position for Statement #2 in the dataframe
  - *l* is the minimum n-gram length the function is observing (i.e., l = 2, two-word chucks)

### reuse_dataset_to_dataset
This is a function returns pairs of statements from a dataframe, to a new dataframe representing the new statement, the added text, the reused test, the terminated text, and the old statement. For the added text, the reused test, the terminated text -- text is reported sequentially, so '[...]' are inserted where text is not sequentually relevent.

    reuse_color_coded_dataset(data,id,new_year,old_year,l)

Where:
  - *data* is the name of the dataframe
  - *id* is the column position for Statement IDs in the dataframe
  - *new_year* is the column position for Statement #1 in the dataframe
  - *old_year* is the column position for Statement #2 in the dataframe
  - *l* is the minimum n-gram length the function is observing (i.e., l = 2, two-word chucks)


## Data Construction

A function to added with dataframe construction.

### construct_dataset
This is a function that takes a variably framed dataframe and conforms it to the structure useful in the above functions.

    construct_dataset(data,id,new_year,old_year)

Where:
  - *data* is the name of the dataframe
  - *id* is the column position for Statement IDs in the dataframe
  - *new_year* is the column position for Statement #1 in the dataframe
  - *old_year* is the column position for Statement #2 in the dataframe
    

## Additional Reuse Functions

These functions are nested into the 'practical functions above, but can be used indamendently if needed.

### id_reuse
This is a function that identifies the longest stretch of words that are shared between to statements passed to the function. This function optimizes (i.e., finds the longest stretch of words), but does not return all reused words if there are two or more chuncks of text that are reused. 

    id_reuse(str1,str2,l)

Where:
  - *str1* is the first string of text passed to the function
  - *str2* is the second string of text passed to the function
  - *l* is the minimum n-gram length the function is observing (i.e., l = 2, two-word chucks)

### reuse_loops2
This is a function that identifies all stretchs of words that are shared between to statements passed to the function. This function first optimizes (i.e., finds the longest stretch of words), loops through the text untill all text chuncks of size *l* are found. 

    reuse_loops2(str1,str2,l)

Where:
  - *str1* is the first string of text passed to the function
  - *str2* is the second string of text passed to the function
  - *l* is the minimum n-gram length the function is observing (i.e., l = 2, two-word chucks)

### Style test

Checks if the best practices and the right coding style has been used.

    Give an example

## Deployment

Add additional notes to deploy this on a live system

## Built With

  - [Contributor Covenant](https://www.contributor-covenant.org/) - Used
    for the Code of Conduct
  - [Creative Commons](https://creativecommons.org/) - Used to choose
    the license

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code
of conduct, and the process for submitting pull requests to us.

## Versioning

We use [Semantic Versioning](http://semver.org/) for versioning. For the versions
available, see the [tags on this
repository](https://github.com/PurpleBooth/a-good-readme-template/tags).

## Authors

  - **Billie Thompson** - *Provided README Template* -
    [PurpleBooth](https://github.com/PurpleBooth)

See also the list of
[contributors](https://github.com/PurpleBooth/a-good-readme-template/contributors)
who participated in this project.

## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

## Acknowledgments

  - Hat tip to anyone whose code is used
  - Inspiration
  - etc
