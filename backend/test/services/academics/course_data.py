"""Course data for tests."""

import pytest
from sqlalchemy.orm import Session
from ....entities.academics import CourseEntity
from ....models.academics import Course
from ..reset_table_id_seq import reset_table_id_seq
from datetime import datetime

__authors__ = ["Ajay Gandecha"]
__copyright__ = "Copyright 2023"
__license__ = "MIT"

comp_110 = Course(
    id="comp110",
    subject_code="COMP",
    number="110",
    title="Introduction to Programming and Data Science",
    description="Introduces students to programming and data science from a computational perspective. With an emphasis on modern applications in society, students gain experience with problem decomposition, algorithms for data analysis, abstraction design, and ethics in computing. No prior programming experience expected. Foundational concepts include data types, sequences, boolean logic, control flow, functions/methods, recursion, classes/objects, input/output, data organization, transformations, and visualizations. Students may not enroll in COMP 110 after receiving credit for COMP 210. IDEAs in Action Gen Ed: FC-QUANT. Requisites: Prerequisite, A C or better in one of the following courses: MATH 130, 152, 210, 231, 129P, or PHIL 155, or STOR 120, 151, 155.",
    credit_hours=3,
    prereqs="'comp210' not in taken_courses",
    isBA=True,
    isBS=True,
)

comp_210 = Course(
    id="comp210",
    subject_code="COMP",
    number="210",
    title="Data Structures and Analysis",
    description="This course will teach you how to organize the data used in computer programs so that manipulation of that data can be done efficiently on large problems and large data instances. Rather than learning to use the data structures found in the libraries of programming languages, you will be learning how those libraries are constructed, and why the items that are included in them are there (and why some are excluded). Requisites: Prerequisites, COMP 110 and MATH 231; a grade of C or better is required in both prerequisite courses ; Pre- or corequisite, COMP 283 or MATH 381.",
    credit_hours=3,
    prereqs="'comp110' in taken_courses and 'math231' in taken_courses",
    isBA=True,
    isBS=True,
)

comp_301 = Course(
    id="comp301",
    subject_code="COMP",
    number="301",
    title="Foundations of Programming",
    description="Students will learn how to reason about how their code is structured, identify whether a given structure is effective in a given context, and look at ways of organizing units of code that support larger programs. In a nutshell, the primary goal of the course is to equip students with tools and techniques that will help them not only in later courses in the major but also in their careers afterwards. Requisites: Prerequisites, COMP 210; COMP 283 or MATH 381; a grade of C or better is required in both prerequisite courses.",
    credit_hours=3,
    prereqs="'comp210' in taken_courses and 'comp283' in taken_courses",
    isBA=True,
    isBS=True,
)

comp_050 = Course(
    id="comp050",
    subject_code="COMP",
    number="050",
    title="First-Year Seminar: Everyday Computing",
    description="The goal of this first-year seminar is to understand the use of computing technology in our daily activities. In this course, we will study various examples of how computing solves problems in different aspects in our daily life. Honors version available.",
    credit_hours=3,
    prereqs="True",
    isBA=False,
    isBS=False,
)

comp_060 = Course(
    id="comp060",
    subject_code="COMP",
    number="060",
    title="First-Year Seminar: Robotics with LEGO®",
    description="This seminar explores the process of design and the nature of computers by designing, building, and programming LEGO robots. Competitions to evaluate various robots are generally held at the middle and at the end of the semester. Previous programming experience is not required. Honors version available.",
    credit_hours=3,
    prereqs="True",
    isBA=False,
    isBS=False,
)

comp_065 = Course(
    id="comp065",
    subject_code="COMP",
    number="065",
    title="First-Year Seminar: Folding, from Paper to Proteins",
    description="Explore the art of origami, the science of protein, and the mathematics of robotics through lectures, discussions, and projects involving artistic folding, mathematical puzzles, scientific exploration, and research. Honors version available.",
    credit_hours=3,
    prereqs="True",
    isBA=False,
    isBS=False,
)

