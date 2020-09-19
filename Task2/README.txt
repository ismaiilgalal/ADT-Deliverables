Firstly I used Google's OCR tool, called tesseract. It wokred perfectly for a lot of trial images, but on passing a screenshot for the schematic from the document, it gave me no results.

So, I tried different techniques for image processing (Mask & blue text images attached) before passing them to the OCR tool. This gave me some results, but it didn't accurately detect the labels correctly. Which led me to use another method.

I used Schemdraw library and defined custom PMOS and NMOS elements, and used both to draw the schematic. The result is correctly displayed upon closing the window, which is an error I was unfortunately unable to fix before the deadline.