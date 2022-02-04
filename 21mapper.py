import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split(",")
  if (len(datalist) == 9) : 
    year,rank_display,university,score,link,country,city,region,logo = datalist

    # print intermediate key-value pairs to standard output
    print(university,"\t",score)