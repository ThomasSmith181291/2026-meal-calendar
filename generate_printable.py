"""
Generate printable A4 shopping lists with QR codes
Shopping lists are derived from actual recipe ingredients
"""

import os
import datetime
import random
import re

random.seed(2026)  # Same seed as generate_pages.py for consistency

output_dir = r"C:\Users\Little Nineveh\2026-meal-calendar\printable"
os.makedirs(output_dir, exist_ok=True)

# Your GitHub Pages URL
BASE_URL = "https://thomassmith181291.github.io/2026-meal-calendar"

# ============================================================
# COMPLETE RECIPE DATABASE (same as generate_pages.py)
# ============================================================

lunch_recipes = {
    "Leek & potato soup": {"ingredients": ["2 leeks, sliced", "3 potatoes, diced", "1 onion, chopped", "1L chicken stock", "2 tbsp butter", "100ml cream"]},
    "Tomato soup": {"ingredients": ["2 tins chopped tomatoes", "1 onion, chopped", "2 garlic cloves", "500ml veg stock", "1 tsp sugar", "Fresh basil"]},
    "Carrot & coriander soup": {"ingredients": ["500g carrots, chopped", "1 onion, chopped", "1L veg stock", "1 tsp ground coriander", "Fresh coriander"]},
    "Butternut squash soup": {"ingredients": ["1 butternut squash, cubed", "1 onion, chopped", "2 garlic cloves", "1L veg stock", "1 tsp cumin"]},
    "Chicken noodle soup": {"ingredients": ["2 chicken breasts", "1.5L chicken stock", "2 carrots, sliced", "2 celery sticks", "100g egg noodles", "Fresh parsley"]},
    "Pea & mint soup": {"ingredients": ["500g frozen peas", "1 onion, chopped", "750ml veg stock", "Fresh mint", "100ml cream"]},
    "French onion soup": {"ingredients": ["4 onions, sliced", "50g butter", "1L beef stock", "100ml white wine", "4 slices baguette", "100g gruyere"]},
    "Minestrone": {"ingredients": ["1 onion, diced", "2 carrots, diced", "2 celery sticks", "1 tin chopped tomatoes", "1 tin cannellini beans", "100g pasta", "1L veg stock"]},
    "Broccoli & stilton soup": {"ingredients": ["1 large broccoli, chopped", "1 onion, chopped", "1L veg stock", "100g stilton, crumbled", "100ml cream"]},
    "Sweetcorn chowder": {"ingredients": ["2 tins sweetcorn", "4 rashers bacon, chopped", "1 onion, diced", "2 potatoes, diced", "500ml chicken stock", "200ml cream"]},
    "Roasted red pepper soup": {"ingredients": ["4 red peppers, halved", "1 onion, chopped", "2 garlic cloves", "750ml veg stock", "1 tbsp balsamic vinegar"]},
    "Mushroom soup": {"ingredients": ["400g mushrooms, sliced", "1 onion, chopped", "2 garlic cloves", "750ml veg stock", "100ml cream", "Fresh thyme"]},
    "Ham & cheese toastie": {"ingredients": ["2 slices bread", "2 slices ham", "50g cheddar, grated", "Butter"]},
    "BLT sandwich": {"ingredients": ["3 rashers bacon", "2 slices bread, toasted", "Lettuce", "1 tomato, sliced", "Mayonnaise"]},
    "Tuna melt": {"ingredients": ["1 tin tuna, drained", "2 tbsp mayo", "2 slices bread", "50g cheddar, sliced"]},
    "Club sandwich": {"ingredients": ["3 slices bread, toasted", "2 rashers bacon", "Sliced chicken", "Lettuce, tomato", "Mayo"]},
    "Croque monsieur": {"ingredients": ["4 slices bread", "4 slices ham", "100g gruyere, grated", "2 tbsp butter", "1 tbsp flour", "150ml milk", "Dijon mustard"]},
    "Coronation chicken sandwich": {"ingredients": ["2 cooked chicken breasts, shredded", "3 tbsp mayo", "1 tbsp curry powder", "1 tbsp mango chutney", "Bread", "Lettuce"]},
    "Egg mayo sandwich": {"ingredients": ["4 eggs, hard boiled", "3 tbsp mayonnaise", "1 tsp mustard", "Salt & pepper", "Bread", "Cress"]},
    "Cheese & pickle sandwich": {"ingredients": ["2 slices bread", "75g mature cheddar, sliced", "2 tbsp Branston pickle", "Butter"]},
    "Welsh rarebit": {"ingredients": ["200g mature cheddar, grated", "25g butter", "1 tbsp flour", "100ml beer or milk", "1 tsp mustard", "4 slices bread"]},
    "Prawn mayo sandwich": {"ingredients": ["100g cooked prawns", "2 tbsp mayo", "Squeeze lemon", "Bread", "Lettuce"]},
    "Smoked salmon bagel": {"ingredients": ["1 bagel", "2 tbsp cream cheese", "2 slices smoked salmon", "Capers", "Lemon"]},
    "Chicken Caesar wrap": {"ingredients": ["1 chicken breast, cooked and sliced", "1 wrap", "Romaine lettuce", "Parmesan, shaved", "Caesar dressing"]},
    "Ham salad wrap": {"ingredients": ["2 slices ham", "1 wrap", "Lettuce", "Tomato", "Cucumber", "Mayo"]},
    "Hummus & veg wrap": {"ingredients": ["3 tbsp hummus", "1 wrap", "Grated carrot", "Cucumber", "Red pepper"]},
    "Cheese toastie": {"ingredients": ["2 slices bread", "75g cheddar, grated", "Butter"]},
    "Cheese omelette": {"ingredients": ["3 eggs", "50g cheese, grated", "1 tbsp butter", "Salt & pepper"]},
    "Jacket potato with beans": {"ingredients": ["1 large potato", "1 tin baked beans", "Butter", "50g cheese, grated"]},
    "Jacket potato with tuna mayo": {"ingredients": ["1 large potato", "1 tin tuna", "2 tbsp mayo", "Sweetcorn", "Butter"]},
    "Jacket potato with cheese & coleslaw": {"ingredients": ["1 large potato", "75g cheddar, grated", "3 tbsp coleslaw", "Butter"]},
    "Beans on toast": {"ingredients": ["1 tin baked beans", "2 slices bread", "Butter", "Cheese (optional)"]},
    "Cheese on toast": {"ingredients": ["2 slices bread", "75g cheddar, grated", "Worcestershire sauce"]},
    "Sardines on toast": {"ingredients": ["1 tin sardines", "2 slices bread", "Butter", "Lemon", "Black pepper"]},
    "Egg fried rice": {"ingredients": ["300g cooked rice (cold)", "2 eggs, beaten", "100g peas", "2 spring onions", "2 tbsp soy sauce"]},
    "Quesadilla": {"ingredients": ["2 tortillas", "75g cheddar, grated", "Sliced peppers", "Salsa, sour cream"]},
    "Avocado on toast": {"ingredients": ["1 avocado", "2 slices sourdough", "Lemon juice", "Chilli flakes", "Salt"]},
    "Greek salad": {"ingredients": ["1 cucumber, chunked", "4 tomatoes, chunked", "1 red onion, sliced", "100g feta", "Olives", "Olive oil", "Oregano"]},
    "Caesar salad": {"ingredients": ["1 romaine lettuce", "1 chicken breast, cooked and sliced", "Croutons", "Parmesan", "Caesar dressing"]},
    "Nicoise salad": {"ingredients": ["200g new potatoes", "100g green beans", "2 eggs, boiled", "1 tin tuna", "Olives", "Olive oil", "Lemon"]},
    "Ploughman's lunch": {"ingredients": ["75g cheddar", "2 slices ham", "Branston pickle", "Crusty bread", "Apple", "Celery"]},
    "Leftover roast sandwich": {"ingredients": ["Sliced roast meat", "2 slices bread", "Stuffing", "Gravy or cranberry sauce"]},
}

