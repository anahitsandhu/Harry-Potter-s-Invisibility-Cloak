# Harry-Potter-s-Invisibility-Cloak
To make a specific color invisible, like it's Harry Potter's Invisibility Cloak

In this code, any black color would be invisible.
First, the code will prompt you to leave the frame so that a snapshot of the background can be taken. Hence, it's not in real-time.
Then, once the webcam starts, any black object in their view will be 'invisible.'
For the background, 30 pictures are clicked on at an interval of 0.1 seconds, and a median of the images clicked is picked up in the background.
morphologyEx is used to remove noise or fill small holes to achieve a cleaner result.
A range of colours is given for black so that it may detect any shade of black and the colors are in HSV
You can press 'q' to release the webcam. 
