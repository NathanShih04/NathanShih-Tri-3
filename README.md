# NathanShih-Tri-3

## Notes 5.1, 5.2, and actions
5.1 Beneficial and Harmful Effects
* Technology can be used to help but also hurt people
* Accelerometer:
  * Automobile industry drove price down
  * Used for airbag deployment and lateral movement detection
* Quadcopter “brain”
* Multirotor
  * Benefit - deliveries, finding lost people, aerial photography
  * Harmful - flying in unregulated zones is illegal and dangerous
* Wii controller
  * Benefit - gets people active with videogames
  * Harmful - Broken TV’s and injuries
* 3D Printers
  * Open-source software for computer and printer
  * Can make organs/prosthetics, houses, shoes
* Internet
  * People spend more time on internet than sleeping
  * Sleep deprivation, depression, anxiety, impulsivity, dopamine feedback loops
* Microtransactions
  * “Free” Games/Apps
  * Cosmetics, paywall to functionality, pay-to-win

5.1 Actions:
* Online chat like Discord
  * Benefit - Easy communication between people
  * Harm - Limits real world interactions and can lead to cyberbullying
* Video Games
  * Benefit - Allows people to have fun with friends and destress
  * Can destract one of grades and other important things in life
* YouTube
  * Benefit - Can learn off of the platform and find entertainment
  * Harm - Can act as a distraction and create toxic interactions

* Dopamine issues are present and things like YouTube and social media impact my personal study and success in highschool by distracting me and taking away time for productive work. There are also things like Discord which allow me to talk to friends and distract me from getting homework done. I get dopamine out of these things and always want to do them even if it hurts my school performance.

5.2 Digital Divide
* Based on socioeconomic and geographic demographics
* In some countries
  * Computers are not common in rural areas
  * Only small number of websites
  * Internet used to protect government
  * High level of surveillance to protect government

5.2 Actions:
* Someone can empower themselves in a digital world by providing help on forums or even creating websites for people that aren't familiar with technology.
* Someone that is empowered can help someone that is not empowered by making a website for a club that isn't familiar with technology. Make a Del Norte website for a Del Norte club.
* Red tape blocking is not empowerment as it hinders one's ability to utilize technology to the fullest. There is red tape blocking at Del Norte in the form of their blocker where some websites cannot be accessed without a vpn. In order to run a deployed website, one has to use a vpn.

## Notes on Data Structures Project
[Repl Menu](https://replit.com/@TankeeTort/NathanShih-Tri-3)
Comments are inside of the code

## Create Task Project
### Ideas
* GPA Calc for student athletes
* Sports game
* Sports Quiz
### Final Decision
The idea we decided on in the end was a sports logo quiz. With the GPA calculator, we weren't able to get a couple requirements. And we weren't sure what sports game to create without it being wildly complicated. Which left us with our quiz. In our quiz, a sports team will be written at the top and you have to try and guess which logo is that team's out of 4 options. It will keep tally of your score and give you a final score at the end.
| Requirement  | Application |
| ------------- | ------------- |
| One list (or other collection type) | List of Questions for quiz.  |
| One Procedure  | Called function to shuffle quiz questions on load.  |
| Algorithm that includes sequencing, selection, and iteration  | Also included in question order randomizer. |
| Calls to student developed procedure | Calls question shuffler for random question order. |
| User Input  | Logo/answers for each question. |
| Instructions for output  | Final score at the end of the quiz. |

### Create Task Plan: Sports Team Logo Guesser Game

□ Instructions for input from one of the following: ◆ the user (including user actions that trigger events) ◆ a device ◆ an online data stream ◆ a file

User input that will be included is the answers to each question which would be the logos.

□ Use of at least one list (or other collection type) to represent a collection of data that is stored and used to manage program complexity and help fulfill the program’s purpose

We have a list of our various questions and their answers in order to be pulled when the user starts the quiz and creates a randomly ordered quiz for them.

□ At least one procedure that contributes to the program’s intended purpose, where you have defined: ◆ the procedure’s name ◆ the return type (if necessary) ◆ one or more parameters

One Procedure that is included is our shuffle function which is called when the page is opened. When called, it takes the list of questions and randomly orders them for the quiz.

□ An algorithm that includes sequencing, selection, and iteration that is in the body of the selected procedure

Algorithm will use selection when it picks a question to display. Iteration will be displayed in that the process of displaying a question, getting an inputted logo answer, and telling the user if they are correct will be completed at the end and the player will be given a score depending on their accuracy. 
   
□ Calls to your student-developed procedure

After the player clicks next when getting a logo guess right/wrong a logo will be displayed for the user to guess.

□ Instructions for output (tactile, audible, visual, or textual) based on input and program functionality

Textual output that displays the user's final score at the end. 
[Wiki/Jekyll page with design ideas and usage](https://github.com/NoahJ214/Team-Aaiaa-Project-Tri-2/wiki/Create-Task-Plan-Tim,-Nat,-Noa) - Clear wiki page with outline of Create Task. Gives ideas of what to improve on, as well as all collegeboard features that are specifically met. 

[Create Performance Task PBL feature](https://aaiaa.crabdance.com/imageQuiz) - Create Task already implemented into PBL website as a key feature. Running and functioning asynchronously. 

[Final committed program code showing algorithms written in JS/Python](https://github.com/NoahJ214/Team-Aaiaa-Project-Tri-2/blob/main/templates/imageQuiz.html) - final program code written in javascript linked in github repo, shows algorithms (line 113 and below specifically)

[Written responses to CollegeBoard prompts](https://github.com/NoahJ214/Team-Aaiaa-Project-Tri-2/wiki/Written-Responses-CB-Create-Task-Nat,-Tim,-Noa) - Link to all written responses, with questions written out in wiki.

[1 min video that meets CB Create Task requirements](https://www.youtube.com/watch?v=tIFjXzPk2rs&feature=youtu.be) - Link to under 1 min video under 30 MB fits all requirements
