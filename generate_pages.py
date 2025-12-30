"""
Generate all 52 weekly recipe pages for GitHub Pages
Full embedded recipes - comprehensive database for full year variety
"""

import os
import datetime
import random

random.seed(2026)  # Consistent randomization

output_dir = r"C:\Users\Little Nineveh\2026-meal-calendar\github-pages"
os.makedirs(output_dir, exist_ok=True)

# ============================================================
# COMPREHENSIVE RECIPE DATABASE - 100+ RECIPES
# ============================================================

lunch_recipes = {
    # SOUPS (12)
    "Leek & potato soup": {
        "time": "30 mins", "serves": "4",
        "ingredients": ["2 leeks, sliced", "3 potatoes, diced", "1 onion, chopped", "1L chicken stock", "2 tbsp butter", "100ml cream"],
        "method": "Melt butter, soften leeks and onion 5 mins. Add potatoes and stock, simmer 20 mins. Blend smooth, stir in cream, season."
    },
    "Tomato soup": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["2 tins chopped tomatoes", "1 onion, chopped", "2 garlic cloves", "500ml veg stock", "1 tsp sugar", "Fresh basil"],
        "method": "Soften onion and garlic. Add tomatoes, stock, sugar. Simmer 15 mins. Blend smooth, serve with basil and crusty bread."
    },
    "Carrot & coriander soup": {
        "time": "30 mins", "serves": "4",
        "ingredients": ["500g carrots, chopped", "1 onion, chopped", "1L veg stock", "1 tsp ground coriander", "Fresh coriander"],
        "method": "Soften onion 5 mins. Add carrots, ground coriander, stock. Simmer 20 mins. Blend smooth, serve with fresh coriander."
    },
    "Butternut squash soup": {
        "time": "40 mins", "serves": "4",
        "ingredients": ["1 butternut squash, cubed", "1 onion, chopped", "2 garlic cloves", "1L veg stock", "1 tsp cumin"],
        "method": "Roast squash at 200C 25 mins. Soften onion and garlic. Add squash, cumin, stock. Simmer 10 mins, blend smooth."
    },
    "Chicken noodle soup": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["2 chicken breasts", "1.5L chicken stock", "2 carrots, sliced", "2 celery sticks", "100g egg noodles", "Fresh parsley"],
        "method": "Poach chicken in stock 15 mins. Shred chicken. Add carrots, celery, simmer 5 mins. Add noodles, cook 4 mins. Add chicken, parsley."
    },
    "Pea & mint soup": {
        "time": "20 mins", "serves": "4",
        "ingredients": ["500g frozen peas", "1 onion, chopped", "750ml veg stock", "Fresh mint", "100ml cream"],
        "method": "Soften onion. Add peas, stock, simmer 5 mins. Blend with mint. Swirl in cream, season."
    },
    "French onion soup": {
        "time": "45 mins", "serves": "4",
        "ingredients": ["4 onions, sliced", "50g butter", "1L beef stock", "100ml white wine", "4 slices baguette", "100g gruyere"],
        "method": "Cook onions in butter slowly 30 mins until caramelized. Add wine, reduce. Add stock, simmer 10 mins. Top with toast and cheese, grill."
    },
    "Minestrone": {
        "time": "35 mins", "serves": "4",
        "ingredients": ["1 onion, diced", "2 carrots, diced", "2 celery sticks", "1 tin chopped tomatoes", "1 tin cannellini beans", "100g pasta", "1L veg stock"],
        "method": "Soften onion, carrots, celery 5 mins. Add tomatoes, beans, stock. Simmer 15 mins. Add pasta, cook 10 mins. Season, serve with parmesan."
    },
    "Broccoli & stilton soup": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["1 large broccoli, chopped", "1 onion, chopped", "1L veg stock", "100g stilton, crumbled", "100ml cream"],
        "method": "Soften onion. Add broccoli, stock, simmer 15 mins. Blend smooth. Stir in stilton and cream until melted."
    },
    "Sweetcorn chowder": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["2 tins sweetcorn", "4 rashers bacon, chopped", "1 onion, diced", "2 potatoes, diced", "500ml chicken stock", "200ml cream"],
        "method": "Fry bacon until crispy. Add onion, potatoes, cook 5 mins. Add stock, sweetcorn, simmer 15 mins. Add cream, blend half, mix back."
    },
    "Roasted red pepper soup": {
        "time": "35 mins", "serves": "4",
        "ingredients": ["4 red peppers, halved", "1 onion, chopped", "2 garlic cloves", "750ml veg stock", "1 tbsp balsamic vinegar"],
        "method": "Roast peppers at 200C 20 mins until charred. Peel. Soften onion, garlic. Add peppers, stock. Simmer 10 mins. Blend, add vinegar."
    },
    "Mushroom soup": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["400g mushrooms, sliced", "1 onion, chopped", "2 garlic cloves", "750ml veg stock", "100ml cream", "Fresh thyme"],
        "method": "Fry mushrooms until golden. Add onion, garlic, cook 5 mins. Add stock, thyme, simmer 10 mins. Blend, stir in cream."
    },

    # SANDWICHES & TOASTIES (15)
    "Ham & cheese toastie": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["2 slices bread", "2 slices ham", "50g cheddar, grated", "Butter"],
        "method": "Butter bread on outside. Layer ham and cheese inside. Fry in pan until golden and cheese melted."
    },
    "BLT sandwich": {
        "time": "10 mins", "serves": "1",
        "ingredients": ["3 rashers bacon", "2 slices bread, toasted", "Lettuce", "1 tomato, sliced", "Mayonnaise"],
        "method": "Fry bacon until crispy. Toast bread, spread with mayo. Layer lettuce, tomato, bacon."
    },
    "Tuna melt": {
        "time": "10 mins", "serves": "1",
        "ingredients": ["1 tin tuna, drained", "2 tbsp mayo", "2 slices bread", "50g cheddar, sliced"],
        "method": "Mix tuna with mayo. Toast bread lightly, spread tuna on top, add cheese. Grill until melted."
    },
    "Club sandwich": {
        "time": "15 mins", "serves": "1",
        "ingredients": ["3 slices bread, toasted", "2 rashers bacon", "Sliced chicken", "Lettuce, tomato", "Mayo"],
        "method": "Spread mayo on toast. Layer: toast, lettuce, chicken, toast, bacon, tomato, toast. Cut into quarters."
    },
    "Croque monsieur": {
        "time": "15 mins", "serves": "2",
        "ingredients": ["4 slices bread", "4 slices ham", "100g gruyere, grated", "2 tbsp butter", "1 tbsp flour", "150ml milk", "Dijon mustard"],
        "method": "Make sauce: melt butter, add flour, stir in milk until thick, add half cheese. Layer bread, ham, sauce. Top with cheese. Bake 200C 10 mins."
    },
    "Coronation chicken sandwich": {
        "time": "10 mins", "serves": "2",
        "ingredients": ["2 cooked chicken breasts, shredded", "3 tbsp mayo", "1 tbsp curry powder", "1 tbsp mango chutney", "Bread", "Lettuce"],
        "method": "Mix chicken with mayo, curry powder, chutney. Spread on bread with lettuce."
    },
    "Egg mayo sandwich": {
        "time": "15 mins", "serves": "2",
        "ingredients": ["4 eggs, hard boiled", "3 tbsp mayonnaise", "1 tsp mustard", "Salt & pepper", "Bread", "Cress"],
        "method": "Mash boiled eggs with mayo, mustard, seasoning. Spread on bread with cress."
    },
    "Cheese & pickle sandwich": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["2 slices bread", "75g mature cheddar, sliced", "2 tbsp Branston pickle", "Butter"],
        "method": "Butter bread, layer cheese and pickle. Press together."
    },
    "Welsh rarebit": {
        "time": "15 mins", "serves": "2",
        "ingredients": ["200g mature cheddar, grated", "25g butter", "1 tbsp flour", "100ml beer or milk", "1 tsp mustard", "4 slices bread"],
        "method": "Melt butter, stir in flour. Add beer/milk, stir until thick. Add cheese and mustard. Toast bread, spread mixture on top, grill until bubbling."
    },
    "Prawn mayo sandwich": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["100g cooked prawns", "2 tbsp mayo", "Squeeze lemon", "Bread", "Lettuce"],
        "method": "Mix prawns with mayo and lemon. Spread on bread with lettuce."
    },
    "Smoked salmon bagel": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["1 bagel", "2 tbsp cream cheese", "2 slices smoked salmon", "Capers", "Lemon"],
        "method": "Toast bagel. Spread cream cheese, top with salmon, capers, squeeze of lemon."
    },
    "Chicken Caesar wrap": {
        "time": "10 mins", "serves": "1",
        "ingredients": ["1 chicken breast, cooked and sliced", "1 wrap", "Romaine lettuce", "Parmesan, shaved", "Caesar dressing"],
        "method": "Lay wrap flat. Add lettuce, chicken, parmesan, drizzle dressing. Roll tightly."
    },
    "Ham salad wrap": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["2 slices ham", "1 wrap", "Lettuce", "Tomato", "Cucumber", "Mayo"],
        "method": "Spread wrap with mayo. Layer ham and salad. Roll tightly."
    },
    "Hummus & veg wrap": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["3 tbsp hummus", "1 wrap", "Grated carrot", "Cucumber", "Red pepper"],
        "method": "Spread hummus across wrap. Add vegetables. Roll tightly."
    },
    "Cheese toastie": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["2 slices bread", "75g cheddar, grated", "Butter"],
        "method": "Butter bread on outside. Fill with cheese. Fry until golden both sides."
    },

    # HOT LUNCHES (15)
    "Cheese omelette": {
        "time": "10 mins", "serves": "1",
        "ingredients": ["3 eggs", "50g cheese, grated", "1 tbsp butter", "Salt & pepper"],
        "method": "Beat eggs, season. Melt butter in pan. Pour in eggs, swirl to cover base. When nearly set, add cheese, fold over."
    },
    "Jacket potato with beans": {
        "time": "1 hour", "serves": "1",
        "ingredients": ["1 large potato", "1 tin baked beans", "Butter", "50g cheese, grated"],
        "method": "Bake potato at 200C for 1 hour (or microwave 10 mins). Cut open, add butter, beans, cheese."
    },
    "Jacket potato with tuna mayo": {
        "time": "1 hour", "serves": "1",
        "ingredients": ["1 large potato", "1 tin tuna", "2 tbsp mayo", "Sweetcorn", "Butter"],
        "method": "Bake potato. Mix tuna, mayo, sweetcorn. Cut potato open, add butter and tuna mix."
    },
    "Jacket potato with cheese & coleslaw": {
        "time": "1 hour", "serves": "1",
        "ingredients": ["1 large potato", "75g cheddar, grated", "3 tbsp coleslaw", "Butter"],
        "method": "Bake potato. Cut open, add butter, cheese, coleslaw."
    },
    "Beans on toast": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["1 tin baked beans", "2 slices bread", "Butter", "Cheese (optional)"],
        "method": "Heat beans. Toast and butter bread. Pour beans over, top with cheese."
    },
    "Cheese on toast": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["2 slices bread", "75g cheddar, grated", "Worcestershire sauce"],
        "method": "Toast bread one side. Flip, cover with cheese, dash of Worcestershire. Grill until bubbling."
    },
    "Sardines on toast": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["1 tin sardines", "2 slices bread", "Butter", "Lemon", "Black pepper"],
        "method": "Toast and butter bread. Top with sardines, lemon juice, pepper."
    },
    "Egg fried rice": {
        "time": "15 mins", "serves": "2",
        "ingredients": ["300g cooked rice (cold)", "2 eggs, beaten", "100g peas", "2 spring onions", "2 tbsp soy sauce"],
        "method": "Scramble eggs, set aside. Stir-fry rice, add peas. Add eggs, spring onions, soy sauce."
    },
    "Quesadilla": {
        "time": "10 mins", "serves": "1",
        "ingredients": ["2 tortillas", "75g cheddar, grated", "Sliced peppers", "Salsa, sour cream"],
        "method": "Layer cheese and peppers between tortillas. Dry fry until golden both sides. Serve with salsa and sour cream."
    },
    "Avocado on toast": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["1 avocado", "2 slices sourdough", "Lemon juice", "Chilli flakes", "Salt"],
        "method": "Toast bread. Mash avocado with lemon, salt. Spread on toast, sprinkle chilli flakes."
    },
    "Greek salad": {
        "time": "10 mins", "serves": "2",
        "ingredients": ["1 cucumber, chunked", "4 tomatoes, chunked", "1 red onion, sliced", "100g feta", "Olives", "Olive oil", "Oregano"],
        "method": "Combine vegetables. Add feta and olives. Dress with olive oil, oregano."
    },
    "Caesar salad": {
        "time": "15 mins", "serves": "2",
        "ingredients": ["1 romaine lettuce", "1 chicken breast, cooked and sliced", "Croutons", "Parmesan", "Caesar dressing"],
        "method": "Tear lettuce. Top with chicken, croutons, parmesan. Drizzle with dressing."
    },
    "Nicoise salad": {
        "time": "20 mins", "serves": "2",
        "ingredients": ["200g new potatoes", "100g green beans", "2 eggs, boiled", "1 tin tuna", "Olives", "Olive oil", "Lemon"],
        "method": "Boil potatoes and beans. Arrange with quartered eggs, tuna, olives. Dress with oil and lemon."
    },
    "Ploughman's lunch": {
        "time": "10 mins", "serves": "1",
        "ingredients": ["75g cheddar", "2 slices ham", "Branston pickle", "Crusty bread", "Apple", "Celery"],
        "method": "Arrange cheese, ham, pickle, bread, apple and celery on a plate."
    },
    "Leftover roast sandwich": {
        "time": "5 mins", "serves": "1",
        "ingredients": ["Sliced roast meat", "2 slices bread", "Stuffing", "Gravy or cranberry sauce"],
        "method": "Layer cold meat, stuffing, and sauce between bread."
    },
}

