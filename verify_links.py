"""
Verify all BBC Good Food recipe links are valid
"""

import urllib.request
import urllib.error
import ssl
import time

# All unique recipe URLs from generate_pages.py
urls = [
    # Lunches
    ("Tuna mayo jacket potato", "https://www.bbcgoodfood.com/recipes/easy-tuna-mayo-jacket"),
    ("Minestrone soup", "https://www.bbcgoodfood.com/recipes/minestrone-soup"),
    ("Cheese & onion quesadilla", "https://www.bbcgoodfood.com/recipes/quesadillas"),
    ("Leek & potato soup", "https://www.bbcgoodfood.com/recipes/leek-potato-soup"),
    ("Grilled cheese with tomato soup", "https://www.bbcgoodfood.com/recipes/grilled-cheese-tomato-soup"),
    ("Omelette", "https://www.bbcgoodfood.com/recipes/omelette"),
    ("Chicken soup", "https://www.bbcgoodfood.com/recipes/chicken-soup"),
    ("Welsh rarebit", "https://www.bbcgoodfood.com/recipes/welsh-rarebit"),
    ("Smoked mackerel pate", "https://www.bbcgoodfood.com/recipes/smoked-mackerel-pate"),
    ("Coronation chicken sandwich", "https://www.bbcgoodfood.com/recipes/coronation-chicken-sandwich"),
    ("Carrot & coriander soup", "https://www.bbcgoodfood.com/recipes/carrot-coriander-soup"),
    ("Scrambled eggs on toast", "https://www.bbcgoodfood.com/recipes/scrambled-eggs-toast"),
    ("Tuna pasta salad", "https://www.bbcgoodfood.com/recipes/tuna-pasta-salad"),
    ("Greek salad", "https://www.bbcgoodfood.com/recipes/greek-salad"),
    ("Butternut squash soup", "https://www.bbcgoodfood.com/recipes/butternut-squash-soup"),
    ("Chicken Caesar wraps", "https://www.bbcgoodfood.com/recipes/chicken-caesar-wraps"),
    ("Prawn cocktail", "https://www.bbcgoodfood.com/recipes/prawn-cocktail"),
    ("Egg fried rice", "https://www.bbcgoodfood.com/recipes/egg-fried-rice"),
    ("Club sandwich", "https://www.bbcgoodfood.com/recipes/club-sandwich"),
    ("Tomato soup", "https://www.bbcgoodfood.com/recipes/tomato-soup"),
    ("Croque monsieur", "https://www.bbcgoodfood.com/recipes/croque-monsieur"),
    ("Avocado toast", "https://www.bbcgoodfood.com/recipes/avocado-toast"),
    ("Fish finger sandwich", "https://www.bbcgoodfood.com/recipes/fish-finger-sandwich"),
    ("Bruschetta", "https://www.bbcgoodfood.com/recipes/bruschetta"),

    # Teas/Dinners
    ("Spaghetti Bolognese", "https://www.bbcgoodfood.com/recipes/best-spaghetti-bolognese-recipe"),
    ("Teriyaki salmon", "https://www.bbcgoodfood.com/recipes/teriyaki-salmon"),
    ("Vegetable curry", "https://www.bbcgoodfood.com/recipes/vegetable-curry"),
    ("Chicken fajitas", "https://www.bbcgoodfood.com/recipes/chicken-fajitas"),
    ("Oven baked fish chips", "https://www.bbcgoodfood.com/recipes/oven-baked-fish-chips"),
    ("Best beef burgers", "https://www.bbcgoodfood.com/recipes/best-beef-burgers"),
    ("Thai green chicken curry", "https://www.bbcgoodfood.com/recipes/thai-green-chicken-curry"),
    ("Cottage pie", "https://www.bbcgoodfood.com/recipes/cottage-pie"),
    ("Prawn linguine", "https://www.bbcgoodfood.com/recipes/prawn-linguine"),
    ("Best macaroni cheese", "https://www.bbcgoodfood.com/recipes/best-macaroni-cheese"),
    ("Pork chops with apples", "https://www.bbcgoodfood.com/recipes/pork-chops-apples"),
    ("Cod parsley sauce", "https://www.bbcgoodfood.com/recipes/cod-parsley-sauce"),
    ("Lamb koftas", "https://www.bbcgoodfood.com/recipes/lamb-koftas"),
    ("Chicken stir-fry", "https://www.bbcgoodfood.com/recipes/chicken-stir-fry"),
    ("Beef stew with dumplings", "https://www.bbcgoodfood.com/recipes/beef-stew-dumplings"),
    ("Easy salmon fishcakes", "https://www.bbcgoodfood.com/recipes/easy-salmon-fishcakes"),
    ("Mushroom risotto", "https://www.bbcgoodfood.com/recipes/mushroom-risotto"),
    ("Bangers mash", "https://www.bbcgoodfood.com/recipes/bangers-mash"),
    ("Easy fish pie", "https://www.bbcgoodfood.com/recipes/easy-fish-pie"),
    ("Beef tacos", "https://www.bbcgoodfood.com/recipes/beef-tacos"),
    ("Toad in the hole", "https://www.bbcgoodfood.com/recipes/toad-hole"),
    ("Shepherd's pie", "https://www.bbcgoodfood.com/recipes/shepherds-pie"),
    ("Prawn stir-fry", "https://www.bbcgoodfood.com/recipes/prawn-stir-fry"),
    ("Cauliflower cheese", "https://www.bbcgoodfood.com/recipes/cauliflower-cheese"),
    ("Chicken tikka masala", "https://www.bbcgoodfood.com/recipes/chicken-tikka-masala"),
    ("Sausage casserole", "https://www.bbcgoodfood.com/recipes/sausage-casserole"),
    ("Pizza margherita", "https://www.bbcgoodfood.com/recipes/pizza-margherita-4-easy-steps"),
    ("Classic lasagne", "https://www.bbcgoodfood.com/recipes/classic-lasagne"),
    ("Salmon pasta bake", "https://www.bbcgoodfood.com/recipes/salmon-pasta-bake"),
    ("Vegetable stir-fry", "https://www.bbcgoodfood.com/recipes/vegetable-stir-fry"),
    ("Chicken & leek pie", "https://www.bbcgoodfood.com/recipes/chicken-leek-pie"),
    ("Easy fishcakes", "https://www.bbcgoodfood.com/recipes/easy-fishcakes"),
    ("Beef stroganoff", "https://www.bbcgoodfood.com/recipes/beef-stroganoff"),
    ("Chilli con carne", "https://www.bbcgoodfood.com/recipes/chilli-con-carne-recipe"),
    ("Meatballs in tomato sauce", "https://www.bbcgoodfood.com/recipes/meatballs-tomato-sauce"),
    ("Teriyaki salmon noodles", "https://www.bbcgoodfood.com/recipes/teriyaki-salmon-noodles"),
    ("Cheese & onion pie", "https://www.bbcgoodfood.com/recipes/cheese-onion-pie"),
    ("Chicken korma", "https://www.bbcgoodfood.com/recipes/chicken-korma"),
    ("Breaded fish", "https://www.bbcgoodfood.com/recipes/breaded-fish"),
    ("Pork meatballs", "https://www.bbcgoodfood.com/recipes/pork-meatballs"),
    ("Chicken fajita bowl", "https://www.bbcgoodfood.com/recipes/chicken-fajita-bowl"),
    ("Cod & chorizo stew", "https://www.bbcgoodfood.com/recipes/cod-chorizo-stew"),
    ("Spinach ricotta cannelloni", "https://www.bbcgoodfood.com/recipes/spinach-ricotta-cannelloni"),
    ("Chicken katsu curry", "https://www.bbcgoodfood.com/recipes/chicken-katsu-curry"),
    ("Smoked haddock risotto", "https://www.bbcgoodfood.com/recipes/smoked-haddock-risotto"),
    ("Lamb chops with mint sauce", "https://www.bbcgoodfood.com/recipes/lamb-chops-mint-sauce"),
    ("Chicken burgers", "https://www.bbcgoodfood.com/recipes/chicken-burgers"),
    ("Bolognese bake", "https://www.bbcgoodfood.com/recipes/bolognese-bake"),
    ("Prawn curry", "https://www.bbcgoodfood.com/recipes/prawn-curry"),
    ("Roasted vegetable pasta", "https://www.bbcgoodfood.com/recipes/roasted-vegetable-pasta"),
    ("Gammon egg chips", "https://www.bbcgoodfood.com/recipes/gammon-egg-chips"),
    ("Fish tacos", "https://www.bbcgoodfood.com/recipes/fish-tacos"),
    ("Turkey tacos", "https://www.bbcgoodfood.com/recipes/turkey-tacos"),
    ("Chicken & mushroom pie", "https://www.bbcgoodfood.com/recipes/chicken-mushroom-pie"),

    # Breakfasts
    ("Ultimate full English", "https://www.bbcgoodfood.com/recipes/ultimate-full-english"),
    ("Eggs Benedict", "https://www.bbcgoodfood.com/recipes/eggs-benedict"),
    ("Easy pancakes", "https://www.bbcgoodfood.com/recipes/easy-pancakes"),
    ("Shakshuka", "https://www.bbcgoodfood.com/recipes/shakshuka"),
    ("French toast", "https://www.bbcgoodfood.com/recipes/french-toast"),
    ("Eggs Florentine", "https://www.bbcgoodfood.com/recipes/eggs-florentine"),
    ("Scrambled eggs smoked salmon", "https://www.bbcgoodfood.com/recipes/scrambled-eggs-smoked-salmon"),
    ("Easy American pancakes", "https://www.bbcgoodfood.com/recipes/easy-american-pancakes"),
    ("Eggs Royale", "https://www.bbcgoodfood.com/recipes/eggs-royale"),
    ("Croissant French toast", "https://www.bbcgoodfood.com/recipes/croissant-french-toast"),
    ("Omelette Arnold Bennett", "https://www.bbcgoodfood.com/recipes/omelette-arnold-bennett"),

    # Roasts
    ("Best roast beef", "https://www.bbcgoodfood.com/recipes/best-roast-beef"),
    ("Perfect roast chicken", "https://www.bbcgoodfood.com/recipes/perfect-roast-chicken"),
    ("Roast pork crackling", "https://www.bbcgoodfood.com/recipes/roast-pork-crackling"),
    ("Roast leg of lamb", "https://www.bbcgoodfood.com/recipes/roast-leg-lamb"),

    # Roast sides
    ("Ultimate roast potatoes", "https://www.bbcgoodfood.com/recipes/ultimate-roast-potatoes"),
    ("Yorkshire puddings", "https://www.bbcgoodfood.com/recipes/yorkshire-puddings"),
    ("Proper gravy", "https://www.bbcgoodfood.com/recipes/proper-gravy"),
]

def check_url(name, url):
    """Check if a URL returns 200 status"""
    try:
        # Create SSL context that doesn't verify certificates (for simplicity)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        response = urllib.request.urlopen(req, timeout=10, context=ctx)
        status = response.getcode()
        if status == 200:
            return True, status
        else:
            return False, status
    except urllib.error.HTTPError as e:
        return False, e.code
    except urllib.error.URLError as e:
        return False, str(e.reason)
    except Exception as e:
        return False, str(e)

print("Verifying BBC Good Food recipe links...")
print("=" * 60)

valid = []
invalid = []

for name, url in urls:
    print(f"Checking: {name}...", end=" ", flush=True)
    success, status = check_url(name, url)
    time.sleep(0.5)  # Be nice to the server

    if success:
        print("OK")
        valid.append((name, url))
    else:
        print(f"FAILED ({status})")
        invalid.append((name, url, status))

print("=" * 60)
print(f"\nResults: {len(valid)} valid, {len(invalid)} invalid")

if invalid:
    print("\nINVALID LINKS:")
    for name, url, status in invalid:
        print(f"  - {name}: {url} (Error: {status})")
else:
    print("\nAll links are valid!")
