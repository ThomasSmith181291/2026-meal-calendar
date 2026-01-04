"""
Generate mobile-friendly shopping lists with interactive checkboxes
BIG SHOP (weeks 1, 5, 9, etc.) = All meat/fish for 4 weeks + monthly items + weekly fresh
TOP-UP (weeks 2,3,4, etc.) = Weekly fresh only (dairy, bread, produce)
"""

import os
import datetime
import random

random.seed(2026)

output_dir = r"C:\Users\Little Nineveh\2026-meal-calendar\printable"
os.makedirs(output_dir, exist_ok=True)

BASE_URL = "https://thomassmith181291.github.io/2026-meal-calendar"

# ============================================================
# RECIPE DATABASE (protein tracking for meat/fish consolidation)
# ============================================================

lunch_recipes = {
    "Leek & potato soup": {"protein": None},
    "Tomato soup": {"protein": None},
    "Carrot & coriander soup": {"protein": None},
    "Butternut squash soup": {"protein": None},
    "Chicken noodle soup": {"protein": "chicken"},
    "Pea & mint soup": {"protein": None},
    "French onion soup": {"protein": None},
    "Minestrone": {"protein": None},
    "Broccoli & stilton soup": {"protein": None},
    "Sweetcorn chowder": {"protein": "pork"},
    "Roasted red pepper soup": {"protein": None},
    "Mushroom soup": {"protein": None},
    "Ham & cheese toastie": {"protein": "pork"},
    "BLT sandwich": {"protein": "pork"},
    "Tuna melt": {"protein": "fish"},
    "Club sandwich": {"protein": "chicken"},
    "Croque monsieur": {"protein": "pork"},
    "Coronation chicken sandwich": {"protein": "chicken"},
    "Egg mayo sandwich": {"protein": None},
    "Cheese & pickle sandwich": {"protein": None},
    "Welsh rarebit": {"protein": None},
    "Prawn mayo sandwich": {"protein": "fish"},
    "Smoked salmon bagel": {"protein": "fish"},
    "Chicken Caesar wrap": {"protein": "chicken"},
    "Ham salad wrap": {"protein": "pork"},
    "Hummus & veg wrap": {"protein": None},
    "Cheese toastie": {"protein": None},
    "Cheese omelette": {"protein": None},
    "Jacket potato with beans": {"protein": None},
    "Jacket potato with tuna mayo": {"protein": "fish"},
    "Jacket potato with cheese & coleslaw": {"protein": None},
    "Beans on toast": {"protein": None},
    "Cheese on toast": {"protein": None},
    "Sardines on toast": {"protein": "fish"},
    "Egg fried rice": {"protein": None},
    "Quesadilla": {"protein": None},
    "Avocado on toast": {"protein": None},
    "Greek salad": {"protein": None},
    "Caesar salad": {"protein": "chicken"},
    "Nicoise salad": {"protein": "fish"},
    "Ploughman's lunch": {"protein": "pork"},
    "Leftover roast sandwich": {"protein": None},
}

dinner_recipes = {
    "Spaghetti Bolognese": {"protein": "beef"},
    "Cottage Pie": {"protein": "beef"},
    "Beef Stroganoff": {"protein": "beef"},
    "Chilli Con Carne": {"protein": "beef"},
    "Beef Stew": {"protein": "beef"},
    "Beef Tacos": {"protein": "beef"},
    "Beef Burgers": {"protein": "beef"},
    "Steak & Chips": {"protein": "beef"},
    "Beef Fajitas": {"protein": "beef"},
    "Lasagne": {"protein": "beef"},
    "Meatballs in Tomato Sauce": {"protein": "beef"},
    "Beef & Broccoli Stir-fry": {"protein": "beef"},
    "Chicken Tikka Masala": {"protein": "chicken"},
    "Chicken Fajitas": {"protein": "chicken"},
    "Chicken Korma": {"protein": "chicken"},
    "Chicken Katsu Curry": {"protein": "chicken"},
    "Thai Green Curry": {"protein": "chicken"},
    "Chicken Stir-fry": {"protein": "chicken"},
    "Chicken Pie": {"protein": "chicken"},
    "Honey Mustard Chicken": {"protein": "chicken"},
    "Chicken Cacciatore": {"protein": "chicken"},
    "Lemon Herb Chicken": {"protein": "chicken"},
    "Chicken Goujons": {"protein": "chicken"},
    "Chicken Noodle Stir-fry": {"protein": "chicken"},
    "Sausage Casserole": {"protein": "pork"},
    "Pork Chops with Apple": {"protein": "pork"},
    "Pulled Pork": {"protein": "pork"},
    "Pork Stir-fry": {"protein": "pork"},
    "Gammon, Egg & Chips": {"protein": "pork"},
    "Toad in the Hole": {"protein": "pork"},
    "Pork Meatballs": {"protein": "pork"},
    "Sweet & Sour Pork": {"protein": "pork"},
    "Shepherd's Pie": {"protein": "lamb"},
    "Lamb Koftas": {"protein": "lamb"},
    "Lamb Chops with Mint": {"protein": "lamb"},
    "Lamb Curry": {"protein": "lamb"},
    "Moussaka": {"protein": "lamb"},
    "Lamb Hotpot": {"protein": "lamb"},
    "Fish & Chips": {"protein": "fish"},
    "Fish Pie": {"protein": "fish"},
    "Fish Tacos": {"protein": "fish"},
    "Salmon Teriyaki": {"protein": "fish"},
    "Prawn Stir-fry": {"protein": "fish"},
    "Salmon Fishcakes": {"protein": "fish"},
    "Prawn Curry": {"protein": "fish"},
    "Cod with Parsley Sauce": {"protein": "fish"},
    "Fish Finger Sandwiches": {"protein": "fish"},
    "Tuna Pasta Bake": {"protein": "fish"},
    "Smoked Haddock Risotto": {"protein": "fish"},
    "Baked Salmon with Lemon": {"protein": "fish"},
    "Cauliflower Cheese": {"protein": None},
    "Mushroom Risotto": {"protein": None},
    "Vegetable Curry": {"protein": None},
    "Macaroni Cheese": {"protein": None},
    "Vegetable Stir-fry": {"protein": None},
    "Vegetable Lasagne": {"protein": None},
    "Cheese & Onion Pie": {"protein": None},
    "Spinach & Ricotta Cannelloni": {"protein": None},
    "Stuffed Peppers": {"protein": None},
    "Vegetable Fajitas": {"protein": None},
}

