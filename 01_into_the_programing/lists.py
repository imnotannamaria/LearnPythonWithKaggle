flowers_list = [
    "pink primrose",
    "hard-leaved pocket orchid",
    "canterbury bells",
    "sweet pea",
    "english marigold",
    "tiger lily",
    "moon orchid",
    "bird of paradise",
    "monkshood",
    "globe thistle"
]

# The list has ten entries
print("List length", len(flowers_list))

print("First entry:", flowers_list[0])
print("Second entry:", flowers_list[1])

# The list has length ten, so we refer to final entry with 9
print("Last entry:", flowers_list[9])

# Slicing
print("First three entries:", flowers_list[:3])
print("Final two entries:", flowers_list[-2:])

# Removing items
flowers_list.remove("globe thistle")

# Adding items
flowers_list.append("cherry blossom")

# Lists are not just for strings
hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
print("Minimum:", min(hardcover_sales))
print("Maximum:", max(hardcover_sales))

print("Total books sold in one week:", sum(hardcover_sales))

# Average

num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

avg_first_seven = sum(num_customers[:7]) / len(num_customers)
avg_last_seven = sum(num_customers[-7:]) / len(num_customers)

print(avg_first_seven)
print(avg_last_seven)


def percentage_liked(ratings):
    list_liked = [i >= 4 for i in ratings]
    # Return true for ratings above or equal 4

    percentage_liked = sum(list_liked) / len(list_liked)

    return percentage_liked


# Do not change: should return 0.5
print(percentage_liked([1, 2, 3, 4, 5, 4, 5, 1]))




