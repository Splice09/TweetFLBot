file = open("TweetID.txt", "w+")

for i in range(10):
    file.write("%d" % i +","+"This is a new line of Patrick\r\n")

file.close()