breakfast_recipes = {
    "Full English": {"protein": "pork"},
    "Eggs Benedict": {"protein": "pork"},
    "Eggs Florentine": {"protein": None},
    "Eggs Royale": {"protein": "fish"},
    "Pancakes": {"protein": None},
    "American Pancakes": {"protein": None},
    "French Toast": {"protein": None},
    "Shakshuka": {"protein": None},
    "Avocado on Toast": {"protein": None},
    "Scrambled Eggs & Smoked Salmon": {"protein": "fish"},
    "Omelette": {"protein": None},
    "Bacon & Egg Muffin": {"protein": "pork"},
    "Kedgeree": {"protein": "fish"},
    "Porridge with Berries": {"protein": None},
    "Croissants with Ham & Cheese": {"protein": "pork"},
}

roast_recipes = {
    "Roast Beef": {"protein": "beef"},
    "Roast Chicken": {"protein": "chicken"},
    "Roast Pork": {"protein": "pork"},
    "Roast Lamb": {"protein": "lamb"},
}

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
roast_idx = 0  # Track roast rotation separately

for week_num in range(1, 53):
    if week_num == 1:
        week_start = datetime.date(2026, 1, 1)
        week_end = datetime.date(2026, 1, 4)
        week_days = ["Thu", "Fri", "Sat", "Sun"]
    else:
        week_start = datetime.date(2026, 1, 5) + datetime.timedelta(weeks=week_num-2)
        week_end = week_start + datetime.timedelta(days=6)
        week_days = days

    has_roast = (week_num % 2 == 1)  # Odd weeks have roast
    if has_roast:
        roast_name = roast_names[roast_idx % 4]  # Cycle: Beef, Chicken, Pork, Lamb
        roast_idx += 1
    else:
        roast_name = None

    lunches = []
    for d in week_days:
        lunches.append((d, all_lunches[lunch_idx % len(all_lunches)]))
        lunch_idx += 1

    dinners = []
    # Pattern: Mon=meat, Tue=fish, Wed=veg, Thu=meat, Fri=fish, Sat=meat, Sun=special
    dinner_pattern = ["meat", "fish", "veg", "meat", "fish", "meat", "special"]

    for i, d in enumerate(week_days):
        if d == "Sun":
            if has_roast:
                # Roast for 7 on odd weeks
                dinners.append((d, "Sunday Roast"))
            else:
                # Regular Sunday dinner for 3 on even weeks (alternate meat/fish)
                if week_num % 4 == 0:
                    dinners.append((d, fish_dinners[fish_idx % len(fish_dinners)]))
                    fish_idx += 1
                else:
                    dinners.append((d, meat_dinners[meat_idx % len(meat_dinners)]))
                    meat_idx += 1
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
        "start": week_start,
        "end": week_end,
        "dates": f"{week_start.strftime('%d %b')} - {week_end.strftime('%d %b %Y')}",
        "month": week_start.strftime("%B"),
        "breakfast": all_breakfasts[breakfast_idx % len(all_breakfasts)],
        "roast": roast_name,
        "lunches": lunches,
        "dinners": dinners,
    }
    breakfast_idx += 1

# ============================================================
# PROTEIN CONSOLIDATION FOR 4 WEEKS
# ============================================================

def get_protein_requirements(week_nums):
    """Get all protein requirements for a set of weeks"""
    proteins = {"beef": [], "chicken": [], "pork": [], "lamb": [], "fish": []}

    for week_num in week_nums:
        data = weeks_data.get(week_num, {})

        breakfast = data.get("breakfast", "")
        if breakfast in breakfast_recipes:
            p = breakfast_recipes[breakfast].get("protein")
            if p == "fish":
                proteins["fish"].append(f"{breakfast}")
            elif p:
                proteins[p].append(f"{breakfast}")

        for day, meal in data.get("lunches", []):
            if meal in lunch_recipes:
                p = lunch_recipes[meal].get("protein")
                if p == "fish":
                    proteins["fish"].append(f"{meal}")
                elif p:
                    proteins[p].append(f"{meal}")

        for day, meal in data.get("dinners", []):
            if meal == "Sunday Roast":
                roast = data.get("roast")
                if roast == "Roast Beef":
                    proteins["beef"].append("Roast joint")
                elif roast == "Roast Chicken":
                    proteins["chicken"].append("Whole chicken")
                elif roast == "Roast Pork":
                    proteins["pork"].append("Pork shoulder")
                elif roast == "Roast Lamb":
                    proteins["lamb"].append("Leg of lamb")
            elif meal in dinner_recipes:
                p = dinner_recipes[meal].get("protein")
                if p == "fish":
                    proteins["fish"].append(f"{meal}")
                elif p:
                    proteins[p].append(f"{meal}")

    return proteins

