## Advanced Python    

###Regular Expressions, Dictionary, Writing to CSV File  

This question has multiple parts, and will take **20+ hours** to complete, depending on your python proficiency level.  Knowing these skills will be extremely beneficial during the first few weeks of the bootcamp.

For Part 1, use of regular expressions is optional.  Work can be completed using a programming approach of your preference. 

---

The data file represents the [Biostats Faculty List at University of Pennsylvania](http://www.med.upenn.edu/cceb/biostat/faculty.shtml)

This data is available in this file:  [faculty.csv](python/faculty.csv)

--- 

###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

There are 8 different degrees (MD,MA,ScD,BSEd, PhD, MPH, MS, JD) along with 1 person having zero (0) degrees. The frequency of each degree is displayed in a dictionary format as follows: 
```{'MD': 1, 'MA': 1, 'ScD': 6, 'BSEd': 1, 'PhD': 31, '0': 1, 'MPH': 2, 'MS': 2, 'JD': 1}.```


####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

There are 3 different titles (Assistant Professor, Associate Professor, Professor of Biostat). The frequency of each degree is displayed in a dictionary format as follows: ```{'Assistant Professor': 12, 'Associate Professor': 12, 'Professor of Biostat': 13}.```


####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

```['bellamys@mail.med.up', 'warren@upenn.edu', 'bryanma@upenn.edu', 'jinboche@upenn.edu', 'sellenbe@upenn.edu', 'jellenbe@mail.med.up', 'ruifeng@upenn.edu', 'bcfrench@mail.med.up', 'pgimotty@upenn.edu', 'wguo@mail.med.upenn.', 'hsu9@mail.med.upenn.', 'rhubb@mail.med.upenn', 'whwang@mail.med.upen', 'mjoffe@mail.med.upen', 'jrlandis@mail.med.up', 'liy3@email.chop.edu', 'mingyao@mail.med.upe', 'hongzhe@upenn.edu', 'rlocalio@upenn.edu', 'nanditam@mail.med.up', 'knashawn@mail.med.up', 'propert@mail.med.upe', 'mputt@mail.med.upenn', 'sratclif@upenn.edu', 'michross@upenn.edu', 'jaroy@mail.med.upenn', 'msammel@cceb.med.upe', 'shawp@upenn.edu', 'rshi@mail.med.upenn.', 'hshou@mail.med.upenn', 'jshults@mail.med.upe', 'alisaste@mail.med.up', 'atroxel@mail.med.upe', 'rxiao@mail.med.upenn', 'sxie@mail.med.upenn.', 'dxie@upenn.edu', 'weiyang@mail.med.upe']```


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

There are 8 different email domains. The following is a list of the different email domains:
```['@upenn.edu', '@mail.med.upenn', '@mail.med.upen', '@cceb.med.upe', '@mail.med.up', '@email.chop.edu', '@mail.med.upenn.', '@mail.med.upe']```

Place your code in this file: [advanced_python_regex.py](python/advanced_python_regex.py)

---

###Part II - Write to CSV File

####Q5.  Write email addresses from Part I to csv file

Place your code in this file: [advanced_python_csv.py](python/advanced_python_csv.py)

The emails.csv file you create should be added and committed to your forked repository.

Your file, emails.csv, will look like this:
```
bellamys@mail.med.upenn.edu
warren@upenn.edu
bryanma@upenn.edu
```

---

### Part III - Dictionary

####Q6.  Create a dictionary in the below format:
```
faculty_dict = { 'Ellenberg': [['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu']],
              'Li': [['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ['Ph.D.', 'Professor', 'hongzhe@upenn.edu']]}
```
Print the first 3 key and value pairs of the dictionary:
```
{'Putt': [' PhD ScD', 'Professor of Biostat', 'mputt@mail.med.upenn'], 'Feng': [' Ph.D', 'Assistant Professor ', 'ruifeng@upenn.edu'], 'Bilker': ['Ph.D.', 'Professor of Biostat', 'warren@upenn.edu']}
```

####Q7.  The previous dictionary does not have the best design for keys.  Create a new dictionary with keys as:

```
professor_dict = {('Susan', 'Ellenberg'): ['Ph.D.', 'Professor', 'sellenbe@upenn.edu'], ('Jonas', 'Ellenberg'): ['Ph.D.', 'Professor', 'jellenbe@mail.med.upenn.edu'], ('Yimei', 'Li'): ['Ph.D.', 'Assistant Professor', 'liy3@email.chop.edu'], ('Mingyao','Li'): ['Ph.D.', 'Associate Professor', 'mingyao@mail.med.upenn.edu'], ('Hongzhe','Li'): ['Ph.D.', 'Professor', 'hongzhe@upenn.edu'] }
```

Print the first 3 key and value pairs of the dictionary:
```
{('Yimei', 'Li'): [' Ph.D.', 'Assistant Professor ', 'liy3@email.chop.edu'], ('Hongzhe', 'Li'): [' Ph.D', 'Professor of Biostat', 'hongzhe@upenn.edu'], ('Justine', 'Shults'): [' Ph.D.', 'Professor of Biostat', 'jshults@mail.med.upe']}
```

####Q8.  It looks like the current dictionary is printing by first name.  Print out the dictionary key value pairs based on alphabetical orders of the last name of the professors

>> REPLACE THIS WITH YOUR RESPONSE

Place your code in this file: [advanced_python_dict.py](python/advanced_python_dict.py)

--- 

If you're all done and looking for an extra challenge, then try the below problem:  

### [Markov](python/markov.py) (Optional)

