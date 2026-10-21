import numpy as np
import pandas as pd
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path('student_performance_dataset.csv').resolve().parent))
functions = importlib.import_module("functions")
assign_grades = functions.assign_grades
calculate_total_and_averages = functions.calculate_total_and_averages
check_pass_fail = functions.check_pass_fail
get_subject_averages = functions.get_subject_averages
get_top_performers = functions.get_top_performers

def main():
    print("=" * 60)
    print("Student Performance Analysis")
    print("=" * 60)

file_path = "student_performance_dataset.csv"
df = pd.read_csv(file_path)

print(df.head())

subjects = ["Math", "Physics", "Chemistry", "English", "Computer_Science"]

df["Total_Marks"], df["Average_Marks"] = calculate_total_and_averages(
      df, subjects)

df["Grade"] = df["Average_Marks"].apply(assign_grades)

df["Status"] = df.apply(
      lambda row: check_pass_fail(row, subjects, threshold=40), axis=1
  )

print("\n" + "=" * 50)
print(" PERFORMANCE ANALYSIS & SUMMARY ")
print("=" * 50)

overall_class_avg = np.mean(df["Average_Marks"].to_numpy())
print(f"Overall Class Average Mark: {overall_class_avg:.2f}")

highest_avg = df["Average_Marks"].max()
lowest_avg = df["Average_Marks"].min()
print(f"Highest Student Average: {highest_avg:.2f}")
print(f"Lowest Student Average: {lowest_avg:.2f}")

pass_count = (df["Status"] == "Pass").sum()
fail_count = (df["Status"] == "Fail").sum()
print(f"\nTotal Students Passed: {pass_count}")
print(f"Total Students Failed: {fail_count}")

print("\nSubject-wise Average Scores:")
subject_avgs = get_subject_averages(df, subjects)
for sub, avg in subject_avgs.items():
    print(f" - {sub}: {avg:.2f}")

best_subject = max(subject_avgs, key=subject_avgs.get)
print(f"\nBest Performing Subject: {best_subject} ({subject_avgs[best_subject]:.2f})")

int("\n" + "=" * 50)
print(" TOP 5 PERFORMING STUDENTS ")
print("=" * 50)
top_students = get_top_performers(df, n=5)
print(
    top_students[[
        "Student ID",
        "Name",
        "Department",
        "Total_Marks",
        "Average_Marks",
        "Grade",
        "Status",
        ]].to_string(index=False))