def consolidate_meat_list(proteins):
    """Convert meal list to shopping quantities"""
    shopping = {"beef": [], "chicken": [], "pork": [], "lamb": [], "fish": []}

    # Beef
    beef_mince = sum(1 for m in proteins["beef"] if any(x in m for x in ["Bolognese", "Cottage", "Chilli", "Taco", "Burger", "Lasagne", "Meatball"]))
    beef_steak = sum(1 for m in proteins["beef"] if any(x in m for x in ["Stroganoff", "Steak", "Fajita", "Stir-fry"]))
    beef_stew = sum(1 for m in proteins["beef"] if "Stew" in m)
    beef_roast = sum(1 for m in proteins["beef"] if "joint" in m.lower())

    if beef_mince > 0: shopping["beef"].append(f"Beef mince ({beef_mince * 500}g)")
    if beef_steak > 0: shopping["beef"].append(f"Beef steak ({beef_steak * 500}g)")
    if beef_stew > 0: shopping["beef"].append(f"Stewing beef ({beef_stew * 500}g)")
    if beef_roast > 0: shopping["beef"].append("Beef roasting joint (1.5kg)")

    # Chicken
    chicken_breast = sum(1 for m in proteins["chicken"] if any(x in m for x in ["Tikka", "Fajita", "Korma", "Katsu", "Stir-fry", "Pie", "Honey", "Lemon", "Goujons", "Caesar", "Coronation", "Club"]))
    chicken_thigh = sum(1 for m in proteins["chicken"] if any(x in m for x in ["Thai", "Cacciatore", "Noodle"]))
    chicken_whole = sum(1 for m in proteins["chicken"] if "Whole" in m)

    if chicken_breast > 0: shopping["chicken"].append(f"Chicken breasts ({chicken_breast * 2})")
    if chicken_thigh > 0: shopping["chicken"].append(f"Chicken thighs ({chicken_thigh * 500}g)")
    if chicken_whole > 0: shopping["chicken"].append("Whole chicken (1.8kg)")

    # Pork
    sausage = sum(1 for m in proteins["pork"] if any(x in m for x in ["Sausage", "Toad", "Full English"]))
    bacon = sum(1 for m in proteins["pork"] if any(x in m for x in ["Bacon", "BLT", "Chowder", "Full English"]))
    ham = sum(1 for m in proteins["pork"] if any(x in m for x in ["Ham", "Benedict", "Croque", "Ploughman", "Croissant"]))
    pork_chop = sum(1 for m in proteins["pork"] if "Chop" in m)
    pork_mince = sum(1 for m in proteins["pork"] if "Meatball" in m)
    pork_tender = sum(1 for m in proteins["pork"] if any(x in m for x in ["Stir-fry", "Sweet"]))
    gammon = sum(1 for m in proteins["pork"] if "Gammon" in m)
    pork_shoulder = sum(1 for m in proteins["pork"] if "shoulder" in m.lower())

    if sausage > 0: shopping["pork"].append(f"Pork sausages ({sausage * 8})")
    if bacon > 0: shopping["pork"].append(f"Bacon ({bacon * 200}g)")
    if ham > 0: shopping["pork"].append(f"Ham ({ham * 150}g)")
    if pork_chop > 0: shopping["pork"].append(f"Pork chops ({pork_chop * 4})")
    if pork_mince > 0: shopping["pork"].append(f"Pork mince ({pork_mince * 500}g)")
    if pork_tender > 0: shopping["pork"].append(f"Pork tenderloin ({pork_tender * 400}g)")
    if gammon > 0: shopping["pork"].append(f"Gammon steaks ({gammon * 2})")
    if pork_shoulder > 0: shopping["pork"].append("Pork shoulder (2kg)")

    # Lamb
    lamb_mince = sum(1 for m in proteins["lamb"] if any(x in m for x in ["Shepherd", "Kofta", "Moussaka"]))
    lamb_chop = sum(1 for m in proteins["lamb"] if "Chop" in m)
    lamb_leg = sum(1 for m in proteins["lamb"] if any(x in m for x in ["Curry", "leg", "Leg"]))
    lamb_neck = sum(1 for m in proteins["lamb"] if "Hotpot" in m)

    if lamb_mince > 0: shopping["lamb"].append(f"Lamb mince ({lamb_mince * 500}g)")
    if lamb_chop > 0: shopping["lamb"].append(f"Lamb chops ({lamb_chop * 8})")
    if lamb_leg > 0: shopping["lamb"].append("Leg of lamb (2kg)")
    if lamb_neck > 0: shopping["lamb"].append(f"Lamb neck ({lamb_neck * 500}g)")

    # Fish
    cod = sum(1 for m in proteins["fish"] if any(x in m for x in ["Chips", "Parsley"]))
    salmon = sum(1 for m in proteins["fish"] if any(x in m for x in ["Teriyaki", "Fishcake", "Baked Salmon"]))
    smoked_salmon = sum(1 for m in proteins["fish"] if any(x in m for x in ["Smoked salmon", "Royale", "Scrambled"]))
    prawn = sum(1 for m in proteins["fish"] if any(x in m for x in ["Prawn", "Fish Pie"]))
    white_fish = sum(1 for m in proteins["fish"] if "Taco" in m)
    haddock = sum(1 for m in proteins["fish"] if any(x in m for x in ["Haddock", "Kedgeree"]))
    tuna = sum(1 for m in proteins["fish"] if any(x in m for x in ["Tuna", "Nicoise"]))
    fish_fingers = sum(1 for m in proteins["fish"] if "Finger" in m)
    sardines = sum(1 for m in proteins["fish"] if "Sardine" in m)

    if cod > 0: shopping["fish"].append(f"Cod fillets ({cod * 4})")
    if salmon > 0: shopping["fish"].append(f"Salmon fillets ({salmon * 4})")
    if smoked_salmon > 0: shopping["fish"].append(f"Smoked salmon ({smoked_salmon * 100}g)")
    if prawn > 0: shopping["fish"].append(f"Prawns ({prawn * 300}g)")
    if white_fish > 0: shopping["fish"].append(f"White fish ({white_fish * 400}g)")
    if haddock > 0: shopping["fish"].append(f"Smoked haddock ({haddock * 300}g)")
    if tuna > 0: shopping["fish"].append(f"Tinned tuna ({tuna * 2} tins)")
    if fish_fingers > 0: shopping["fish"].append("Fish fingers (2 packs)")
    if sardines > 0: shopping["fish"].append(f"Tinned sardines ({sardines} tins)")

    return shopping

def get_weekly_breakdown(week_nums):
    """Get protein breakdown by week for portioning guide, ordered by day"""
    weekly_breakdown = {}
    day_order = {"Mon": 1, "Tue": 2, "Wed": 3, "Thu": 4, "Fri": 5, "Sat": 6, "Sun": 7}

    for week_num in week_nums:
        data = weeks_data.get(week_num, {})
        if not data:
            continue

        # Collect all meals with their day and sort order
        meals_list = []

        # Weekend breakfast (shown at start)
        breakfast = data.get("breakfast", "")
        if breakfast in breakfast_recipes:
            p = breakfast_recipes[breakfast].get("protein")
            if p:
                portion = get_breakfast_portion(breakfast)
                meals_list.append((0, f"Weekend Breakfast: {breakfast} ({portion})", p))

        # Lunches
        for day, meal in data.get("lunches", []):
            if meal in lunch_recipes:
                p = lunch_recipes[meal].get("protein")
                if p:
                    portion = get_lunch_portion(meal)
                    sort_key = day_order.get(day, 8) * 10 + 1  # lunch = .1
                    meals_list.append((sort_key, f"{day} Lunch: {meal} ({portion})", p))

        # Dinners
        for day, meal in data.get("dinners", []):
            sort_key = day_order.get(day, 8) * 10 + 2  # dinner = .2
            if meal == "Sunday Roast":
                roast = data.get("roast")
                if roast == "Roast Beef":
                    meals_list.append((sort_key, "Sun Dinner: Roast Beef (1.5kg joint, for 7)", "beef"))
                elif roast == "Roast Chicken":
                    meals_list.append((sort_key, "Sun Dinner: Roast Chicken (whole, for 7)", "chicken"))
                elif roast == "Roast Pork":
                    meals_list.append((sort_key, "Sun Dinner: Roast Pork (2kg shoulder, for 7)", "pork"))
                elif roast == "Roast Lamb":
                    meals_list.append((sort_key, "Sun Dinner: Roast Lamb (2kg leg, for 7)", "lamb"))
            elif meal in dinner_recipes:
                p = dinner_recipes[meal].get("protein")
                if p:
                    portion = get_portion_size(meal)
                    meals_list.append((sort_key, f"{day} Dinner: {meal} ({portion})", p))

        # Sort by day order
        meals_list.sort(key=lambda x: x[0])

        # Build ordered list
        ordered_items = [item[1] for item in meals_list]
        weekly_breakdown[week_num] = ordered_items

    return weekly_breakdown

def get_breakfast_portion(meal):
    """Get portion info for breakfast items"""
    if "Full English" in meal:
        return "sausages + bacon"
    elif "Benedict" in meal or "Muffin" in meal:
        return "bacon/ham"
    elif "Royale" in meal or "Salmon" in meal:
        return "smoked salmon"
    elif "Kedgeree" in meal:
        return "smoked haddock"
    elif "Croissant" in meal:
        return "ham"
    else:
        return "1 portion"

def get_lunch_portion(meal):
    """Get portion info for lunch items"""
    meal_lower = meal.lower()
    if any(x in meal_lower for x in ["chicken noodle", "club", "coronation", "caesar"]):
        return "chicken"
    elif any(x in meal_lower for x in ["ham", "blt", "croque", "ploughman", "chowder"]):
        return "ham/bacon"
    elif any(x in meal_lower for x in ["tuna", "prawn", "salmon", "sardine", "nicoise"]):
        return "fish"
    else:
        return "1 portion"

def get_portion_size(meal):
    """Get standard portion size for a meal"""
    # Fish dishes - check first to avoid chicken curry matching
    if any(x in meal for x in ["Fish & Chips", "Cod", "Parsley"]):
        return "4 cod fillets"
    elif any(x in meal for x in ["Salmon", "Teriyaki", "Fishcake"]):
        return "4 salmon fillets"
    elif any(x in meal for x in ["Prawn"]):
        return "300g prawns"
    elif "Fish Pie" in meal:
        return "mixed fish 400g"
    elif "Fish Taco" in meal:
        return "400g white fish"
    elif "Tuna" in meal:
        return "2 tins tuna"
    elif "Haddock" in meal:
        return "300g haddock"
    # Mince dishes
    elif any(x in meal for x in ["Bolognese", "Cottage", "Chilli", "Lasagne", "Meatball", "Shepherd", "Moussaka"]):
        return "500g mince"
    elif any(x in meal for x in ["Taco", "Burger", "Kofta"]):
        return "500g mince"
    # Steak/stewing
    elif any(x in meal for x in ["Stroganoff", "Steak", "Stew"]):
        return "500g steak/stewing"
    # Strips/stir-fry
    elif any(x in meal for x in ["Fajita", "Stir-fry"]):
        return "400g strips"
    # Chicken dishes
    elif any(x in meal for x in ["Tikka", "Korma", "Katsu", "Thai", "Curry", "Cacciatore", "Honey", "Lemon", "Goujons"]):
        return "4 breasts/500g"
    elif any(x in meal for x in ["Pie"]) and "Fish" not in meal:
        return "400g diced"
    # Pork
    elif "Sausage" in meal or "Toad" in meal:
        return "8 sausages"
    elif any(x in meal for x in ["Chop"]):
        return "4 chops"
    elif "Gammon" in meal:
        return "2 steaks"
    elif any(x in meal for x in ["Pulled", "Sweet", "Pork Stir"]):
        return "400g"
    else:
        return "1 portion"

# ============================================================
# SHOPPING LIST ITEMS
# ============================================================

# ============================================================
# WEEKLY FRESH ITEMS (every week)
# ============================================================
weekly_fresh = {
    "dairy": [
        ("Whole milk", "4 pints"),
        ("Plant milk (oat/almond)", "1L"),
        ("Butter", "250g"),
        ("Cheddar cheese", "400g"),
        ("Cream cheese", "200g"),
        ("Eggs (farmshop)", "24"),
    ],
    "bread": [
        ("White sliced loaf", "1"),
        ("Fresh bakery loaf", "1"),
        ("Bread rolls/baps", "6"),
        ("Wraps/tortillas", "8 pack"),
        ("Crumpets or muffins", "6 pack"),
        ("Croissants/pastries", "4"),
        ("Porridge oats", "1kg"),
    ],
    "produce": [
        ("Onions", "1kg"),
        ("Garlic", "2 bulbs"),
        ("Potatoes", "2.5kg"),
        ("Carrots", "1kg"),
        ("Bananas", "bunch"),
        ("Apples", "6"),
        ("Fresh herbs", "as needed"),
        ("Seasonal fruit", "as needed"),
        ("Seasonal veg", "as needed"),
    ],
    "drinks": [
        ("Fizzy drinks", "2x 2L"),
        ("Squash", "1L"),
    ],
    "snacks": [
        ("Crisps", "multipack"),
        ("Biscuits", "1 pack"),
    ],
}

# Fortnightly items (add to odd-numbered weeks within each month)
fortnightly_items = {
    "dairy": [
        ("Greek yogurt", "500g"),
        ("Feta cheese", "200g"),
    ],
    "drinks": [
        ("Tea bags", "80 pack"),
        ("Coffee", "200g"),
    ],
    "snacks": [
        ("Crackers", "1 pack"),
    ],
}

# ============================================================
# MONTHLY ITEMS (BIG SHOP only)
# ============================================================
monthly_items = {
    "pantry": [
        ("Tinned tomatoes", "4 tins"),
        ("Baked beans", "4 tins"),
        ("Kidney beans", "2 tins"),
        ("Chickpeas", "2 tins"),
        ("Coconut milk", "2 tins"),
        ("Pasta (various)", "2kg"),
        ("Rice", "2kg"),
        ("Noodles", "4 packs"),
        ("Plain flour", "1.5kg"),
        ("Sugar", "1kg"),
        ("Stock cubes", "24"),
        ("Gravy granules", "2"),
        ("Pesto", "190g jar"),
    ],
    "condiments": [
        ("Ketchup", "as needed"),
        ("Hot sauce", "as needed"),
        ("Olive oil", "as needed"),
        ("Vegetable oil", "as needed"),
        ("Balsamic vinegar", "as needed"),
        ("Honey", "as needed"),
    ],
    "spices": [
        ("Mixed herbs", "as needed"),
        ("Paprika", "as needed"),
        ("Cumin", "as needed"),
        ("Curry powder", "as needed"),
    ],
    "frozen": [
        ("Frozen peas", "2kg"),
        ("Oven chips", "1.5kg"),
        ("Fish fingers", "2 packs"),
        ("Frozen pizza", "2"),
        ("Garlic bread", "2"),
    ],
    "household": [
        ("Toilet roll", "9 pack"),
        ("Kitchen roll", "4 pack"),
        ("Washing up liquid", "1"),
        ("Bin bags", "1 roll"),
        ("Cleaning products", "as needed"),
    ],
    "toiletries": [
        ("Toothpaste", "2"),
        ("Shampoo/conditioner", "as needed"),
        ("Shower gel/soap", "as needed"),
        ("Deodorant", "2"),
    ],
}

# ============================================================
# MOBILE-FRIENDLY HTML TEMPLATE
# ============================================================