dinner_recipes = {
    "Spaghetti Bolognese": {"ingredients": ["500g beef mince", "1 onion, diced", "2 garlic cloves", "2 carrots, diced", "2 tins chopped tomatoes", "2 tbsp tomato puree", "400g spaghetti", "Parmesan"]},
    "Cottage Pie": {"ingredients": ["500g beef mince", "1 onion, diced", "2 carrots, diced", "400ml beef stock", "2 tbsp tomato puree", "800g potatoes", "50g butter", "Milk"]},
    "Beef Stroganoff": {"ingredients": ["500g beef sirloin, sliced thin", "250g mushrooms, sliced", "1 onion, sliced", "200ml beef stock", "150ml sour cream", "1 tbsp paprika", "Rice"]},
    "Chilli Con Carne": {"ingredients": ["500g beef mince", "1 onion, diced", "2 garlic cloves", "1 tin tomatoes", "1 tin kidney beans", "2 tsp cumin", "1 tsp chilli powder", "Rice"]},
    "Beef Stew": {"ingredients": ["500g stewing beef, cubed", "2 onions, quartered", "4 carrots, chunked", "4 potatoes, chunked", "500ml beef stock", "2 tbsp flour", "Thyme"]},
    "Beef Tacos": {"ingredients": ["500g beef mince", "1 onion, diced", "2 tbsp taco seasoning", "8 taco shells", "Lettuce, tomato, cheese", "Sour cream, salsa"]},
    "Beef Burgers": {"ingredients": ["500g beef mince", "1 onion, grated", "1 egg", "4 burger buns", "Lettuce, tomato, onion", "Cheese, ketchup, mustard"]},
    "Steak & Chips": {"ingredients": ["2 sirloin steaks", "500g potatoes, cut into chips", "Oil for frying", "Butter", "Peas"]},
    "Beef Fajitas": {"ingredients": ["500g beef steak, sliced", "2 peppers, sliced", "1 onion, sliced", "2 tbsp fajita seasoning", "8 tortillas", "Sour cream, guacamole"]},
    "Lasagne": {"ingredients": ["500g beef mince", "1 onion", "2 tins tomatoes", "Lasagne sheets", "50g butter", "50g flour", "500ml milk", "100g parmesan"]},
    "Meatballs in Tomato Sauce": {"ingredients": ["500g beef mince", "1 onion, grated", "50g breadcrumbs", "1 egg", "2 tins tomatoes", "2 garlic cloves", "Fresh basil", "Spaghetti"]},
    "Beef & Broccoli Stir-fry": {"ingredients": ["400g beef steak, sliced", "1 head broccoli, florets", "3 garlic cloves", "3 tbsp soy sauce", "1 tbsp honey", "Rice"]},
    "Chicken Tikka Masala": {"ingredients": ["500g chicken breast, cubed", "2 tbsp tikka paste", "1 onion", "1 tin tomatoes", "200ml cream", "Coriander", "Rice"]},
    "Chicken Fajitas": {"ingredients": ["500g chicken breast, sliced", "2 peppers, sliced", "1 onion, sliced", "2 tbsp fajita seasoning", "8 tortillas", "Sour cream, salsa"]},
    "Chicken Korma": {"ingredients": ["500g chicken breast, cubed", "1 onion", "3 tbsp korma paste", "200ml coconut cream", "100g ground almonds", "Sultanas", "Rice"]},
    "Chicken Katsu Curry": {"ingredients": ["4 chicken breasts", "100g flour", "2 eggs", "150g panko breadcrumbs", "1 onion", "2 tbsp curry powder", "400ml chicken stock", "Rice"]},
    "Thai Green Curry": {"ingredients": ["500g chicken thigh, sliced", "2 tbsp green curry paste", "400ml coconut milk", "1 aubergine, cubed", "Green beans", "Thai basil", "Rice"]},
    "Chicken Stir-fry": {"ingredients": ["500g chicken breast, sliced", "2 peppers, sliced", "1 onion, sliced", "2 pak choi", "3 tbsp soy sauce", "1 tbsp honey", "Noodles"]},
    "Chicken Pie": {"ingredients": ["500g chicken breast, cubed", "3 leeks, sliced", "200ml chicken stock", "200ml cream", "1 tbsp Dijon mustard", "1 sheet puff pastry", "1 egg"]},
    "Honey Mustard Chicken": {"ingredients": ["4 chicken breasts", "3 tbsp honey", "2 tbsp wholegrain mustard", "2 tbsp soy sauce", "New potatoes", "Green veg"]},
    "Chicken Cacciatore": {"ingredients": ["8 chicken thighs", "1 onion, sliced", "2 peppers, sliced", "2 tins tomatoes", "100ml red wine", "Olives", "Fresh basil"]},
    "Lemon Herb Chicken": {"ingredients": ["4 chicken breasts", "2 lemons, juiced", "4 garlic cloves", "Fresh rosemary, thyme", "Olive oil", "Roast potatoes", "Salad"]},
    "Chicken Goujons": {"ingredients": ["4 chicken breasts, cut into strips", "100g flour", "2 eggs", "150g breadcrumbs", "Oil for frying", "Chips", "Peas"]},
    "Chicken Noodle Stir-fry": {"ingredients": ["400g chicken, sliced", "300g egg noodles", "2 pak choi", "100g beansprouts", "3 tbsp soy sauce", "1 tbsp sesame oil"]},
    "Sausage Casserole": {"ingredients": ["8 pork sausages", "1 onion, sliced", "2 peppers, sliced", "2 tins tomatoes", "1 tin cannellini beans", "2 tsp smoked paprika"]},
    "Pork Chops with Apple": {"ingredients": ["4 pork chops", "2 apples, sliced", "1 onion, sliced", "200ml cider", "1 tbsp wholegrain mustard", "Mashed potato"]},
    "Pulled Pork": {"ingredients": ["1.5kg pork shoulder", "2 tbsp smoked paprika", "1 tbsp brown sugar", "200ml BBQ sauce", "Burger buns", "Coleslaw"]},
    "Pork Stir-fry": {"ingredients": ["400g pork tenderloin, sliced", "1 red pepper", "1 courgette", "100g mangetout", "3 tbsp hoisin sauce", "Rice or noodles"]},
    "Gammon, Egg & Chips": {"ingredients": ["2 gammon steaks", "4 eggs", "500g potatoes, cut into chips", "Oil", "Peas"]},
    "Toad in the Hole": {"ingredients": ["8 sausages", "140g flour", "4 eggs", "200ml milk", "Vegetable oil", "Onion gravy"]},
    "Pork Meatballs": {"ingredients": ["500g pork mince", "1 onion, grated", "50g breadcrumbs", "1 egg", "2 tins tomatoes", "Fresh basil", "Spaghetti"]},
    "Sweet & Sour Pork": {"ingredients": ["400g pork tenderloin, cubed", "1 pepper, chunked", "1 onion, chunked", "1 tin pineapple chunks", "3 tbsp tomato ketchup", "2 tbsp soy sauce", "1 tbsp vinegar", "Rice"]},
    "Shepherd's Pie": {"ingredients": ["500g lamb mince", "1 onion, diced", "2 carrots, diced", "400ml lamb stock", "2 tbsp tomato puree", "800g potatoes", "50g butter"]},
    "Lamb Koftas": {"ingredients": ["500g lamb mince", "1 onion, grated", "2 garlic cloves", "1 tsp cumin", "Fresh mint", "Pitta bread", "Tzatziki, salad"]},
    "Lamb Chops with Mint": {"ingredients": ["8 lamb chops", "Fresh mint, chopped", "2 tbsp olive oil", "2 garlic cloves", "New potatoes", "Green beans"]},
    "Lamb Curry": {"ingredients": ["500g lamb leg, cubed", "1 onion", "3 tbsp curry paste", "400ml coconut milk", "200g spinach", "Rice", "Naan bread"]},
    "Moussaka": {"ingredients": ["500g lamb mince", "2 aubergines, sliced", "1 onion", "2 tins tomatoes", "1 tsp cinnamon", "50g butter", "50g flour", "500ml milk", "100g feta"]},
    "Lamb Hotpot": {"ingredients": ["500g lamb neck, sliced", "2 onions, sliced", "3 carrots, sliced", "500ml lamb stock", "Fresh thyme", "800g potatoes, sliced"]},
    "Fish & Chips": {"ingredients": ["4 cod fillets", "150g flour", "200ml sparkling water", "1 tsp baking powder", "1kg potatoes", "Oil", "Mushy peas", "Tartare sauce"]},
    "Fish Pie": {"ingredients": ["400g mixed fish (salmon, cod, smoked haddock)", "200g prawns", "500ml milk", "50g butter", "50g flour", "800g potatoes", "Fresh parsley"]},
    "Fish Tacos": {"ingredients": ["400g white fish", "2 tsp cumin", "1 tsp paprika", "8 tortillas", "Cabbage, shredded", "Lime", "Sour cream", "Coriander"]},
    "Salmon Teriyaki": {"ingredients": ["4 salmon fillets", "4 tbsp soy sauce", "2 tbsp honey", "1 tbsp rice vinegar", "1 garlic clove", "Rice", "Broccoli"]},
    "Prawn Stir-fry": {"ingredients": ["400g prawns", "2 peppers, sliced", "100g mangetout", "2 pak choi", "3 tbsp soy sauce", "1 tbsp sesame oil", "Noodles"]},
    "Salmon Fishcakes": {"ingredients": ["400g salmon fillets", "400g potatoes, mashed", "2 spring onions, sliced", "1 tbsp capers", "Flour, egg, breadcrumbs", "Salad", "Tartare sauce"]},
    "Prawn Curry": {"ingredients": ["400g prawns", "1 onion", "2 tbsp curry paste", "400ml coconut milk", "200g spinach", "Rice", "Naan"]},
    "Cod with Parsley Sauce": {"ingredients": ["4 cod fillets", "50g butter", "50g flour", "500ml milk", "Large bunch parsley, chopped", "New potatoes", "Peas"]},
    "Fish Finger Sandwiches": {"ingredients": ["12 fish fingers", "8 slices bread", "Tartare sauce", "Lettuce", "Lemon"]},
    "Tuna Pasta Bake": {"ingredients": ["300g pasta", "2 tins tuna", "1 tin sweetcorn", "50g butter", "50g flour", "500ml milk", "150g cheddar"]},
    "Smoked Haddock Risotto": {"ingredients": ["400g smoked haddock", "300g risotto rice", "1 onion", "150ml white wine", "1L fish stock", "100g peas", "50g parmesan"]},
    "Baked Salmon with Lemon": {"ingredients": ["4 salmon fillets", "2 lemons", "Fresh dill", "Olive oil", "New potatoes", "Asparagus"]},
    "Cauliflower Cheese": {"ingredients": ["1 large cauliflower", "50g butter", "50g flour", "500ml milk", "200g cheddar", "1 tsp mustard"]},
    "Mushroom Risotto": {"ingredients": ["300g risotto rice", "300g mushrooms", "1 onion", "150ml white wine", "1L veg stock", "50g parmesan", "Fresh thyme"]},
    "Vegetable Curry": {"ingredients": ["1 cauliflower, florets", "2 potatoes, cubed", "200g spinach", "1 onion", "3 tbsp curry paste", "400ml coconut milk", "Rice"]},
    "Macaroni Cheese": {"ingredients": ["350g macaroni", "50g butter", "50g flour", "600ml milk", "250g cheddar", "1 tsp mustard"]},
    "Vegetable Stir-fry": {"ingredients": ["1 broccoli, florets", "2 peppers, sliced", "2 pak choi", "100g beansprouts", "3 tbsp soy sauce", "1 tbsp sesame oil", "Noodles or rice"]},
    "Vegetable Lasagne": {"ingredients": ["2 courgettes, sliced", "1 aubergine, sliced", "2 peppers, sliced", "2 tins tomatoes", "Lasagne sheets", "50g butter", "50g flour", "500ml milk", "100g parmesan"]},
    "Cheese & Onion Pie": {"ingredients": ["500g potatoes, sliced", "2 onions, sliced", "200g cheddar, grated", "300ml cream", "1 sheet puff pastry", "1 egg"]},
    "Spinach & Ricotta Cannelloni": {"ingredients": ["12 cannelloni tubes", "500g spinach, wilted", "250g ricotta", "100g parmesan", "2 tins tomatoes", "2 garlic cloves"]},
    "Stuffed Peppers": {"ingredients": ["4 large peppers", "200g rice, cooked", "1 tin chickpeas", "100g feta", "Fresh herbs", "Olive oil"]},
    "Vegetable Fajitas": {"ingredients": ["2 peppers, sliced", "1 courgette, sliced", "1 onion, sliced", "1 tin black beans", "2 tbsp fajita seasoning", "8 tortillas", "Sour cream, salsa"]},
}

