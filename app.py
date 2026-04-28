from flask import Flask,render_template,flash,redirect,request,send_from_directory,url_for, send_file
import pymysql, os
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img 
from keras.preprocessing import image
import numpy as np
from ultralytics import YOLO
from collections import defaultdict
import numpy as np
# Load YOLO model
model = YOLO("best.pt")

# Static calorie values per class
calorie_map = {
    "Dosa": 133,
    "Idli": 39,
    "Butter Naan": 260,
    "Normal Naan": 220,
    "Chocolate Ice-Cream": 207,
    "Vanilla Ice-Cream": 137,
    "Vada": 155,
    "Samosa": 262,
    "Pizza": 285,
    "Burger": 295
}

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
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
        # Ensure unique filename for annotated image
        base, ext = os.path.splitext(fn)
        annotated_fn = f"{base}_annotated{ext}"
        mypath = os.path.join('static/user_images/', fn)
        annotated_path = os.path.join('static/user_images/', annotated_fn)
        myfile.save(mypath)

        # Process image with YOLO
        results = model(mypath)

        # Save annotated image
        annotated_image = results[0].plot()  # Get annotated image with bounding boxes
        from PIL import Image
        Image.fromarray(annotated_image[..., ::-1]).save(annotated_path)  # Convert BGR to RGB and save

        # Count detected objects and calculate calories
        object_counts = defaultdict(int)
        total_calories = 0
        detected_items = []

        for box in results[0].boxes:
            class_id = int(box.cls[0])
            label = model.names[class_id]
            object_counts[label] += 1
            # Only store unique items for display
            if label not in [item['label'] for item in detected_items]:
                confidence = box.conf[0].item()
                detected_items.append({
                    'label': label,
                    'confidence': round(confidence, 2)
                })

        # Generate calorie report
        calorie_report = []
        for label, count in object_counts.items():
            calories = calorie_map.get(label, 0) * count
            total_calories += calories
            calorie_report.append({
                'label': label,
                'count': count,
                'calories_per_item': calorie_map.get(label, 0),
                'total_calories': calories
            })

        # Prepare prediction data
        prediction = {
            'detected_items': detected_items,
            'calorie_report': calorie_report,
            'total_calories': total_calories
        }

        return render_template('upload.html', path=annotated_path, prediction=prediction)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug = True)