def generate_mobile_html(week_num, is_big_shop):
    """Generate mobile-friendly shopping list with interactive checkboxes"""
    data = weeks_data[week_num]
    month = data["month"]

    # Calculate week number within month
    month_start = data["start"].replace(day=1)
    week_of_month = ((data["start"] - month_start).days // 7) + 1

    title = f"{month} Week {week_of_month}"
    shop_type = "Monthly Big Shop" if is_big_shop else "Weekly Top-up"

    # Build items list
    items_html = ""

    if is_big_shop:
        # Get meat/fish for 4 weeks
        month_weeks = [week_num + i for i in range(4) if week_num + i <= 52]
        proteins = get_protein_requirements(month_weeks)
        shopping = consolidate_meat_list(proteins)
        weekly_breakdown = get_weekly_breakdown(month_weeks)

        # MEAT
        all_meat = shopping["beef"] + shopping["chicken"] + shopping["pork"] + shopping["lamb"]
        if all_meat:
            items_html += '<div class="section"><div class="section-title">Meat (Freeze)</div>'
            for item in all_meat:
                items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span></label>'
            items_html += '</div>'

        # FISH
        if shopping["fish"]:
            items_html += '<div class="section"><div class="section-title">Fish (Freeze)</div>'
            for item in shopping["fish"]:
                items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span></label>'
            items_html += '</div>'

        # PORTIONING GUIDE - use relative labels
        portion_labels = ["This Week", "Week 2", "Week 3", "Week 4"]
        portion_html = '<div class="section portioning"><div class="section-title">Freezer Portioning Guide</div>'
        for idx, wk in enumerate(month_weeks):
            meals = weekly_breakdown.get(wk, [])

            if meals:
                label = portion_labels[idx] if idx < len(portion_labels) else f"Week {idx+1}"
                portion_html += f'<div class="portion-week"><div class="portion-week-title">{label}</div>'
                for item in meals:
                    portion_html += f'<div class="portion-item">{item}</div>'
                portion_html += '</div>'

        portion_html += '</div>'
        items_html += portion_html

        # PANTRY (monthly)
        items_html += '<div class="section"><div class="section-title">Pantry & Cupboard</div>'
        for item, qty in monthly_items["pantry"]:
            items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
        items_html += '</div>'

        # CONDIMENTS (monthly - check stock)
        items_html += '<div class="section"><div class="section-title">Condiments & Oils (check stock)</div>'
        for item, qty in monthly_items["condiments"]:
            items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
        items_html += '</div>'

        # SPICES (monthly - check stock)
        items_html += '<div class="section"><div class="section-title">Spices (check stock)</div>'
        for item, qty in monthly_items["spices"]:
            items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
        items_html += '</div>'

        # FROZEN (monthly)
        items_html += '<div class="section"><div class="section-title">Frozen</div>'
        for item, qty in monthly_items["frozen"]:
            items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
        items_html += '</div>'

        # HOUSEHOLD (monthly)
        items_html += '<div class="section"><div class="section-title">Household</div>'
        for item, qty in monthly_items["household"]:
            items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
        items_html += '</div>'

        # TOILETRIES (monthly)
        items_html += '<div class="section"><div class="section-title">Toiletries</div>'
        for item, qty in monthly_items["toiletries"]:
            items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
        items_html += '</div>'

    # Determine if this is a fortnightly week (odd weeks: 1, 3, 5, 7, etc.)
    is_fortnightly = (week_num % 2 == 1)

    # WEEKLY FRESH ITEMS (every week)
    items_html += '<div class="section"><div class="section-title">Dairy & Eggs</div>'
    for item, qty in weekly_fresh["dairy"]:
        items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
    # Add fortnightly dairy items
    if is_fortnightly:
        for item, qty in fortnightly_items["dairy"]:
            items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
    items_html += '</div>'

    items_html += '<div class="section"><div class="section-title">Bread & Cereals</div>'
    for item, qty in weekly_fresh["bread"]:
        items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
    items_html += '</div>'

    items_html += '<div class="section"><div class="section-title">Fresh Produce</div>'
    for item, qty in weekly_fresh["produce"]:
        items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
    items_html += '</div>'

    items_html += '<div class="section"><div class="section-title">Drinks</div>'
    for item, qty in weekly_fresh["drinks"]:
        items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
    # Add fortnightly drinks
    if is_fortnightly:
        for item, qty in fortnightly_items["drinks"]:
            items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
    items_html += '</div>'

    items_html += '<div class="section"><div class="section-title">Snacks</div>'
    for item, qty in weekly_fresh["snacks"]:
        items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
    # Add fortnightly snacks
    if is_fortnightly:
        for item, qty in fortnightly_items["snacks"]:
            items_html += f'<label class="item"><input type="checkbox"><span class="text">{item}</span><span class="qty">{qty}</span></label>'
    items_html += '</div>'

    recipe_url = f"{BASE_URL}/week-{week_num:02d}.html"

    header_color = "#c62828" if is_big_shop else "#2c5530"

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
    <title>{title} Shopping List</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #f5f5f5;
            min-height: 100vh;
            padding-bottom: 80px;
        }}
        .header {{
            background: {header_color};
            color: white;
            padding: 20px 16px;
            position: sticky;
            top: 0;
            z-index: 100;
        }}
        .header h1 {{
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 4px;
        }}
        .header .subtitle {{
            font-size: 14px;
            opacity: 0.9;
        }}
        .header .dates {{
            font-size: 12px;
            opacity: 0.7;
            margin-top: 4px;
        }}
        .recipe-link {{
            display: block;
            background: rgba(255,255,255,0.2);
            color: white;
            text-decoration: none;
            padding: 10px;
            border-radius: 8px;
            margin-top: 12px;
            text-align: center;
            font-size: 14px;
        }}
        .content {{
            padding: 12px;
        }}
        .section {{
            background: white;
            border-radius: 12px;
            margin-bottom: 12px;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }}
        .section-title {{
            background: #f8f8f8;
            padding: 12px 16px;
            font-weight: 600;
            font-size: 14px;
            color: #333;
            border-bottom: 1px solid #eee;
        }}
        .item {{
            display: flex;
            align-items: center;
            padding: 14px 16px;
            border-bottom: 1px solid #f0f0f0;
            cursor: pointer;
            -webkit-tap-highlight-color: transparent;
        }}
        .item:last-child {{
            border-bottom: none;
        }}
        .item:active {{
            background: #f5f5f5;
        }}
        .item input[type="checkbox"] {{
            width: 24px;
            height: 24px;
            margin-right: 14px;
            accent-color: {header_color};
            cursor: pointer;
        }}
        .item .text {{
            flex: 1;
            font-size: 16px;
            color: #333;
        }}
        .item .qty {{
            font-size: 14px;
            color: #888;
            margin-left: 8px;
        }}
        .item.checked .text {{
            text-decoration: line-through;
            color: #aaa;
        }}
        .progress {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: white;
            padding: 16px;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .progress-bar {{
            flex: 1;
            height: 8px;
            background: #e0e0e0;
            border-radius: 4px;
            overflow: hidden;
        }}
        .progress-fill {{
            height: 100%;
            background: {header_color};
            width: 0%;
            transition: width 0.3s;
        }}
        .progress-text {{
            font-size: 14px;
            color: #666;
            min-width: 50px;
        }}
        .clear-btn {{
            background: none;
            border: 1px solid #ddd;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 12px;
            color: #666;
            cursor: pointer;
        }}
        .portioning {{
            background: #fff8e1;
        }}
        .portioning .section-title {{
            background: #ffc107;
            color: #333;
        }}
        .portion-week {{
            padding: 12px 16px;
            border-bottom: 1px solid #ffe082;
        }}
        .portion-week:last-child {{
            border-bottom: none;
        }}
        .portion-week-title {{
            font-weight: 600;
            font-size: 14px;
            color: #e65100;
            margin-bottom: 8px;
        }}
        .portion-item {{
            font-size: 13px;
            color: #555;
            padding: 4px 0;
            padding-left: 12px;
            border-left: 3px solid #ffc107;
            margin-bottom: 4px;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <div class="subtitle">{shop_type}</div>
        <div class="dates">{data["dates"]}</div>
        <a href="{recipe_url}" class="recipe-link">View This Week's Recipes</a>
    </div>

    <div class="content">
        {items_html}
    </div>

    <div class="progress">
        <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
        <div class="progress-text" id="progressText">0/0</div>
        <button class="clear-btn" onclick="clearAll()">Clear</button>
    </div>

    <script>
        const STORAGE_KEY = 'shopping-week-{week_num}';

        function saveState() {{
            const items = document.querySelectorAll('.item input');
            const state = Array.from(items).map(cb => cb.checked);
            localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
            updateProgress();
        }}

        function loadState() {{
            const saved = localStorage.getItem(STORAGE_KEY);
            if (saved) {{
                const state = JSON.parse(saved);
                const items = document.querySelectorAll('.item input');
                items.forEach((cb, i) => {{
                    if (state[i]) {{
                        cb.checked = true;
                        cb.closest('.item').classList.add('checked');
                    }}
                }});
            }}
            updateProgress();
        }}

        function updateProgress() {{
            const items = document.querySelectorAll('.item input');
            const checked = document.querySelectorAll('.item input:checked').length;
            const total = items.length;
            const pct = total > 0 ? (checked / total * 100) : 0;

            document.getElementById('progressFill').style.width = pct + '%';
            document.getElementById('progressText').textContent = checked + '/' + total;
        }}

        function clearAll() {{
            if (confirm('Clear all ticked items?')) {{
                document.querySelectorAll('.item input').forEach(cb => {{
                    cb.checked = false;
                    cb.closest('.item').classList.remove('checked');
                }});
                saveState();
            }}
        }}

        document.querySelectorAll('.item').forEach(item => {{
            item.addEventListener('click', function(e) {{
                if (e.target.tagName !== 'INPUT') {{
                    const cb = this.querySelector('input');
                    cb.checked = !cb.checked;
                }}
                this.classList.toggle('checked', this.querySelector('input').checked);
                saveState();
            }});
        }});

        loadState();
    </script>
</body>
</html>'''

    return html

# ============================================================
# GENERATE ALL SHOPPING LISTS
# ============================================================

print("Generating mobile-friendly shopping lists...")
print("=" * 60)

for week_num in range(1, 53):
    is_big_shop = (week_num - 1) % 4 == 0
    html = generate_mobile_html(week_num, is_big_shop)

    filename = os.path.join(output_dir, f"shopping-week-{week_num:02d}.html")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

    data = weeks_data[week_num]
    month = data["month"]
    month_start = data["start"].replace(day=1)
    week_of_month = ((data["start"] - month_start).days // 7) + 1

    shop_type = "BIG SHOP" if is_big_shop else "Top-up"
    print(f"Week {week_num:02d}: {month} Week {week_of_month} ({shop_type})")

print("=" * 60)
print("Done! Mobile-friendly shopping lists with interactive checkboxes.")
print(f"Files in: {output_dir}")
