from datetime import datetime, timedelta
from typing import List, Dict, Optional

# Black Friday date
BLACK_FRIDAY = datetime(2026, 11, 27, 0, 0, 0)

# Category structure with subcategories
CATEGORIES = {
    "Elektronik": {
        "subcategories": ["Datorer & Laptops", "Mobiler & Surfplattor", "TV & Ljud", "Smartklockor", "Gaming"],
        "icon": "💻"
    },
    "Mode": {
        "subcategories": ["Skor", "Kläder", "Accessoarer", "Sport & Träning"],
        "icon": "👟"
    },
    "Hem & Hushåll": {
        "subcategories": ["Kök", "Städning", "Möbler", "Inredning"],
        "icon": "🏠"
    },
    "Skönhet": {
        "subcategories": ["Hårvård", "Hudvård", "Makeup", "Parfym"],
        "icon": "💄"
    },
    "Sport & Fritid": {
        "subcategories": ["Träningsutrustning", "Utomhus", "Cykel", "Vintersport"],
        "icon": "⚽"
    }
}

# Generate price history (last 30 days)
def generate_price_history(current_price: float, original_price: float) -> List[Dict]:
    """Generate realistic price history for the last 30 days."""
    history = []
    today = datetime.now()

    # Start from 30 days ago at original price
    for days_ago in range(30, -1, -1):
        date = today - timedelta(days=days_ago)

        # Gradual price drop over time, with Black Friday being the lowest
        if days_ago > 20:
            price = original_price
        elif days_ago > 10:
            # Slight drop
            price = original_price - (original_price - current_price) * 0.3
        elif days_ago > 5:
            # Bigger drop
            price = original_price - (original_price - current_price) * 0.6
        else:
            # Black Friday price
            price = current_price

        history.append({
            "date": date.strftime("%Y-%m-%d"),
            "price": round(price, 2)
        })

    return history