comp_089 = Course(
    id="comp089",
    subject_code="COMP",
    number="089",
    title="First-Year Seminar: Special Topics",
    description="Special topics course. Content will vary each semester. Honors version available.",
    credit_hours=3,
    prereqs="True",
    isBA=False,
    isBS=False,
)

comp_116 = Course(
    id="comp116",
    subject_code="COMP",
    number="116",
    title="Introduction to Scientific Programming",
    description="An introduction to programming for computationally oriented scientists. Fundamental programming skills, typically using MATLAB or Python. Problem analysis and algorithm design with examples drawn from simple numerical and discrete problems. Requisites: Prerequisite, MATH 231 or 241",
    credit_hours=3,
    prereqs="'math231' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_126 = Course(
    id="comp126",
    subject_code="COMP",
    number="126",
    title="Practical Web Design and Development for Everyone",
    description="A ground-up introduction to current principles, standards, and best practice in website design, usability, accessibility, development, and management through project-based skills development in HTML5, CSS, and basic JavaScript. Intended for nonmajors. IDEAs in Action Gen Ed: FC-CREATE.",
    credit_hours=3,
    prereqs="True",
    isBA=False,
    isBS=False,
)

comp_211 = Course(
    id="comp211",
    subject_code="COMP",
    number="211",
    title="Systems Fundamentals",
    description="This is the first course in the introductory systems sequence. Students enter the course having taken an introductory programming course in a high-level programming language (COMP 110) and a course in discrete structures. The overarching goal is to bridge the gap between a students' knowledge of a high-level programming language (COMP 110) and computer organization (COMP 311). Requisites: Prerequisites, COMP 210; COMP 283 or MATH 381; a grade of C or better is required in both prerequisite courses.",
    credit_hours=3,
    prereqs="'comp210' in taken_courses and 'comp283' in taken_courses",
    isBA=True,
    isBS=True,
)

comp_227 = Course(
    id="comp227",
    subject_code="COMP",
    number="227",
    title="Foundations of Software Engineering",
    description="Fundamentals of computer science pedagogy and instructional practice with primary focus on training undergraduate learning assistants for computer science courses. Emphasis on awareness of social identity in learning, active learning in the computer science classroom, and effective mentorship. All students must be granted a computer science learning assistantship or obtain prior approval to substitute relevant practicum experience prior to enrollment. IDEAs in Action Gen Ed: HI-LEARNTA. Requisites: Pre- or corequisite, COMP 210 or 401.",
    credit_hours=3,
    prereqs="True",
    isBA=False,
    isBS=False,
)

comp_283 = Course(
    id="comp283",
    subject_code="COMP",
    number="283",
    title="Discrete Structures",
    description="Introduces discrete structures (sets, tuples, relations, functions, graphs, trees) and the formal mathematics (logic, proof, induction) used to establish their properties and those of algorithms that work with them. Develops problem-solving skills through puzzles and applications central to computer science. The same as MATH 381. Honors version available. IDEAs in Action Gen Ed: FC-QUANT. Requisites: Prerequisite, MATH 231 or MATH 241",
    credit_hours=3,
    prereqs="'math231' in taken_courses",
    isBA=True,
    isBS=True,
)

comp_290 = Course(
    id="comp290",
    subject_code="COMP",
    number="290",
    title="Special Topics in Computer Science",
    description="Non-technical topics in computer science for computer science majors. May not be used to satisfy any degree requirements for a computer science major. This course has variable content and may be taken multiple times for credit.",
    credit_hours=1,
    prereqs="True",
    isBA=False,
    isBS=False,
)

comp_311 = Course(
    id="comp311",
    subject_code="COMP",
    number="311",
    title="Computer Organization",
    description="Introduction to computer organization and design. Students will be introduced to the conceptual design of a basic microprocessor, along with assembly programming. The course includes fundamental concepts such as binary numbers, binary arithmetic, and representing information as well as instructions. Students learn to program in assembly (i.e., machine) language. The course covers the fundamentals of computer hardware design, transistors and logic gates, progressing through basic combinational and sequential components, culminating in the conceptual design CPU. Requisites: Prerequisite, COMP 211; a grade of C or better is required.",
    credit_hours=3,
    prereqs="'comp211' in taken_courses",
    isBA=True,
    isBS=True,
)