dinner_recipes = {
    # BEEF (12)
    "Spaghetti Bolognese": {
        "time": "45 mins", "serves": "4",
        "ingredients": ["500g beef mince", "1 onion, diced", "2 garlic cloves", "2 carrots, diced", "2 tins chopped tomatoes", "2 tbsp tomato puree", "400g spaghetti", "Parmesan"],
        "method": "Brown mince, drain. Add onion, garlic, carrots, cook 5 mins. Add tomatoes, puree, simmer 30 mins. Serve with spaghetti and parmesan."
    },
    "Cottage Pie": {
        "time": "1 hour", "serves": "4",
        "ingredients": ["500g beef mince", "1 onion, diced", "2 carrots, diced", "400ml beef stock", "2 tbsp tomato puree", "800g potatoes", "50g butter", "Milk"],
        "method": "Brown mince, add veg. Add stock, puree, simmer 20 mins. Mash potatoes with butter, milk. Top mince with mash. Bake 200C 25 mins."
    },
    "Beef Stroganoff": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["500g beef sirloin, sliced thin", "250g mushrooms, sliced", "1 onion, sliced", "200ml beef stock", "150ml sour cream", "1 tbsp paprika", "Rice"],
        "method": "Fry beef quickly, set aside. Cook onion, mushrooms 5 mins. Add paprika, stock, simmer 5 mins. Return beef, stir in sour cream. Serve with rice."
    },
    "Chilli Con Carne": {
        "time": "45 mins", "serves": "4",
        "ingredients": ["500g beef mince", "1 onion, diced", "2 garlic cloves", "1 tin tomatoes", "1 tin kidney beans", "2 tsp cumin", "1 tsp chilli powder", "Rice"],
        "method": "Brown mince, add onion, garlic, spices. Add tomatoes, beans. Simmer 30 mins. Serve with rice, sour cream."
    },
    "Beef Stew": {
        "time": "2 hours", "serves": "4",
        "ingredients": ["500g stewing beef, cubed", "2 onions, quartered", "4 carrots, chunked", "4 potatoes, chunked", "500ml beef stock", "2 tbsp flour", "Thyme"],
        "method": "Toss beef in flour, brown. Add all ingredients, simmer gently 1.5-2 hours until beef tender."
    },
    "Beef Tacos": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["500g beef mince", "1 onion, diced", "2 tbsp taco seasoning", "8 taco shells", "Lettuce, tomato, cheese", "Sour cream, salsa"],
        "method": "Brown mince with onion. Add seasoning, splash of water, simmer 10 mins. Serve in shells with toppings."
    },
    "Beef Burgers": {
        "time": "20 mins", "serves": "4",
        "ingredients": ["500g beef mince", "1 onion, grated", "1 egg", "4 burger buns", "Lettuce, tomato, onion", "Cheese, ketchup, mustard"],
        "method": "Mix mince, onion, egg, season. Shape into 4 patties. Grill 5-6 mins each side. Serve in buns with toppings."
    },
    "Steak & Chips": {
        "time": "30 mins", "serves": "2",
        "ingredients": ["2 sirloin steaks", "500g potatoes, cut into chips", "Oil for frying", "Butter", "Peas"],
        "method": "Fry chips until golden. Season steaks, fry 3-4 mins each side for medium. Rest 5 mins. Serve with chips and peas."
    },
    "Beef Fajitas": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["500g beef steak, sliced", "2 peppers, sliced", "1 onion, sliced", "2 tbsp fajita seasoning", "8 tortillas", "Sour cream, guacamole"],
        "method": "Toss beef in seasoning. Fry beef 3 mins. Add peppers, onion, cook 5 mins. Serve in warm tortillas."
    },
    "Lasagne": {
        "time": "1 hr 15 mins", "serves": "6",
        "ingredients": ["500g beef mince", "1 onion", "2 tins tomatoes", "Lasagne sheets", "50g butter", "50g flour", "500ml milk", "100g parmesan"],
        "method": "Make meat sauce: brown mince, add onion, tomatoes, simmer 20 mins. Make white sauce: butter, flour, milk. Layer meat, pasta, white sauce. Top with cheese. Bake 180C 40 mins."
    },
    "Meatballs in Tomato Sauce": {
        "time": "40 mins", "serves": "4",
        "ingredients": ["500g beef mince", "1 onion, grated", "50g breadcrumbs", "1 egg", "2 tins tomatoes", "2 garlic cloves", "Fresh basil", "Spaghetti"],
        "method": "Mix mince, onion, breadcrumbs, egg. Roll into balls. Make sauce with tomatoes, garlic. Add meatballs, simmer 25 mins. Serve with spaghetti."
    },
    "Beef & Broccoli Stir-fry": {
        "time": "20 mins", "serves": "4",
        "ingredients": ["400g beef steak, sliced", "1 head broccoli, florets", "3 garlic cloves", "3 tbsp soy sauce", "1 tbsp honey", "Rice"],
        "method": "Stir-fry beef 2 mins, set aside. Stir-fry broccoli 3 mins. Add garlic, soy sauce, honey, return beef. Serve with rice."
    },

    # CHICKEN (12)
    "Chicken Tikka Masala": {
        "time": "40 mins", "serves": "4",
        "ingredients": ["500g chicken breast, cubed", "2 tbsp tikka paste", "1 onion", "1 tin tomatoes", "200ml cream", "Coriander", "Rice"],
        "method": "Coat chicken in paste, fry until golden. Cook onion, add remaining paste, tomatoes. Simmer, add cream and chicken. Serve with rice."
    },
    "Chicken Fajitas": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["500g chicken breast, sliced", "2 peppers, sliced", "1 onion, sliced", "2 tbsp fajita seasoning", "8 tortillas", "Sour cream, salsa"],
        "method": "Toss chicken in seasoning. Fry chicken 5 mins. Add peppers, onion, cook 5 mins. Serve in tortillas."
    },
    "Chicken Korma": {
        "time": "35 mins", "serves": "4",
        "ingredients": ["500g chicken breast, cubed", "1 onion", "3 tbsp korma paste", "200ml coconut cream", "100g ground almonds", "Sultanas", "Rice"],
        "method": "Fry chicken until golden. Cook onion, add paste. Add coconut cream, almonds, sultanas, chicken. Simmer 15 mins."
    },
    "Chicken Katsu Curry": {
        "time": "35 mins", "serves": "4",
        "ingredients": ["4 chicken breasts", "100g flour", "2 eggs", "150g panko breadcrumbs", "1 onion", "2 tbsp curry powder", "400ml chicken stock", "Rice"],
        "method": "Make sauce: fry onion, add curry powder, flour, stock, simmer 10 mins. Coat chicken in flour, egg, panko. Shallow fry 5 mins each side. Slice, serve with sauce and rice."
    },
    "Thai Green Curry": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["500g chicken thigh, sliced", "2 tbsp green curry paste", "400ml coconut milk", "1 aubergine, cubed", "Green beans", "Thai basil", "Rice"],
        "method": "Fry paste 1 min. Add chicken, cook 3 mins. Add coconut milk, aubergine. Simmer 15 mins. Add beans last 5 mins. Serve with rice."
    },
    "Chicken Stir-fry": {
        "time": "20 mins", "serves": "4",
        "ingredients": ["500g chicken breast, sliced", "2 peppers, sliced", "1 onion, sliced", "2 pak choi", "3 tbsp soy sauce", "1 tbsp honey", "Noodles"],
        "method": "Stir-fry chicken 5 mins. Add vegetables, cook 3 mins. Add soy sauce, honey. Serve with noodles."
    },
    "Chicken Pie": {
        "time": "1 hour", "serves": "4",
        "ingredients": ["500g chicken breast, cubed", "3 leeks, sliced", "200ml chicken stock", "200ml cream", "1 tbsp Dijon mustard", "1 sheet puff pastry", "1 egg"],
        "method": "Poach chicken in stock. Cook leeks in stock. Add cream, mustard, chicken. Pour into dish. Top with pastry, brush with egg. Bake 200C 25 mins."
    },
    "Honey Mustard Chicken": {
        "time": "30 mins", "serves": "4",
        "ingredients": ["4 chicken breasts", "3 tbsp honey", "2 tbsp wholegrain mustard", "2 tbsp soy sauce", "New potatoes", "Green veg"],
        "method": "Mix honey, mustard, soy sauce. Coat chicken, bake at 200C 25 mins, basting halfway. Serve with potatoes and veg."
    },
    "Chicken Cacciatore": {
        "time": "45 mins", "serves": "4",
        "ingredients": ["8 chicken thighs", "1 onion, sliced", "2 peppers, sliced", "2 tins tomatoes", "100ml red wine", "Olives", "Fresh basil"],
        "method": "Brown chicken. Add onion, peppers, cook 5 mins. Add tomatoes, wine, olives. Cover, simmer 30 mins. Serve with crusty bread."
    },
    "Lemon Herb Chicken": {
        "time": "35 mins", "serves": "4",
        "ingredients": ["4 chicken breasts", "2 lemons, juiced", "4 garlic cloves", "Fresh rosemary, thyme", "Olive oil", "Roast potatoes", "Salad"],
        "method": "Marinate chicken in lemon, garlic, herbs, oil. Bake at 200C 25 mins. Serve with roast potatoes and salad."
    },
    "Chicken Goujons": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["4 chicken breasts, cut into strips", "100g flour", "2 eggs", "150g breadcrumbs", "Oil for frying", "Chips", "Peas"],
        "method": "Coat chicken in flour, egg, breadcrumbs. Shallow fry 4-5 mins until golden. Serve with chips and peas."
    },
    "Chicken Noodle Stir-fry": {
        "time": "20 mins", "serves": "4",
        "ingredients": ["400g chicken, sliced", "300g egg noodles", "2 pak choi", "100g beansprouts", "3 tbsp soy sauce", "1 tbsp sesame oil"],
        "method": "Cook noodles. Stir-fry chicken 5 mins. Add pak choi, beansprouts, noodles, soy sauce, sesame oil. Toss together."
    },

    # PORK (8)
    "Sausage Casserole": {
        "time": "45 mins", "serves": "4",
        "ingredients": ["8 pork sausages", "1 onion, sliced", "2 peppers, sliced", "2 tins tomatoes", "1 tin cannellini beans", "2 tsp smoked paprika"],
        "method": "Brown sausages. Add onion, peppers, cook 5 mins. Add tomatoes, paprika, beans, sausages. Cover, simmer 30 mins."
    },
    "Pork Chops with Apple": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["4 pork chops", "2 apples, sliced", "1 onion, sliced", "200ml cider", "1 tbsp wholegrain mustard", "Mashed potato"],
        "method": "Season and fry chops 5 mins each side. Remove. Fry onion, apple. Add cider, mustard, simmer 5 mins. Return chops. Serve with mash."
    },
    "Pulled Pork": {
        "time": "4 hours", "serves": "6",
        "ingredients": ["1.5kg pork shoulder", "2 tbsp smoked paprika", "1 tbsp brown sugar", "200ml BBQ sauce", "Burger buns", "Coleslaw"],
        "method": "Rub pork with paprika, sugar, salt. Slow cook at 150C 3-4 hours until falling apart. Shred, mix with BBQ sauce. Serve in buns with coleslaw."
    },
    "Pork Stir-fry": {
        "time": "20 mins", "serves": "4",
        "ingredients": ["400g pork tenderloin, sliced", "1 red pepper", "1 courgette", "100g mangetout", "3 tbsp hoisin sauce", "Rice or noodles"],
        "method": "Stir-fry pork 3 mins. Add vegetables, cook 4 mins. Add hoisin sauce, toss. Serve with rice or noodles."
    },
    "Gammon, Egg & Chips": {
        "time": "30 mins", "serves": "2",
        "ingredients": ["2 gammon steaks", "4 eggs", "500g potatoes, cut into chips", "Oil", "Peas"],
        "method": "Fry chips until golden. Grill or fry gammon 5 mins each side. Fry eggs. Serve with peas."
    },
    "Toad in the Hole": {
        "time": "45 mins", "serves": "4",
        "ingredients": ["8 sausages", "140g flour", "4 eggs", "200ml milk", "Vegetable oil", "Onion gravy"],
        "method": "Put sausages and oil in roasting tin, bake at 220C 15 mins. Mix flour, eggs, milk for batter. Pour over sausages. Bake 25 mins until risen. Serve with gravy."
    },
    "Pork Meatballs": {
        "time": "35 mins", "serves": "4",
        "ingredients": ["500g pork mince", "1 onion, grated", "50g breadcrumbs", "1 egg", "2 tins tomatoes", "Fresh basil", "Spaghetti"],
        "method": "Mix mince, onion, breadcrumbs, egg. Roll into balls. Make tomato sauce. Add meatballs, simmer 20 mins. Serve with spaghetti."
    },
    "Sweet & Sour Pork": {
        "time": "30 mins", "serves": "4",
        "ingredients": ["400g pork tenderloin, cubed", "1 pepper, chunked", "1 onion, chunked", "1 tin pineapple chunks", "3 tbsp tomato ketchup", "2 tbsp soy sauce", "1 tbsp vinegar", "Rice"],
        "method": "Fry pork until golden. Add vegetables, cook 3 mins. Add pineapple, ketchup, soy sauce, vinegar. Simmer 5 mins. Serve with rice."
    },

    # LAMB (6)
    "Shepherd's Pie": {
        "time": "1 hour", "serves": "4",
        "ingredients": ["500g lamb mince", "1 onion, diced", "2 carrots, diced", "400ml lamb stock", "2 tbsp tomato puree", "800g potatoes", "50g butter"],
        "method": "Brown lamb, add veg. Add stock, puree, simmer 20 mins. Mash potatoes with butter. Top lamb with mash. Bake 200C 25 mins."
    },
    "Lamb Koftas": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["500g lamb mince", "1 onion, grated", "2 garlic cloves", "1 tsp cumin", "Fresh mint", "Pitta bread", "Tzatziki, salad"],
        "method": "Mix lamb, onion, garlic, cumin, mint. Shape around skewers. Grill 10-12 mins. Serve in pitta with tzatziki and salad."
    },
    "Lamb Chops with Mint": {
        "time": "20 mins", "serves": "4",
        "ingredients": ["8 lamb chops", "Fresh mint, chopped", "2 tbsp olive oil", "2 garlic cloves", "New potatoes", "Green beans"],
        "method": "Rub chops with oil, garlic, mint. Grill 4-5 mins each side. Serve with new potatoes and beans."
    },
    "Lamb Curry": {
        "time": "1 hour", "serves": "4",
        "ingredients": ["500g lamb leg, cubed", "1 onion", "3 tbsp curry paste", "400ml coconut milk", "200g spinach", "Rice", "Naan bread"],
        "method": "Brown lamb. Fry onion, add paste. Add lamb, coconut milk. Simmer 45 mins. Stir in spinach. Serve with rice and naan."
    },
    "Moussaka": {
        "time": "1 hr 15 mins", "serves": "6",
        "ingredients": ["500g lamb mince", "2 aubergines, sliced", "1 onion", "2 tins tomatoes", "1 tsp cinnamon", "50g butter", "50g flour", "500ml milk", "100g feta"],
        "method": "Fry aubergines. Brown lamb, add onion, tomatoes, cinnamon, simmer 20 mins. Make white sauce. Layer aubergine, lamb, sauce. Top with feta. Bake 180C 40 mins."
    },
    "Lamb Hotpot": {
        "time": "2 hours", "serves": "4",
        "ingredients": ["500g lamb neck, sliced", "2 onions, sliced", "3 carrots, sliced", "500ml lamb stock", "Fresh thyme", "800g potatoes, sliced"],
        "method": "Layer lamb, onions, carrots in pot. Pour over stock, add thyme. Top with overlapping potato slices, brush with butter. Cover, bake 160C 1.5 hours. Uncover, bake 30 mins to crisp potatoes."
    },

    # FISH (12)
    "Fish & Chips": {
        "time": "45 mins", "serves": "4",
        "ingredients": ["4 cod fillets", "150g flour", "200ml sparkling water", "1 tsp baking powder", "1kg potatoes", "Oil", "Mushy peas", "Tartare sauce"],
        "method": "Soak chips, dry well. Fry chips at 160C, then 190C until golden. Make batter with flour, water, baking powder. Dip fish, fry 6-8 mins. Serve with peas and tartare."
    },
    "Fish Pie": {
        "time": "1 hour", "serves": "4",
        "ingredients": ["400g mixed fish (salmon, cod, smoked haddock)", "200g prawns", "500ml milk", "50g butter", "50g flour", "800g potatoes", "Fresh parsley"],
        "method": "Poach fish in milk. Make sauce with butter, flour, milk. Add fish, prawns, parsley. Top with mash. Bake 200C 25 mins."
    },
    "Fish Tacos": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["400g white fish", "2 tsp cumin", "1 tsp paprika", "8 tortillas", "Cabbage, shredded", "Lime", "Sour cream", "Coriander"],
        "method": "Season fish, pan fry 3-4 mins each side. Flake. Serve in tortillas with cabbage, sour cream, coriander, lime."
    },
    "Salmon Teriyaki": {
        "time": "20 mins", "serves": "4",
        "ingredients": ["4 salmon fillets", "4 tbsp soy sauce", "2 tbsp honey", "1 tbsp rice vinegar", "1 garlic clove", "Rice", "Broccoli"],
        "method": "Mix soy sauce, honey, vinegar, garlic. Marinate salmon 10 mins. Pan fry salmon 4 mins each side, glazing with sauce. Serve with rice and broccoli."
    },
    "Prawn Stir-fry": {
        "time": "15 mins", "serves": "4",
        "ingredients": ["400g prawns", "2 peppers, sliced", "100g mangetout", "2 pak choi", "3 tbsp soy sauce", "1 tbsp sesame oil", "Noodles"],
        "method": "Stir-fry prawns 2 mins. Add vegetables, cook 3 mins. Add soy sauce, sesame oil. Serve with noodles."
    },
    "Salmon Fishcakes": {
        "time": "35 mins", "serves": "4",
        "ingredients": ["400g salmon fillets", "400g potatoes, mashed", "2 spring onions, sliced", "1 tbsp capers", "Flour, egg, breadcrumbs", "Salad", "Tartare sauce"],
        "method": "Poach salmon, flake. Mix with mash, spring onions, capers. Shape into cakes. Coat in flour, egg, breadcrumbs. Fry 4 mins each side. Serve with salad and tartare."
    },
    "Prawn Curry": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["400g prawns", "1 onion", "2 tbsp curry paste", "400ml coconut milk", "200g spinach", "Rice", "Naan"],
        "method": "Fry onion, add paste. Add coconut milk, simmer 10 mins. Add prawns, cook 5 mins. Stir in spinach. Serve with rice and naan."
    },
    "Cod with Parsley Sauce": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["4 cod fillets", "50g butter", "50g flour", "500ml milk", "Large bunch parsley, chopped", "New potatoes", "Peas"],
        "method": "Poach cod in milk 10 mins. Make sauce with butter, flour, cooking milk. Add parsley. Serve fish with sauce, potatoes and peas."
    },
    "Fish Finger Sandwiches": {
        "time": "20 mins", "serves": "4",
        "ingredients": ["12 fish fingers", "8 slices bread", "Tartare sauce", "Lettuce", "Lemon"],
        "method": "Cook fish fingers per packet instructions. Spread bread with tartare sauce. Add lettuce, fish fingers, squeeze of lemon."
    },
    "Tuna Pasta Bake": {
        "time": "35 mins", "serves": "4",
        "ingredients": ["300g pasta", "2 tins tuna", "1 tin sweetcorn", "50g butter", "50g flour", "500ml milk", "150g cheddar"],
        "method": "Cook pasta. Make cheese sauce with butter, flour, milk, half cheese. Mix pasta, tuna, sweetcorn, sauce. Top with cheese. Bake 200C 20 mins."
    },
    "Smoked Haddock Risotto": {
        "time": "35 mins", "serves": "4",
        "ingredients": ["400g smoked haddock", "300g risotto rice", "1 onion", "150ml white wine", "1L fish stock", "100g peas", "50g parmesan"],
        "method": "Poach haddock, flake. Cook onion, add rice. Add wine, then stock ladle by ladle. Add peas and haddock last 5 mins. Stir in parmesan."
    },
    "Baked Salmon with Lemon": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["4 salmon fillets", "2 lemons", "Fresh dill", "Olive oil", "New potatoes", "Asparagus"],
        "method": "Place salmon on foil. Top with lemon slices, dill, oil. Wrap loosely. Bake 200C 15-20 mins. Serve with potatoes and asparagus."
    },

    # VEGETARIAN (10)
    "Cauliflower Cheese": {
        "time": "35 mins", "serves": "4",
        "ingredients": ["1 large cauliflower", "50g butter", "50g flour", "500ml milk", "200g cheddar", "1 tsp mustard"],
        "method": "Boil cauliflower 5 mins. Make sauce with butter, flour, milk, most of cheese and mustard. Put cauliflower in dish, pour over sauce, top with cheese. Bake 200C 20 mins."
    },
    "Mushroom Risotto": {
        "time": "35 mins", "serves": "4",
        "ingredients": ["300g risotto rice", "300g mushrooms", "1 onion", "150ml white wine", "1L veg stock", "50g parmesan", "Fresh thyme"],
        "method": "Fry mushrooms, set aside. Cook onion, add rice. Add wine, then stock ladle by ladle, stirring. Add mushrooms, parmesan, thyme."
    },
    "Vegetable Curry": {
        "time": "30 mins", "serves": "4",
        "ingredients": ["1 cauliflower, florets", "2 potatoes, cubed", "200g spinach", "1 onion", "3 tbsp curry paste", "400ml coconut milk", "Rice"],
        "method": "Fry onion, add paste. Add cauliflower, potatoes, coconut milk. Simmer 20 mins. Stir in spinach. Serve with rice."
    },
    "Macaroni Cheese": {
        "time": "30 mins", "serves": "4",
        "ingredients": ["350g macaroni", "50g butter", "50g flour", "600ml milk", "250g cheddar", "1 tsp mustard"],
        "method": "Cook macaroni. Make sauce with butter, flour, milk, most of cheese and mustard. Mix with pasta. Top with remaining cheese. Grill until golden."
    },
    "Vegetable Stir-fry": {
        "time": "15 mins", "serves": "4",
        "ingredients": ["1 broccoli, florets", "2 peppers, sliced", "2 pak choi", "100g beansprouts", "3 tbsp soy sauce", "1 tbsp sesame oil", "Noodles or rice"],
        "method": "Stir-fry broccoli 2 mins. Add peppers, pak choi, beansprouts, cook 3 mins. Add soy sauce, sesame oil. Serve with noodles or rice."
    },
    "Vegetable Lasagne": {
        "time": "1 hr 15 mins", "serves": "6",
        "ingredients": ["2 courgettes, sliced", "1 aubergine, sliced", "2 peppers, sliced", "2 tins tomatoes", "Lasagne sheets", "50g butter", "50g flour", "500ml milk", "100g parmesan"],
        "method": "Roast vegetables. Make tomato sauce. Make white sauce. Layer vegetables, tomato sauce, pasta, white sauce. Top with parmesan. Bake 180C 40 mins."
    },
    "Cheese & Onion Pie": {
        "time": "1 hour", "serves": "4",
        "ingredients": ["500g potatoes, sliced", "2 onions, sliced", "200g cheddar, grated", "300ml cream", "1 sheet puff pastry", "1 egg"],
        "method": "Layer potatoes, onions, cheese in dish. Pour over cream. Top with pastry. Brush with egg. Bake 200C 45 mins."
    },
    "Spinach & Ricotta Cannelloni": {
        "time": "1 hour", "serves": "4",
        "ingredients": ["12 cannelloni tubes", "500g spinach, wilted", "250g ricotta", "100g parmesan", "2 tins tomatoes", "2 garlic cloves"],
        "method": "Mix spinach, ricotta, half parmesan. Fill tubes. Make sauce with tomatoes, garlic. Pour sauce in dish, add tubes. Top with parmesan. Bake 180C 35 mins."
    },
    "Stuffed Peppers": {
        "time": "45 mins", "serves": "4",
        "ingredients": ["4 large peppers", "200g rice, cooked", "1 tin chickpeas", "100g feta", "Fresh herbs", "Olive oil"],
        "method": "Cut tops off peppers, remove seeds. Mix rice, chickpeas, feta, herbs. Fill peppers. Drizzle with oil. Bake 200C 30 mins."
    },
    "Vegetable Fajitas": {
        "time": "25 mins", "serves": "4",
        "ingredients": ["2 peppers, sliced", "1 courgette, sliced", "1 onion, sliced", "1 tin black beans", "2 tbsp fajita seasoning", "8 tortillas", "Sour cream, salsa"],
        "method": "Fry vegetables with seasoning 10 mins. Add beans, heat through. Serve in tortillas with sour cream and salsa."
    },
}