# Curated premium deals with multiple stores and price comparison
deals_db = [
    {
        "id": 1,
        "name": "Apple MacBook Pro 16\" M3 Max",
        "original_price": 42995,
        "category": "Elektronik",
        "subcategory": "Datorer & Laptops",
        "image_url": "https://images.unsplash.com/photo-1611186871348-b1ce696e52c9?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "16-tums MacBook Pro med M3 Max-chip, 36GB RAM, 1TB SSD. Perfekt för krävande professionella uppgifter.",
        "stores": [
            {"store": "Webhallen", "price": 34895, "url": "https://webhallen.se/macbook-pro", "in_stock": True},
            {"store": "Apple Store", "price": 34995, "url": "https://apple.com/macbook-pro", "in_stock": True},
            {"store": "Media Markt", "price": 35990, "url": "https://mediamarkt.se/macbook-pro", "in_stock": True},
            {"store": "Elgiganten", "price": 35790, "url": "https://elgiganten.se/macbook-pro", "in_stock": True}
        ],
        "price_history": generate_price_history(34995, 42995)
    },
    {
        "id": 2,
        "name": "Sony WH-1000XM5 Wireless Headphones",
        "original_price": 4490,
        "category": "Elektronik",
        "subcategory": "TV & Ljud",
        "image_url": "https://images.unsplash.com/photo-1618366712010-f4ae9c647dcb?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Branschledande brusreducering, exceptionell ljudkvalitet och 30 timmars batteritid.",
        "stores": [
            {"store": "Webhallen", "price": 2890, "url": "https://webhallen.se/sony-wh1000xm5", "in_stock": True},
            {"store": "Media Markt", "price": 2990, "url": "https://mediamarkt.se/sony-wh1000xm5", "in_stock": True},
            {"store": "NetOnNet", "price": 3090, "url": "https://netonnet.se/sony-wh1000xm5", "in_stock": True},
            {"store": "Elgiganten", "price": 3190, "url": "https://elgiganten.se/sony-wh1000xm5", "in_stock": True}
        ],
        "price_history": generate_price_history(2990, 4490)
    },
    {
        "id": 3,
        "name": "Nike Air Jordan 1 Retro High",
        "original_price": 1899,
        "category": "Mode",
        "subcategory": "Skor",
        "image_url": "https://images.unsplash.com/photo-1556906781-9a412961c28c?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Ikoniska Air Jordan 1 i klassisk high-top design. Tidlös stil och komfort.",
        "stores": [
            {"store": "Nike", "price": 1299, "url": "https://nike.com/air-jordan-1", "in_stock": True},
            {"store": "Foot Locker", "price": 1399, "url": "https://footlocker.se/air-jordan-1", "in_stock": True},
            {"store": "Zalando", "price": 1349, "url": "https://zalando.se/air-jordan-1", "in_stock": False}
        ],
        "price_history": generate_price_history(1299, 1899)
    },
    {
        "id": 4,
        "name": "Samsung 65\" OLED 4K Smart TV",
        "original_price": 24990,
        "category": "Elektronik",
        "subcategory": "TV & Ljud",
        "image_url": "https://images.unsplash.com/photo-1601944177325-f8867652837f?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "65-tums OLED-TV med 4K-upplösning, HDR10+ och smart TV-funktioner. Perfekt svärta och fantastiska färger.",
        "stores": [
            {"store": "Elgiganten", "price": 17490, "url": "https://elgiganten.se/samsung-oled", "in_stock": True},
            {"store": "NetOnNet", "price": 17590, "url": "https://netonnet.se/samsung-oled", "in_stock": True},
            {"store": "Media Markt", "price": 17990, "url": "https://mediamarkt.se/samsung-oled", "in_stock": True},
            {"store": "Webhallen", "price": 18290, "url": "https://webhallen.se/samsung-oled", "in_stock": False}
        ],
        "price_history": generate_price_history(17990, 24990)
    },
    {
        "id": 5,
        "name": "Dyson Airwrap Complete",
        "original_price": 5990,
        "category": "Skönhet",
        "subcategory": "Hårvård",
        "image_url": "https://images.unsplash.com/photo-1627225925683-91c79f83fe0c?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Multifunktionell hårstyler med Coanda-effekt. Locka, forma och torka håret utan extremvärme.",
        "stores": [
            {"store": "Åhléns", "price": 4290, "url": "https://ahlens.se/dyson-airwrap", "in_stock": True},
            {"store": "Media Markt", "price": 4390, "url": "https://mediamarkt.se/dyson-airwrap", "in_stock": True},
            {"store": "Elgiganten", "price": 4490, "url": "https://elgiganten.se/dyson-airwrap", "in_stock": True}
        ],
        "price_history": generate_price_history(4490, 5990)
    },
    {
        "id": 6,
        "name": "iPad Pro 12.9\" M2 256GB",
        "original_price": 15995,
        "category": "Elektronik",
        "subcategory": "Mobiler & Surfplattor",
        "image_url": "https://images.unsplash.com/photo-1544244015-0df4b3ffc6b0?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "12.9-tums iPad Pro med M2-chip och Liquid Retina XDR-skärm. Professionell prestanda i surfplatte-format.",
        "stores": [
            {"store": "NetOnNet", "price": 12495, "url": "https://netonnet.se/ipad-pro", "in_stock": True},
            {"store": "Apple Store", "price": 12695, "url": "https://apple.com/ipad-pro", "in_stock": True},
            {"store": "Elgiganten", "price": 12890, "url": "https://elgiganten.se/ipad-pro", "in_stock": True},
            {"store": "Media Markt", "price": 12990, "url": "https://mediamarkt.se/ipad-pro", "in_stock": False}
        ],
        "price_history": generate_price_history(12995, 15995)
    },
    {
        "id": 7,
        "name": "Adidas Ultraboost 23 Running Shoes",
        "original_price": 1899,
        "category": "Mode",
        "subcategory": "Skor",
        "image_url": "https://images.unsplash.com/photo-1562183241-b937e95585b6?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Premium löparsko med Boost-dämpning och Primeknit-ovandel. Maximal komfort och energiåtergivning.",
        "stores": [
            {"store": "Adidas", "price": 1199, "url": "https://adidas.se/ultraboost", "in_stock": True},
            {"store": "Stadium", "price": 1249, "url": "https://stadium.se/ultraboost", "in_stock": True},
            {"store": "Zalando", "price": 1229, "url": "https://zalando.se/ultraboost", "in_stock": True}
        ],
        "price_history": generate_price_history(1199, 1899)
    },
    {
        "id": 8,
        "name": "Bose QuietComfort Ultra Earbuds",
        "original_price": 3490,
        "category": "Elektronik",
        "subcategory": "TV & Ljud",
        "image_url": "https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Trådlösa earbuds med världsledande brusreducering och spatial audio. Premium ljudkvalitet.",
        "stores": [
            {"store": "Webhallen", "price": 2390, "url": "https://webhallen.se/bose-qc-ultra", "in_stock": True},
            {"store": "NetOnNet", "price": 2490, "url": "https://netonnet.se/bose-qc-ultra", "in_stock": True},
            {"store": "Elgiganten", "price": 2590, "url": "https://elgiganten.se/bose-qc-ultra", "in_stock": True},
            {"store": "Media Markt", "price": 2690, "url": "https://mediamarkt.se/bose-qc-ultra", "in_stock": False}
        ],
        "price_history": generate_price_history(2490, 3490)
    },
    {
        "id": 9,
        "name": "Le Creuset Dutch Oven 5.5L",
        "original_price": 3295,
        "category": "Hem & Hushåll",
        "subcategory": "Kök",
        "image_url": "https://images.unsplash.com/photo-1585515320310-259814833e62?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Klassisk gjutjärnsgryta med emaljerad yta. Perfekt för långkok, grytor och brödbakning.",
        "stores": [
            {"store": "NK", "price": 2295, "url": "https://nk.se/le-creuset", "in_stock": True},
            {"store": "Åhléns", "price": 2395, "url": "https://ahlens.se/le-creuset", "in_stock": True},
            {"store": "Cervera", "price": 2345, "url": "https://cervera.se/le-creuset", "in_stock": True}
        ],
        "price_history": generate_price_history(2295, 3295)
    },
    {
        "id": 10,
        "name": "Apple Watch Ultra 2",
        "original_price": 9995,
        "category": "Elektronik",
        "subcategory": "Smartklockor",
        "image_url": "https://images.unsplash.com/photo-1579586337278-3befd40fd17a?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Extrem smartklocka med titaniumboett, dubbel GPS-frekvens och 36 timmars batteritid.",
        "stores": [
            {"store": "Webhallen", "price": 7695, "url": "https://webhallen.se/watch-ultra", "in_stock": True},
            {"store": "Apple Store", "price": 7795, "url": "https://apple.com/watch-ultra", "in_stock": True},
            {"store": "Elgiganten", "price": 7890, "url": "https://elgiganten.se/watch-ultra", "in_stock": True},
            {"store": "Media Markt", "price": 7990, "url": "https://mediamarkt.se/watch-ultra", "in_stock": True}
        ],
        "price_history": generate_price_history(7995, 9995)
    },
    {
        "id": 11,
        "name": "iPhone 15 Pro Max 256GB",
        "original_price": 15995,
        "category": "Elektronik",
        "subcategory": "Mobiler & Surfplattor",
        "image_url": "https://images.unsplash.com/photo-1695048064808-981f98c01e32?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "iPhone 15 Pro Max med A17 Pro-chip, titaniumdesign och 48MP kamera. 256GB lagring.",
        "stores": [
            {"store": "Telia", "price": 13495, "url": "https://telia.se/iphone-15-pro", "in_stock": True},
            {"store": "Apple Store", "price": 13695, "url": "https://apple.com/iphone-15-pro", "in_stock": True},
            {"store": "Tele2", "price": 13795, "url": "https://tele2.se/iphone-15-pro", "in_stock": True},
            {"store": "Elgiganten", "price": 13990, "url": "https://elgiganten.se/iphone-15-pro", "in_stock": True}
        ],
        "price_history": generate_price_history(13995, 15995)
    },
    {
        "id": 12,
        "name": "Samsung Galaxy S24 Ultra 512GB",
        "original_price": 15990,
        "category": "Elektronik",
        "subcategory": "Mobiler & Surfplattor",
        "image_url": "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Samsung Galaxy S24 Ultra med S Pen, 200MP kamera och 512GB lagring. Snapdragon 8 Gen 3.",
        "stores": [
            {"store": "Samsung", "price": 12990, "url": "https://samsung.com/galaxy-s24", "in_stock": True},
            {"store": "Elgiganten", "price": 13490, "url": "https://elgiganten.se/galaxy-s24", "in_stock": True},
            {"store": "Media Markt", "price": 13290, "url": "https://mediamarkt.se/galaxy-s24", "in_stock": True},
            {"store": "Webhallen", "price": 13190, "url": "https://webhallen.se/galaxy-s24", "in_stock": True}
        ],
        "price_history": generate_price_history(12990, 15990)
    },
    {
        "id": 13,
        "name": "AirPods Pro 2nd Gen",
        "original_price": 2995,
        "category": "Elektronik",
        "subcategory": "TV & Ljud",
        "image_url": "https://images.unsplash.com/photo-1600294037681-c80b4cb5b434?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "AirPods Pro med aktiv brusreducering, Spatial Audio och USB-C laddningsetui.",
        "stores": [
            {"store": "Apple Store", "price": 2295, "url": "https://apple.com/airpods-pro", "in_stock": True},
            {"store": "Media Markt", "price": 2345, "url": "https://mediamarkt.se/airpods-pro", "in_stock": True},
            {"store": "Elgiganten", "price": 2390, "url": "https://elgiganten.se/airpods-pro", "in_stock": True},
            {"store": "NetOnNet", "price": 2395, "url": "https://netonnet.se/airpods-pro", "in_stock": False}
        ],
        "price_history": generate_price_history(2495, 2995)
    },
    {
        "id": 14,
        "name": "LG 55\" OLED C3 4K Smart TV",
        "original_price": 16990,
        "category": "Elektronik",
        "subcategory": "TV & Ljud",
        "image_url": "https://images.unsplash.com/photo-1593784991095-a205069470b6?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "LG OLED C3 med α9 Gen 6 processor, Dolby Vision IQ och 120Hz för gaming.",
        "stores": [
            {"store": "Elgiganten", "price": 12490, "url": "https://elgiganten.se/lg-c3", "in_stock": True},
            {"store": "NetOnNet", "price": 12590, "url": "https://netonnet.se/lg-c3", "in_stock": True},
            {"store": "Webhallen", "price": 12790, "url": "https://webhallen.se/lg-c3", "in_stock": True},
            {"store": "Media Markt", "price": 12990, "url": "https://mediamarkt.se/lg-c3", "in_stock": True}
        ],
        "price_history": generate_price_history(12990, 16990)
    },
    {
        "id": 15,
        "name": "New Balance 2002R Protection Pack",
        "original_price": 1699,
        "category": "Mode",
        "subcategory": "Skor",
        "image_url": "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "New Balance 2002R i premium suede och mesh. Retro-stil med modern komfort.",
        "stores": [
            {"store": "New Balance", "price": 1199, "url": "https://newbalance.se/2002r", "in_stock": True},
            {"store": "Zalando", "price": 1249, "url": "https://zalando.se/2002r", "in_stock": True},
            {"store": "Foot Locker", "price": 1299, "url": "https://footlocker.se/2002r", "in_stock": False}
        ],
        "price_history": generate_price_history(1199, 1699)
    },
    {
        "id": 16,
        "name": "Canada Goose Expedition Parka",
        "original_price": 11995,
        "category": "Mode",
        "subcategory": "Kläder",
        "image_url": "https://images.unsplash.com/photo-1539533018447-63fcce2678e3?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Extrem vinterrock för arktiska temperaturer. 625 fill-power dun och TEI 5 klassning.",
        "stores": [
            {"store": "NK", "price": 9495, "url": "https://nk.se/canada-goose", "in_stock": True},
            {"store": "Canada Goose", "price": 9495, "url": "https://canadagoose.se/expedition", "in_stock": True},
            {"store": "Åhléns", "price": 9795, "url": "https://ahlens.se/canada-goose", "in_stock": False}
        ],
        "price_history": generate_price_history(9995, 11995)
    },
    {
        "id": 17,
        "name": "Acne Studios Leather Jacket",
        "original_price": 8495,
        "category": "Mode",
        "subcategory": "Kläder",
        "image_url": "https://images.unsplash.com/photo-1521223890158-f9f7c3d5d504?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Minimalistisk skinnjacka i premium nappa-läder. Klassisk biker-stil från Acne Studios.",
        "stores": [
            {"store": "NK", "price": 6695, "url": "https://nk.se/acne-studios", "in_stock": True},
            {"store": "Acne Studios", "price": 6695, "url": "https://acnestudios.com/leather", "in_stock": True},
            {"store": "Åhléns", "price": 6895, "url": "https://ahlens.se/acne-studios", "in_stock": False}
        ],
        "price_history": generate_price_history(6995, 8495)
    },
    {
        "id": 18,
        "name": "Ray-Ban Wayfarer Classic",
        "original_price": 1595,
        "category": "Mode",
        "subcategory": "Accessoarer",
        "image_url": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Ikoniska Wayfarer solglasögon med G-15 linser. Tidlös design sedan 1952.",
        "stores": [
            {"store": "Smarteyes", "price": 1095, "url": "https://smarteyes.se/ray-ban", "in_stock": True},
            {"store": "Synoptik", "price": 1195, "url": "https://synoptik.se/ray-ban", "in_stock": True},
            {"store": "Specsavers", "price": 1095, "url": "https://specsavers.se/ray-ban", "in_stock": True}
        ],
        "price_history": generate_price_history(1095, 1595)
    },
    {
        "id": 19,
        "name": "KitchenAid Artisan Köksmaskin",
        "original_price": 5995,
        "category": "Hem & Hushåll",
        "subcategory": "Kök",
        "image_url": "https://images.unsplash.com/photo-1570222094114-d054a817e56b?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "KitchenAid Artisan med 4.8L skål och planetarisk rörelse. 300W motor och 10 hastigheter.",
        "stores": [
            {"store": "Elgiganten", "price": 4295, "url": "https://elgiganten.se/kitchenaid", "in_stock": True},
            {"store": "Cervera", "price": 4395, "url": "https://cervera.se/kitchenaid", "in_stock": True},
            {"store": "Media Markt", "price": 4490, "url": "https://mediamarkt.se/kitchenaid", "in_stock": True}
        ],
        "price_history": generate_price_history(4495, 5995)
    },
    {
        "id": 20,
        "name": "Dyson V15 Detect Absolute",
        "original_price": 7990,
        "category": "Hem & Hushåll",
        "subcategory": "Städning",
        "image_url": "https://images.unsplash.com/photo-1558317374-067fb2f1b562?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Dyson V15 med laserdetektion som visar osynligt damm. 60 minuters batteritid.",
        "stores": [
            {"store": "Dustin", "price": 5790, "url": "https://dustin.se/dyson-v15", "in_stock": True},
            {"store": "Elgiganten", "price": 5990, "url": "https://elgiganten.se/dyson-v15", "in_stock": True},
            {"store": "NetOnNet", "price": 5990, "url": "https://netonnet.se/dyson-v15", "in_stock": True},
            {"store": "Media Markt", "price": 6190, "url": "https://mediamarkt.se/dyson-v15", "in_stock": False}
        ],
        "price_history": generate_price_history(5990, 7990)
    },
    {
        "id": 21,
        "name": "MAC Cosmetics Lipstick Set",
        "original_price": 795,
        "category": "Skönhet",
        "subcategory": "Makeup",
        "image_url": "https://images.unsplash.com/photo-1631214524020-7e18db9a8f92?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "MAC Cosmetics läppstiftsset med 5 klassiska nyanser. Långvarig formula.",
        "stores": [
            {"store": "Åhléns", "price": 495, "url": "https://ahlens.se/mac-lipstick", "in_stock": True},
            {"store": "NK", "price": 545, "url": "https://nk.se/mac-lipstick", "in_stock": True},
            {"store": "Kicks", "price": 495, "url": "https://kicks.se/mac-lipstick", "in_stock": True}
        ],
        "price_history": generate_price_history(495, 795)
    },
    {
        "id": 22,
        "name": "NARS Orgasm Blush",
        "original_price": 395,
        "category": "Skönhet",
        "subcategory": "Makeup",
        "image_url": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Ikonisk NARS Orgasm rouge i peachy-pink med guld shimmer.",
        "stores": [
            {"store": "Kicks", "price": 295, "url": "https://kicks.se/nars-orgasm", "in_stock": True},
            {"store": "Åhléns", "price": 315, "url": "https://ahlens.se/nars-orgasm", "in_stock": True},
            {"store": "NK", "price": 295, "url": "https://nk.se/nars-orgasm", "in_stock": False}
        ],
        "price_history": generate_price_history(295, 395)
    },
    {
        "id": 23,
        "name": "Peloton Bike+",
        "original_price": 24995,
        "category": "Sport & Fritid",
        "subcategory": "Träningsutrustning",
        "image_url": "https://images.unsplash.com/photo-1556817411-31ae72fa3ea0?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Peloton Bike+ med roterande 24-tums HD-skärm och Auto-Follow motstånd.",
        "stores": [
            {"store": "Peloton", "price": 19995, "url": "https://onepeloton.se/bike", "in_stock": True},
            {"store": "Gymgrossisten", "price": 20495, "url": "https://gymgrossisten.se/peloton", "in_stock": False}
        ],
        "price_history": generate_price_history(19995, 24995)
    },
    {
        "id": 24,
        "name": "Garmin Forerunner 965",
        "original_price": 7495,
        "category": "Sport & Fritid",
        "subcategory": "Träningsutrustning",
        "image_url": "https://images.unsplash.com/photo-1508685096489-7aacd43bd3b1?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Premium GPS-sportklocka med AMOLED-skärm och träningsmetrik.",
        "stores": [
            {"store": "Stadium", "price": 5995, "url": "https://stadium.se/garmin-965", "in_stock": True},
            {"store": "XXL", "price": 6195, "url": "https://xxl.se/garmin-965", "in_stock": True},
            {"store": "Elgiganten", "price": 5995, "url": "https://elgiganten.se/garmin-965", "in_stock": True}
        ],
        "price_history": generate_price_history(5995, 7495)
    },
    {
        "id": 25,
        "name": "GoPro Hero 12 Black",
        "original_price": 5495,
        "category": "Sport & Fritid",
        "subcategory": "Utomhus",
        "image_url": "https://images.unsplash.com/photo-1606041008023-472dfb5e530f?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "GoPro Hero 12 med 5.3K60 video och HyperSmooth 6.0 stabilisering.",
        "stores": [
            {"store": "Webhallen", "price": 4095, "url": "https://webhallen.se/gopro-12", "in_stock": True},
            {"store": "Elgiganten", "price": 4195, "url": "https://elgiganten.se/gopro-12", "in_stock": True},
            {"store": "Media Markt", "price": 4290, "url": "https://mediamarkt.se/gopro-12", "in_stock": True}
        ],
        "price_history": generate_price_history(4195, 5495)
    },
    {
        "id": 26,
        "name": "Lululemon Define Jacket",
        "original_price": 1595,
        "category": "Mode",
        "subcategory": "Sport & Träning",
        "image_url": "https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Lululemon Define Jacket i Luon fabric. Perfekt för yoga och vardagsbruk.",
        "stores": [
            {"store": "Lululemon", "price": 1195, "url": "https://lululemon.se/define-jacket", "in_stock": True},
            {"store": "Zalando", "price": 1295, "url": "https://zalando.se/lululemon", "in_stock": False}
        ],
        "price_history": generate_price_history(1195, 1595)
    },
    {
        "id": 27,
        "name": "PlayStation 5 Slim Digital",
        "original_price": 5495,
        "category": "Elektronik",
        "subcategory": "Gaming",
        "image_url": "https://images.unsplash.com/photo-1622297845775-5ff3fef71d13?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "PlayStation 5 Slim Digital Edition med 1TB lagring. Inkluderar controller.",
        "stores": [
            {"store": "Webhallen", "price": 4295, "url": "https://webhallen.se/ps5-slim", "in_stock": True},
            {"store": "Elgiganten", "price": 4395, "url": "https://elgiganten.se/ps5-slim", "in_stock": True},
            {"store": "NetOnNet", "price": 4490, "url": "https://netonnet.se/ps5-slim", "in_stock": True},
            {"store": "Media Markt", "price": 4495, "url": "https://mediamarkt.se/ps5-slim", "in_stock": False}
        ],
        "price_history": generate_price_history(4495, 5495)
    },
    {
        "id": 28,
        "name": "Nintendo Switch OLED",
        "original_price": 3795,
        "category": "Elektronik",
        "subcategory": "Gaming",
        "image_url": "https://images.unsplash.com/photo-1585857182446-721e7cb40fe0?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Nintendo Switch OLED med 7-tums OLED-skärm och 64GB lagring.",
        "stores": [
            {"store": "Webhallen", "price": 2895, "url": "https://webhallen.se/switch-oled", "in_stock": True},
            {"store": "Elgiganten", "price": 2995, "url": "https://elgiganten.se/switch-oled", "in_stock": True},
            {"store": "Media Markt", "price": 3090, "url": "https://mediamarkt.se/switch-oled", "in_stock": True}
        ],
        "price_history": generate_price_history(2995, 3795)
    },
    {
        "id": 29,
        "name": "IKEA POÄNG Fåtölj",
        "original_price": 1295,
        "category": "Hem & Hushåll",
        "subcategory": "Möbler",
        "image_url": "https://images.unsplash.com/photo-1567538096630-e0c55bd6374c?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Klassisk IKEA POÄNG fåtölj i björkfanér med beige klädsel.",
        "stores": [
            {"store": "IKEA", "price": 895, "url": "https://ikea.se/poang", "in_stock": True}
        ],
        "price_history": generate_price_history(895, 1295)
    },
    {
        "id": 30,
        "name": "Chanel No. 5 Eau de Parfum",
        "original_price": 1595,
        "category": "Skönhet",
        "subcategory": "Parfym",
        "image_url": "https://images.unsplash.com/photo-1594035910387-fea47794261f?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Ikonisk Chanel No. 5 parfym 100ml. Tidlös och elegant doft.",
        "stores": [
            {"store": "NK", "price": 1295, "url": "https://nk.se/chanel-no5", "in_stock": True},
            {"store": "Åhléns", "price": 1345, "url": "https://ahlens.se/chanel-no5", "in_stock": True},
            {"store": "Kicks", "price": 1295, "url": "https://kicks.se/chanel-no5", "in_stock": False}
        ],
        "price_history": generate_price_history(1295, 1595)
    },
    {
        "id": 31,
        "name": "The Ordinary Skincare Set",
        "original_price": 495,
        "category": "Skönhet",
        "subcategory": "Hudvård",
        "image_url": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "The Ordinary hudvårdsset med Niacinamide, Hyaluronic Acid och Retinol.",
        "stores": [
            {"store": "Kicks", "price": 295, "url": "https://kicks.se/the-ordinary", "in_stock": True},
            {"store": "Åhléns", "price": 315, "url": "https://ahlens.se/the-ordinary", "in_stock": True},
            {"store": "Lyko", "price": 295, "url": "https://lyko.se/the-ordinary", "in_stock": True}
        ],
        "price_history": generate_price_history(295, 495)
    },
    {
        "id": 32,
        "name": "Philips Hue Starter Kit",
        "original_price": 1995,
        "category": "Hem & Hushåll",
        "subcategory": "Inredning",
        "image_url": "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Philips Hue White & Color Ambiance starter kit med 3 lampor och bridge.",
        "stores": [
            {"store": "Elgiganten", "price": 1495, "url": "https://elgiganten.se/philips-hue", "in_stock": True},
            {"store": "Media Markt", "price": 1590, "url": "https://mediamarkt.se/philips-hue", "in_stock": True},
            {"store": "NetOnNet", "price": 1495, "url": "https://netonnet.se/philips-hue", "in_stock": True}
        ],
        "price_history": generate_price_history(1495, 1995)
    },
    {
        "id": 33,
        "name": "Specialized Rockhopper Mountain Bike",
        "original_price": 8995,
        "category": "Sport & Fritid",
        "subcategory": "Cykel",
        "image_url": "https://images.unsplash.com/photo-1511994298241-608e28f14fde?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Specialized Rockhopper 29\" MTB med 21 växlar och hydrauliska bromsar.",
        "stores": [
            {"store": "XXL", "price": 6995, "url": "https://xxl.se/specialized-rockhopper", "in_stock": True},
            {"store": "Stadium", "price": 7195, "url": "https://stadium.se/specialized-rockhopper", "in_stock": False}
        ],
        "price_history": generate_price_history(6995, 8995)
    },
    {
        "id": 34,
        "name": "Burton Snowboard Custom",
        "original_price": 5995,
        "category": "Sport & Fritid",
        "subcategory": "Vintersport",
        "image_url": "https://images.unsplash.com/photo-1519657337289-077653f724ed?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Burton Custom snowboard 158cm. All-mountain freestyle board.",
        "stores": [
            {"store": "XXL", "price": 4495, "url": "https://xxl.se/burton-custom", "in_stock": True},
            {"store": "Friluftsland", "price": 4695, "url": "https://friluftsland.se/burton", "in_stock": True}
        ],
        "price_history": generate_price_history(4495, 5995)
    },
    {
        "id": 35,
        "name": "Nespresso Vertuo Next",
        "original_price": 1795,
        "category": "Hem & Hushåll",
        "subcategory": "Kök",
        "image_url": "https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Nespresso Vertuo Next kaffemaskin med Centrifusion-teknologi.",
        "stores": [
            {"store": "Elgiganten", "price": 1295, "url": "https://elgiganten.se/nespresso", "in_stock": True},
            {"store": "Media Markt", "price": 1390, "url": "https://mediamarkt.se/nespresso", "in_stock": True},
            {"store": "Åhléns", "price": 1295, "url": "https://ahlens.se/nespresso", "in_stock": True}
        ],
        "price_history": generate_price_history(1295, 1795)
    },
    {
        "id": 36,
        "name": "H&M Studio Collection Wool Coat",
        "original_price": 2495,
        "category": "Mode",
        "subcategory": "Kläder",
        "image_url": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "H&M Studio Collection ullrock i premium kvalitet. Tidlös design.",
        "stores": [
            {"store": "H&M", "price": 1795, "url": "https://hm.se/studio-coat", "in_stock": True},
            {"store": "Zalando", "price": 1895, "url": "https://zalando.se/hm-studio", "in_stock": True}
        ],
        "price_history": generate_price_history(1795, 2495)
    },
    {
        "id": 37,
        "name": "Levi's 501 Original Jeans",
        "original_price": 1295,
        "category": "Mode",
        "subcategory": "Kläder",
        "image_url": "https://images.unsplash.com/photo-1604176354204-9268737828e4?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Klassiska Levi's 501 jeans i original straight fit. 100% bomull.",
        "stores": [
            {"store": "Levi's", "price": 895, "url": "https://levis.se/501-original", "in_stock": True},
            {"store": "Zalando", "price": 945, "url": "https://zalando.se/levis-501", "in_stock": True},
            {"store": "Åhléns", "price": 895, "url": "https://ahlens.se/levis-501", "in_stock": True}
        ],
        "price_history": generate_price_history(895, 1295)
    },
    {
        "id": 38,
        "name": "Hermès H24 Eau de Toilette",
        "original_price": 1395,
        "category": "Skönhet",
        "subcategory": "Parfym",
        "image_url": "https://images.unsplash.com/photo-1587017539504-67cfbddac569?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Hermès H24 herr-EDT 100ml. Modern och urban doft.",
        "stores": [
            {"store": "NK", "price": 1095, "url": "https://nk.se/hermes-h24", "in_stock": True},
            {"store": "Åhléns", "price": 1145, "url": "https://ahlens.se/hermes-h24", "in_stock": True}
        ],
        "price_history": generate_price_history(1095, 1395)
    },
    {
        "id": 39,
        "name": "Ninja Foodi MAX Multi-Cooker",
        "original_price": 2995,
        "category": "Hem & Hushåll",
        "subcategory": "Kök",
        "image_url": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Ninja Foodi MAX 15-i-1 multi-cooker. Tryckkok, air fryer och mer.",
        "stores": [
            {"store": "Elgiganten", "price": 2295, "url": "https://elgiganten.se/ninja-foodi", "in_stock": True},
            {"store": "Media Markt", "price": 2390, "url": "https://mediamarkt.se/ninja-foodi", "in_stock": True},
            {"store": "Åhléns", "price": 2295, "url": "https://ahlens.se/ninja-foodi", "in_stock": False}
        ],
        "price_history": generate_price_history(2295, 2995)
    },
    {
        "id": 40,
        "name": "Reebok Nano X3 Training Shoes",
        "original_price": 1699,
        "category": "Mode",
        "subcategory": "Sport & Träning",
        "image_url": "https://images.unsplash.com/photo-1543163521-1bf539c55dd2?w=800&h=600&fit=crop&q=90&auto=format",
        "description": "Reebok Nano X3 crossfit-skor. Perfekt för CrossFit och HIIT-träning.",
        "stores": [
            {"store": "Reebok", "price": 1195, "url": "https://reebok.se/nano-x3", "in_stock": True},
            {"store": "Stadium", "price": 1249, "url": "https://stadium.se/nano-x3", "in_stock": True},
            {"store": "XXL", "price": 1195, "url": "https://xxl.se/nano-x3", "in_stock": True}
        ],
        "price_history": generate_price_history(1195, 1699)
    }
]