comp_380 = Course(
    id="comp380",
    subject_code="COMP",
    number="380",
    title="Technology, Ethics, & Culture",
    description="This discussion-based, participatory course explores the personal, sociocultural, and ethical effects and implications of the development and use of computing technologies and the Internet. Honors version available. IDEAs in Action Gen Ed: FC-VALUES.",
    credit_hours=3,
    prereqs="True",
    isBA=False,
    isBS=False,
)

comp_393 = Course(
    id="comp393",
    subject_code="COMP",
    number="393",
    title="Software Engineering Practicum",
    description="Students develop a software program for a real client under the supervision of a faculty member. Projects may be proposed by the student but must have real users. Course is intended for students desiring practical experiences in software engineering but lacking the experience required for external opportunities. Majors only. Requisites: Prerequisites, COMP 211 and 301 a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp211' in taken_courses and 'comp301' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_401 = Course(
    id="comp401",
    subject_code="COMP",
    number="401",
    title="Foundation of Programming",
    description="Required preparation, a first formal course in computer programming (e.g., COMP 110, COMP 116). Advanced programming: object-oriented design, classes, interfaces, packages, inheritance, delegation, observers, MVC (model view controller), exceptions, assertions. Students may not receive credit for this course after receiving credit for COMP 301. Honors version available.",
    credit_hours=4,
    prereqs="True",
    isBA=False,
    isBS=False,
)

comp_421 = Course(
    id="comp421",
    subject_code="COMP",
    number="421",
    title="Files and Databases",
    description="Placement of data on secondary storage. File organization. Database history, practice, major models, system structure and design. Requisites: Prerequisites, COMP 210, 211, and 301; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp211' in taken_courses and 'comp301' in taken_courses and 'comp210' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_426 = Course(
    id="comp426",
    subject_code="COMP",
    number="426",
    title="Modern Web Programming",
    description="Developing applications for the World Wide Web including both client-side and server-side programming. Emphasis on Model-View-Controller architecture, AJAX, RESTful Web services, and database interaction. Requisites: Prerequisites, COMP 211 and 301; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp211' in taken_courses and 'comp301' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_431 = Course(
    id="comp431",
    subject_code="COMP",
    number="431",
    title="Internet Services and Protocols",
    description="Application-level protocols HTTP, SMTP, FTP, transport protocols TCP and UDP, and the network-level protocol IP. Internet architecture, naming, addressing, routing, and DNS. Sockets programming. Physical-layer technologies. Ethernet, ATM, and wireless. Requisites: Prerequisites, COMP 210, 211, and 301; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp211' in taken_courses and 'comp301' in taken_courses and 'comp210' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_433 = Course(
    id="comp433",
    subject_code="COMP",
    number="433",
    title="Mobile Computing Systems",
    description="Principles of mobile applications, mobile OS, mobile networks, and embedded sensor systems. Coursework includes programming assignments, reading from recent research literature, and a semester-long project on a mobile computing platform (e.g., Android, Arduino, iOS, etc.). ",
    credit_hours=3,
    prereqs="True",
    isBA=False,
    isBS=False,
)

comp_435 = Course(
    id="comp435",
    subject_code="COMP",
    number="435",
    title="Computer Security Concepts",
    description="Introduction to topics in computer security including confidentiality, integrity, availability, authentication policies, basic cryptography and cryptographic protocols, ethics, and privacy. A student may not receive credit for this course after receiving credit for COMP 535. Requisites: Prerequisites, COMP 210, 211, and 301; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp210' in taken_courses and 'comp211' in taken_courses and 'comp301' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_455 = Course(
    id="comp455",
    subject_code="COMP",
    number="455",
    title="Models of Languages and Computation",
    description="Introduction to the theory of computation. Finite automata, regular languages, pushdown automata, context-free languages, and Turing machines. Undecidable problems. Requisites: Prerequisites, COMP 210 and COMP 283 or MATH 381; a grade of C or better in all prerequisite courses is required.",
    credit_hours=3,
    prereqs="'comp210' in taken_courses and ('comp283' in taken_courses)",
    isBA=False,
    isBS=True,
)