breakfast_recipes = {
    "Full English": {"ingredients": ["4 rashers bacon", "4 sausages", "4 eggs", "2 tomatoes, halved", "200g mushrooms", "1 tin baked beans", "Toast"]},
    "Eggs Benedict": {"ingredients": ["4 eggs", "2 English muffins", "4 slices ham", "For hollandaise: 2 egg yolks, 100g butter, 1 tbsp lemon juice"]},
    "Eggs Florentine": {"ingredients": ["4 eggs", "200g spinach", "2 English muffins", "Hollandaise sauce", "Butter"]},
    "Eggs Royale": {"ingredients": ["4 eggs", "2 English muffins", "100g smoked salmon", "Hollandaise sauce"]},
    "Pancakes": {"ingredients": ["200g self-raising flour", "1 egg", "300ml milk", "Butter", "Maple syrup, bacon or berries"]},
    "American Pancakes": {"ingredients": ["200g self-raising flour", "1 tsp baking powder", "1 egg", "250ml milk", "2 tbsp melted butter", "Maple syrup, blueberries"]},
    "French Toast": {"ingredients": ["4 thick slices bread (brioche is best)", "2 eggs", "100ml milk", "1 tsp cinnamon", "Vanilla", "Butter", "Berries, maple syrup"]},
    "Shakshuka": {"ingredients": ["1 tin tomatoes", "1 red pepper, diced", "1 onion", "2 garlic cloves", "1 tsp cumin", "1 tsp paprika", "4 eggs", "Coriander", "Crusty bread"]},
    "Avocado on Toast": {"ingredients": ["2 avocados", "4 slices sourdough", "4 eggs", "Chilli flakes", "Lemon", "Salt & pepper"]},
    "Scrambled Eggs & Smoked Salmon": {"ingredients": ["6 eggs", "2 tbsp butter", "100g smoked salmon", "Fresh chives", "Toast"]},
    "Omelette": {"ingredients": ["3 eggs", "Filling of choice (cheese, ham, mushrooms, herbs)", "1 tbsp butter"]},
    "Bacon & Egg Muffin": {"ingredients": ["4 rashers bacon", "2 eggs", "2 English muffins", "2 slices cheese", "Brown sauce or ketchup"]},
    "Kedgeree": {"ingredients": ["300g smoked haddock", "250g rice", "4 eggs, hard boiled", "1 onion", "2 tsp curry powder", "Fresh parsley"]},
    "Porridge with Berries": {"ingredients": ["100g porridge oats", "400ml milk", "Honey", "Fresh berries", "Seeds (optional)"]},
    "Croissants with Ham & Cheese": {"ingredients": ["2 croissants", "4 slices ham", "50g gruyere, sliced", "Dijon mustard"]},
}