next_id = 41


def get_all_deals() -> List[Dict]:
    """Return all deals with enriched data."""
    enriched_deals = []
    for deal in deals_db:
        deal_copy = deal.copy()
        # Get best price from stores
        best_store = min(deal["stores"], key=lambda x: x["price"])
        deal_copy["deal_price"] = best_store["price"]
        deal_copy["best_store"] = best_store["store"]
        deal_copy["in_stock"] = any(store["in_stock"] for store in deal["stores"])

        # Calculate savings
        savings = calculate_savings(deal["original_price"], best_store["price"])
        deal_copy["savings_kr"] = savings["savings_kr"]
        deal_copy["savings_percent"] = savings["savings_percent"]

        enriched_deals.append(deal_copy)

    return enriched_deals


def get_deal_by_id(deal_id: int) -> Optional[Dict]:
    """Get a specific deal by ID with enriched data."""
    for deal in deals_db:
        if deal["id"] == deal_id:
            deal_copy = deal.copy()
            # Get best price from stores
            best_store = min(deal["stores"], key=lambda x: x["price"])
            deal_copy["deal_price"] = best_store["price"]
            deal_copy["best_store"] = best_store["store"]
            deal_copy["in_stock"] = any(store["in_stock"] for store in deal["stores"])

            # Calculate savings
            savings = calculate_savings(deal["original_price"], best_store["price"])
            deal_copy["savings_kr"] = savings["savings_kr"]
            deal_copy["savings_percent"] = savings["savings_percent"]

            return deal_copy
    return None


