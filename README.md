# Microbit-
The purpose of this task is to implement a utility capable of executing Linux bash commands.

The Python script  reads commands from the keyboard that it executes. Once run, the executable will display a prompt in the form cmd: it will receive a command followed by the parameters. Pressing the ENTER key marks the end of the command. After each order, the program will display the result, if any, and then wait for another command. The program will end its execution by receiving the exit or quit command.

Supported commands:

led [parameter] x y - controls the LED on the Micro: bit located on the x line and the y column. Depending on the parameters you receive, the order will perform the following actions:
on - illuminates the LED
off - turn off the LED
blink <interval> <count> - flashes the LED every millisecond. The value for the count will be in the range 0-20.
toggle - brings the LED to the opposite state (if the LED is on, turns it off, and if it is off, turns it on)
brightness [set <val>] - used without the set parameter, displays the brightness of the specified LED
set <val> - using the set parameter it will set the brightness to the val value, somewhere the val is an integer 0-9 and the value displayed in the console is the new brightness

The command will display the following errors for the following cases:

Invalid LED. - if the values for x and / or y are not in the range 0-4
Invalid count value. - if the value for the count is not in the range 0-20.
Invalid brightness. - if the value for the val is outside the range 0-9.  
   

button <button> - button can be A or B, representing one of the two buttons on the board. The command displays the text True if the specified button is pressed and the text False if the button is not pressed.
The command will display the following errors for the following cases:

Invalid button. - if button is different from a or b  
  
  
light - Displays the value of the light sensor on the board.
  
  
temperature <deg> - Depending on the value of <deg> which can be C / F / K, the value of the temperature taken by the temperature sensor in degrees celsius, fahrenheit or kelvin will be displayed.
  
  
echo [parameter] arguments [> / »file] - Displays the arguments in the console followed by the new line.
-n does not add a new line at the end
> file - Redirects the text that will be displayed by the echo command in the file file, and nothing will be displayed on the screen. If the file does not exist, it will be created. If the file exists, its contents will be overwritten.
»File - Redirects the text that will be displayed by the echo command in the file file, and nothing will be displayed on the screen. If the file does not exist, the command will fail and display the error message: Cannot append redirect. If the file exists, its contents will be added to what already exists in the file.  
  
cat files - Concatenate the contents of the files and display it at standard output. In case of an error, the text: Cannot print file 
  
  
mv destination source - Rename the source file to the destination. In case of error, it will display the message Cannot move file.
  
  
rm [option] files - Delete files given in the command line. With no options, it just delete the files that are empty. If an attempt is made to delete a non-empty file, the error message will be displayed: Cannot remove file. File not empty 
-r, -R, --recursive delete files regardless of whether they are empty or not  
  
ls [options] - Lists the contents of the directory. Without the -a / –all option, hidden / hidden files (whose name starts with.) the hidden files are not displayed . If it receives a file name as a parameter, it will display the parameter itself. Each file will be displayed on a new line.
-a, --all also show hidden files / directories (whose names start with.)
-l, --long displays file size information in the form: name size.  
  
cp destination source - Copies a file with the destination name. In case of error, the message Cannot copy file will be displayed.
  
set <var> <cmd> - Saves the result of running the cmd command in the var variable.  
  
  
  
  
  

