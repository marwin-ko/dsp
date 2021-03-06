##[Mastering Markdown](https://guides.github.com/features/mastering-markdown/)  

**Important:**  Look at your rendered markdown file before submitting!  :boom:  

#### Table of Contents
[1)  Text Formatting](#section-a)  
[2)  Referencing Other Markdown Files](#section-b)  
[3)  Line Breaks](#section-c)  
[4)  Horizontal Rules](#section-d)  
[5)  Emoji's](#section-e)  
[6)  Links](#section-f)  
[7)  Block Code, Language-specific](#section-g)  
[8)  Tables](#section-h)  
[9)  Practice Examples](#section-i)  
[References](#section-r)

---

## <a name="section-a"></a>1) Text Formatting  

bold: `**bold**`  **bold**  
italic:  `*italic*` *italic*  
italic:  `_italic_` _italic_  

---

## <a name="section-b"></a>2) Referencing Other Markdown Files 

In a markdown file on GitHub, to see how it was formatted, click on "raw" on upper right corner.

---

## <a name="section-c"></a>3) Line Breaks 

How to add line breaks:  
1.  can enclose text in triple back quotes  
2.  add two spaces to end of line 

---

## <a name="section-d"></a>4) Horizontal Rules 

Code for line separators:  

```
Rule #1 

---

Rule #2
*******
Rule #3
___
```

Rendered code for line separators:  

Rule #1

---

Rule #2
*******
Rule #3
___

---

## <a name="section-e"></a>5) Emoji's 

Code for emoji's:
```
:fireworks:
:smiley:
:watermelon:
```
Rendered emoji's:  
:fireworks:  
:smiley:  
:watermelon:  
 
---

## <a name="section-f"></a>6) Links 

Text for link:  
```Here's an inline link to [Google](http://www.google.com/).```  
Rendered link:  
Here's an inline link to [Google](http://www.google.com/).  

---

## <a name="section-g"></a>7) Block Code, Language-specific 

####python

Block code that is non-specific:  
```
print "hello world!"
print "hello moon"
```

Block code that is **python**-specific:  
```python
print "hello world!"
print "hello moon"
```

####bash or console

Block code that is non-specific:  
```
$ git status
$ git remote -v
```

Block code that is **bash**-specific:  
```console
$ git status
$ git remote -v

$ ps awx | grep mongo
```

####sql

Block code that is non-specific:  
```
SELECT * FROM Customers WHERE Country='Sweden';
```

Block code that is **sql**-specific:  
```sql
SELECT * FROM Customers WHERE Country='Sweden';
```

####Yes, this works for scores of other languages:  [Syntax highlighting in markdown](https://support.codebasehq.com/articles/tips-tricks/syntax-highlighting-in-markdown) 

---

## <a name="section-h"></a>8) Tables 

```
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column
```

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

---

## <a name="section-i"></a>9) Practice Examples 

####Data Science Trivia 

####Q1.  
What is the most installed language in the world?  
- Python
- SAS
- R
- Spark
- Javascript

Javascript

-

####Q2.  
In hypothesis testing, we use the t score when the sample size is < 30 and the populations SD is unknown; else we use the Z score. 
What is the distribution of t-squared?
 * Normal
 * F
 * Chi-squared
 * Beta
 * Bivariate Normal

F distribution

***

####Q3.  
In the scikit-learn's official source repo, about how many issues are outstanding? (go ahead and check out their page)  
1. 7  
2. 70  
3. 700  
4. 7000  

Approximately 700 issues!

---

## <a name="section-r"></a>References 

[Markdown Help](http://mathoverflow.net/editing-help)