roast_recipes = {
    "Roast Beef": {"ingredients": ["1.5kg beef joint", "Olive oil", "Salt & pepper", "Fresh rosemary"]},
    "Roast Chicken": {"ingredients": ["1.8kg whole chicken", "1 lemon, halved", "1 garlic bulb", "Fresh thyme", "50g butter"]},
    "Roast Pork": {"ingredients": ["2kg pork shoulder, skin scored", "Olive oil", "Sea salt", "Fresh sage"]},
    "Roast Lamb": {"ingredients": ["2kg leg of lamb", "6 garlic cloves", "Fresh rosemary", "Olive oil"]},
    "Roast Potatoes": {"ingredients": ["1.5kg potatoes, quartered", "4 tbsp goose fat or oil", "Salt", "Fresh rosemary"]},
    "Yorkshire Puddings": {"ingredients": ["140g flour", "4 eggs", "200ml milk", "Oil"]},
    "Onion Gravy": {"ingredients": ["2 onions, sliced", "2 tbsp butter", "1 tbsp flour", "500ml stock", "Meat juices"]},
}

# ============================================================
# INGREDIENT CATEGORIZATION
# ============================================================

def categorize_ingredient(ingredient):
    """Categorize an ingredient into shopping list sections"""
    ing_lower = ingredient.lower()

    # Meat
    if any(x in ing_lower for x in ["beef", "mince", "steak", "sirloin", "stewing"]):
        return "meat_beef"
    if any(x in ing_lower for x in ["chicken", "thigh"]):
        return "meat_chicken"
    if any(x in ing_lower for x in ["pork", "gammon", "sausage", "bacon", "ham"]):
        return "meat_pork"
    if any(x in ing_lower for x in ["lamb"]):
        return "meat_lamb"

    # Fish
    if any(x in ing_lower for x in ["salmon", "cod", "haddock", "fish", "prawn", "mackerel", "tuna", "sardine"]):
        return "fish"

    # Dairy
    if any(x in ing_lower for x in ["milk", "cream", "butter", "cheese", "cheddar", "parmesan", "feta", "gruyere", "stilton", "ricotta", "yogurt", "sour cream"]):
        return "dairy"

    # Eggs
    if "egg" in ing_lower:
        return "eggs"

    # Bread/Bakery
    if any(x in ing_lower for x in ["bread", "baguette", "roll", "bun", "wrap", "tortilla", "pitta", "naan", "croissant", "muffin", "bagel", "crouton"]):
        return "bread"

    # Pasta/Rice/Carbs
    if any(x in ing_lower for x in ["pasta", "spaghetti", "macaroni", "lasagne", "noodle", "rice", "cannelloni"]):
        return "carbs"

    # Fresh Produce - Vegetables
    if any(x in ing_lower for x in ["onion", "garlic", "carrot", "potato", "leek", "celery", "pepper", "tomato", "lettuce", "cucumber", "courgette", "aubergine", "broccoli", "cauliflower", "spinach", "mushroom", "bean", "pea", "asparagus", "pak choi", "cabbage", "squash", "avocado", "spring onion", "beansprout", "mangetout"]):
        return "produce_veg"

    # Fresh Produce - Fruit
    if any(x in ing_lower for x in ["lemon", "lime", "apple", "berries", "pineapple", "banana"]):
        return "produce_fruit"

    # Fresh Herbs
    if any(x in ing_lower for x in ["basil", "coriander", "parsley", "mint", "thyme", "rosemary", "sage", "dill", "chives"]):
        return "herbs"

    # Tinned/Jarred
    if any(x in ing_lower for x in ["tin", "tinned", "baked beans", "kidney beans", "cannellini", "chickpea", "chopped tomatoes", "sweetcorn"]):
        return "tins"

    # Sauces/Condiments
    if any(x in ing_lower for x in ["sauce", "paste", "ketchup", "mustard", "mayo", "pickle", "chutney", "salsa", "vinegar", "oil", "soy sauce", "hoisin", "honey"]):
        return "condiments"

    # Stock/Cooking
    if any(x in ing_lower for x in ["stock", "wine", "cider", "beer"]):
        return "cooking"

    # Spices
    if any(x in ing_lower for x in ["cumin", "paprika", "cinnamon", "curry", "chilli", "seasoning", "oregano", "pepper", "salt"]):
        return "spices"

    # Baking
    if any(x in ing_lower for x in ["flour", "sugar", "breadcrumb", "baking powder", "panko"]):
        return "baking"

    # Frozen
    if "frozen" in ing_lower:
        return "frozen"

    # Nuts/Dried
    if any(x in ing_lower for x in ["almond", "sultana", "olive", "caper", "raisin"]):
        return "dried"

    return "other"