comp_475 = Course(
    id="comp475",
    subject_code="COMP",
    number="475",
    title="2D Computer Graphics",
    description="Fundamentals of modern software 2D graphics; geometric primitives, scan conversion, clipping, transformations, compositing, texture sampling. Advanced topics may include gradients, antialiasing, filtering, parametric curves, and geometric stroking. Requisites: Prerequisites, COMP 210, 211, and 301; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp210' in taken_courses and 'comp211' in taken_courses and 'comp301' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_488 = Course(
    id="comp488",
    subject_code="COMP",
    number="488",
    title="Data Science in the Business World",
    description="Students will acquire hands-on data science skills enabling them to solve real-world business problems. Since data science is an interdisciplinary field, business and computer science students learn and work together in this course. Leveraging each other's skills and knowledge, students create data-driven business insights using modern analytics.",
    credit_hours=3,
    prereqs="True",
    isBA=False,
    isBS=False,
)

comp_520 = Course(
    id="comp520",
    subject_code="COMP",
    number="520",
    title="Compilers",
    description="Design and construction of compilers. Theory and pragmatics of lexical, syntactic, and semantic analysis. Interpretation. Code generation for a modern architecture. Run-time environments. Includes a large compiler implementation project. Requisites: Prerequisites, COMP 301, 311, and 455; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp301' in taken_courses and 'comp311' in taken_courses and 'comp455' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_523 = Course(
    id="comp523",
    subject_code="COMP",
    number="523",
    title="Software Engineering Laboratory",
    description="Organization and scheduling of software engineering projects, structured programming, and design. Each team designs, codes, and debugs program components and synthesizes them into a tested, documented program product. IDEAs in Action Gen Ed: FC-CREATE. Requisites: Prerequisites, COMP 301 and 311; or COMP 401, 410, and 411; as well as at least two chosen from COMP 421, 426, 431, 433, 520, 530, 535, 575, 580.",
    credit_hours=4,
    prereqs="('comp301' in taken_courses and 'comp311' in taken_courses) or ('comp401' in taken_courses and 'comp410' in taken_courses and 'comp411' in taken_courses) and (sum([('comp421' in taken_courses), ('comp426' in taken_courses), ('comp431' in taken_courses), ('comp433' in taken_courses), ('comp520' in taken_courses), ('comp530' in taken_courses), ('comp535' in taken_courses), ('comp575' in taken_courses), ('comp580' in taken_courses)]) >= 2)",
    isBA=False,
    isBS=False,
)

comp_524 = Course(
    id="comp524",
    subject_code="COMP",
    number="524",
    title="Programming Language Concepts",
    description="Concepts of high-level programming and their realization in specific languages. Data types, scope, control structures, procedural abstraction, classes, concurrency. Run-time implementation. Requisites: Prerequisites, COMP 301, 311, and 455; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp301' in taken_courses and 'comp311' in taken_courses and 'comp455' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_530 = Course(
    id="comp530",
    subject_code="COMP",
    number="530",
    title="Operating Systems",
    description="Types of operating systems. Concurrent programming. Management of storage, processes, devices. Scheduling, protection. Case study. Course includes a programming laboratory. Honors version available. Requisites: Prerequisites, COMP 301 and 311; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp301' in taken_courses and 'comp311' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_533 = Course(
    id="comp533",
    subject_code="COMP",
    number="533",
    title="Distributed Systems",
    description="Distributed systems and their goals; resource naming, synchronization of distributed processes; consistency and replication; fault tolerance; security and trust; distributed object-based systems; distributed file systems; distributed Web-based systems; and peer-to-peer systems. Requisites: Prerequisite, COMP 431, 524, or 530; a grade of C or better is required; permission of the instructor for students lacking the prerequisite.",
    credit_hours=3,
    prereqs="'comp431' in taken_courses or 'comp524' in taken_courses or 'comp530' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_535 = Course(
    id="comp535",
    subject_code="COMP",
    number="535",
    title="Introduction to Computer Security",
    description="Principles of securing the creation, storage, and transmission of data and ensuring its integrity, confidentiality and availability. Topics include access control, cryptography and cryptographic protocols, network security, and online privacy. Requisites: Prerequisites, COMP 301 and 311; as well as COMP 550, and COMP 283 or MATH 381; a grade of C or better is required in all prerequisites.",
    credit_hours=3,
    prereqs="'comp301' in taken_courses and 'comp311' in taken_courses and 'comp550' in taken_courses and ('comp283' in taken_courses)",
    isBA=False,
    isBS=False,
)

