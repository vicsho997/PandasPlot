import pandas as pd
import numpy as np
"""

BROKEN FILE BECAUSE OF RAW


"""
df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6],
                   "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']}

#Convert the raw grades to a categorical data type.

df["grade"] = df["raw_grade"].astype("category")

df["grade"])


#Rename the categories to more meaningful names (assigning to Series.cat.categories is inplace!).

df["grade"].cat.categories = ["very good", "good", "very bad"]



#Reorder the categories and simultaneously add the missing categories (methods under Series .cat return a new Series by default).
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium",
  "good", "very good"])

df["grade"]

#Sorting is per order in the categories, not lexical order.
df.sort_values(by="grade")

#Grouping by a categorical column also shows empty categories.
df.groupby("grade").size()