# ============================================================
# BUILD MEAL SCHEDULE (same as generate_pages.py)
# ============================================================

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

all_lunches = list(lunch_recipes.keys())
all_dinners = list(dinner_recipes.keys())
all_breakfasts = list(breakfast_recipes.keys())
roast_names = ["Roast Beef", "Roast Chicken", "Roast Pork", "Roast Lamb"]

meat_dinners = [d for d in all_dinners if any(m in d for m in ["Beef", "Chicken", "Pork", "Lamb", "Sausage", "Burger", "Steak", "Meatball", "Gammon", "Toad", "Lasagne", "Bolognese", "Cottage", "Shepherd", "Chilli", "Fajita", "Taco", "Stew", "Stroganoff", "Korma", "Tikka", "Thai", "Curry", "Katsu", "Cacciatore", "Hotpot", "Moussaka", "Goujons", "Honey", "Lemon", "Pulled", "Sweet"])]
fish_dinners = [d for d in all_dinners if any(f in d for f in ["Fish", "Salmon", "Cod", "Prawn", "Tuna", "Haddock"])]
veg_dinners = [d for d in all_dinners if d in ["Cauliflower Cheese", "Mushroom Risotto", "Vegetable Curry", "Macaroni Cheese", "Vegetable Stir-fry", "Vegetable Lasagne", "Cheese & Onion Pie", "Spinach & Ricotta Cannelloni", "Stuffed Peppers", "Vegetable Fajitas"]]

weeks_data = {}
lunch_idx = 0
meat_idx = 0
fish_idx = 0
veg_idx = 0
breakfast_idx = 0

for week_num in range(1, 53):
    if week_num == 1:
        week_start = datetime.date(2026, 1, 1)
        week_end = datetime.date(2026, 1, 4)
        week_days = ["Thu", "Fri", "Sat", "Sun"]
    else:
        week_start = datetime.date(2026, 1, 5) + datetime.timedelta(weeks=week_num-2)
        week_end = week_start + datetime.timedelta(days=6)
        week_days = days

    has_roast = (week_num % 2 == 1)
    roast_name = roast_names[(week_num - 1) % 4] if has_roast else None

    lunches = []
    for d in week_days:
        lunches.append((d, all_lunches[lunch_idx % len(all_lunches)]))
        lunch_idx += 1

    dinners = []
    dinner_pattern = ["meat", "fish", "veg", "meat", "fish", "meat", "veg"]

    for i, d in enumerate(week_days):
        if d == "Sun" and has_roast:
            dinners.append((d, "Sunday Roast"))
        else:
            pattern_idx = days.index(d) if d in days else i
            category = dinner_pattern[pattern_idx % 7]

            if category == "meat":
                dinners.append((d, meat_dinners[meat_idx % len(meat_dinners)]))
                meat_idx += 1
            elif category == "fish":
                dinners.append((d, fish_dinners[fish_idx % len(fish_dinners)]))
                fish_idx += 1
            else:
                dinners.append((d, veg_dinners[veg_idx % len(veg_dinners)]))
                veg_idx += 1

    weeks_data[week_num] = {
        "dates": f"{week_start.strftime('%d %b')} - {week_end.strftime('%d %b %Y')}",
        "month": week_start.strftime("%B"),
        "breakfast": all_breakfasts[breakfast_idx % len(all_breakfasts)],
        "roast": roast_name,
        "lunches": lunches,
        "dinners": dinners,
    }
    breakfast_idx += 1

