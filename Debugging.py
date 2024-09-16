//Question: You have been tasked with reviewing and updating this program. What steps would you take to identify any issues in the code?
Your Response:

	First understand the goal of the code. Then I will break down the body of code into sections to understand how each is being used. After that I will change what is needed.

Question: What actions could the developer have taken to minimize the number of errors?
Your Response:

	Developer should plan and outline before actually coding as well as test the code to see its outcome. 

Debbugging Exercise:

// This pseudocode is intended to determine whether students have
// passed or failed a course; student needs to average 60 or
// more on two tests. 
start
   Declarations
      num firstTest
      num secondTest
      float average
      num PASSING 
      PASSING = 60
   firstTest = input("Enter first score or 0 to quit")
   while firstTest <> to 0
      output "Enter second score "
      input secondTest
      average = (firstTest + secondTest) / 2
      ouput "Average is ", average
      if average >= PASSING then
         output "Pass"
      else
         output "Fail"
      endif
      
      output "Enter first score or 0 to quit "
      input firstTest
   endwhile
stop