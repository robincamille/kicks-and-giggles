## Robin Camille Davis
## March 24, 2014
## downloads all items in a given Internet Archive collection
## See http://programminghistorian.org/lessons/data-mining-the-internet-archive for more detailed info

import internetarchive as ia

coll = ia.Search('collection:xxxxxxxx') #fill this in -- searches for the ID of a collection in IA
## example of collection page: https://archive.org/details/johnjaycollegeofcriminaljustice
## the collection ID for that page is johnjaycollegeofcriminaljustice
## you can tell a page is a collection if it has a 'Spotlight Item' on the left

num = 0

for result in coll.results(): #for all items in a collection
    num = num + 1 #item count
    itemid = result['identifier']
    print 'Downloading: #' + str(num) + '\t' + itemid
    
    item = ia.Item(itemid)
    item.download() #download all associated files (large!)
    print '\t\t Download success.'
    
    
    