# ============================================================
# COLLECT INGREDIENTS FOR EACH WEEK
# ============================================================

def get_week_ingredients(week_num):
    """Collect all ingredients needed for a week's meals"""
    data = weeks_data[week_num]
    all_ingredients = []

    # Breakfast
    if data["breakfast"] in breakfast_recipes:
        all_ingredients.extend(breakfast_recipes[data["breakfast"]]["ingredients"])

    # Lunches
    for day, meal in data["lunches"]:
        if meal in lunch_recipes:
            all_ingredients.extend(lunch_recipes[meal]["ingredients"])

    # Dinners
    for day, meal in data["dinners"]:
        if meal == "Sunday Roast":
            if data["roast"]:
                all_ingredients.extend(roast_recipes[data["roast"]]["ingredients"])
                all_ingredients.extend(roast_recipes["Roast Potatoes"]["ingredients"])
                all_ingredients.extend(roast_recipes["Yorkshire Puddings"]["ingredients"])
                all_ingredients.extend(roast_recipes["Onion Gravy"]["ingredients"])
        elif meal in dinner_recipes:
            all_ingredients.extend(dinner_recipes[meal]["ingredients"])

    return all_ingredients

def organize_shopping_list(ingredients):
    """Organize ingredients into shopping categories"""
    categories = {
        "meat_beef": [], "meat_chicken": [], "meat_pork": [], "meat_lamb": [],
        "fish": [], "dairy": [], "eggs": [], "bread": [], "carbs": [],
        "produce_veg": [], "produce_fruit": [], "herbs": [],
        "tins": [], "condiments": [], "cooking": [], "spices": [],
        "baking": [], "frozen": [], "dried": [], "other": []
    }

    # Count occurrences and consolidate
    ingredient_counts = {}
    for ing in ingredients:
        # Clean up ingredient string
        clean_ing = ing.strip()
        cat = categorize_ingredient(clean_ing)

        if clean_ing not in ingredient_counts:
            ingredient_counts[clean_ing] = {"count": 0, "category": cat}
        ingredient_counts[clean_ing]["count"] += 1

    # Add to categories
    for ing, info in ingredient_counts.items():
        categories[info["category"]].append((ing, info["count"]))

    return categories

# ============================================================
# WEEKLY STAPLES
# ============================================================

weekly_staples = {
    "dairy": [
        ("Whole milk", "2x 2L", "£2.40"),
        ("Oat milk", "1L", "£1.80"),
        ("Butter", "250g", "£2.00"),
    ],
    "bread": [
        ("White sliced loaf", "1", "£1.20"),
        ("Crusty bread", "1", "£1.50"),
        ("Wraps/tortillas", "8 pack", "£1.50"),
        ("Porridge oats", "1kg", "£1.20"),
    ],
    "produce_staples": [
        ("Onions", "1kg bag", "£1.00"),
        ("Garlic", "2 bulbs", "£0.80"),
        ("Potatoes", "2.5kg", "£2.00"),
        ("Bananas", "6", "£0.80"),
    ],
    "drinks": [
        ("Fizzy drinks", "2x 2L", "£2.00"),
        ("Squash", "1L", "£1.50"),
    ],
    "snacks": [
        ("Crisps multipack", "6", "£2.00"),
        ("Biscuits", "1 pack", "£1.00"),
    ],
}

monthly_staples = {
    "household": [
        ("Toilet roll", "9 pack", "£4.50"),
        ("Washing up liquid", "1", "£1.20"),
        ("Kitchen roll", "2 pack", "£2.00"),
        ("Bin bags", "20", "£1.50"),
    ],
    "toiletries": [
        ("Toothpaste", "2 tubes", "£3.00"),
        ("Deodorant", "2", "£3.00"),
        ("Shampoo", "1", "£2.00"),
        ("Shower gel", "2", "£2.00"),
    ],
    "pantry": [
        ("Tinned tomatoes", "4 tins", "£3.20"),
        ("Baked beans", "4 tins", "£2.40"),
        ("Pasta (various)", "1kg", "£1.50"),
        ("Rice", "1kg", "£2.00"),
        ("Stock cubes", "12", "£1.50"),
    ],
    "frozen": [
        ("Frozen peas", "1kg", "£1.50"),
        ("Oven chips", "1.5kg", "£2.00"),
        ("Fish fingers", "10 pack", "£2.00"),
    ],
}

# ============================================================
# HTML GENERATION
# ============================================================

