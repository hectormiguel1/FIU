# 1. Basic Rule Creation

The 'databse' below has four transactions. What ssociation rules can be found in this set. if the minimum support (ie coverage) is 60% and minimum confidence (ie accuracy) is 80%?

| Tans_id | ItemList |
| - | - |
| T1 | {K, A, D, B} |
| T2 | {D,A,C,E,B} |
| T3 | {C, A, B, E } |
| T3 | {B, A, D} |

Show each step of your calculation in details (ie item sets containing one item, two items like this), as each step will be graded individually.

# 2. Using  the XML Decument bellow (library with books), define the following queries in XQuery:

a. Give the titles of all books sorted by price.

```xquery
    for $book in doc("library.xml")/bib/book
    order by $book/price
    return $book/title
```

b. How many books were written by Abiteboul?

```xquery
    count(doc("library.xml")/bib/book[author="Abiteboul"])
```

c. Give for each author, the number of books they have written.

```xquery
    for $author in doc("library.xml")/bib/book/author
    return count(doc("library.xml")/bib/book[author=$author])
```

## Privided XML Document (library.xml)

```xml
 <?xml version="1.0"?>
 <bib>
    <book year="1994">
        <title>TCP/IP</title>
        <author>Stevens</author>
        <publisher>Addison-Wesley</publisher>
        <price>65.95</price>
    </book>
    <book year="1994">
        <title>Principles of Databses</title>
        <author> Abiteboul</author>
        <publisher>Addison-Wesley</publisher>
        <price>35.89</price>
    </book>
    <book year="1994">
        <title>Advanced Programming in the Unix enviroment</title>
        <author>Stevens</author>
        <publisher>Addison-Wesley</publisher>
        <price>65.95</price>
    </book>
    <book year="2000">
        <title> Data on the Web </title>
        <author>Abiteboul</author>
        <author>Bunenman</author>
        <author>Suciu</author>
        <publisher>Morgan Kaufmann Publishers</publisher>
        <price>39.95</price>
    </book>
    <book year="1992">
        <title>The Economics of Technology and Content for Digital TV</title>
        <editor>
            <affiliation>CITI</affiliation>
        </editor>
        <publisher>Kluwer Academix Publishers</publisher>
        <price>129.95</price>
    </book>
 </bib>
```

=============== Originality Declaration =====================

Name: Hector Ramirez

Panther-ID: 5708475

Course: COP-4751

Assignment#: 3

Due: 11/12/2021

I hereby certify that this work is my own and none of it is the work of any other person.

Signature: Hector Ramirez

=========================================================
