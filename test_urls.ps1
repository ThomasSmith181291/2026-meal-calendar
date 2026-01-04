$urls = @(
    # Bolognese variations
    'https://www.bbcgoodfood.com/recipes/spaghetti-bolognese',
    'https://www.bbcgoodfood.com/recipes/bolognese-sauce',
    'https://www.bbcgoodfood.com/recipes/easy-bolognese',

    # Roasts
    'https://www.bbcgoodfood.com/recipes/roast-chicken',
    'https://www.bbcgoodfood.com/recipes/slow-roast-pork-shoulder',
    'https://www.bbcgoodfood.com/recipes/roast-leg-of-lamb-garlic-rosemary',
    'https://www.bbcgoodfood.com/recipes/simple-roast-beef',

    # Sides
    'https://www.bbcgoodfood.com/recipes/perfect-roast-potatoes',
    'https://www.bbcgoodfood.com/recipes/yorkshire-puddings',
    'https://www.bbcgoodfood.com/recipes/best-ever-yorkshire-puddings',
    'https://www.bbcgoodfood.com/recipes/onion-gravy',

    # Main dishes
    'https://www.bbcgoodfood.com/recipes/chicken-tikka-masala',
    'https://www.bbcgoodfood.com/recipes/cottage-pie',
    'https://www.bbcgoodfood.com/recipes/shepherds-pie',
    'https://www.bbcgoodfood.com/recipes/fish-pie',
    'https://www.bbcgoodfood.com/recipes/easy-fish-pie',
    'https://www.bbcgoodfood.com/recipes/lasagne',
    'https://www.bbcgoodfood.com/recipes/classic-lasagne',
    'https://www.bbcgoodfood.com/recipes/bangers-mash',
    'https://www.bbcgoodfood.com/recipes/sausage-mash',
    'https://www.bbcgoodfood.com/recipes/sausage-casserole',
    'https://www.bbcgoodfood.com/recipes/toad-in-the-hole',
    'https://www.bbcgoodfood.com/recipes/chilli-con-carne',
    'https://www.bbcgoodfood.com/recipes/beef-stew',
    'https://www.bbcgoodfood.com/recipes/beef-stew-dumplings',
    'https://www.bbcgoodfood.com/recipes/beef-stroganoff',
    'https://www.bbcgoodfood.com/recipes/chicken-fajitas',
    'https://www.bbcgoodfood.com/recipes/chicken-korma',
    'https://www.bbcgoodfood.com/recipes/chicken-stir-fry',
    'https://www.bbcgoodfood.com/recipes/easy-chicken-stir-fry',
    'https://www.bbcgoodfood.com/recipes/thai-green-curry',
    'https://www.bbcgoodfood.com/recipes/thai-green-chicken-curry',
    'https://www.bbcgoodfood.com/recipes/chicken-katsu-curry',
    'https://www.bbcgoodfood.com/recipes/chicken-pie',
    'https://www.bbcgoodfood.com/recipes/chicken-mushroom-pie',
    'https://www.bbcgoodfood.com/recipes/chicken-leek-pie',
    'https://www.bbcgoodfood.com/recipes/macaroni-cheese',
    'https://www.bbcgoodfood.com/recipes/cauliflower-cheese',
    'https://www.bbcgoodfood.com/recipes/mushroom-risotto',
    'https://www.bbcgoodfood.com/recipes/pizza-margherita',

    # Fish
    'https://www.bbcgoodfood.com/recipes/fish-chips',
    'https://www.bbcgoodfood.com/recipes/fish-finger-sandwiches',
    'https://www.bbcgoodfood.com/recipes/salmon-fishcakes',
    'https://www.bbcgoodfood.com/recipes/easy-salmon-fishcakes',
    'https://www.bbcgoodfood.com/recipes/fishcakes',
    'https://www.bbcgoodfood.com/recipes/salmon-teriyaki',
    'https://www.bbcgoodfood.com/recipes/teriyaki-salmon',
    'https://www.bbcgoodfood.com/recipes/fish-tacos',
    'https://www.bbcgoodfood.com/recipes/prawn-stir-fry',
    'https://www.bbcgoodfood.com/recipes/prawn-linguine',
    'https://www.bbcgoodfood.com/recipes/prawn-curry',
    'https://www.bbcgoodfood.com/recipes/cod-chorizo',

    # Burgers/Tacos
    'https://www.bbcgoodfood.com/recipes/beef-burgers',
    'https://www.bbcgoodfood.com/recipes/best-ever-burger',
    'https://www.bbcgoodfood.com/recipes/beef-tacos',
    'https://www.bbcgoodfood.com/recipes/turkey-tacos',
    'https://www.bbcgoodfood.com/recipes/lamb-koftas',

    # Soups
    'https://www.bbcgoodfood.com/recipes/leek-potato-soup',
    'https://www.bbcgoodfood.com/recipes/carrot-coriander-soup',
    'https://www.bbcgoodfood.com/recipes/tomato-soup',
    'https://www.bbcgoodfood.com/recipes/butternut-squash-soup',
    'https://www.bbcgoodfood.com/recipes/chicken-soup',
    'https://www.bbcgoodfood.com/recipes/minestrone',

    # Breakfasts
    'https://www.bbcgoodfood.com/recipes/full-english-breakfast',
    'https://www.bbcgoodfood.com/recipes/eggs-benedict',
    'https://www.bbcgoodfood.com/recipes/eggs-florentine',
    'https://www.bbcgoodfood.com/recipes/shakshuka',
    'https://www.bbcgoodfood.com/recipes/pancakes',
    'https://www.bbcgoodfood.com/recipes/american-pancakes',
    'https://www.bbcgoodfood.com/recipes/french-toast',
    'https://www.bbcgoodfood.com/recipes/scrambled-eggs',
    'https://www.bbcgoodfood.com/recipes/perfect-scrambled-eggs',
    'https://www.bbcgoodfood.com/recipes/omelette',
    'https://www.bbcgoodfood.com/recipes/cheese-omelette',

    # Lunches
    'https://www.bbcgoodfood.com/recipes/welsh-rarebit',
    'https://www.bbcgoodfood.com/recipes/greek-salad',
    'https://www.bbcgoodfood.com/recipes/club-sandwich',
    'https://www.bbcgoodfood.com/recipes/croque-monsieur',
    'https://www.bbcgoodfood.com/recipes/egg-fried-rice',
    'https://www.bbcgoodfood.com/recipes/avocado-toast',
    'https://www.bbcgoodfood.com/recipes/quesadillas',
    'https://www.bbcgoodfood.com/recipes/cheese-quesadilla',
    'https://www.bbcgoodfood.com/recipes/tuna-pasta-salad',
    'https://www.bbcgoodfood.com/recipes/jacket-potatoes',
    'https://www.bbcgoodfood.com/recipes/jacket-potato'
)

Write-Host "Testing BBC Good Food URLs..."
Write-Host "=============================="

$valid = @()
$invalid = @()

foreach ($url in $urls) {
    try {
        $response = Invoke-WebRequest -Uri $url -Method HEAD -UseBasicParsing -TimeoutSec 10
        Write-Host "OK: $url"
        $valid += $url
    } catch {
        Write-Host "FAIL: $url"
        $invalid += $url
    }
    Start-Sleep -Milliseconds 300
}

Write-Host ""
Write-Host "=============================="
Write-Host "VALID URLs ($($valid.Count)):"
foreach ($url in $valid) {
    Write-Host "  $url"
}
Write-Host ""
Write-Host "INVALID URLs ($($invalid.Count)):"
foreach ($url in $invalid) {
    Write-Host "  $url"
}
