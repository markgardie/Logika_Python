import pandas as pd

df = pd.read_csv(r"digital_edu\train.csv")

df.drop(["id", "bdate", "has_photo"], axis=1, inplace=True)

def fill_form(form):
    if form == "Full-time":
        return 1
    return 0

df["education_form"] = df["education_form"].apply(fill_form, axis=1)

def fill_status(status):
    if status == "Alumnus (Specialist)":
        return 0
    if status == "Student (Bachelor's)":
        return 1
    if status == "Alumnus (Master's)":
        return 2
    return 3

df["education_form"] = df["education_form"].apply(fill_form, axis=1)

print(df.groupby(["education_status"], axis=1))