import matplotlib.pyplot as plt

# ---------------- SIMPLE DATA ----------------

days_simple = ["Mon", "Tue", "Wed", "Thu", "Fri"]
hours_simple = [1, 2, 3, 5, 7]

students_simple = ["Alice", "Bob", "Charlie", "David"]
books_simple = [4, 7, 2, 3]

scores_simple = [55, 62, 65, 70, 72, 75, 78, 85, 88, 95]

# ---------------- COMPLEX DATA ----------------

days_complex = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours_complex = [2, 4, 3, 6, 8, 7, 9]

students_complex = [
    "Alice", "Bob", "Charlie", "David",
    "Emma", "Frank", "Grace", "Henry"
]
books_complex = [4, 7, 2, 3, 8, 5, 6, 9]

scores_complex = [
    45, 50, 55, 58, 60, 62, 65, 67, 70, 72,
    74, 75, 78, 80, 82, 85, 88, 90, 92, 95
]

# Create 2 rows and 3 columns
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 8))

fig.suptitle(
    "Comparison of Simple Data vs Complex Data",
    fontsize=16,
    fontweight="bold"
)

# =================================================
# SIMPLE DATA VISUALIZATION (ROW 1)
# =================================================

# Line Plot
axes[0, 0].plot(days_simple, hours_simple, marker="o", color="blue")
axes[0, 0].set_title("Simple Line Plot")
axes[0, 0].set_xlabel("Days")
axes[0, 0].set_ylabel("Study Hours")
axes[0, 0].grid(True)

# Bar Chart
axes[0, 1].bar(students_simple, books_simple,
               color=["pink", "skyblue", "lightgreen", "orange"])
axes[0, 1].set_title("Simple Bar Chart")
axes[0, 1].set_xlabel("Students")
axes[0, 1].set_ylabel("Books Read")

# Histogram
axes[0, 2].hist(scores_simple,
                bins=[50, 60, 70, 80, 90, 100],
                color="purple",
                edgecolor="black")
axes[0, 2].set_title("Simple Histogram")
axes[0, 2].set_xlabel("Score Range")
axes[0, 2].set_ylabel("Frequency")

# =================================================
# COMPLEX DATA VISUALIZATION (ROW 2)
# =================================================

# Line Plot
axes[1, 0].plot(days_complex, hours_complex,
                marker="o", color="red", linewidth=2)
axes[1, 0].set_title("Complex Line Plot")
axes[1, 0].set_xlabel("Days")
axes[1, 0].set_ylabel("Study Hours")
axes[1, 0].grid(True)

# Bar Chart
axes[1, 1].bar(students_complex, books_complex,
               color="lightgreen")
axes[1, 1].set_title("Complex Bar Chart")
axes[1, 1].set_xlabel("Students")
axes[1, 1].set_ylabel("Books Read")
axes[1, 1].tick_params(axis='x', rotation=45)

# Histogram
axes[1, 2].hist(scores_complex,
                bins=[40, 50, 60, 70, 80, 90, 100],
                color="orange",
                edgecolor="black")
axes[1, 2].set_title("Complex Histogram")
axes[1, 2].set_xlabel("Score Range")
axes[1, 2].set_ylabel("Frequency")

plt.tight_layout()
plt.show()