breakfast_recipes = {
    "Full English": {
        "time": "20 mins", "serves": "2",
        "ingredients": ["4 rashers bacon", "4 sausages", "4 eggs", "2 tomatoes, halved", "200g mushrooms", "1 tin baked beans", "Toast"],
        "method": "Grill sausages 15 mins. Add bacon last 5 mins. Fry mushrooms and tomatoes. Fry or poach eggs. Heat beans. Serve together with toast."
    },
    "Eggs Benedict": {
        "time": "20 mins", "serves": "2",
        "ingredients": ["4 eggs", "2 English muffins", "4 slices ham", "For hollandaise: 2 egg yolks, 100g butter, 1 tbsp lemon juice"],
        "method": "Make hollandaise: whisk yolks and lemon over simmering water, slowly add melted butter. Poach eggs 3 mins. Toast muffins, top with ham, egg, hollandaise."
    },
    "Eggs Florentine": {
        "time": "20 mins", "serves": "2",
        "ingredients": ["4 eggs", "200g spinach", "2 English muffins", "Hollandaise sauce", "Butter"],
        "method": "Wilt spinach in butter. Toast muffins. Poach eggs. Layer muffin, spinach, egg, hollandaise."
    },
    "Eggs Royale": {
        "time": "20 mins", "serves": "2",
        "ingredients": ["4 eggs", "2 English muffins", "100g smoked salmon", "Hollandaise sauce"],
        "method": "Toast muffins. Poach eggs. Layer muffin, salmon, egg, hollandaise."
    },
    "Pancakes": {
        "time": "20 mins", "serves": "4",
        "ingredients": ["200g self-raising flour", "1 egg", "300ml milk", "Butter", "Maple syrup, bacon or berries"],
        "method": "Mix flour, egg, milk to smooth batter. Heat butter, add ladle of batter. Cook until bubbles appear, flip. Serve stacked with toppings."
    },
    "American Pancakes": {
        "time": "20 mins", "serves": "4",
        "ingredients": ["200g self-raising flour", "1 tsp baking powder", "1 egg", "250ml milk", "2 tbsp melted butter", "Maple syrup, blueberries"],
        "method": "Mix dry ingredients. Add egg, milk, butter. Cook small rounds until bubbles form, flip. Stack and serve with syrup and berries."
    },
    "French Toast": {
        "time": "15 mins", "serves": "2",
        "ingredients": ["4 thick slices bread (brioche is best)", "2 eggs", "100ml milk", "1 tsp cinnamon", "Vanilla", "Butter", "Berries, maple syrup"],
        "method": "Whisk eggs, milk, cinnamon, vanilla. Dip bread. Fry in butter 2-3 mins each side. Serve with berries and maple syrup."
    },
    "Shakshuka": {
        "time": "25 mins", "serves": "2",
        "ingredients": ["1 tin tomatoes", "1 red pepper, diced", "1 onion", "2 garlic cloves", "1 tsp cumin", "1 tsp paprika", "4 eggs", "Coriander", "Crusty bread"],
        "method": "Fry onion and pepper. Add garlic, spices, tomatoes. Simmer 10 mins. Make wells, crack in eggs. Cover, cook 5-8 mins. Serve with coriander and bread."
    },
    "Avocado on Toast": {
        "time": "10 mins", "serves": "2",
        "ingredients": ["2 avocados", "4 slices sourdough", "4 eggs", "Chilli flakes", "Lemon", "Salt & pepper"],
        "method": "Toast bread. Mash avocados with lemon, seasoning. Poach eggs. Spread avocado on toast, top with egg, chilli flakes."
    },
    "Scrambled Eggs & Smoked Salmon": {
        "time": "10 mins", "serves": "2",
        "ingredients": ["6 eggs", "2 tbsp butter", "100g smoked salmon", "Fresh chives", "Toast"],
        "method": "Beat eggs. Melt butter over low heat. Add eggs, stir gently until just set. Serve on toast with salmon and chives."
    },
    "Omelette": {
        "time": "10 mins", "serves": "1",
        "ingredients": ["3 eggs", "Filling of choice (cheese, ham, mushrooms, herbs)", "1 tbsp butter"],
        "method": "Beat eggs, season. Melt butter in pan. Pour in eggs, swirl. When nearly set, add filling to one half, fold over."
    },
    "Bacon & Egg Muffin": {
        "time": "15 mins", "serves": "2",
        "ingredients": ["4 rashers bacon", "2 eggs", "2 English muffins", "2 slices cheese", "Brown sauce or ketchup"],
        "method": "Grill bacon. Fry eggs. Toast muffins. Layer bacon, egg, cheese, sauce in muffins."
    },
    "Kedgeree": {
        "time": "30 mins", "serves": "4",
        "ingredients": ["300g smoked haddock", "250g rice", "4 eggs, hard boiled", "1 onion", "2 tsp curry powder", "Fresh parsley"],
        "method": "Poach haddock, flake. Cook rice. Fry onion with curry powder. Mix rice, fish, quartered eggs, parsley."
    },
    "Porridge with Berries": {
        "time": "10 mins", "serves": "2",
        "ingredients": ["100g porridge oats", "400ml milk", "Honey", "Fresh berries", "Seeds (optional)"],
        "method": "Simmer oats and milk 5 mins, stirring. Serve with honey, berries, seeds."
    },
    "Croissants with Ham & Cheese": {
        "time": "10 mins", "serves": "2",
        "ingredients": ["2 croissants", "4 slices ham", "50g gruyere, sliced", "Dijon mustard"],
        "method": "Slice croissants. Fill with ham, cheese, mustard. Bake at 180C 5 mins until cheese melts."
    },
}

