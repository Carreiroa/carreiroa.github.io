<!---
layout: page
title: "Program Shell"
permalink: https://Carreiroa.github.io/ProgramShell/
--->

### [Home](/index) | [Java Index](./JavaIndex)

---

## Java Program Shell

Java is an object oriented programming language and, as such, when we write our first java program we create a class that contains a main method. It's the main method that the JVM (Java Virtual Machine) looks for to get things started.

### Creating Our Class and Main Method

Source code is simply a text file written in whatever language your are choosing to code in, in this case, Java. We can write our code in any program of our choosing, but try to avoid word processors like Microsoft Word or Apple's Pages since these are really meant for document editing and can leave unwanted characters in our file that will cause us problems. Try to code using an IDE (Integrated Development Environment) or a text editor like Notepad.

```java
class MyFirstClass {

}
```

Here we have a class called MyFirstClass and everything within the curly braces belongs to that class. You'll notice that my class name follows Oracle's naming convention called camel case, where there are no spaces between words, and words always start with a capital letter. Please note that capitalizing the first letter of the class is standard, but for methods and variables we will always start with a lower case (eg. myVariableName).

Now that we have our class we will need a main method in-order for this program to run on its own.

```java
class MyFirstClass {
	public static void main (String [] args) {

	}
}
```

We have now added a main method to our class. Just like our class, it too has an open and closing curly brace that indicate everything that belongs to that method. It's within these braces that we will write our first code.
You'll notice that our main method has a few modifiers that are important to java and all main methods must be written this way. We will worry about what these modifiers mean a little later.

**Note:** Java is case sensitive. That means, to Java, public static is not the same as Public Static.

And that's it. You have successfully written the shell to your first Java program. It doesn't do a thing, but it is still a program. We'll add some content after we do our first save.

### Saving Our Source Code

We will need to save our source code if we would like to be able to compile it and run our new creation. Save your file with the **exact same** name as the class and give it the extension .java (eg. MyFirstClass.java). And that's it. Well, that's it if you're happy with your program doing nothing. Let's modify our code with the content below and then save your changes, compile it and run it.

```java
class MyFirstClass {
	public static void main (String [] args) {

		System.out.println("Hello World!");

	}
}
```

Congratulations, you now have written your very first Java program.

Happy Coding
