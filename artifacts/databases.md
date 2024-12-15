---
layout: default
title: "Databases"
---

# Databases

## Original and Enhanced Artifact  
- [Original Code](../GroceryTrackerOriginal/)  
- [Enhanced Code](../GroceryItemTrackerSQLite/)

## Narrative Addressing Enhancements  

**Enhancements Implemented:**  
1. Brief Description of the Artifact
The artifact I chose for my ePortfolio is the Grocery Store Item Tracker, a command-line application originally developed in C++ during my CS-210 Programming Languages course. This program reads a list of grocery items from a text file, tracks the frequency of each item, and allows users to interact with the data through a menu-driven interface. The project introduced me to foundational programming concepts, including file I/O, frequency mapping, and user interaction.
For this enhancement, I transitioned the artifact from C++ to Python and replaced the text file storage with an SQLite database to provide a more robust and scalable solution. Additional features, such as item deletion, quantity subtraction, and data export, were also introduced to extend the program’s functionality and align it with industry expectations.

2. Justification for Including the Artifact
I included the Grocery Store Item Tracker in my ePortfolio because it effectively demonstrates my ability to adapt foundational software to meet higher standards of scalability, maintainability, and usability. This project highlights my skills in:
- Database Integration: I replaced a simple text file storage mechanism with an SQLite database, improving data persistence and enabling advanced operations such as searching, sorting, and analytics.
- Innovative Design: New features like CSV export and enhanced error handling showcase my ability to anticipate user needs and design solutions that deliver value.
- Problem-Solving: The artifact demonstrates my ability to address technical challenges, such as managing duplicate entries through case normalization and ensuring quantity updates respect logical constraints.
The enhancements made to this artifact align with real-world software engineering practices and illustrate my proficiency in designing user-focused and database-driven applications.

3. Meeting Course Outcomes
- Outcome 1:
"Employ strategies for building collaborative environments that enable diverse audiences to support organizational decision making in the field of computer science."
While this was a solo project, the modular design, structured database schema, and clear commenting ensure that the artifact can be easily understood and maintained by other developers. This supports collaboration in team-based projects.
- Outcome 2:
"Design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts."
The program outputs, such as frequency histograms and CSV export files, are designed to be clear and user-friendly, enabling communication of data insights to a diverse audience. Additionally, I provided comprehensive documentation and modular code structure, ensuring the artifact remains adaptable and easy to understand.
- Outcome 3:
"Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution, while managing the trade-offs involved in design choices (data structures and algorithms)."
Transitioning the program from text file storage to an SQLite database required designing and implementing an optimized database schema. I ensured that the solution efficiently handled data retrieval, updates, and analytics while balancing trade-offs such as data normalization and ease of use.
- Outcome 4:
"Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals (software engineering/design/database)."
I applied modern database tools and techniques, such as:
- Parameterized SQL queries to secure against SQL injection.
- Quantity subtraction and item deletion to improve user functionality.
- CSV export functionality to enable data sharing and reporting.
These enhancements showcase my ability to build database-driven solutions that deliver value and align with real-world practices.
- Outcome 5:
"Develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources."
I incorporated a security-first approach by using parameterized queries to mitigate SQL injection risks and implementing input validation to ensure data integrity. For example, I prevented logical errors, such as subtracting quantities below zero, which could compromise the application’s reliability


4. Reflection on the Enhancement Process
Enhancing the Grocery Store Item Tracker was a challenging yet rewarding experience that solidified my understanding of software engineering and database design. Transitioning from text file storage to a database system required me to rethink data flow and optimize performance. Implementing features like item deletion, quantity updates, and CSV export tested my ability to anticipate and address user needs while ensuring the program’s functionality remained robust.
One of the primary challenges was ensuring data integrity, particularly in handling duplicate entries with different capitalizations and updating quantities logically. Through iterative testing and debugging, I successfully resolved these issues, improving the artifact’s reliability and usability.
This enhancement process deepened my understanding of modular design, database integration, and secure coding practices. It also reinforced my ability to translate foundational programming concepts into real-world applications, making this artifact a meaningful representation of my growth as a computer science professional.

Conclusion
The enhanced Grocery Store Item Tracker represents a comprehensive demonstration of my skills in database management, software engineering, and secure application design. By aligning this artifact with key program outcomes, I have shown my ability to create scalable, innovative, and secure solutions that deliver value to users. This project exemplifies my readiness to contribute to complex software development environments and is a valuable addition to my ePortfolio.


