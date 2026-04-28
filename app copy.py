from flask import Flask,render_template,flash,redirect,request,send_from_directory,url_for, send_file
import mysql.connector, os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img 
from keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database='foods12'
)

mycursor = mydb.cursor()

def executionquery(query,values):
    mycursor.execute(query,values)
    mydb.commit()
    return

def retrivequery1(query,values):
    mycursor.execute(query,values)
    data = mycursor.fetchall()
    return data

def retrivequery2(query):
    mycursor.execute(query)
    data = mycursor.fetchall()
    return data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        c_password = request.form['c_password']
        if password == c_password:
            query = "SELECT UPPER(email) FROM users"
            email_data = retrivequery2(query)
            email_data_list = []
            for i in email_data:
                email_data_list.append(i[0])
            if email.upper() not in email_data_list:
                query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
                values = (name, email, password)
                executionquery(query, values)
                return render_template('login.html', message="Successfully Registered! Please go to login section")
            return render_template('register.html', message="This email ID is already exists!")
        return render_template('register.html', message="Conform password is not match!")
    return render_template('register.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        query = "SELECT UPPER(email) FROM users"
        email_data = retrivequery2(query)
        email_data_list = []
        for i in email_data:
            email_data_list.append(i[0])
        
        if email.upper() in email_data_list:
            query = "SELECT UPPER(password) FROM users WHERE email = %s"
            values = (email,)
            password__data = retrivequery1(query, values)
            if password.upper() == password__data[0][0]:
                global user_email
                user_email = email

                return redirect("/home")
            return render_template('home.html', message= "Invalid Password!!")
        return render_template('login.html', message= "This email ID does not exist!")
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        myfile = request.files['image']
        fn = myfile.filename
        mypath = os.path.join('static/user_images/', fn)
        myfile.save(mypath)

        classes = [
    "apple_pie","burger", "butter_naan", "chai", "chapati","chocolate_cake",
    "chole_bhature", "dal_makhani", "deviled_eggs", "dhokla", "french_fries", "fried_rice",
    "idli", "jalebi", "kaathi_rolls", "kadai_paneer",
    "kulfi",  "macarons", "masala_dosa", "momos", "paani_puri", "pakode",
    "pav_bhaji", "pizza", "samosa"
     
]

        
        model=load_model("final_cnn1.h5")
        test_img=image.load_img(mypath,target_size=(224,224))
        test_img=image.img_to_array(test_img)
        test_img = np.expand_dims(test_img, axis=0)
        test_img=test_img/255.0
        
        # Perform prediction
        prediction = model.predict(test_img)
        result=classes[np.argmax(prediction)]
        print(11111111, result)
        name = result.upper()

        query = "SELECT * FROM recipies WHERE UPPER(name) = %s"
        values = (name, )
        data = retrivequery1(query, values)

        if data:
            prediction = data
        else:
            prediction = "Unknown"

        return render_template('upload.html', path = mypath, prediction = prediction)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug = True)