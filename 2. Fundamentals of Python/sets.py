set1 = {"Roger", "Syd"}
set2 = {"Roger"}
set3 = {"Roger", "Luna"}

intersection = set1 & set2
union = set1 | set2
diff = set1 - set2
# Is set2 a subset of set1
compare = set1 > set2  ## True

print(list(set1))
