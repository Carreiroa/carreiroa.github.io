<!---
layout: page
title: "Math.random"
permalink: https://Carreiroa.github.io/MathRandom/
--->
### [Home](/index) | [Java Index](/JavaIndex)

---

## Math.random()
There are a couple of ways to generate random number in Java. Using the Math class and its random() method is one such way. This class will generate a random number between 0 and less than 1.0 and its return type is a double. This means that if you want to store its returned value in an integer variable, you will need to cast it. More on that in a bit. Generating random numbers is a pretty handy thing to do in a program and it has many uses, however it's hard to think of those uses when you can only generate decimal values between 0 and 1.0. So, to navigate this issue we will need to do some math with its return value. Let's dive into the syntax of using the method.

### Assigning a random number to a double.

```java
double x = 0;
x = Math.random();
```
The ```.random()``` method's return type is a double and using it on its own like this will return a decimal value between 0 and 1.0.

### Assigning a random number to a double within a range of values.

```java
double x = 0;
x = Math.random()*10+1;
```
In this example we have multiplied the return value of ```Math.random()``` by a factor of ten. This will shift the decimal over by one placeholder resulting in generating random numbers > 0.0 and < 10.0. Adding one to the equation will allow the entire equation to return a single value > 1 and < 11.

To simplify, 10 is your range of numbers, or number of numbers and 1 is your starting point.

### Assigning a random number to an integer within a range of values.

```java
int x = 0;
x = (int)(Math.random()*10+1);
```
Here we have a random number being assigned to an integer variable. The difference being here is that now we are casting the equation to an integer type so that it can be assigned to the variable ```x```. By casting the equation to an integer we now lose the precision of any decimal that the equation will return. For example, 1.999 will be cast to 1. In this case ```x``` will be assigned an integer value between 1 and 10 inclusively.