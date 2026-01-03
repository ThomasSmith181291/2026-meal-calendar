"""
Generate printable A4 shopping lists with QR codes
BIG SHOP (weeks 1, 5, 9, etc.) = All meat/fish for 4 weeks + monthly items
TOP-UP (weeks 2,3,4, etc.) = Fresh produce, dairy, bread only
"""

import os
import datetime
import random
import re
from collections import defaultdict

random.seed(2026)

output_dir = r"C:\Users\Little Nineveh\2026-meal-calendar\printable"
os.makedirs(output_dir, exist_ok=True)

BASE_URL = "https://thomassmith181291.github.io/2026-meal-calendar"

# ============================================================
# RECIPE DATABASE (ingredients only - for shopping list extraction)
# ============================================================

lunch_recipes = {
    "Leek & potato soup": {"ingredients": ["2 leeks", "500g potatoes", "1 onion", "100ml cream"], "protein": None},
    "Tomato soup": {"ingredients": ["2 tins chopped tomatoes", "1 onion", "2 garlic cloves"], "protein": None},
    "Carrot & coriander soup": {"ingredients": ["500g carrots", "1 onion", "Fresh coriander"], "protein": None},
    "Butternut squash soup": {"ingredients": ["1 butternut squash", "1 onion", "2 garlic cloves"], "protein": None},
    "Chicken noodle soup": {"ingredients": ["2 chicken breasts", "2 carrots", "2 celery sticks", "100g egg noodles", "Fresh parsley"], "protein": "chicken"},
    "Pea & mint soup": {"ingredients": ["500g frozen peas", "1 onion", "100ml cream", "Fresh mint"], "protein": None},
    "French onion soup": {"ingredients": ["4 onions", "100ml white wine", "100g gruyere", "Baguette"], "protein": None},
    "Minestrone": {"ingredients": ["1 onion", "2 carrots", "2 celery sticks", "1 tin chopped tomatoes", "1 tin cannellini beans", "100g pasta"], "protein": None},
    "Broccoli & stilton soup": {"ingredients": ["1 large broccoli", "1 onion", "100g stilton", "100ml cream"], "protein": None},
    "Sweetcorn chowder": {"ingredients": ["2 tins sweetcorn", "200g bacon", "1 onion", "2 potatoes", "200ml cream"], "protein": "pork"},
    "Roasted red pepper soup": {"ingredients": ["4 red peppers", "1 onion", "2 garlic cloves"], "protein": None},
    "Mushroom soup": {"ingredients": ["400g mushrooms", "1 onion", "2 garlic cloves", "100ml cream", "Fresh thyme"], "protein": None},
    "Ham & cheese toastie": {"ingredients": ["Bread", "100g ham", "50g cheddar"], "protein": "pork"},
    "BLT sandwich": {"ingredients": ["150g bacon", "Bread", "Lettuce", "2 tomatoes", "Mayonnaise"], "protein": "pork"},
    "Tuna melt": {"ingredients": ["1 tin tuna", "Bread", "50g cheddar"], "protein": "fish"},
    "Club sandwich": {"ingredients": ["Bread", "100g bacon", "200g cooked chicken", "Lettuce", "2 tomatoes"], "protein": "chicken"},
    "Croque monsieur": {"ingredients": ["Bread", "200g ham", "100g gruyere", "150ml milk"], "protein": "pork"},
    "Coronation chicken sandwich": {"ingredients": ["2 chicken breasts", "Bread", "Lettuce", "Mango chutney"], "protein": "chicken"},
    "Egg mayo sandwich": {"ingredients": ["4 eggs", "Bread", "Mayonnaise"], "protein": None},
    "Cheese & pickle sandwich": {"ingredients": ["Bread", "75g cheddar", "Branston pickle"], "protein": None},
    "Welsh rarebit": {"ingredients": ["200g mature cheddar", "100ml beer or milk", "Bread"], "protein": None},
    "Prawn mayo sandwich": {"ingredients": ["150g cooked prawns", "Bread", "Lettuce", "Mayonnaise"], "protein": "fish"},
    "Smoked salmon bagel": {"ingredients": ["Bagels", "100g smoked salmon", "Cream cheese", "Capers"], "protein": "fish"},
    "Chicken Caesar wrap": {"ingredients": ["1 chicken breast", "Wraps", "Romaine lettuce", "Parmesan", "Caesar dressing"], "protein": "chicken"},
    "Ham salad wrap": {"ingredients": ["100g ham", "Wraps", "Lettuce", "Tomato", "Cucumber"], "protein": "pork"},
    "Hummus & veg wrap": {"ingredients": ["Hummus", "Wraps", "Carrots", "Cucumber", "Red pepper"], "protein": None},
    "Cheese toastie": {"ingredients": ["Bread", "75g cheddar"], "protein": None},
    "Cheese omelette": {"ingredients": ["3 eggs", "50g cheese"], "protein": None},
    "Jacket potato with beans": {"ingredients": ["2 large potatoes", "1 tin baked beans", "50g cheese"], "protein": None},
    "Jacket potato with tuna mayo": {"ingredients": ["2 large potatoes", "1 tin tuna", "Sweetcorn"], "protein": "fish"},
    "Jacket potato with cheese & coleslaw": {"ingredients": ["2 large potatoes", "75g cheddar", "Coleslaw"], "protein": None},
    "Beans on toast": {"ingredients": ["1 tin baked beans", "Bread", "Cheese"], "protein": None},
    "Cheese on toast": {"ingredients": ["Bread", "75g cheddar"], "protein": None},
    "Sardines on toast": {"ingredients": ["1 tin sardines", "Bread", "Lemon"], "protein": "fish"},
    "Egg fried rice": {"ingredients": ["300g rice", "2 eggs", "100g frozen peas", "2 spring onions", "Soy sauce"], "protein": None},
    "Quesadilla": {"ingredients": ["Tortillas", "75g cheddar", "1 pepper", "Salsa", "Sour cream"], "protein": None},
    "Avocado on toast": {"ingredients": ["2 avocados", "Sourdough bread", "Lemon", "Chilli flakes"], "protein": None},
    "Greek salad": {"ingredients": ["1 cucumber", "4 tomatoes", "1 red onion", "100g feta", "Olives"], "protein": None},
    "Caesar salad": {"ingredients": ["Romaine lettuce", "1 chicken breast", "Croutons", "Parmesan", "Caesar dressing"], "protein": "chicken"},
    "Nicoise salad": {"ingredients": ["200g new potatoes", "100g green beans", "2 eggs", "1 tin tuna", "Olives"], "protein": "fish"},
    "Ploughman's lunch": {"ingredients": ["75g cheddar", "100g ham", "Branston pickle", "Crusty bread", "1 apple", "Celery"], "protein": "pork"},
    "Leftover roast sandwich": {"ingredients": ["Bread", "Stuffing", "Cranberry sauce"], "protein": None},
}