roast_recipes = {
    "Roast Beef": {
        "time": "1.5 hours + rest", "serves": "6-8",
        "ingredients": ["1.5kg beef joint", "Olive oil", "Salt & pepper", "Fresh rosemary"],
        "method": "Remove from fridge 1 hour before. Rub with oil, season. Roast at 220C 20 mins, reduce to 170C. Cook 15 mins per 500g for medium-rare. Rest 30 mins."
    },
    "Roast Chicken": {
        "time": "1.5 hours", "serves": "4-6",
        "ingredients": ["1.8kg whole chicken", "1 lemon, halved", "1 garlic bulb", "Fresh thyme", "50g butter"],
        "method": "Spread butter under skin. Put lemon and garlic inside. Season. Roast at 200C 1hr 20 mins until juices run clear. Rest 15 mins."
    },
    "Roast Pork": {
        "time": "2.5 hours", "serves": "6-8",
        "ingredients": ["2kg pork shoulder, skin scored", "Olive oil", "Sea salt", "Fresh sage"],
        "method": "Dry skin well. Rub with oil and salt. Roast at 220C 30 mins. Reduce to 160C, cook 2 hours. Rest 20 mins."
    },
    "Roast Lamb": {
        "time": "1.5 hours + rest", "serves": "6-8",
        "ingredients": ["2kg leg of lamb", "6 garlic cloves", "Fresh rosemary", "Olive oil"],
        "method": "Make slits in lamb, insert garlic and rosemary. Rub with oil, season. Roast at 200C 20 mins, reduce to 180C. Cook 25 mins per 500g for pink. Rest 20 mins."
    },
    "Roast Potatoes": {
        "time": "1 hour", "serves": "6",
        "ingredients": ["1.5kg potatoes, quartered", "4 tbsp goose fat or oil", "Salt", "Fresh rosemary"],
        "method": "Boil potatoes 10 mins, drain, shake to roughen. Heat fat at 200C. Add potatoes. Roast 45-50 mins, turning halfway."
    },
    "Yorkshire Puddings": {
        "time": "30 mins", "serves": "12",
        "ingredients": ["140g flour", "4 eggs", "200ml milk", "Oil"],
        "method": "Mix flour, eggs, milk until smooth. Rest 30 mins. Put oil in 12-hole tin, heat at 230C until smoking. Pour in batter. Bake 20-25 mins. Don't open oven!"
    },
    "Onion Gravy": {
        "time": "25 mins", "serves": "6",
        "ingredients": ["2 onions, sliced", "2 tbsp butter", "1 tbsp flour", "500ml stock", "Meat juices"],
        "method": "Cook onions in butter 15 mins until golden. Add flour, cook 1 min. Add stock and meat juices. Simmer 5 mins."
    },
}

