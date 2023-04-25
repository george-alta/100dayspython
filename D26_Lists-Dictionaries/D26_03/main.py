import pandas

data1 = pandas.read_csv(
    "D26_Lists-Dictionaries/D26_03/file1.txt", names=["numbers"])
data2 = pandas.read_csv(
    "D26_Lists-Dictionaries/D26_03/file2.txt", names=["numbers"])

list1 = data1["numbers"].to_list()
list2 = data2["numbers"].to_list()

result = [int(n) for n in list1 if n in list2]

# Write your code above 👆

print(result)