dinner_recipes = {
    "Spaghetti Bolognese": {"ingredients": ["500g beef mince", "1 onion", "2 carrots", "2 tins chopped tomatoes", "400g spaghetti", "Parmesan"], "protein": "beef"},
    "Cottage Pie": {"ingredients": ["500g beef mince", "1 onion", "2 carrots", "800g potatoes"], "protein": "beef"},
    "Beef Stroganoff": {"ingredients": ["500g beef sirloin", "250g mushrooms", "1 onion", "150ml sour cream", "Rice"], "protein": "beef"},
    "Chilli Con Carne": {"ingredients": ["500g beef mince", "1 onion", "1 tin tomatoes", "1 tin kidney beans", "Rice"], "protein": "beef"},
    "Beef Stew": {"ingredients": ["500g stewing beef", "2 onions", "4 carrots", "4 potatoes"], "protein": "beef"},
    "Beef Tacos": {"ingredients": ["500g beef mince", "1 onion", "Taco shells", "Lettuce", "Tomatoes", "Cheese", "Sour cream"], "protein": "beef"},
    "Beef Burgers": {"ingredients": ["500g beef mince", "1 onion", "Burger buns", "Lettuce", "Tomato", "Cheese"], "protein": "beef"},
    "Steak & Chips": {"ingredients": ["2 sirloin steaks", "500g potatoes", "Peas"], "protein": "beef"},
    "Beef Fajitas": {"ingredients": ["500g beef steak", "2 peppers", "1 onion", "Tortillas", "Sour cream"], "protein": "beef"},
    "Lasagne": {"ingredients": ["500g beef mince", "1 onion", "2 tins tomatoes", "Lasagne sheets", "500ml milk", "100g parmesan"], "protein": "beef"},
    "Meatballs in Tomato Sauce": {"ingredients": ["500g beef mince", "1 onion", "2 tins tomatoes", "Spaghetti"], "protein": "beef"},
    "Beef & Broccoli Stir-fry": {"ingredients": ["400g beef steak", "1 head broccoli", "3 garlic cloves", "Soy sauce", "Rice"], "protein": "beef"},
    "Chicken Tikka Masala": {"ingredients": ["500g chicken breast", "1 onion", "1 tin tomatoes", "200ml cream", "Rice"], "protein": "chicken"},
    "Chicken Fajitas": {"ingredients": ["500g chicken breast", "2 peppers", "1 onion", "Tortillas", "Sour cream"], "protein": "chicken"},
    "Chicken Korma": {"ingredients": ["500g chicken breast", "1 onion", "200ml coconut cream", "100g ground almonds", "Rice"], "protein": "chicken"},
    "Chicken Katsu Curry": {"ingredients": ["4 chicken breasts", "Panko breadcrumbs", "1 onion", "Rice"], "protein": "chicken"},
    "Thai Green Curry": {"ingredients": ["500g chicken thigh", "400ml coconut milk", "1 aubergine", "Green beans", "Rice"], "protein": "chicken"},
    "Chicken Stir-fry": {"ingredients": ["500g chicken breast", "2 peppers", "1 onion", "2 pak choi", "Soy sauce", "Noodles"], "protein": "chicken"},
    "Chicken Pie": {"ingredients": ["500g chicken breast", "3 leeks", "200ml cream", "Puff pastry"], "protein": "chicken"},
    "Honey Mustard Chicken": {"ingredients": ["4 chicken breasts", "Honey", "Wholegrain mustard", "New potatoes"], "protein": "chicken"},
    "Chicken Cacciatore": {"ingredients": ["8 chicken thighs", "1 onion", "2 peppers", "2 tins tomatoes", "Olives"], "protein": "chicken"},
    "Lemon Herb Chicken": {"ingredients": ["4 chicken breasts", "2 lemons", "Fresh rosemary", "Fresh thyme", "Potatoes"], "protein": "chicken"},
    "Chicken Goujons": {"ingredients": ["4 chicken breasts", "Breadcrumbs", "Chips", "Peas"], "protein": "chicken"},
    "Chicken Noodle Stir-fry": {"ingredients": ["400g chicken", "300g egg noodles", "2 pak choi", "100g beansprouts", "Soy sauce"], "protein": "chicken"},
    "Sausage Casserole": {"ingredients": ["8 pork sausages", "1 onion", "2 peppers", "2 tins tomatoes", "1 tin cannellini beans"], "protein": "pork"},
    "Pork Chops with Apple": {"ingredients": ["4 pork chops", "2 apples", "1 onion", "200ml cider", "Mashed potato"], "protein": "pork"},
    "Pulled Pork": {"ingredients": ["1.5kg pork shoulder", "BBQ sauce", "Burger buns", "Coleslaw"], "protein": "pork"},
    "Pork Stir-fry": {"ingredients": ["400g pork tenderloin", "1 red pepper", "1 courgette", "100g mangetout", "Hoisin sauce", "Noodles"], "protein": "pork"},
    "Gammon, Egg & Chips": {"ingredients": ["2 gammon steaks", "4 eggs", "500g potatoes", "Peas"], "protein": "pork"},
    "Toad in the Hole": {"ingredients": ["8 sausages", "140g flour", "4 eggs", "200ml milk"], "protein": "pork"},
    "Pork Meatballs": {"ingredients": ["500g pork mince", "1 onion", "2 tins tomatoes", "Spaghetti"], "protein": "pork"},
    "Sweet & Sour Pork": {"ingredients": ["400g pork tenderloin", "1 pepper", "1 onion", "1 tin pineapple", "Rice"], "protein": "pork"},
    "Shepherd's Pie": {"ingredients": ["500g lamb mince", "1 onion", "2 carrots", "800g potatoes"], "protein": "lamb"},
    "Lamb Koftas": {"ingredients": ["500g lamb mince", "1 onion", "Fresh mint", "Pitta bread", "Tzatziki"], "protein": "lamb"},
    "Lamb Chops with Mint": {"ingredients": ["8 lamb chops", "Fresh mint", "New potatoes", "Green beans"], "protein": "lamb"},
    "Lamb Curry": {"ingredients": ["500g lamb leg", "1 onion", "400ml coconut milk", "200g spinach", "Rice", "Naan bread"], "protein": "lamb"},
    "Moussaka": {"ingredients": ["500g lamb mince", "2 aubergines", "1 onion", "2 tins tomatoes", "500ml milk", "100g feta"], "protein": "lamb"},
    "Lamb Hotpot": {"ingredients": ["500g lamb neck", "2 onions", "3 carrots", "800g potatoes"], "protein": "lamb"},
    "Fish & Chips": {"ingredients": ["4 cod fillets", "150g flour", "1kg potatoes", "Mushy peas", "Tartare sauce"], "protein": "fish"},
    "Fish Pie": {"ingredients": ["400g mixed fish", "200g prawns", "500ml milk", "800g potatoes"], "protein": "fish"},
    "Fish Tacos": {"ingredients": ["400g white fish", "Tortillas", "Cabbage", "Lime", "Sour cream"], "protein": "fish"},
    "Salmon Teriyaki": {"ingredients": ["4 salmon fillets", "Soy sauce", "Honey", "Rice", "Broccoli"], "protein": "fish"},
    "Prawn Stir-fry": {"ingredients": ["400g prawns", "2 peppers", "100g mangetout", "2 pak choi", "Noodles"], "protein": "fish"},
    "Salmon Fishcakes": {"ingredients": ["400g salmon fillets", "400g potatoes", "2 spring onions", "Breadcrumbs", "Salad"], "protein": "fish"},
    "Prawn Curry": {"ingredients": ["400g prawns", "1 onion", "400ml coconut milk", "200g spinach", "Rice"], "protein": "fish"},
    "Cod with Parsley Sauce": {"ingredients": ["4 cod fillets", "500ml milk", "Fresh parsley", "New potatoes", "Peas"], "protein": "fish"},
    "Fish Finger Sandwiches": {"ingredients": ["12 fish fingers", "Bread", "Tartare sauce", "Lettuce"], "protein": "fish"},
    "Tuna Pasta Bake": {"ingredients": ["300g pasta", "2 tins tuna", "1 tin sweetcorn", "500ml milk", "150g cheddar"], "protein": "fish"},
    "Smoked Haddock Risotto": {"ingredients": ["400g smoked haddock", "300g risotto rice", "1 onion", "150ml white wine", "100g peas"], "protein": "fish"},
    "Baked Salmon with Lemon": {"ingredients": ["4 salmon fillets", "2 lemons", "Fresh dill", "New potatoes", "Asparagus"], "protein": "fish"},
    "Cauliflower Cheese": {"ingredients": ["1 large cauliflower", "500ml milk", "200g cheddar"], "protein": None},
    "Mushroom Risotto": {"ingredients": ["300g risotto rice", "300g mushrooms", "1 onion", "150ml white wine", "50g parmesan"], "protein": None},
    "Vegetable Curry": {"ingredients": ["1 cauliflower", "2 potatoes", "200g spinach", "1 onion", "400ml coconut milk", "Rice"], "protein": None},
    "Macaroni Cheese": {"ingredients": ["350g macaroni", "600ml milk", "250g cheddar"], "protein": None},
    "Vegetable Stir-fry": {"ingredients": ["1 broccoli", "2 peppers", "2 pak choi", "100g beansprouts", "Soy sauce", "Noodles"], "protein": None},
    "Vegetable Lasagne": {"ingredients": ["2 courgettes", "1 aubergine", "2 peppers", "2 tins tomatoes", "Lasagne sheets", "500ml milk", "100g parmesan"], "protein": None},
    "Cheese & Onion Pie": {"ingredients": ["500g potatoes", "2 onions", "200g cheddar", "300ml cream", "Puff pastry"], "protein": None},
    "Spinach & Ricotta Cannelloni": {"ingredients": ["Cannelloni tubes", "500g spinach", "250g ricotta", "100g parmesan", "2 tins tomatoes"], "protein": None},
    "Stuffed Peppers": {"ingredients": ["4 large peppers", "200g rice", "1 tin chickpeas", "100g feta"], "protein": None},
    "Vegetable Fajitas": {"ingredients": ["2 peppers", "1 courgette", "1 onion", "1 tin black beans", "Tortillas", "Sour cream"], "protein": None},
}