def estimate_price(ingredient, count=1):
    """Estimate price for an ingredient"""
    ing_lower = ingredient.lower()

    # Meats (most expensive)
    if any(x in ing_lower for x in ["beef", "steak", "sirloin"]):
        return count * 4.00
    if any(x in ing_lower for x in ["chicken breast"]):
        return count * 2.50
    if any(x in ing_lower for x in ["chicken thigh", "thigh"]):
        return count * 2.00
    if any(x in ing_lower for x in ["pork", "gammon"]):
        return count * 3.00
    if any(x in ing_lower for x in ["lamb"]):
        return count * 4.50
    if any(x in ing_lower for x in ["sausage"]):
        return count * 1.50
    if any(x in ing_lower for x in ["bacon", "ham"]):
        return count * 1.80
    if any(x in ing_lower for x in ["mince"]):
        return count * 3.00

    # Fish
    if any(x in ing_lower for x in ["salmon"]):
        return count * 3.50
    if any(x in ing_lower for x in ["cod", "haddock"]):
        return count * 3.00
    if any(x in ing_lower for x in ["prawn"]):
        return count * 3.00
    if any(x in ing_lower for x in ["smoked salmon"]):
        return count * 2.50

    # Dairy
    if any(x in ing_lower for x in ["cream", "sour cream"]):
        return count * 1.20
    if any(x in ing_lower for x in ["cheese", "cheddar", "parmesan"]):
        return count * 1.50
    if any(x in ing_lower for x in ["butter"]):
        return count * 0.80
    if any(x in ing_lower for x in ["milk"]):
        return count * 0.60
    if any(x in ing_lower for x in ["egg"]):
        return count * 0.50

    # Produce
    if any(x in ing_lower for x in ["onion", "carrot", "potato", "garlic"]):
        return count * 0.40
    if any(x in ing_lower for x in ["pepper", "tomato", "mushroom"]):
        return count * 0.80
    if any(x in ing_lower for x in ["broccoli", "cauliflower", "spinach"]):
        return count * 1.00
    if any(x in ing_lower for x in ["avocado"]):
        return count * 1.20
    if any(x in ing_lower for x in ["lemon", "lime"]):
        return count * 0.40

    # Herbs
    if any(x in ing_lower for x in ["basil", "coriander", "parsley", "mint", "thyme", "rosemary"]):
        return count * 0.80

    # Carbs
    if any(x in ing_lower for x in ["pasta", "spaghetti", "macaroni", "noodle"]):
        return count * 0.60
    if any(x in ing_lower for x in ["rice"]):
        return count * 0.50
    if any(x in ing_lower for x in ["bread", "wrap", "tortilla"]):
        return count * 0.80

    # Tins
    if "tin" in ing_lower:
        return count * 0.80

    # Default
    return count * 0.50

