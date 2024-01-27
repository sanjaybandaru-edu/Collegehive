@echo off

REM Creating directories and .md files for Information Systems and E-Business (ISEB)
mkdir ISEB
cd ISEB

REM Unit 1: Foundation of Information Systems
mkdir "Unit-1 Foundation of Information Systems"
cd "Unit-1 Foundation of Information Systems"
type nul > "1.a Concept of Information System.md"
type nul > "1.b Role of Information System in Business.md"
type nul > "1.c Trends in Information System.md"
type nul > "1.d Types of Information System.md"
type nul > "1.e Components of Information System.md"
type nul > "1.f Information System Resources.md"
type nul > "1.g Information System Activities.md"
type nul > "1.h Business Process.md"
type nul > "1.i Role of Information Systems Function in Business.md"
cd ..

REM Unit 2: Data Resource Management
mkdir "Unit-2 Data Resource Management"
cd "Unit-2 Data Resource Management"
type nul > "2.a DBMS Concepts and Models.md"
type nul > "2.b Business Intelligence Infrastructure.md"
type nul > "2.c Data Warehouse and Analytical Tools.md"
type nul > "2.d OLAP and OLTP.md"
type nul > "2.e Data Mining, Web Mining, Text Mining.md"
type nul > "2.f Information Policy for Managing Firm's Data Resources.md"
cd ..

REM Unit 3: Emerging Technologies
mkdir "Unit-3 Emerging Technologies"
cd "Unit-3 Emerging Technologies"
type nul > "3.a Digital Transformation.md"
type nul > "3.b Overview of Emerging Technologies.md"
type nul > "3.c Data to Analytics to AI.md"
type nul > "3.d Connected Clouds.md"
type nul > "3.e Augmented Reality.md"
type nul > "3.f Internet of Things (IoT).md"
type nul > "3.g Big Data and Industry 4.0.md"
type nul > "3.h Future Technologies.md"
cd ..

REM Unit 4: E-Business
mkdir "Unit-4 E-Business"
cd "Unit-4 E-Business"
type nul > "4.a Introduction to E-Business.md"
type nul > "4.b Cross Functional Enterprise Applications.md"
type nul > "4.c IT in Business.md"
type nul > "4.d Marketing Systems.md"
type nul > "4.e Manufacturing Systems.md"
type nul > "4.f Human Resource System.md"
type nul > "4.g Financial Management Systems.md"
cd ..

REM Unit 5: E-Commerce
mkdir "Unit-5 E-Commerce"
cd "Unit-5 E-Commerce"
type nul > "5.a E-Commerce Today.md"
type nul > "5.b New E-commerce (SMAC).md"
type nul > "5.c Key Concepts in E-Commerce.md"
type nul > "5.d Ecommerce Types and Business Models.md"
type nul > "5.e Revenue Model.md"
type nul > "5.f Social E-commerce.md"
type nul > "5.g E-Payment Systems.md"
cd ..

REM Unit 6: M-Commerce
mkdir "Unit-6 M-Commerce"
cd "Unit-6 M-Commerce"
type nul > "6.a Emerging Mobile Digital Platform.md"
type nul > "6.b Evolution of M-commerce.md"
type nul > "6.c M-commerce Applications.md"
type nul > "6.d Challenges of M-commerce.md"
type nul > "6.e Components of Mobile Commerce.md"
type nul > "6.f Payment Systems.md"
type nul > "6.g Growth of M-commerce.md"
cd ..

REM Unit 7: Ethical and Social Challenges in Information Systems
mkdir "Unit-7 Ethical and Social Challenges in Information Systems"
cd "Unit-7 Ethical and Social Challenges in Information Systems"
type nul > "7.a Ethical and Social Issues.md"
type nul > "7.b Legal Issues.md"
type nul > "7.c Privacy Issues.md"
type nul > "7.d Ethical Issues.md"
type nul > "7.e Accountability and Liability Issues.md"
type nul > "7.f Internet Challenges to Privacy.md"
type nul > "7.g Information Act in India.md"
cd ..

REM Return to the main directory
cd ..