breakfast_recipes = {
    "Full English": {"ingredients": ["200g bacon", "8 sausages", "4 eggs", "2 tomatoes", "200g mushrooms", "1 tin baked beans", "Bread"], "protein": "pork"},
    "Eggs Benedict": {"ingredients": ["4 eggs", "English muffins", "200g ham"], "protein": "pork"},
    "Eggs Florentine": {"ingredients": ["4 eggs", "200g spinach", "English muffins"], "protein": None},
    "Eggs Royale": {"ingredients": ["4 eggs", "English muffins", "200g smoked salmon"], "protein": "fish"},
    "Pancakes": {"ingredients": ["200g flour", "1 egg", "300ml milk", "Maple syrup"], "protein": None},
    "American Pancakes": {"ingredients": ["200g flour", "1 egg", "250ml milk", "Maple syrup", "Blueberries"], "protein": None},
    "French Toast": {"ingredients": ["Thick bread", "2 eggs", "100ml milk", "Berries", "Maple syrup"], "protein": None},
    "Shakshuka": {"ingredients": ["1 tin tomatoes", "1 red pepper", "1 onion", "4 eggs", "Crusty bread"], "protein": None},
    "Avocado on Toast": {"ingredients": ["2 avocados", "Sourdough bread", "4 eggs"], "protein": None},
    "Scrambled Eggs & Smoked Salmon": {"ingredients": ["6 eggs", "100g smoked salmon", "Fresh chives", "Toast"], "protein": "fish"},
    "Omelette": {"ingredients": ["3 eggs", "Cheese", "Ham or mushrooms"], "protein": None},
    "Bacon & Egg Muffin": {"ingredients": ["200g bacon", "2 eggs", "English muffins", "Cheese"], "protein": "pork"},
    "Kedgeree": {"ingredients": ["300g smoked haddock", "250g rice", "4 eggs", "1 onion", "Fresh parsley"], "protein": "fish"},
    "Porridge with Berries": {"ingredients": ["100g porridge oats", "400ml milk", "Berries", "Honey"], "protein": None},
    "Croissants with Ham & Cheese": {"ingredients": ["Croissants", "200g ham", "50g gruyere"], "protein": "pork"},
}

roast_recipes = {
    "Roast Beef": {"ingredients": ["1.5kg beef joint"], "protein": "beef"},
    "Roast Chicken": {"ingredients": ["1.8kg whole chicken", "1 lemon", "1 garlic bulb", "Fresh thyme"], "protein": "chicken"},
    "Roast Pork": {"ingredients": ["2kg pork shoulder"], "protein": "pork"},
    "Roast Lamb": {"ingredients": ["2kg leg of lamb", "Fresh rosemary"], "protein": "lamb"},
}

# Roast sides (for 7 people - doubled quantities)
roast_sides = {
    "potatoes": "3kg potatoes",
    "yorkshires": "Yorkshire pudding mix",
    "gravy": "Gravy granules",
    "vegetables": "Selection of veg for 7",
}

# ============================================================
# PROTEIN CONSOLIDATION - what meat/fish to buy for 4 weeks
# ============================================================

def get_protein_requirements(week_nums):
    """Get all protein requirements for a set of weeks"""
    proteins = {
        "beef": [],
        "chicken": [],
        "pork": [],
        "lamb": [],
        "fish": [],
    }

    for week_num in week_nums:
        data = weeks_data.get(week_num, {})

        # Check breakfast
        breakfast = data.get("breakfast", "")
        if breakfast in breakfast_recipes:
            p = breakfast_recipes[breakfast].get("protein")
            if p == "fish":
                proteins["fish"].append(f"{breakfast} breakfast")
            elif p:
                proteins[p].append(f"{breakfast} breakfast")

        # Check lunches
        for day, meal in data.get("lunches", []):
            if meal in lunch_recipes:
                p = lunch_recipes[meal].get("protein")
                if p == "fish":
                    proteins["fish"].append(f"{meal}")
                elif p:
                    proteins[p].append(f"{meal}")

        # Check dinners
        for day, meal in data.get("dinners", []):
            if meal == "Sunday Roast":
                roast = data.get("roast")
                if roast == "Roast Beef":
                    proteins["beef"].append("Roast Beef joint (1.5kg)")
                elif roast == "Roast Chicken":
                    proteins["chicken"].append("Whole chicken (1.8kg)")
                elif roast == "Roast Pork":
                    proteins["pork"].append("Pork shoulder (2kg)")
                elif roast == "Roast Lamb":
                    proteins["lamb"].append("Leg of lamb (2kg)")
            elif meal in dinner_recipes:
                p = dinner_recipes[meal].get("protein")
                if p == "fish":
                    proteins["fish"].append(f"{meal}")
                elif p:
                    proteins[p].append(f"{meal}")

    return proteins

def consolidate_meat_list(proteins):
    """Convert meal list to actual shopping quantities"""
    shopping = {
        "beef": [],
        "chicken": [],
        "pork": [],
        "lamb": [],
        "fish": [],
    }

    # Count occurrences of mince vs steak etc
    beef_mince_count = sum(1 for m in proteins["beef"] if any(x in m for x in ["Bolognese", "Cottage", "Chilli", "Taco", "Burger", "Lasagne", "Meatball"]))
    beef_steak_count = sum(1 for m in proteins["beef"] if any(x in m for x in ["Stroganoff", "Steak", "Fajita", "Stir-fry"]))
    beef_stew_count = sum(1 for m in proteins["beef"] if "Stew" in m)
    beef_roast_count = sum(1 for m in proteins["beef"] if "joint" in m)

    if beef_mince_count > 0:
        shopping["beef"].append(f"Beef mince ({beef_mince_count * 500}g)")
    if beef_steak_count > 0:
        shopping["beef"].append(f"Beef steak/sirloin ({beef_steak_count * 500}g)")
    if beef_stew_count > 0:
        shopping["beef"].append(f"Stewing beef ({beef_stew_count * 500}g)")
    if beef_roast_count > 0:
        shopping["beef"].append("Beef roasting joint (1.5kg)")

    # Chicken
    chicken_breast_count = sum(1 for m in proteins["chicken"] if any(x in m for x in ["Tikka", "Fajita", "Korma", "Katsu", "Stir-fry", "Pie", "Honey", "Lemon", "Goujons", "Caesar", "Coronation"]))
    chicken_thigh_count = sum(1 for m in proteins["chicken"] if any(x in m for x in ["Thai", "Cacciatore", "Noodle"]))
    chicken_whole_count = sum(1 for m in proteins["chicken"] if "Whole" in m or "1.8kg" in m)

    if chicken_breast_count > 0:
        shopping["chicken"].append(f"Chicken breasts ({chicken_breast_count * 2})")
    if chicken_thigh_count > 0:
        shopping["chicken"].append(f"Chicken thighs ({chicken_thigh_count * 500}g)")
    if chicken_whole_count > 0:
        shopping["chicken"].append("Whole chicken (1.8kg)")

    # Pork
    sausage_count = sum(1 for m in proteins["pork"] if any(x in m for x in ["Sausage", "Toad", "Full English"]))
    bacon_count = sum(1 for m in proteins["pork"] if any(x in m for x in ["Bacon", "BLT", "Chowder", "Full English"]))
    ham_count = sum(1 for m in proteins["pork"] if any(x in m for x in ["Ham", "Benedict", "Croque", "Ploughman", "Croissant"]))
    pork_chop_count = sum(1 for m in proteins["pork"] if "Chop" in m)
    pork_mince_count = sum(1 for m in proteins["pork"] if "Meatball" in m)
    pork_tender_count = sum(1 for m in proteins["pork"] if any(x in m for x in ["Stir-fry", "Sweet"]))
    gammon_count = sum(1 for m in proteins["pork"] if "Gammon" in m)
    pork_shoulder = sum(1 for m in proteins["pork"] if any(x in m for x in ["Pulled", "shoulder", "2kg"]))

    if sausage_count > 0:
        shopping["pork"].append(f"Pork sausages ({sausage_count * 8})")
    if bacon_count > 0:
        shopping["pork"].append(f"Bacon ({bacon_count * 200}g)")
    if ham_count > 0:
        shopping["pork"].append(f"Ham slices ({ham_count * 200}g)")
    if pork_chop_count > 0:
        shopping["pork"].append(f"Pork chops ({pork_chop_count * 4})")
    if pork_mince_count > 0:
        shopping["pork"].append(f"Pork mince ({pork_mince_count * 500}g)")
    if pork_tender_count > 0:
        shopping["pork"].append(f"Pork tenderloin ({pork_tender_count * 400}g)")
    if gammon_count > 0:
        shopping["pork"].append(f"Gammon steaks ({gammon_count * 2})")
    if pork_shoulder > 0:
        shopping["pork"].append("Pork shoulder (2kg)")

    # Lamb
    lamb_mince_count = sum(1 for m in proteins["lamb"] if any(x in m for x in ["Shepherd", "Kofta", "Moussaka"]))
    lamb_chop_count = sum(1 for m in proteins["lamb"] if "Chop" in m)
    lamb_leg_count = sum(1 for m in proteins["lamb"] if any(x in m for x in ["Curry", "leg", "2kg"]))
    lamb_neck_count = sum(1 for m in proteins["lamb"] if "Hotpot" in m)

    if lamb_mince_count > 0:
        shopping["lamb"].append(f"Lamb mince ({lamb_mince_count * 500}g)")
    if lamb_chop_count > 0:
        shopping["lamb"].append(f"Lamb chops ({lamb_chop_count * 8})")
    if lamb_leg_count > 0:
        shopping["lamb"].append("Leg of lamb (2kg)")
    if lamb_neck_count > 0:
        shopping["lamb"].append(f"Lamb neck ({lamb_neck_count * 500}g)")

    # Fish
    cod_count = sum(1 for m in proteins["fish"] if any(x in m for x in ["Chips", "Parsley"]))
    salmon_count = sum(1 for m in proteins["fish"] if any(x in m for x in ["Teriyaki", "Fishcake", "Baked Salmon"]))
    smoked_salmon_count = sum(1 for m in proteins["fish"] if any(x in m for x in ["Smoked", "Royale", "Scrambled"]))
    prawn_count = sum(1 for m in proteins["fish"] if any(x in m for x in ["Prawn", "Pie"]))
    white_fish_count = sum(1 for m in proteins["fish"] if "Taco" in m)
    mixed_fish_count = sum(1 for m in proteins["fish"] if "Pie" in m)
    haddock_count = sum(1 for m in proteins["fish"] if any(x in m for x in ["Haddock", "Kedgeree"]))
    tuna_count = sum(1 for m in proteins["fish"] if any(x in m for x in ["Tuna", "Nicoise"]))
    fish_fingers_count = sum(1 for m in proteins["fish"] if "Finger" in m)
    sardines_count = sum(1 for m in proteins["fish"] if "Sardine" in m)

    if cod_count > 0:
        shopping["fish"].append(f"Cod fillets ({cod_count * 4})")
    if salmon_count > 0:
        shopping["fish"].append(f"Salmon fillets ({salmon_count * 4})")
    if smoked_salmon_count > 0:
        shopping["fish"].append(f"Smoked salmon ({smoked_salmon_count * 100}g)")
    if prawn_count > 0:
        shopping["fish"].append(f"Prawns ({prawn_count * 300}g)")
    if white_fish_count > 0:
        shopping["fish"].append(f"White fish fillets ({white_fish_count * 400}g)")
    if haddock_count > 0:
        shopping["fish"].append(f"Smoked haddock ({haddock_count * 400}g)")
    if tuna_count > 0:
        shopping["fish"].append(f"Tinned tuna ({tuna_count * 2} tins)")
    if fish_fingers_count > 0:
        shopping["fish"].append("Fish fingers (2 packs)")
    if sardines_count > 0:
        shopping["fish"].append(f"Tinned sardines ({sardines_count} tins)")

    return shopping

# ============================================================
# BUILD MEAL SCHEDULE
# ============================================================

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

all_lunches = list(lunch_recipes.keys())
all_dinners = list(dinner_recipes.keys())
all_breakfasts = list(breakfast_recipes.keys())
roast_names = ["Roast Beef", "Roast Chicken", "Roast Pork", "Roast Lamb"]

meat_dinners = [d for d in all_dinners if dinner_recipes[d].get("protein") in ["beef", "chicken", "pork", "lamb"]]
fish_dinners = [d for d in all_dinners if dinner_recipes[d].get("protein") == "fish"]
veg_dinners = [d for d in all_dinners if dinner_recipes[d].get("protein") is None]

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
# WEEKLY AND MONTHLY STAPLES
# ============================================================

weekly_staples = {
    "dairy": [
        ("Whole milk", "4 pints", "£1.50"),
        ("Butter", "250g", "£2.00"),
        ("Cheddar cheese", "400g", "£3.50"),
        ("Eggs (farmshop)", "24", "£6.00"),
    ],
    "bread": [
        ("White sliced loaf", "1", "£1.20"),
        ("Crusty bread/rolls", "1", "£1.50"),
        ("Wraps/tortillas", "8 pack", "£1.50"),
    ],
    "produce": [
        ("Onions", "1kg", "£1.00"),
        ("Garlic", "2 bulbs", "£0.80"),
        ("Potatoes", "2.5kg", "£2.50"),
        ("Carrots", "1kg", "£0.80"),
        ("Bananas", "bunch", "£0.90"),
        ("Seasonal fruit", "varies", "£3.00"),
        ("Seasonal veg", "varies", "£5.00"),
    ],
    "drinks": [
        ("Fizzy drinks", "2x 2L", "£2.00"),
        ("Squash", "1L", "£1.50"),
    ],
    "snacks": [
        ("Crisps", "6 pack", "£2.00"),
        ("Biscuits", "1 pack", "£1.20"),
    ],
}

monthly_staples = {
    "pantry": [
        ("Tinned tomatoes", "8 tins", "£6.40"),
        ("Baked beans", "4 tins", "£2.40"),
        ("Kidney beans", "2 tins", "£1.60"),
        ("Coconut milk", "4 tins", "£4.00"),
        ("Pasta (various)", "2kg", "£3.00"),
        ("Rice", "2kg", "£4.00"),
        ("Noodles", "4 packs", "£4.00"),
        ("Stock cubes", "24", "£2.00"),
        ("Gravy granules", "2", "£3.00"),
    ],
    "frozen": [
        ("Frozen peas", "2kg", "£3.00"),
        ("Oven chips", "1.5kg", "£2.50"),
        ("Fish fingers", "2 packs", "£4.00"),
    ],
    "household": [
        ("Toilet roll", "9 pack", "£5.00"),
        ("Kitchen roll", "4 pack", "£3.00"),
        ("Washing up liquid", "1", "£1.50"),
        ("Bin bags", "1 roll", "£2.00"),
        ("Cleaning products", "as needed", "£5.00"),
    ],
    "toiletries": [
        ("Toothpaste", "2", "£3.00"),
        ("Shampoo/conditioner", "as needed", "£5.00"),
        ("Shower gel/soap", "as needed", "£3.00"),
        ("Deodorant", "2", "£4.00"),
    ],
}

# ============================================================
# HTML GENERATION
# ============================================================

