dates = ['2006-04-15', '2012-02-21', '2018-07-06', '2003-11-14', '2009-10-24', '2005-08-09',
     '2014-04-03', '2009-11-19', '2009-06-24', '2002-03-18', '2000-05-25', '2020-06-09',
     '2005-05-11', '2007-02-11', '2005-03-02', '2011-11-20', '2011-10-11', '2019-11-09',
     '2014-09-13', '2020-08-26', '2011-08-25', '2012-06-12', '2008-04-25', '2008-01-01',
     '2004-02-03', '2003-09-23', '2007-08-02', '2004-10-22', '2005-06-06', '2010-08-12',
     '2003-10-06', '2004-05-09', '2004-05-07', '2012-03-21', '2016-05-19', '2000-05-11',
     '2020-02-21', '2008-06-04', '2002-10-26', '2008-01-20', '2013-09-26', '2016-05-02',
     '2003-08-18', '2017-09-10', '2016-03-14', '2011-10-12', '2019-03-25', '2006-06-19',
     '2016-09-16', '2001-11-11']

year = str(input("what year do you want to filter by? ")) #user input year to filter by
x = [] #create an empty list to represent dates in year

#iterate through the list and find dates with the YYYY == year, and then print the list x
if __name__ == '__main__':
    for date in dates:
        if date[0:4] == year:
            x.append(date)
    if len(x) != 0:
        print(x)
    else:
        print('year not found in list of dates')
