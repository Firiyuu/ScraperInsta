
import time
import csv
from datetime import date, timedelta
from time import gmtime, strftime





def compareData(last,current):
    today = date.today()
    today.strftime('%m%d%y')

    last_no = len(last)
    current_no = len(current)

    file_name = 'followers.csv'

    new_followers = last_no - current_no

    if(new_followers>0):
        writeToCsv((str(today) + ',' + str(new_followers)), file_name)
        print("Follower Monitor: " + str(new_followers) + ' more people have followed you!')
    else:
        writeToCsv((str(today) + ',' + str(new_followers)), file_name)
        print("Follower Monitor: " + str(abs(new_followers)) + ' people have unfollowed you! Here they are: ')
        unfollower_starts_at = current_no - new_followers
        GetUnfollowersNames(unfollower_starts_at, last)




    


#GET DATA A WEEK AGO AND COMPARE IT TO DATA THIS WEEK
def GetUnfollowersNames(index, wholelist):
    lastweek = date.today() - timedelta(7)
    lastweek.strftime('%m%d%y')

    file_name = 'unfollowers.csv'

    for i in range(index, len(wholelist)):
        print(wholelist[i])
        fields = wholelist[i] + ',' + str(lastweek)
        writeToCsv(fields,file_name)







#GET DATA A WEEK AGO AND COMPARE IT TO DATA THIS WEEK
def analyzeCsvFeed():

    lastweek = date.today() - timedelta(7)
    lastweek.strftime('%m%d%y')
    today = date.today()
    today.strftime('%m%d%y')




    csv_file_lastweek = 'followers' + str(lastweek) +'.csv'
    csv_file_thisweek = 'followers' + str(today) +'.csv'

    lastweek_list = []
    thisweek_list = []
    with open(csv_file_lastweek) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if(row[0] != 'None' and row[0] != None):
                  lastweek_list.append(row[0]) 
        
    with open(csv_file_thisweek) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            if(row[0] != 'None' and row[0] != None):
                  thisweek_list.append(row[0])

    compareData(lastweek_list, thisweek_list)





def writeToCsv(fields,file_name):


    today = date.today()
    today.strftime('%m%d%y')
    

    
    print(file_name)

    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        with open(file_name, 'a', newline='') as f:
           writer = csv.writer(f, delimiter=' ', quotechar = ' ')
           writer.writerow(fields)
           print('Written Follower to CSV!')
        f.close()






# def monitoringCsv(fields):


#     today = date.today()
#     today.strftime('%m%d%y')
    

#     file_name ='Monitoring' + str(today) + '.csv'
#     print(file_name)

#     with open(file_name) as csvfile:
#         readCSV = csv.reader(csvfile, delimiter=',')
#         with open(file_name, 'a', newline='') as f:
#            writer = csv.writer(f, delimiter=' ', quotechar = ' ')
#            writer.writerow(fields)
#            print('Written Follower to CSV!')
#         f.close()
