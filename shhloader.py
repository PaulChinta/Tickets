import mysql.connector
from sshtunnel import SSHTunnelForwarder

#credentials
host_='acadmysqldb001p.uta.edu'
user_='pxc6866'
password_='Yogapandu12345'
db_='pxc6866'

#method to create an ssh tunnel from local system to remote server @UTAOmega
def sshTunnel():
    tunnel = SSHTunnelForwarder(
        ('Omega.uta.edu', 22),
        ssh_username = 'pxc6866',
        ssh_password = 'Yoga@12345',
        remote_bind_address = ('127.0.0.1', 3306),
    )
    tunnel.start()


#method to extract data from csv
def files():
    csv={}
    filenames=['User.csv','Tickets.csv','Flights_in_ticket']
    csv['Country']=(open("Country.csv", "r"))
    csv['Players']=(open("Players.csv","r"))
    csv['Player_cards']=open("Player_cards.csv","r")
    csv['Player_assists_goals']=open("Player_Assists_Goals.csv","r")
    csv['Match_results']=open("Match_results.csv","r")
    return csv

if __name__=='__main__':
    #creating connection with mysql server on uta Omega
    connection = mysql.connector.connect(host=host_,
                                                user=user_,
                                                password=password_,
                                                database=db_)
    curs=connection.cursor()
    #calling files function to extract data from csv files in local storage.
    data=files()

    #inserting all records into the tables on mysql UTA OMEGA
    for table in data.keys():
        for i in data[table]:
            curs.execute("Insert into "+table+" values("+i+");")
            connection.commit()
        print('Records entered into table: '+table)
    print('All records uploaded successfully')

connection.close()