comp_537 = Course(
    id="comp537",
    subject_code="COMP",
    number="537",
    title="Cryptography",
    description="Introduces both the applied and theoretical sides of cryptography. Main focus will be on the inner workings of cryptographic primitives and how to use them correctly. Begins with standard cryptographic tools such as symmetric and public-key encryption, message authentication, key exchange, and digital signatures before moving on to more advanced topics. Potential advanced topics include elliptic curves, post-quantum cryptography, and zero-knowledge proofs. Honors version available. Requisites: Prerequisites, COMP 211 and COMP 301; permission of the instructor for students lacking the prerequisites.",
    credit_hours=3,
    prereqs="'comp211' in taken_courses and 'comp301' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_541 = Course(
    id="comp541",
    subject_code="COMP",
    number="541",
    title="Digital Logic and Computer Design",
    description="This course is an introduction to digital logic as well as the structure and electronic design of modern processors. Students will implement a working computer during the laboratory sessions. Requisites: Prerequisites, COMP 301 and 311; a grade of C or better is required in all prerequisite courses.",
    credit_hours=4,
    prereqs="'comp301' in taken_courses and 'comp311' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_545 = Course(
    id="comp545",
    subject_code="COMP",
    number="545",
    title="Programming Intelligent Physical Systems",
    description="Introduction to programming embedded control systems that lie at the heart of robots, drones, and autonomous vehicles. Topics will include modeling physical systems, designing feedback controllers, timing analysis of embedded systems and software, software implementations of controllers on distributed embedded platforms and their verification. Honors version available. Requisites: Prerequisites, COMP 301 and COMP 311; a C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp301' in taken_courses and 'comp311' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_550 = Course(
    id="comp550",
    subject_code="COMP",
    number="550",
    title="Algorithms and Analysis",
    description="Formal specification and verification of programs. Techniques of algorithm analysis. Problem-solving paradigms. Survey of selected algorithms. IDEAs in Action Gen Ed: FC-QUANT. Requisites: Prerequisites, COMP 211 and 301; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp211' in taken_courses and 'comp301' in taken_courses",
    isBA=False,
    isBS=True,
)

comp_560 = Course(
    id="comp560",
    subject_code="COMP",
    number="560",
    title="Artificial Intelligence",
    description="Introduction to techniques and applications of modern artificial intelligence. Combinatorial search, probabilistic models and reasoning, and applications to natural language understanding, robotics, and computer vision. Requisites: Prerequisites, COMP 211 and 301; as well as MATH 231; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp211' in taken_courses and 'comp301' in taken_courses and 'math231' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_562 = Course(
    id="comp562",
    subject_code="COMP",
    number="562",
    title="Introduction to Machine Learning",
    description="Machine learning as applied to speech recognition, tracking, collaborative filtering, and recommendation systems. Classification, regression, support vector machines, hidden Markov models, principal component analysis, and deep learning. Honors version available. Requisites: Prerequisites, COMP 211 and 301; as well as MATH 233, 347, and STOR 435; a grade of C or better is required in all prerequisite courses; permission of the instructor for students lacking the prerequisites.",
    credit_hours=3,
    prereqs="'comp211' in taken_courses and 'comp301' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_572 = Course(
    id="comp572",
    subject_code="COMP",
    number="572",
    title="Computational Photography",
    description="The course provides a hands-on introduction to techniques in computational photography--the process of digitally recording light and then performing computational manipulations on those measurements to produce an image or other representation. The course includes an introduction to relevant concepts in computer vision and computer graphics. Requisites: Prerequisites, COMP 301; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp301' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_581 = Course(
    id="comp581",
    subject_code="COMP",
    number="581",
    title="Introduction to Robotics",
    description="Hands-on introduction to robotics with a focus on the computational aspects. Students will build and program mobile robots. Topics include kinematics, actuation, sensing, configuration spaces, control, and motion planning. Applications include industrial, mobile, personal, and medical robots. Honors version available. Requisites: Prerequisites, COMP 301 and 311; a grade of C or better is required in all prerequisite courses.",
    credit_hours=3,
    prereqs="'comp301' in taken_courses and 'comp311' in taken_courses",
    isBA=False,
    isBS=False,
)