def generate_shopping_html(week_num):
    """Generate shopping list HTML for a specific week"""
    data = weeks_data[week_num]
    is_big_shop = (week_num - 1) % 4 == 0

    # Get ingredients for this week
    ingredients = get_week_ingredients(week_num)
    organized = organize_shopping_list(ingredients)

    dates = data["dates"]
    month = data["month"]
    shop_type = "BIG SHOP (Monthly Bulk Buy)" if is_big_shop else "Top-up Shop"

    categories_html = ""
    total_estimate = 0

    # Generate meat section
    all_meat = []
    for cat in ["meat_beef", "meat_chicken", "meat_pork", "meat_lamb"]:
        all_meat.extend(organized.get(cat, []))

    if all_meat:
        rows = ""
        for item, count in all_meat:
            price = estimate_price(item, count)
            total_estimate += price
            qty = f"x{count}" if count > 1 else ""
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">~£{price:.2f}</td></tr>\n'
        categories_html += f'''
    <div class="category">
        <h3>🥩 MEAT</h3>
        <table>{rows}</table>
    </div>'''

    # Generate fish section
    fish = organized.get("fish", [])
    if fish:
        rows = ""
        for item, count in fish:
            price = estimate_price(item, count)
            total_estimate += price
            qty = f"x{count}" if count > 1 else ""
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">~£{price:.2f}</td></tr>\n'
        categories_html += f'''
    <div class="category">
        <h3>🐟 FISH</h3>
        <table>{rows}</table>
    </div>'''

    # Generate dairy section (including weekly staples)
    dairy = organized.get("dairy", [])
    eggs = organized.get("eggs", [])
    if dairy or eggs or is_big_shop:
        rows = ""
        # Add weekly staples
        for item, qty, price in weekly_staples["dairy"]:
            price_val = float(price.replace("£", ""))
            total_estimate += price_val
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
        # Add recipe-specific dairy
        seen = set()
        for item, count in dairy:
            if item not in seen:
                price = estimate_price(item, count)
                total_estimate += price
                qty = f"x{count}" if count > 1 else ""
                rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">~£{price:.2f}</td></tr>\n'
                seen.add(item)
        for item, count in eggs:
            price = estimate_price(item, count)
            total_estimate += price
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">x{count}</td><td class="price">~£{price:.2f}</td></tr>\n'
        categories_html += f'''
    <div class="category">
        <h3>🧀 DAIRY & EGGS</h3>
        <table>{rows}</table>
    </div>'''

    # Generate bread section
    bread = organized.get("bread", [])
    rows = ""
    for item, qty, price in weekly_staples["bread"]:
        price_val = float(price.replace("£", ""))
        total_estimate += price_val
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    seen = set()
    for item, count in bread:
        if item not in seen:
            price = estimate_price(item, count)
            total_estimate += price
            qty = f"x{count}" if count > 1 else ""
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">~£{price:.2f}</td></tr>\n'
            seen.add(item)
    categories_html += f'''
    <div class="category">
        <h3>🍞 BREAD & BAKERY</h3>
        <table>{rows}</table>
    </div>'''

    # Generate produce section
    produce = organized.get("produce_veg", []) + organized.get("produce_fruit", [])
    if produce:
        rows = ""
        for item, qty, price in weekly_staples["produce_staples"]:
            price_val = float(price.replace("£", ""))
            total_estimate += price_val
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
        seen = set()
        for item, count in produce:
            # Skip basics already in staples
            if any(x in item.lower() for x in ["onion", "garlic", "potato", "banana"]) and count < 3:
                continue
            if item not in seen:
                price = estimate_price(item, count)
                total_estimate += price
                qty = f"x{count}" if count > 1 else ""
                rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">~£{price:.2f}</td></tr>\n'
                seen.add(item)
        categories_html += f'''
    <div class="category">
        <h3>🥬 FRESH PRODUCE</h3>
        <table>{rows}</table>
    </div>'''

    # Generate herbs section
    herbs = organized.get("herbs", [])
    if herbs:
        rows = ""
        seen = set()
        for item, count in herbs:
            if item not in seen:
                price = estimate_price(item, count)
                total_estimate += price
                rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty"></td><td class="price">~£{price:.2f}</td></tr>\n'
                seen.add(item)
        categories_html += f'''
    <div class="category">
        <h3>🌿 FRESH HERBS</h3>
        <table>{rows}</table>
    </div>'''

    # Generate carbs section
    carbs = organized.get("carbs", [])
    if carbs:
        rows = ""
        seen = set()
        for item, count in carbs:
            if item not in seen:
                price = estimate_price(item, count)
                total_estimate += price
                qty = f"x{count}" if count > 1 else ""
                rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">~£{price:.2f}</td></tr>\n'
                seen.add(item)
        categories_html += f'''
    <div class="category">
        <h3>🍝 PASTA, RICE & NOODLES</h3>
        <table>{rows}</table>
    </div>'''

    # Generate tins section
    tins = organized.get("tins", [])
    if tins:
        rows = ""
        seen = set()
        for item, count in tins:
            if item not in seen:
                price = estimate_price(item, count)
                total_estimate += price
                qty = f"x{count}" if count > 1 else ""
                rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">~£{price:.2f}</td></tr>\n'
                seen.add(item)
        categories_html += f'''
    <div class="category">
        <h3>🥫 TINS & JARS</h3>
        <table>{rows}</table>
    </div>'''

    # Add staple sections
    rows = ""
    for item, qty, price in weekly_staples["drinks"]:
        price_val = float(price.replace("£", ""))
        total_estimate += price_val
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🥤 DRINKS</h3>
        <table>{rows}</table>
    </div>'''

    rows = ""
    for item, qty, price in weekly_staples["snacks"]:
        price_val = float(price.replace("£", ""))
        total_estimate += price_val
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🍪 SNACKS</h3>
        <table>{rows}</table>
    </div>'''

    # Add monthly sections for big shop weeks
    if is_big_shop:
        rows = ""
        for item, qty, price in monthly_staples["household"]:
            price_val = float(price.replace("£", ""))
            total_estimate += price_val
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
        categories_html += f'''
    <div class="category">
        <h3>🧻 HOUSEHOLD</h3>
        <table>{rows}</table>
    </div>'''

        rows = ""
        for item, qty, price in monthly_staples["toiletries"]:
            price_val = float(price.replace("£", ""))
            total_estimate += price_val
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
        categories_html += f'''
    <div class="category">
        <h3>🧴 TOILETRIES</h3>
        <table>{rows}</table>
    </div>'''

        rows = ""
        for item, qty, price in monthly_staples["pantry"]:
            price_val = float(price.replace("£", ""))
            total_estimate += price_val
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
        categories_html += f'''
    <div class="category">
        <h3>🏪 PANTRY STAPLES</h3>
        <table>{rows}</table>
    </div>'''

        rows = ""
        for item, qty, price in monthly_staples["frozen"]:
            price_val = float(price.replace("£", ""))
            total_estimate += price_val
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
        categories_html += f'''
    <div class="category">
        <h3>❄️ FROZEN</h3>
        <table>{rows}</table>
    </div>'''

    # Round budget estimate
    budget = f"~£{int(round(total_estimate, -1))}"

    # QR code URL
    recipe_url = f"{BASE_URL}/week-{week_num:02d}.html"
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=120x120&data={recipe_url}"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Week {week_num} Shopping List</title>
    <style>
        @page {{ size: A4; margin: 10mm; }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: Arial, sans-serif;
            font-size: 11px;
            line-height: 1.3;
            padding: 10px;
        }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            border-bottom: 3px solid #2c5530;
            padding-bottom: 10px;
            margin-bottom: 10px;
        }}
        .header-left h1 {{
            font-size: 18px;
            color: #2c5530;
            margin-bottom: 3px;
        }}
        .header-left .dates {{ color: #666; font-size: 12px; }}
        .header-left .shop-type {{
            background: #2c5530;
            color: white;
            padding: 3px 8px;
            border-radius: 3px;
            font-size: 10px;
            display: inline-block;
            margin-top: 5px;
        }}
        .meals-summary {{
            font-size: 9px;
            color: #666;
            margin-top: 5px;
        }}
        .qr-section {{
            text-align: center;
        }}
        .qr-section img {{
            width: 80px;
            height: 80px;
        }}
        .qr-section p {{
            font-size: 9px;
            color: #666;
            margin-top: 3px;
        }}
        .content {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }}
        .category {{
            break-inside: avoid;
            margin-bottom: 8px;
        }}
        .category h3 {{
            background: #e8f5e9;
            padding: 4px 8px;
            font-size: 11px;
            color: #2c5530;
            margin-bottom: 3px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        td {{
            padding: 2px 4px;
            border-bottom: 1px solid #eee;
            font-size: 10px;
        }}
        .checkbox {{ width: 20px; text-align: center; }}
        .qty {{ width: 50px; color: #666; text-align: right; }}
        .price {{ width: 55px; text-align: right; color: #2c5530; font-weight: bold; }}
        .budget {{
            text-align: right;
            margin-top: 10px;
            padding-top: 5px;
            border-top: 2px solid #2c5530;
            font-size: 14px;
            font-weight: bold;
            color: #2c5530;
        }}
        @media print {{
            body {{ padding: 0; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <div class="header-left">
            <h1>Week {week_num} - {month}</h1>
            <div class="dates">{dates}</div>
            <div class="shop-type">{shop_type}</div>
            <div class="meals-summary">Breakfast: {data["breakfast"]} | {"Roast: " + data["roast"] if data["roast"] else "No roast this week"}</div>
        </div>
        <div class="qr-section">
            <img src="{qr_url}" alt="QR Code">
            <p>Scan for recipes</p>
        </div>
    </div>

    <div class="content">
        {categories_html}
    </div>

    <div class="budget">
        Estimated Budget: {budget}
    </div>
</body>
</html>'''

    return html

# ============================================================
# GENERATE ALL SHOPPING LISTS
# ============================================================

print("Generating shopping lists from recipe ingredients...")
print("=" * 50)

for week_num in range(1, 53):
    html = generate_shopping_html(week_num)
    filename = os.path.join(output_dir, f"shopping-week-{week_num:02d}.html")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

    is_big = "(BIG SHOP)" if (week_num - 1) % 4 == 0 else ""
    print(f"Created shopping-week-{week_num:02d}.html {is_big}")

print("=" * 50)
print("All 52 shopping lists created with recipe-based ingredients!")
print(f"Files are in: {output_dir}")
