from flask import Flask, redirect, url_for, request,render_template , session 
# from firebase_admin import firestore
# from flask_jwt_extended import jwt_required
import sqlite3
import mka
import exel
# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore
# from firebase_admin import auth

import testmet
thetempss = []

def connect_co():
    connd = sqlite3.connect('daily_counter.db')
    cursor = connd.cursor()
    return cursor , connd

# Create a table to store counts if it doesn't already exist


# Commit the changes

# Load the service account key from the JSON data
# service_account_key_data = '''
# {
#   "type": "service_account",
#   "project_id": "magictech-a68b3",
#   "private_key_id": "c8ad41ef83968dc5b01802fa04a41c56b7d894eb",
#   "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDGASAuK8nnftzx\\n66isqy11oGuv57FDWRQ7vzZrjw406SDJb2EvPec1wV3JviQJvW7piY4182IzQwpJ\\noY1r1U47d4slwhmQDyi42UCHzPQPJyj/+NmcUeUZ08LIL/gVTzOyfQhse2Lqk8EB\\nNEG6ktBcXZd1P4eJXqJKuH7nGY/wBnJSUMrISv7e4PeiB89H4A9pqEQVpKp9n0Lr\\nZEfaCtERxBHe9XKVsq3GaceyQDa8SJy+r/a8PUVqI+3XMxDGj3h/tXLFOZR6lKuM\\njRjOL8NB6eGsbb0KyRfIzpKyk5iJgvF85wDJOLdTQvcmXTbOr/vd105C8GvHAOdH\\nKB/UTimVAgMBAAECggEAXXVLkK93ee6N8BxI/dNAPkyNd7ZXG5BQthC/aY5Y6M1+\\n/cU2LHu+Bcfy8lXuobBJyS51su5hlAuZL/7yhwrkBbqbsaNHuJEHKhTVWiP5sKtN\\ntWBqqleXWRT0U9Qcd0Zugtl0X+vvWQSLrXtSaPOCKI6+fgeR/FtwI++oaoFMyMAV\\no9490jVUJyJdEx1VpYtXbEIhl9H3G2alZeVDHxOk2JQI0+Q2ZJyz7djIwTET+qp2\\n7p3SBWzIf0ZhrlWjR1n6vgX+7AuyaGZYZO/mNXXHRFC0TZzePcAvLBv3HijMayiq\\nw2wSAJlAbEo0ps98UIV0VJ6OQUtlMFUDenC7/V8CowKBgQDlVWPpexspNRrT+fu1\\nsGhoV+bLXnbBn3k6NXvSaEc72GMysGKCRbsnUKQG+FwKnv8X5F1FHz0LM03Py/tB\\nefjg43+MgDQj20E6jFOAgr2ptI//uPAvFZ06gfMefDRTVvM9ag2bFf47QD7BIXAW\\n1E0k1W6JrjK5+WT+1dgZwNwVUwKBgQDdBye7Y/GxUfrWhIlXAvuXETaWh5J8ewGe\\nMkJXn7Jcj9lp/AuvRz9eBRVB/Y9V44KRRz48HpXTa3ergkRjWGmJs+GtTG1X3D38\\n8U89NUVQN6BUXJeHhbNqJCSn48N9ZAI2YCnMJjGqpnYj+lLlT4zg0pFWRQ5YvsXf\\nQLHNl7bAdwKBgHdGCvmyujSbVwGqgTxErHigRvu8fJ1FOMKKcITFEU9Rwn3peMJy\\nS90ttrGdWBl6Cgg+EDhT/+akXzLUzy+FpWgpSfwj7Xo8nVc7Bm7PEJ+DtmT0pY6H\\nekeksHJJfNlfXpCxaLQhIyFjz3+YyXhGIH0ouB3JSL6qs9lKFOOIB67bAoGALZZF\\nNpwlhGohL0+EuCKQW5ccSC3MI8qHCebZ0hLJCdhNglOO4WbzhePMf6DZiGB1VJt6\\nFZJFWqbGtuQWUNsyYUltmX2y67UsP9hRfJFZK3NdqSizxCrqV1D/EnWio2EWJ7rr\\nxAR4p/bPVRpTMKKYruIfQcjabaljTGmegoXxFn8CgYBzDrC/keoC5wurNkzede5p\\nxa+7+k9sl9YWyib4yUwkf5/M4xNvIjtZCq+4XffBaEzAT+dzmlOizVk3ltuQzK/g\\neElUELYEfrl6yKrNKqW1JXg/C2fmxjh25Vks5xyEqMrtNyTDscljFRhspBLI3gNt\\n5ic8f/93iyV3Fv8EwQFnaw==\\n-----END PRIVATE KEY-----\\n",
#   "client_email": "firebase-adminsdk-9exhf@magictech-a68b3.iam.gserviceaccount.com",
#   "client_id": "101015886303015615111",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://oauth2.googleapis.com/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-9exhf%40magictech-a68b3.iam.gserviceaccount.com",
#   "universe_domain": "googleapis.com"
# }
# '''

# Parse the JSON data
# service_account_key = json.loads(service_account_key_data)
# cred = credentials.Certificate(service_account_key)

# appd = firebase_admin.initialize_app(cred,
#                                      {
#     'storageBucket': 'magictech-a68b3.appspot.com'
# })
from datetime import date , time
import datetime 

# Function to create/connect to the database

appf = Flask(__name__)

appf.secret_key = 'thetopsecretmajd1234'
# db = firestore.client()
#new 999999999999999999999999999999999999

# Function to connect to the SQLite database



   

def add_seller(conn, username, name,  password):
   c = conn.cursor()
   c.execute('''INSERT INTO workers (username, name, pass)
               VALUES (?, ?, ?)''', (username, name, password))


   conn.commit()
