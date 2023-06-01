# slicing= create a substring by extracting elements from another string
#                   indexing[] or slice()
#                   [start:stop:step]


#name = "Cauê Justen Garbi"

#first_name = name[0:4:1]
#last_name = name[12:17:1]       # 12= where it started to show
                                # 17 = where it ended
                                # 1 = how much spaces it goes by

#reversed_name = name[::-1]

#print(reversed_name)


website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])