def get_categories() -> Dict:
    """Get all categories with their subcategories."""
    return CATEGORIES


def search_deals(query: str) -> List[Dict]:
    """Search deals by name, category, or subcategory."""
    query_lower = query.lower()
    results = []

    for deal in deals_db:
        if (query_lower in deal["name"].lower() or
            query_lower in deal["category"].lower() or
            query_lower in deal["subcategory"].lower() or
            query_lower in deal.get("description", "").lower()):

            deal_copy = deal.copy()
            best_store = min(deal["stores"], key=lambda x: x["price"])
            deal_copy["deal_price"] = best_store["price"]
            deal_copy["best_store"] = best_store["store"]
            deal_copy["in_stock"] = any(store["in_stock"] for store in deal["stores"])

            savings = calculate_savings(deal["original_price"], best_store["price"])
            deal_copy["savings_kr"] = savings["savings_kr"]
            deal_copy["savings_percent"] = savings["savings_percent"]

            results.append(deal_copy)

    return results


def filter_by_category(category: str, subcategory: Optional[str] = None) -> List[Dict]:
    """Filter deals by category and optionally subcategory."""
    results = []

    for deal in deals_db:
        if deal["category"] == category:
            if subcategory is None or deal["subcategory"] == subcategory:
                deal_copy = deal.copy()
                best_store = min(deal["stores"], key=lambda x: x["price"])
                deal_copy["deal_price"] = best_store["price"]
                deal_copy["best_store"] = best_store["store"]
                deal_copy["in_stock"] = any(store["in_stock"] for store in deal["stores"])

                savings = calculate_savings(deal["original_price"], best_store["price"])
                deal_copy["savings_kr"] = savings["savings_kr"]
                deal_copy["savings_percent"] = savings["savings_percent"]

                results.append(deal_copy)

    return results


