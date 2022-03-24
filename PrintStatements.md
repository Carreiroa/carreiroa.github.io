<!---
layout: page
title: "Print Statements"
permalink: https://Carreiroa.github.io/PrintStatements/
--->
### [Home](/index) | [Java Index](/JavaIndex)

---

## Print Statements

Almost every program has some form of output to for its user. The simplest and easiest form of output in a Java program is one that outputs to the console or terminal. To do that we can use a print statement. Print statements are functions in Java that output a value to the screen, and Java has three functions / methods to choose from.

- System.out.print ()
- System.out.println ()
- System.out.printf ()

### System.out.print ()

```java
System.out.print ("Hello World.");
System.out.print ("I love Java!");
```

The print() outputs the characters contained within the quotation marks. This statement leaves the cursor immediately after the last character it outputs.

**Output**: 
Hello World.I love Java!

### System.out.println ()

```java
System.out.println ("Hello World.");
System.out.println ("I love Java!");
```

The println() outputs the characters contained within the quotation marks. This statement returns a new line immediately after the last character it outputs.

**Output**: 
Hello World.
I love Java!

### System.out.printf ()

The printf () is the more complex, but most versatile of the three print statements. Called the print format function, it allows one to format their output in a specific fashion using various place holders. Its syntax is simple but takes a little getting use to.

```java
int age = 12;
double shoeSize = 8.5;
String name = "Elias";

System.out.printf ("%s is %d years old and wears size %.1f shoes.",name,age,shoeSize);
```

**Output**:
Elias is 12 years old and wears size 8.5 shoes.

When you examine the statement you can see that I have declared three variables that I use within the print statement. It isn't necessary, but it helps illustrates one of the most common use cases for the statement. In the printf() statement we have our context contained within the quotation marks and symbols, or place holders, that are later substituted when the program runs with the variables that are named immediately after the last quotation mark in the example. The place holders correspond with each variable in the order that they appear and if they don't match the expected type of the placeholder, an error will be thrown.

%s String
%d integer
%f floating point

You will also notice that when dealing with a floating point, it is possible to determine how many decimal places are displayed by indicating a precision with a .1 to indicate once decimal place.
It is also possible to add, within the quotation marks, \n to return a new line or \t to tab.

# Happy Coding :sunglasses: :computer:
