$urls = @(
    'https://www.bbcgoodfood.com/recipes/one-pot-sausage-mash',
    'https://www.bbcgoodfood.com/recipes/sausages-onion-gravy-mash',
    'https://www.bbcgoodfood.com/recipes/slow-cooker-sausage-casserole',
    'https://www.bbcgoodfood.com/recipes/ultimate-toad-in-the-hole',
    'https://www.bbcgoodfood.com/recipes/chilli',
    'https://www.bbcgoodfood.com/recipes/easy-chilli',
    'https://www.bbcgoodfood.com/recipes/slow-cooker-beef-stew',
    'https://www.bbcgoodfood.com/recipes/easy-beef-stew',
    'https://www.bbcgoodfood.com/recipes/stir-fried-chicken',
    'https://www.bbcgoodfood.com/recipes/quick-chicken-stir-fry',
    'https://www.bbcgoodfood.com/recipes/easy-mac-cheese',
    'https://www.bbcgoodfood.com/recipes/easy-macaroni-cheese',
    'https://www.bbcgoodfood.com/recipes/homemade-pizza',
    'https://www.bbcgoodfood.com/recipes/easy-pizza',
    'https://www.bbcgoodfood.com/recipes/simple-fish-pie',
    'https://www.bbcgoodfood.com/recipes/roast-beef',
    'https://www.bbcgoodfood.com/recipes/roast-lamb',
    'https://www.bbcgoodfood.com/recipes/roast-leg-lamb',
    'https://www.bbcgoodfood.com/recipes/ultimate-beef-burger',
    'https://www.bbcgoodfood.com/recipes/homemade-burgers',
    'https://www.bbcgoodfood.com/recipes/slow-cooker-chilli-con-carne',
    'https://www.bbcgoodfood.com/recipes/prawn-fried-rice',
    'https://www.bbcgoodfood.com/recipes/garlic-prawn-linguine',
    'https://www.bbcgoodfood.com/recipes/easy-prawn-curry',
    'https://www.bbcgoodfood.com/recipes/teriyaki-salmon-sticky-rice',
    'https://www.bbcgoodfood.com/recipes/miso-salmon',
    'https://www.bbcgoodfood.com/recipes/easy-salmon',
    'https://www.bbcgoodfood.com/recipes/crispy-salmon',
    'https://www.bbcgoodfood.com/recipes/full-english',
    'https://www.bbcgoodfood.com/recipes/classic-fry-up',
    'https://www.bbcgoodfood.com/recipes/scrambled-egg',
    'https://www.bbcgoodfood.com/recipes/minestrone-soup',
    'https://www.bbcgoodfood.com/recipes/classic-minestrone',
    'https://www.bbcgoodfood.com/recipes/easy-chicken-noodle-soup',
    'https://www.bbcgoodfood.com/recipes/tacos',
    'https://www.bbcgoodfood.com/recipes/easy-tacos',
    'https://www.bbcgoodfood.com/recipes/chicken-quesadilla',
    'https://www.bbcgoodfood.com/recipes/spicy-prawn-tacos',
    'https://www.bbcgoodfood.com/recipes/honey-teriyaki-salmon'
)

foreach ($url in $urls) {
    try {
        $response = Invoke-WebRequest -Uri $url -Method HEAD -UseBasicParsing -TimeoutSec 5
        Write-Host "OK: $url"
    } catch {
        Write-Host "FAIL: $url"
    }
    Start-Sleep -Milliseconds 200
}
