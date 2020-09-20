The equation plotter takes an equation input from the user as a string, I parced this string into coefficents and degrees correctly, so I could use both lists to substitue into the equation to get y values. It also takes a minimum value and maximum value for x, and a step, using the previous values I created a list with evenly spaced x values.

I used the x list to substitue in the equation and get a corresponding y for each x-value. Then, I passed both x and y values to Matplotlib which plotted the function.

The equation plotter is functionally correct. However, the plot button is not functional, and the plot result is displayed upon closing the GUI window, which is an error I was unfortunately unable to fix before the deadline. Attached in this repository is Task1.py.

I tried fixing that error, by including a canvas in the GUI to display the plot on clicking the plot button. I succesfully added a canvas but I wasn't able to display the plot on clicking the plot. Attached in this repository are TRIAL.py and TRIAL.png.