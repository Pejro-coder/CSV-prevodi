import csv

# Step 1: Read translations from "Russian translations.csv"
with open("Russian translations.csv", "r", encoding="utf-8") as file:
    read_file = csv.reader(file, delimiter=";")
    next(read_file)  # Skip the header
    translations = {row[0]: row[1] for row in read_file}

print("Translations:", translations)

# Step 2: Read data from "Add russian.csv"
with open("Add russian.csv", "r", encoding="utf-8") as file:
    read_file = csv.reader(file, delimiter=";")
    next(read_file)  # Skip the header
    empty_translations = {line[0]: line[2] for line in read_file}

# Step 3: Update missing translations
missing_count = 0
for key, value in translations.items():
    if key in empty_translations:
        empty_translations[key] = value
    else:
        missing_count += 1

print("Updated translations:", empty_translations)
print(f"Missing translations count: {missing_count}")

# Step 4: Write updated data back to "Add russian.csv"
with open("Add russian.csv", "w", encoding="utf-8", newline="") as file:
    write = csv.writer(file, delimiter=";")
    # Write a header row (if needed)
    write.writerow(["Key", "Column 2", "Translation"])  # Adjust based on your file structure
    # Write the data
    for key, value in empty_translations.items():
        write.writerow([key, "", value])  # Assuming column 2 is empty