comp_590 = Course(
    id="comp590",
    subject_code="COMP",
    number="590",
    title="Topics in Computer Science",
    description="This course has variable content and may be taken multiple times for credit. Different sections may be taken in the same semester. Honors version available.",
    credit_hours=3,
    prereqs="True",
    isBA=False,
    isBS=False,
)


math_231 = Course(
    id="math231",
    subject_code="MATH",
    number="231",
    title="Calculus of Functions of One Variable I",
    description="Limits, derivatives, and integrals of functions of one variable. Students may not receive credit for both MATH 231 and MATH 241. Honors version available. IDEAs in Action Gen Ed: FY-LAUNCH (only designated sections), FC-QUANT. Requisites: Prerequisite, MATH 110 and MATH 130; Requires a grade of C- or better in MATH 130 or placement by the department.",
    credit_hours=4,
    prereqs="True",
    isBA=True,
    isBS=True,
)

math_232 = Course(
    id="math232",
    subject_code="MATH",
    number="232",
    title="Calculus of Functions of One Variable II",
    description="Calculus of the elementary transcendental functions, techniques of integration, indeterminate forms, Taylor's formula, infinite series. Honors version available. IDEAs in Action Gen Ed: FY-LAUNCH (only designated sections), FC-QUANT. Requisites: Prerequisite, A grade of C- or better in MATH 231 or placement by the department.",
    credit_hours=4,
    prereqs="'math231' in taken_courses",
    isBA=False,
    isBS=True,
)


edited_comp_110 = Course(
    id="comp110",
    subject_code="COMP",
    number="110",
    title="Introduction to Programming",
    description="Introduces students to programming and data science from a computational perspective. With an emphasis on modern applications in society, students gain experience with problem decomposition, algorithms for data analysis, abstraction design, and ethics in computing. No prior programming experience expected. Foundational concepts include data types, sequences, boolean logic, control flow, functions/methods, recursion, classes/objects, input/output, data organization, transformations, and visualizations.",
    credit_hours=3,
    prereqs="true",
    isBA=True,
    isBS=True,
)

new_course = Course(
    id="comp423",
    subject_code="COMP",
    number="423",
    title="Foundations of Software Engineering",
    description="Best course in the department : )",
    credit_hours=3,
    prereqs="",
    isBA=False,
    isBS=False,
)

courses = [
    comp_110,
    comp_210,
    comp_301,
    comp_050,
    comp_060,
    comp_065,
    comp_089,
    comp_116,
    comp_126,
    comp_211,
    comp_227,
    comp_283,
    comp_290,
    comp_311,
    comp_380,
    comp_393,
    comp_421,
    comp_426,
    comp_431,
    comp_433,
    comp_435,
    comp_455,
    comp_475,
    comp_488,
    comp_520,
    comp_523,
    comp_524,
    comp_530,
    comp_533,
    comp_535,
    comp_537,
    comp_541,
    comp_545,
    comp_550,
    comp_560,
    comp_562,
    comp_572,
    comp_581,
    comp_590,
    math_231,
    math_232,
    comp_401,
]


def insert_fake_data(session: Session):
    for course in courses:
        entity = CourseEntity.from_model(course)
        session.add(entity)


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
