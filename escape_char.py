tabbedString = "1\t2\t3\t4\5\t6"
splitString = "String has been \nsplit over \nseveral\nlines"
othersplitString = """Text also can be splitted 
with tripple quotes 
and we can add more 
lines ! """
samelinesbackslash = """Text also can be splitted \
with tripple quotes \
and we can tupe it in diff lines  \
but backslash at he endd will turn it to single line  ! """
print(splitString)
print(tabbedString)
print('This is how to escape single quote in \'single quote\' print ')
print("This is how to escape double  quote in \"double quote\" print ")
print(""" We can also escape 'any' "quote" without slash but with "tripple quotes" """)
print(othersplitString)
print(samelinesbackslash)
print("This is how we can escape backslash C:\\Users\\tim\\nano.txt")
print(r"This is how we can escape backslash with raw and without double slash  C:\Users\tim\nano.txt")
