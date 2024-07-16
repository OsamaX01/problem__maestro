# Problem Maestro
## Abstract
This is a project on implementing a new web application that aims to enhance the learning experience
in programming among college students. The program is trying to solve time-consuming in making
problems in programming and the need for customized solutions. Partnering with course instructors,
this app will be using OpenAI's API with professors wanting to create customized questions relevant to
the university curriculum about programming. This interactive platform offers a lot of challenging
problems with AI-driven guidance and solutions to bridge the gap from theory to practice. We would
like to build an active culture for learning programming that would foster programming skills and
further engage our college's programming community.

## High Level Design 
<img src="https://github.com/user-attachments/assets/969843df-ce34-44f2-8f88-534a85fea51c" alt="image" width="400"/>

The system will have four main components:
1. Instructor: This component is responsible for managing and creating educational content,
such as courses, problem sets, and assignments.
2. Student: This component represents the person who accesses the system to solve
problems, submit their work, and receive feedback.
3. Database: This component is responsible for storing and managing the system's data,
including user information, course information, problem sets, and student progress. It
ensures that the system's data is accurate, up-to-date, and easily accessible.
4. Open AI: This component is focused on AI technology to enhance the system's
functionality. The AI will mainly help instructors generate problems and automate the problem-writing process.

## App Demo 
[![Video Title](https://img.youtube.com/vi/Zq8W_oVmqmk/0.jpg)](https://www.youtube.com/watch?v=Zq8W_oVmqmk)

## App Flowchart
![flowchart_page-0001](https://github.com/user-attachments/assets/59db7b0c-3572-4b02-bb5e-a6329e8447f9)

## ER Diagram
<img src="https://github.com/user-attachments/assets/14d9fc97-e78f-4a15-b487-1cc8c66473b1" alt="image" width="800"/>

## System Architecture and Design
### Django's Reusable Apps
Each app in Django is designed to handle a specific piece of functionality, encapsulating related
models, views, templates, and static files. This feature supports the single responsibility and the
separation of concerns principles and helps us to maintain and test components independently,
reducing the complexity of the code.
In our application, the apps are divided as follows:

1. Course App: Responsible for managing courses.
2. Problem App: Responsible for managing problems.
3. Dashboard App: Responsible for managing the dashboard and navbar.
4. Editor App: Responsible for running codes and validating solutions.
5. Users App: Responsible for managing users' authentication system.
6. OpenAI API App: Responsible for integrating generative AI capabilities.

### Apps Structure & MVT Architectural Pattern
The choice of a robust architectural pattern is crucial for the success of any software project, Model-View-Template (MVT) architectural pattern is adopted in each app, with a specific
focus on Python Django Web Framework.
MVT provides a structured and modular approach to organizing code, separating concerns
related to data models, user interfaces, and control flow. The MVC components in our system
are organized as follows:
1. Model (M): The data models represent the structure of programming problems, user
information, and other relevant entities. These models are designed to encapsulate data
and business logic, ensuring a clear and maintainable representation of our application's
core entities.
2. View (V): Handles the presentation logic. In Django, views process incoming HTTP
requests, interact with the models to retrieve or manipulate data and return appropriate
HTTP responses. The views are responsible for processing user input, interacting with
the models, and rendering templates to generate the final output.
3. Template (T): Defines how the data from the views should be presented. Django
Templates are responsible for dynamically generating HTML based on the data
provided by the views.

<img src="https://github.com/user-attachments/assets/1970fe74-206c-48a3-9fee-3f06a51776a6" alt="image" width="800"/>

