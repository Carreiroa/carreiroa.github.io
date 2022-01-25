<!---
layout: page
title: "testFile"
permalink: https://Carreiroa.github.io/WhileLoops/
--->
#### [Home](/index)

---

## Java While Loops

While loops are a type of repetitive flow that test a boolean expression to determine if the loop is to be repeated. Just as its name suggests you perform a loop "While" some condition is true. In Java, the syntax for a while loop is as follow.
&NewLine;
&NewLine;
### Syntax
```java
int sentinelVariable = 0; // initialization

while (sentinelVariable < 5){ // condition
	System.out.println("While loop iteration #"+(sentinelVariable+1));
	sentinelVariable++; // incrementation
}
```

In every loop we have initialization, a condition and incrementation. In our program we initialize a sentinel variable (a variable that will be used in the condition). The condition is boolean and the code within the while code block runs in a continuous loop until that condition tests false. Incrementation is when the sentinel variable is incremented so as to prevent the loop from entering into an infinite loop. 