# ============================================================
# BUILD MEAL SCHEDULE
# ============================================================

# Create varied weekly schedules
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Get all recipe names
all_lunches = list(lunch_recipes.keys())
all_dinners = list(dinner_recipes.keys())
all_breakfasts = list(breakfast_recipes.keys())
roast_names = ["Roast Beef", "Roast Chicken", "Roast Pork", "Roast Lamb"]

# Categorize dinners for proper ratio (45% meat, 35% fish, 20% veg)
meat_dinners = [d for d in all_dinners if any(m in d for m in ["Beef", "Chicken", "Pork", "Lamb", "Sausage", "Burger", "Steak", "Meatball", "Gammon", "Toad", "Lasagne", "Bolognese", "Cottage", "Shepherd", "Chilli", "Fajita", "Taco", "Stew", "Stroganoff", "Korma", "Tikka", "Thai", "Curry", "Katsu", "Cacciatore", "Hotpot", "Moussaka", "Goujons", "Honey", "Lemon", "Pulled", "Sweet"])]
fish_dinners = [d for d in all_dinners if any(f in d for f in ["Fish", "Salmon", "Cod", "Prawn", "Tuna", "Haddock"])]
veg_dinners = [d for d in all_dinners if d in ["Cauliflower Cheese", "Mushroom Risotto", "Vegetable Curry", "Macaroni Cheese", "Vegetable Stir-fry", "Vegetable Lasagne", "Cheese & Onion Pie", "Spinach & Ricotta Cannelloni", "Stuffed Peppers", "Vegetable Fajitas"]]

