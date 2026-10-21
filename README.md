Student Performance Analysis System 🎓📊
A Python-based data analysis tool designed to process student academic records, calculate aggregate marks and averages using NumPy and Pandas, determine subject-wise performance, assign grades, and identify top-performing students.

🚀 Features
Automated Data Processing: Loads and cleans student records directly from CSV datasets using Pandas.   
Vectorized Calculations: Utilizes NumPy arrays for high-performance computation of total marks and average scores.   
Academic Grading & Evaluation: Automatically maps average marks to letter grades and evaluates pass/fail status based on customized thresholds.   
Subject-Wise Analytics: Computes average scores across multiple subjects (Math, Physics, Chemistry, English, and Computer Science) to highlight strongest academic areas.   
IPYNB
Top Performers Ranking: Sorts and extracts the top 
N performing students to recognize academic excellence.   

📂 Project Structure
Plaintext
├── student_performance_dataset.csv   # Dataset containing student marks, attendance, and departments
├── main.py                           # Main execution script running the data pipeline and reporting
├── functions.py                      # Modular utility functions for calculations, grading, and sorting
└── README.md                         # Project documentation

📊 Dataset Schema (student_performance_dataset.csv)
The dataset contains records for 50 students across various engineering departments (Computer Science, Electronics, Civil, Mechanical, and Information Technology).   
Column Name	Data Type	Description
Student ID	String	
Unique identifier for each student (e.g., STU1001) 

Name	String	
Full name of the student 
Department	String	
Engineering branch / department 
Math	Integer	
Marks obtained in Mathematics (0–100) 
Physics	Integer	
Marks obtained in Physics (0–100) 
Chemistry	Integer	
Marks obtained in Chemistry (0–100) 
English	Integer	
Marks obtained in English (0–100) 
Computer_Science	Integer	
Marks obtained in Computer Science (0–100) 
Attendance	Integer	
Student attendance percentage 

🛠️ Requirements & Dependencies
Make sure you have Python installed along with the required data science libraries:
'pip install pandas numpy'

⚙️ How to Run
Clone the repository and navigate to the project directory.
Ensure student_performance_dataset.csv, main.py, and functions.py are in the same folder.

Run the analysis script:
'python main.py'

📈 Sample Output Overview
When executed, the script outputs a comprehensive terminal summary including:
1) Overall Class Average Mark   
2) Highest and Lowest Student Averages   
3) Total Passing vs. Failing Students Count   
4) Subject-wise Average Performance Breakdown & Best Performing Subject   
5) A neatly formatted table of the Top 5 Performing Students