def calculate_savings(original_price: float, deal_price: float) -> Dict:
    """Calculate savings in kr and percentage."""
    savings_kr = original_price - deal_price
    savings_percent = (savings_kr / original_price) * 100
    return {
        "savings_kr": round(savings_kr, 2),
        "savings_percent": round(savings_percent, 2)
    }


def get_best_deals() -> List[Dict]:
    """Get deals sorted by savings percentage (highest first)."""
    deals_with_savings = get_all_deals()
    return sorted(deals_with_savings, key=lambda x: x["savings_percent"], reverse=True)


def check_legit(deal_id: int) -> Dict:
    """Check if a deal is legit based on discount percentage."""
    deal = get_deal_by_id(deal_id)
    if not deal:
        return {"error": "Deal not found"}

    discount = deal["savings_percent"]

    if discount > 80:
        status = "suspicious"
        message = "Troligen fake! Rabatt över 80% är extremt ovanligt."
        color = "red"
    elif discount >= 50:
        status = "check"
        message = "Kolla extra! Rabatt 50-80% kan vara äkta men dubbelkolla originalpriset."
        color = "yellow"
    else:
        status = "legit"
        message = "Troligen äkta! Rabatt under 50% är rimligt för Black Friday."
        color = "green"

    return {
        "deal_id": deal_id,
        "deal_name": deal["name"],
        "discount_percent": round(discount, 2),
        "status": status,
        "message": message,
        "color": color
    }