# Build 52 weeks of meals
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

    # Build lunches
    lunches = []
    for d in week_days:
        lunches.append((d, all_lunches[lunch_idx % len(all_lunches)]))
        lunch_idx += 1

    # Build dinners with proper ratio (approx 3 meat, 2 fish, 2 veg per week)
    dinners = []
    dinner_pattern = ["meat", "fish", "veg", "meat", "fish", "meat", "veg"]  # 3 meat, 2 fish, 2 veg

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
# HTML GENERATION
# ============================================================

def generate_recipe_html(name, recipe):
    ingredients_html = "".join([f"<li>{ing}</li>" for ing in recipe["ingredients"]])
    return f'''
    <div class="recipe-card">
        <div class="recipe-header">
            <h3>{name}</h3>
            <span class="recipe-meta">{recipe["time"]} | Serves {recipe["serves"]}</span>
        </div>
        <div class="recipe-body">
            <div class="ingredients">
                <strong>Ingredients:</strong>
                <ul>{ingredients_html}</ul>
            </div>
            <div class="method">
                <strong>Method:</strong>
                <p>{recipe["method"]}</p>
            </div>
        </div>
    </div>'''

def generate_week_html(week_num, data):
    breakfast_html = generate_recipe_html(data["breakfast"], breakfast_recipes[data["breakfast"]])

    lunches_html = ""
    for day, meal in data["lunches"]:
        if meal in lunch_recipes:
            lunches_html += f'<div class="day-meal"><span class="day-label">{day}</span>{generate_recipe_html(meal, lunch_recipes[meal])}</div>'

    dinners_html = ""
    for day, meal in data["dinners"]:
        if meal == "Sunday Roast":
            dinners_html += f'<div class="day-meal sunday-roast"><span class="day-label">{day}</span><p class="see-roast">See Sunday Roast section below</p></div>'
        elif meal in dinner_recipes:
            dinners_html += f'<div class="day-meal"><span class="day-label">{day}</span>{generate_recipe_html(meal, dinner_recipes[meal])}</div>'

    roast_html = ""
    if data["roast"]:
        roast_html = f'''
        <div class="section roast-section">
            <h2>Sunday Roast (for 7)</h2>
            {generate_recipe_html(data["roast"], roast_recipes[data["roast"]])}
            <h3 class="sides-header">Sides</h3>
            {generate_recipe_html("Roast Potatoes", roast_recipes["Roast Potatoes"])}
            {generate_recipe_html("Yorkshire Puddings", roast_recipes["Yorkshire Puddings"])}
            {generate_recipe_html("Onion Gravy", roast_recipes["Onion Gravy"])}
        </div>'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Week {week_num} Recipes - 2026 Meal Calendar</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f5f5; padding: 10px; line-height: 1.4; font-size: 14px; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        .header {{ background: linear-gradient(135deg, #2c5530, #4a7c50); color: white; padding: 20px; border-radius: 10px; text-align: center; margin-bottom: 15px; }}
        .header h1 {{ font-size: 1.5em; margin-bottom: 5px; }}
        .section {{ background: white; border-radius: 10px; padding: 15px; margin-bottom: 15px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        .section h2 {{ color: #2c5530; border-bottom: 2px solid #e8f5e9; padding-bottom: 8px; margin-bottom: 15px; }}
        .day-meal {{ margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px solid #eee; }}
        .day-meal:last-child {{ border-bottom: none; }}
        .day-label {{ display: inline-block; background: #2c5530; color: white; padding: 3px 10px; border-radius: 15px; font-size: 12px; font-weight: bold; margin-bottom: 8px; }}
        .recipe-card {{ background: #fafafa; border-radius: 8px; overflow: hidden; }}
        .recipe-header {{ background: #e8f5e9; padding: 10px 12px; }}
        .recipe-header h3 {{ color: #2c5530; font-size: 1.1em; margin-bottom: 3px; }}
        .recipe-meta {{ color: #666; font-size: 12px; }}
        .recipe-body {{ padding: 12px; }}
        .ingredients ul {{ margin: 5px 0 10px 20px; font-size: 13px; }}
        .ingredients li {{ margin-bottom: 2px; }}
        .method p {{ font-size: 13px; line-height: 1.5; }}
        .roast-section {{ background: linear-gradient(135deg, #fff5f5, #ffe8e8); }}
        .roast-section h2 {{ color: #c62828; border-color: #ffcdd2; }}
        .sides-header {{ color: #c62828; margin: 20px 0 10px 0; font-size: 1.1em; }}
        .see-roast {{ background: #ffebee; padding: 10px; border-radius: 5px; color: #c62828; font-style: italic; }}
        .back {{ display: inline-block; margin-bottom: 15px; color: #2c5530; text-decoration: none; padding: 8px 15px; background: white; border-radius: 20px; font-size: 14px; }}
        .breakfast-section {{ background: linear-gradient(135deg, #fffde7, #fff9c4); }}
        .breakfast-section h2 {{ color: #f57f17; border-color: #ffee58; }}
        @media (max-width: 600px) {{ body {{ padding: 5px; font-size: 13px; }} .section {{ padding: 10px; }} }}
    </style>
</head>
<body>
    <div class="container">
        <a href="index.html" class="back">&#8592; All Weeks</a>
        <div class="header">
            <h1>Week {week_num}</h1>
            <div>{data["dates"]}</div>
        </div>
        <div class="section breakfast-section">
            <h2>Weekend Breakfast</h2>
            {breakfast_html}
        </div>
        <div class="section">
            <h2>Lunches</h2>
            {lunches_html}
        </div>
        <div class="section">
            <h2>Dinners</h2>
            {dinners_html}
        </div>
        {roast_html}
    </div>
</body>
</html>'''
    return html

