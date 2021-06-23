import csv
import matplotlib.pyplot as plt

# with open('lightcurves_edited.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         else:
#             print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#             line_count += 1
#     # print(f'Processed {line_count} lines.')




# with open('lightcurves_edited.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")


# data317 = np.genfromtxt("lightcurves_edited.csv", delimiter=",", names=["timestamp", "317 nm"]
# plt.plot('timestamp', '317 nm', data=data317)

x317 = [], y317 = []

with open('lightcurves_original.csv') as dataFile:  
   plots = csv.reader(dataFile, delimiter = ",")

   for row in plots:
       x317.append(row[0])
       y317.appened(int(row[1])) 

plt.bar(x317, y317, color = 'g', width = 0.72, label = "Reflectance value")
plt.xlabel('Timestamps')
plt.ylabel('Reflectance value')
plt.title('Reflectance values vs Timestamps (317 nm)')
plt.legend()
plt.show()