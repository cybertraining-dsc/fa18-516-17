from pyhive import hive

host_name = "10.0.2.15"
port = 10000
user = "hduser"
password = "trainingbrad@99"
database="default"

def hiveconnection(host_name, port, user,password, database):
    conn = hive.Connection(host=host_name, port=port, username=user, password=password,
                           database=database, auth='CUSTOM')
    cur = conn.cursor()
    cur.execute('Select Item_Key,(POSSales/POSQty) AS AverageRetail FROM (Select Item_Key, sum(POSSales) AS POSSales, sum(POSQty) AS POSQty From retaildata GROUP BY Item_Key) byitem ORDER BY Item_Key')
    result = cur.fetchall()

    return result

# Call above function
output = hiveconnection(host_name, port, user,password, database)
print(output)