def generate_index_html():
    weeks_list = ""
    for week_num in range(1, 53):
        data = weeks_data[week_num]
        roast_badge = ' <span class="badge">Roast</span>' if data["roast"] else ""
        weeks_list += f'''
        <a href="week-{week_num:02d}.html" class="week-card">
            <span class="week-num">Week {week_num}</span>
            <span class="week-dates">{data["dates"]}</span>
            {roast_badge}
        </a>'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>2026 Meal Calendar - Full Recipes</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #f5f5f5; padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        h1 {{ text-align: center; color: #2c5530; margin-bottom: 5px; }}
        .subtitle {{ text-align: center; color: #666; margin-bottom: 25px; }}
        .weeks-grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 12px; }}
        .week-card {{ display: block; background: white; padding: 15px; border-radius: 8px; text-decoration: none; box-shadow: 0 2px 5px rgba(0,0,0,0.1); transition: transform 0.2s; }}
        .week-card:hover {{ transform: translateY(-2px); }}
        .week-num {{ display: block; font-weight: bold; color: #2c5530; margin-bottom: 3px; }}
        .week-dates {{ display: block; font-size: 12px; color: #666; }}
        .badge {{ display: inline-block; background: #c62828; color: white; font-size: 10px; padding: 2px 6px; border-radius: 8px; margin-top: 5px; }}
        .stats {{ text-align: center; margin-top: 20px; padding: 15px; background: white; border-radius: 10px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>2026 Meal Calendar</h1>
        <p class="subtitle">Complete recipes for every meal - 100+ unique recipes</p>
        <div class="weeks-grid">{weeks_list}</div>
        <div class="stats">
            <strong>Recipe counts:</strong> {len(lunch_recipes)} lunches | {len(dinner_recipes)} dinners | {len(breakfast_recipes)} breakfasts | 4 roasts + sides
        </div>
    </div>
</body>
</html>'''

# ============================================================
# GENERATE FILES
# ============================================================

print("Generating 2026 Meal Calendar with 100+ recipes...")
print("=" * 50)
print(f"Lunches: {len(lunch_recipes)}")
print(f"Dinners: {len(dinner_recipes)}")
print(f"Breakfasts: {len(breakfast_recipes)}")
print(f"Roasts: 4 + 3 sides")
print("=" * 50)

with open(os.path.join(output_dir, "index.html"), 'w', encoding='utf-8') as f:
    f.write(generate_index_html())
print("Created index.html")

for week_num in range(1, 53):
    html = generate_week_html(week_num, weeks_data[week_num])
    filename = os.path.join(output_dir, f"week-{week_num:02d}.html")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created week-{week_num:02d}.html")

print("=" * 50)
print("Done! Full recipes embedded for every meal.")