def get_countdown() -> Dict:
    """Get countdown to Black Friday."""
    now = datetime.now()

    if now > BLACK_FRIDAY:
        return {
            "message": "Black Friday 2026 är över!",
            "days": 0,
            "hours": 0,
            "minutes": 0,
            "seconds": 0,
            "expired": True
        }

    diff = BLACK_FRIDAY - now
    days = diff.days
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    seconds = diff.seconds % 60

    return {
        "message": "Black Friday 2026 startar om:",
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "expired": False
    }


def add_deal(name: str, original_price: float, price: float,
             category: str, subcategory: str, store: str, url: str = "",
             in_stock: bool = True, description: str = "") -> Dict:
    """Add a new deal to the database."""
    global next_id

    new_deal = {
        "id": next_id,
        "name": name,
        "original_price": original_price,
        "category": category,
        "subcategory": subcategory,
        "description": description,
        "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&h=600&fit=crop&q=90",
        "stores": [
            {"store": store, "price": price, "url": url or f"https://example.com/deal-{next_id}", "in_stock": in_stock}
        ],
        "price_history": generate_price_history(price, original_price)
    }

    deals_db.append(new_deal)
    next_id += 1

    # Return enriched deal
    return get_deal_by_id(new_deal["id"])


def compare_deals(deal_ids: List[int]) -> Dict:
    """Compare multiple deals and find the best savings."""
    if len(deal_ids) < 2:
        return {"error": "Need at least 2 deals to compare"}

    comparison = []
    for deal_id in deal_ids:
        deal = get_deal_by_id(deal_id)
        if not deal:
            continue

        comparison.append({
            "id": deal["id"],
            "name": deal["name"],
            "original_price": deal["original_price"],
            "deal_price": deal["deal_price"],
            "savings_kr": deal["savings_kr"],
            "savings_percent": deal["savings_percent"],
            "store": deal["best_store"]
        })

    if not comparison:
        return {"error": "No valid deals found"}

    # Find best by percentage
    best_percent = max(comparison, key=lambda x: x["savings_percent"])

    # Find best by kr amount
    best_kr = max(comparison, key=lambda x: x["savings_kr"])

    return {
        "deals": comparison,
        "best_by_percent": {
            "deal": best_percent,
            "message": f"Bästa rabatten i procent: {best_percent['name']} ({best_percent['savings_percent']:.1f}%)"
        },
        "best_by_kr": {
            "deal": best_kr,
            "message": f"Största besparingen i kr: {best_kr['name']} ({best_kr['savings_kr']:.0f} kr)"
        }
    }
