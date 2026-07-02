# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

time_count_dict = dict()

for line in handle:
    if 'From ' not in line:
        continue
    
    line.rstrip()
    words = line.split()
    time_array = words[5].split(':')
    time_count_dict[time_array[0]] = time_count_dict.get(time_array[0], 0) + 1
    
for time, count in sorted(time_count_dict.items()):
    print(time, count)