def generate_big_shop_html(week_num):
    """Generate BIG SHOP list - all meat/fish for 4 weeks + monthly items"""
    data = weeks_data[week_num]

    # Determine which 4 weeks this big shop covers
    month_weeks = [week_num, week_num + 1, week_num + 2, week_num + 3]
    month_weeks = [w for w in month_weeks if w <= 52]

    # Get all proteins needed for these 4 weeks
    proteins = get_protein_requirements(month_weeks)
    shopping = consolidate_meat_list(proteins)

    dates = data["dates"]
    month = data["month"]

    categories_html = ""
    total = 0

    # MEAT SECTION
    all_meat = shopping["beef"] + shopping["chicken"] + shopping["pork"] + shopping["lamb"]
    if all_meat:
        rows = ""
        for item in all_meat:
            # Estimate prices
            if "mince" in item.lower():
                price = 4.50 * (int(re.search(r'\d+', item).group()) // 500) if re.search(r'\d+', item) else 4.50
            elif "steak" in item.lower() or "sirloin" in item.lower():
                price = 6.00 * (int(re.search(r'\d+', item).group()) // 500) if re.search(r'\d+', item) else 6.00
            elif "joint" in item.lower() or "shoulder" in item.lower() or "leg" in item.lower():
                price = 15.00
            elif "chicken" in item.lower() and "whole" in item.lower():
                price = 6.00
            elif "breast" in item.lower():
                price = 2.50 * (int(re.search(r'\d+', item).group()) if re.search(r'\d+', item) else 4)
            elif "thigh" in item.lower():
                price = 3.50 * (int(re.search(r'\d+', item).group()) // 500) if re.search(r'\d+', item) else 3.50
            elif "sausage" in item.lower():
                price = 3.00 * (int(re.search(r'\d+', item).group()) // 8) if re.search(r'\d+', item) else 3.00
            elif "bacon" in item.lower():
                price = 3.50 * (int(re.search(r'\d+', item).group()) // 200) if re.search(r'\d+', item) else 3.50
            elif "ham" in item.lower():
                price = 2.50 * (int(re.search(r'\d+', item).group()) // 200) if re.search(r'\d+', item) else 2.50
            elif "chop" in item.lower():
                price = 5.00 * (int(re.search(r'\d+', item).group()) // 4) if re.search(r'\d+', item) else 5.00
            elif "gammon" in item.lower():
                price = 4.00
            else:
                price = 5.00
            total += price
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="price">~£{price:.0f}</td></tr>\n'
        categories_html += f'''
    <div class="category">
        <h3>🥩 MEAT (Month Supply - Freeze)</h3>
        <table>{rows}</table>
    </div>'''

    # FISH SECTION
    if shopping["fish"]:
        rows = ""
        for item in shopping["fish"]:
            if "salmon" in item.lower():
                price = 8.00
            elif "cod" in item.lower():
                price = 7.00
            elif "prawn" in item.lower():
                price = 5.00
            elif "haddock" in item.lower():
                price = 6.00
            elif "tuna" in item.lower():
                price = 2.50
            elif "finger" in item.lower():
                price = 4.00
            else:
                price = 5.00
            total += price
            rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="price">~£{price:.0f}</td></tr>\n'
        categories_html += f'''
    <div class="category">
        <h3>🐟 FISH (Month Supply - Freeze)</h3>
        <table>{rows}</table>
    </div>'''

    # DAIRY & EGGS
    rows = ""
    for item, qty, price in weekly_staples["dairy"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🧀 DAIRY & EGGS</h3>
        <table>{rows}</table>
    </div>'''

    # BREAD
    rows = ""
    for item, qty, price in weekly_staples["bread"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🍞 BREAD & BAKERY</h3>
        <table>{rows}</table>
    </div>'''

    # FRESH PRODUCE
    rows = ""
    for item, qty, price in weekly_staples["produce"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🥬 FRESH PRODUCE</h3>
        <table>{rows}</table>
    </div>'''

    # PANTRY (Monthly)
    rows = ""
    for item, qty, price in monthly_staples["pantry"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🏪 PANTRY STAPLES (Monthly)</h3>
        <table>{rows}</table>
    </div>'''

    # FROZEN (Monthly)
    rows = ""
    for item, qty, price in monthly_staples["frozen"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>❄️ FROZEN (Monthly)</h3>
        <table>{rows}</table>
    </div>'''

    # DRINKS
    rows = ""
    for item, qty, price in weekly_staples["drinks"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🥤 DRINKS</h3>
        <table>{rows}</table>
    </div>'''

    # SNACKS
    rows = ""
    for item, qty, price in weekly_staples["snacks"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🍪 SNACKS</h3>
        <table>{rows}</table>
    </div>'''

    # HOUSEHOLD (Monthly)
    rows = ""
    for item, qty, price in monthly_staples["household"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🧹 HOUSEHOLD (Monthly)</h3>
        <table>{rows}</table>
    </div>'''

    # TOILETRIES (Monthly)
    rows = ""
    for item, qty, price in monthly_staples["toiletries"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🧴 TOILETRIES (Monthly)</h3>
        <table>{rows}</table>
    </div>'''

    recipe_url = f"{BASE_URL}/week-{week_num:02d}.html"
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=120x120&data={recipe_url}"

    budget = f"~£{int(round(total / 10) * 10)}"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Week {week_num} Shopping List - BIG SHOP</title>
    <style>
        @page {{ size: A4; margin: 8mm; }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: Arial, sans-serif; font-size: 10px; line-height: 1.2; padding: 8px; }}
        .header {{ display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 3px solid #c62828; padding-bottom: 8px; margin-bottom: 8px; }}
        .header-left h1 {{ font-size: 16px; color: #c62828; margin-bottom: 2px; }}
        .header-left .dates {{ color: #666; font-size: 11px; }}
        .header-left .shop-type {{ background: #c62828; color: white; padding: 2px 8px; border-radius: 3px; font-size: 10px; font-weight: bold; display: inline-block; margin-top: 4px; }}
        .header-left .note {{ font-size: 9px; color: #666; margin-top: 4px; font-style: italic; }}
        .qr-section {{ text-align: center; }}
        .qr-section img {{ width: 70px; height: 70px; }}
        .qr-section p {{ font-size: 8px; color: #666; margin-top: 2px; }}
        .content {{ display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }}
        .category {{ break-inside: avoid; margin-bottom: 6px; }}
        .category h3 {{ background: #ffebee; padding: 3px 6px; font-size: 10px; color: #c62828; margin-bottom: 2px; }}
        table {{ width: 100%; border-collapse: collapse; }}
        td {{ padding: 1px 3px; border-bottom: 1px solid #eee; font-size: 9px; }}
        .checkbox {{ width: 16px; text-align: center; }}
        .qty {{ width: 50px; color: #666; text-align: right; }}
        .price {{ width: 40px; text-align: right; color: #c62828; font-weight: bold; }}
        .budget {{ text-align: right; margin-top: 8px; padding-top: 5px; border-top: 2px solid #c62828; font-size: 14px; font-weight: bold; color: #c62828; }}
        @media print {{ body {{ padding: 0; }} }}
    </style>
</head>
<body>
    <div class="header">
        <div class="header-left">
            <h1>Week {week_num} - {month}</h1>
            <div class="dates">{dates}</div>
            <div class="shop-type">BIG SHOP - Monthly Bulk Buy</div>
            <div class="note">Meat & fish for weeks {week_num}-{min(week_num+3, 52)} - portion and freeze</div>
        </div>
        <div class="qr-section">
            <img src="{qr_url}" alt="QR Code">
            <p>Scan for recipes</p>
        </div>
    </div>
    <div class="content">{categories_html}</div>
    <div class="budget">Estimated Budget: {budget}</div>
</body>
</html>'''
    return html


def generate_topup_shop_html(week_num):
    """Generate TOP-UP SHOP list - fresh produce, dairy, bread only"""
    data = weeks_data[week_num]
    dates = data["dates"]
    month = data["month"]

    categories_html = ""
    total = 0

    # DAIRY & EGGS
    rows = ""
    for item, qty, price in weekly_staples["dairy"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🧀 DAIRY & EGGS</h3>
        <table>{rows}</table>
    </div>'''

    # BREAD
    rows = ""
    for item, qty, price in weekly_staples["bread"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🍞 BREAD & BAKERY</h3>
        <table>{rows}</table>
    </div>'''

    # FRESH PRODUCE
    rows = ""
    for item, qty, price in weekly_staples["produce"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🥬 FRESH PRODUCE</h3>
        <table>{rows}</table>
    </div>'''

    # DRINKS
    rows = ""
    for item, qty, price in weekly_staples["drinks"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🥤 DRINKS</h3>
        <table>{rows}</table>
    </div>'''

    # SNACKS
    rows = ""
    for item, qty, price in weekly_staples["snacks"]:
        total += float(price.replace("£", ""))
        rows += f'<tr><td class="checkbox">&#9744;</td><td>{item}</td><td class="qty">{qty}</td><td class="price">{price}</td></tr>\n'
    categories_html += f'''
    <div class="category">
        <h3>🍪 SNACKS</h3>
        <table>{rows}</table>
    </div>'''

    recipe_url = f"{BASE_URL}/week-{week_num:02d}.html"
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=120x120&data={recipe_url}"

    budget = f"~£{int(round(total / 5) * 5)}"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Week {week_num} Shopping List - Top-up</title>
    <style>
        @page {{ size: A4; margin: 10mm; }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: Arial, sans-serif; font-size: 11px; line-height: 1.3; padding: 10px; }}
        .header {{ display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 3px solid #2c5530; padding-bottom: 10px; margin-bottom: 10px; }}
        .header-left h1 {{ font-size: 18px; color: #2c5530; margin-bottom: 3px; }}
        .header-left .dates {{ color: #666; font-size: 12px; }}
        .header-left .shop-type {{ background: #2c5530; color: white; padding: 3px 8px; border-radius: 3px; font-size: 10px; display: inline-block; margin-top: 5px; }}
        .header-left .note {{ font-size: 9px; color: #666; margin-top: 4px; font-style: italic; }}
        .qr-section {{ text-align: center; }}
        .qr-section img {{ width: 80px; height: 80px; }}
        .qr-section p {{ font-size: 9px; color: #666; margin-top: 3px; }}
        .content {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
        .category {{ break-inside: avoid; margin-bottom: 10px; }}
        .category h3 {{ background: #e8f5e9; padding: 4px 8px; font-size: 11px; color: #2c5530; margin-bottom: 3px; }}
        table {{ width: 100%; border-collapse: collapse; }}
        td {{ padding: 3px 4px; border-bottom: 1px solid #eee; font-size: 10px; }}
        .checkbox {{ width: 20px; text-align: center; }}
        .qty {{ width: 50px; color: #666; text-align: right; }}
        .price {{ width: 45px; text-align: right; color: #2c5530; font-weight: bold; }}
        .budget {{ text-align: right; margin-top: 10px; padding-top: 5px; border-top: 2px solid #2c5530; font-size: 14px; font-weight: bold; color: #2c5530; }}
        @media print {{ body {{ padding: 0; }} }}
    </style>
</head>
<body>
    <div class="header">
        <div class="header-left">
            <h1>Week {week_num} - {month}</h1>
            <div class="dates">{dates}</div>
            <div class="shop-type">Top-up Shop</div>
            <div class="note">Fresh items only - meat & fish from freezer</div>
        </div>
        <div class="qr-section">
            <img src="{qr_url}" alt="QR Code">
            <p>Scan for recipes</p>
        </div>
    </div>
    <div class="content">{categories_html}</div>
    <div class="budget">Estimated Budget: {budget}</div>
</body>
</html>'''
    return html


# ============================================================
# GENERATE ALL SHOPPING LISTS
# ============================================================

print("Generating shopping lists...")
print("BIG SHOP = Weeks 1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49")
print("TOP-UP = All other weeks")
print("=" * 60)

for week_num in range(1, 53):
    is_big_shop = (week_num - 1) % 4 == 0

    if is_big_shop:
        html = generate_big_shop_html(week_num)
        shop_type = "BIG SHOP"
    else:
        html = generate_topup_shop_html(week_num)
        shop_type = "Top-up"

    filename = os.path.join(output_dir, f"shopping-week-{week_num:02d}.html")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Week {week_num:02d}: {shop_type}")

print("=" * 60)
print("Done! Shopping lists match the monthly shopping structure.")
print(f"Files in: {output_dir}")
