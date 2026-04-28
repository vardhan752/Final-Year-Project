DROP DATABASE IF EXISTS foods12;
CREATE DATABASE foods12;
USE foods12;

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(225),
    email VARCHAR(225),
    password VARCHAR(225)
);

CREATE TABLE recipies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(225),
    image VARCHAR(225), 
    calaries VARCHAR(500)
);

INSERT INTO recipies (name, image, calaries) VALUES
("burger", "static/images/burger.jpg", "Calories: 250 to 500 kcal (depends on size, filling, and type of burger), Proteins: 10 to 20g, Fats: 10 to 20g, Vitamins: Vitamin A, B12, folate (from cheese, lettuce, etc.)"),
("butter_naan", "static/images/butter_naan.jpg","Calories: 200 to 300 kcal (per piece), Proteins: 5 to 6g, Fats: 10 to 15g (due to butter), Vitamins: Vitamin A, Vitamin C (from ghee/butter)"),
("chai", "static/images/chai.jpg", "Calories: 30 to 80 kcal (depending on sugar and milk), Proteins: 1 to 2g (from milk), Fats: 2 to 5g (from milk), Vitamins: Vitamin A, B2, B12 (from milk)"),
("chapati", "static/images/chapati.jpg","Calories: 70 to 120 kcal (per piece), Proteins: 2 to 3g, Fats: 1 to 2g, Vitamins: B vitamins (thiamine, niacin)"),
("chole_bhature", "static/images/chole_bhature.jpg","Calories: 350 to 600 kcal (per serving, includes chole and bhature), Proteins: 10 to 15g, Fats: 15 to 20g (due to frying), Vitamins: Vitamin C (from tomatoes and spices)"),
("dal_makhani", "static/images/dal_makhani.jpg","Calories: 300 to 450 kcal (per serving), Proteins: 12 to 18g, Fats: 15 to 25g (due to butter/cream), Vitamins: Vitamin A, Vitamin C, folate"),
("dhokla", "static/images/dhokla.jpg","Calories: 150 to 250 kcal (per serving), Proteins: 5 to 6g, Fats: 5 to 7g, Vitamins: Vitamin C (from fermented ingredients)"),
("fried_rice", "static/images/fried_rice.jpg","Calories: 300 to 500 kcal (depending on oil and ingredients), Proteins: 7 to 12g (from vegetables, eggs, or tofu), Fats: 15 to 25g (depending on oil used), Vitamins: Vitamin C, A (from vegetables)"),
("idli", "static/images/idli.jpg","Calories: 35 to 50 kcal (per piece), Proteins: 1 to 2g, Fats: 0.5 to 1g, Vitamins: B vitamins (mainly B1, B2)"),
("jalebi", "static/images/jalebi.jpg","Calories: 150 to 250 kcal (per serving, around 3 to 4 pieces), Proteins: 1 to 3g, Fats: 8 to 12g (from frying), Vitamins: Vitamin A (from ghee or oil used)"),
("kaathi_rolls", "static/images/kaathi_rolls.jpg","Calories: 300 to 500 kcal (depending on fillings and size), Proteins: 15 to 20g (from chicken or paneer), Fats: 12 to 20g, Vitamins: Vitamin A, C (from vegetables and sauce)"),
("kadai_paneer", "static/images/kadai_paneer.jpg","Calories: 300 to 450 kcal (per serving), Proteins: 18 to 20g (from paneer), Fats: 20 to 30g (due to oil/ghee), Vitamins: Vitamin A, Vitamin C (from tomatoes, bell peppers)"),
("kulfi", "static/images/kulfi.jpg","Calories: 150 to 250 kcal (per piece), Proteins: 4 to 6g, Fats: 10 to 15g, Vitamins: Vitamin A, D, and calcium (from milk)"),
("masala_dosa", "static/images/masala_dosa.jpg","Calories: 250 to 350 kcal (per dosa), Proteins: 5 to 7g, Fats: 10 to 15g, Vitamins: B vitamins (B1, B2), Vitamin A (from potato filling)"),
("momos", "static/images/momos.jpg","Calories: 150 to 300 kcal (per 4 pieces, depending on stuffing), Proteins: 6 to 10g (from meat or vegetables), Fats: 5 to 10g (depending on steaming or frying), Vitamins: Vitamin C (from vegetables)"),
("paani_puri", "static/images/paani_puri.jpg","Calories: 100 to 150 kcal (per serving of 6 to 7 puris), Proteins: 2 to 3g, Fats: 4 to 7g (due to frying), Vitamins: Vitamin C (from tamarind and mint)"),
("pakode", "static/images/pakode.jpg","Calories: 200 to 350 kcal (depending on size and filling), Proteins: 5 to 8g, Fats: 15 to 20g (from frying), Vitamins: Vitamin A, C (from vegetables)"),
("pav_bhaji", "static/images/pav_bhaji.jpg","Calories: 400 to 600 kcal (per serving), Proteins: 10–12g, Fats: 20 to 30g (due to butter and oil), Vitamins: Vitamin C, A (from vegetables and butter)"),
("pizza", "static/images/pizza.jpg","Calories: 250 to 350 kcal (per slice), Proteins: 10 to 15g (from cheese, meats), Fats: 10 to 20g (from cheese and toppings), Vitamins: Vitamin A, B12 (from cheese)"),
("samosa", "static/images/samosa.JPG","Calories: 150 to 250 kcal (per piece), Proteins: 3 to 5g, Fats: 7 to 12g (from frying), Vitamins: Vitamin A, Vitamin C (from spices and vegetables)"),
("apple_pie", "static/images/apple_pie.jpg", "Calories: 200 to 300 kcal (per slice), Proteins: 2 to 4g, Fats: 8 to 15g (from butter), Vitamins: Vitamin A, C (from apples and spices)"),
("chocolate_cake", "static/images/chocolate_cake.jpg", "Calories: 250 to 400 kcal (per slice), Proteins: 3 to 6g, Fats: 12 to 25g (from butter and chocolate), Vitamins: Vitamin A, C (from ingredients)"),
("deviled_eggs", "static/images/deviled_eggs.jpg", "Calories: 70 to 100 kcal (per piece), Proteins: 5 to 7g, Fats: 5 to 8g (from egg yolk and mayonnaise), Vitamins: Vitamin A, D (from eggs)"),
("french_fries", "static/images/french_fries.jpg", "Calories: 150 to 300 kcal (depending on portion size), Proteins: 2 to 4g, Fats: 8 to 15g (from frying), Vitamins: Vitamin C (from potatoes)"),
("macarons", "static/images/macarons.jpg", "Calories: 70 to 100 kcal (per piece), Proteins: 1 to 2g, Fats: 3 to 6g (from almond flour and butter), Vitamins: Vitamin A, C (from ingredients)");