# d,f = connect_co()

@appf.route('/addadmin',methods = ['POST', 'GET'])
def addadmin():
   if 'username' in session:
      
      if request.method == 'POST':
         # file = request.files['picture']
         passw = request.form['pass']
         name = request.form['name']
         email = request.form['email']
         
         # print(file)
         # file= ''     
         ad,conn  = connect_co()
         add_seller(conn, email,name ,passw)
         # url = upload_picture(file)
         # dadtafire =addadHmina( name , email ,occ,user, per , passw, url)
         # majd = session.get('username')
         return redirect(url_for('orderss'))
         # if dadtafire != None:
         #    return dadtafire
         
      return render_template("addadmin.html" )
   else:
      return redirect(url_for('login'))   
      
 
# Function to retrieve number of bills and customers for today
def getusers(conn, username , passw): 
    d = conn.cursor()
    try:
        d.execute('''SELECT pass ,name FROM workers WHERE username = ?''', (username,))
    except:
        return False
    

    
    dd = d.fetchone()
    if dd:
      if passw == dd[0]:
         return dd[1]
      return 'WRONG PASSWORD'
    else: return None
import threading

# Define a lock for synchronization
lock = threading.Lock()

def dfdf(i1 , i2 ,tete):
    # Acquire the lock before entering critical section
    with lock:
        try:
                     # Connect to the database
            cursor, connd = connect_co()
            
            # Clear the list thecountforeb
            
            
            # Call exel.code() with the integer value of use
            exel.code(i1, i2 , tete)
            
            # Append the integer value of use to thetempss list
            thetempss.append(i1)
            
            # Append the incremented count to thecountforeb list
            
            
            # Close the database connection
            connd.close()
               
        except :
            # Handle exceptions or errors appropriately
            print('error')
def fdf(i1 , i2):
    # Acquire the lock before entering critical section
    with lock:
        try:
            # Connect to the database
            cursor, connd = connect_co()
            
            # Clear the list thecountforeb
            
            
            # Call exel.code() with the integer value of use
            exel.dcode(i1, i2)
            
            # Append the integer value of use to thetempss list
            thetempss.remove(i1)
            
            # Append the incremented count to thecountforeb list
            
            
            # Close the database connection
            connd.close()

        except Exception as e:
            # Handle exceptions or errors appropriately
            print(f"Error: {e}")
@appf.route('/codea/<use>')
def codea(use):
   
   usee = use.split("m")
   i1 = int(float(usee[0]))
   if i1 not in thetempss:
      i2= int(float(usee[1]))
      dfdf(i1, i2,session.get('username'))
   
   # session['proname'] =data
   
   
   return  redirect(url_for('orderss'))
@appf.route('/create_filtered_workbook', methods=['POST'])
def jhlkj():
   
   mka.create_filtered_workbook()
   # session['proname'] =data
   
   
   return  'File exported successfully!'

@appf.route('/deletedone/<use>')
def coxcddea(use):
   
   usee = use.split("m")
   i1 = int(float(usee[0]))

   i2= int(float(usee[1]))
   fdf(i1, i2)
   
   # session['proname'] =data
   
   
   return  redirect(url_for('orderss'))
@appf.route('/orders',methods = ['POST', 'GET'])
def orderss():
   if 'username' in session:
      cursor, connd = connect_co()
      thebest , ii= testmet.d_count(cursor, connd)
      if request.method == 'POST':
         search = request.form['search']
         select = request.form['select']

         data= exel.ssds(search , select)
         if data != []:

            shit = len(data[0])
         else:
            shit = 0
         
         datae= exel.get_datfi()
         data = [datae, data]
         
         
         print( ii )
         con = exel.row -1
         total= con - thebest
      
      
         return render_template("orders.html" ,  data = data , shit= shit , co =thebest , con = con , tot=total , s= ii)

      data =exel.get_dat()
      if data != []:

         shit = len(data[0])
      else:
         shit = 0
      
      datae= exel.get_datfi()
      data = [datae, data]
      con = exel.row -1
      total= con - thebest

      return render_template("orders.html" ,  data = data ,shit= shit , co = thebest , con = con, tot= total ,s= ii)
   else:
      return redirect(url_for('login'))   
@appf.route('/',methods = ['POST', 'GET'])
def login():

   if request.method == 'POST':
      session.pop('username', None)

      user = request.form['email']
      passw = request.form['pass']
      dd , conn= connect_co()
      userafter = getusers(conn,user, passw)
   
      # print(f'dd{user}')
      if not userafter :
         return 'WRONG USERNAME'
      elif userafter == 'WRONG PASSWORD':
         return userafter
      else:

      

         session['username'] =userafter
         return redirect(url_for('orderss'))
   # else:
   #    user = request.args.get('email')
   #    passw = request.args.get('pass')
   #    user = data.seacha(user,passw)
   #    # print(user')  
   #    if  user == False:
   #       return redirect(url_for('false' ))
   #    else:
   #       return redirect(url_for('admins', use = user ))
   # majd = session.get('username')
   # print(majd)
   # if majd != None:return redirect(url_for('orderss'))
   return render_template("login.html")


@appf.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@appf.route('/workerss')
def fsdfdsf():
    if 'username' in session:
     

      thebest , ii= testmet.d_count(0, 0)
      print()
      return render_template("counttt.html" , s = ii )


import os
import webbrowser


def open_browser():
    # Open the default web browser with the local URL
   webbrowser.open('http://127.0.0.1:5545')
   

if __name__ == '__main__':
   
   from threading import Thread
   Thread(target=open_browser).start()
   appf.run(debug = True ,host='0.0.0.0', port=5545)
