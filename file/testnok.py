file1 = open('expecte.txt', 'r')
file2 = open('actual.txt', 'r')
FO = open('diff.txt', 'w')

for line1 in file1:
    for line2 in file2:
        if line1 == line2:
            FO.write("%s\n" %(line1))

FO.close()
file1.close()
file2.close()

# reading files
# f1 = open('expecte.txt', "r")
# f2 = open('actual.txt', "r")
#
# i = 0
#
# for line1 in f1:
#     i += 1
#
#     for line2 in f2:
#
#         # matching line1 from both files
#         if line1 == line2:
#             # print IDENTICAL if similar
#             print("Line ", i, ": IDENTICAL")
#         else:
#             print("Line ", i, ":")
#             # else print that line from both files
#             print("\tFile 1:", line1, end='')
#             print("\tFile 2:", line2, end='')
#         break
#
# # closing files
# f1.close()
# f2.close()