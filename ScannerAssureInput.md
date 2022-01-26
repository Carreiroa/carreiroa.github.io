<!---
layout: page
title: "Scanner Assure Input"
permalink: https://Carreiroa.github.io/ScannerAssureInput/
--->
### [Home](/index) | [Java Index](/JavaIndex)

---

## Scanner: Assure Input

One of the more challenging things to a new programmer is handling user input so that your program doesn't crash. It's hard enough trying to make sure that your program and its flow is in order, let alone worry about how your user will interact with your program in terms of their input. There are multiple ways around this issue in Java and one such way is to program our own little routine to ensure that the user's input doesn't crash.

Remember that all input via the input stream is taken in as characters. So if the user enters 1, that character is just a character and not an integer. It isn't until we ask for a Scanner object to return that input as an integer that we can use it as such. If we ask the user to return what's in its stream as an integer, but the user enters a decimal or a string, we will get a run-time error. 

Luckily, the Scanner has numerous methods and we can use one of them to help us out. The ```.hasNextInt()``` behaves similarly to ```.nextInt()``` but instead of trying to return an integer value, it returns a ```true``` or ```false``` depending if the scanner object is holding an integer value before the next token. It's important to note here, if you haven't caught it already, that ```.hasNextInt()``` returns a boolean leaving the input in the scanner and ```.nextInt()``` returns an integer moving the scanner's pointer to the next token. This means that after returning the value from the scanner, we can consider that input no longer in the scanner object.

Since ```.hasNextInt()``` returns a boolean value we can use it in condition statements like those in an ```if``` or in a ```while```. 
&NewLine;
&NewLine;
### Assure Integer Input
```java
Scanner userInput = new Scanner(System.in);
int x = 0;

System.out.print("Please enter an integer. ");

while (!userInput.hasNextInt()){
	System.out.println("Invalid input. Please try again.");
	userInput.next();
}

x = userInput.nextInt();
```

#### Code Breakdown
In the above code we place the ```.hasNextInt()``` as a condition. At this point, if there is no input in the scanner because none has been entered or because values in it have all been returned, it will wait for input on that line and once there is input it will return either ```true``` or ```false``` depending on the input *type*. Regardless of the result of the boolean expression, the scanner object still retains the user's input waiting for it to be returned with an appropriate method like ```.next()``` or ```.nextInt()```.

If that condition tests false, meaning we do not have an integer in the scanner, we negate the result with the ```!``` so that we enter the while loop. At this point, other than *"keeping the user in the loop"* with some feedback (bad Dad Joke!), we will need to move the pointer in the scanner since we don't want the user's input. To do that, we simply call the ```.next()``` method without assigning its return to a variable. At this point we are ready to test a new user input at the top of the loop.


#### Challenge
Test the code out. Can you wrap the code above in a do while loop so that it also assures the integer falls within a certain range?