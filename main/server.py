from flask import Flask
from flask import render_template
from flask import redirect, url_for
from flask import Response, request, jsonify
app = Flask(__name__, static_url_path='/static')


Data = {
    "1": {
        "Id": "1",
        "Name": "Bare Water Cushion",
        "Image": "https://d1flfk77wl2xk4.cloudfront.net/Assets/86/672/XXL_p0186767286.jpg",
        "Price": "$18.70",
        "Summary": """Vegan cushion infused with only plant-derived ingredients. Enriched with 70% moisturizing essence 
        containing 10 kinds of Hyaluronic Acid, Peach Blossom, Aqua Ceramide and Baobab Tree Extract. Instantly replenishes ample moisture 
        and keeps skin fully hydrated for 48 hours without leaving any skin inner dryness. Fine mesh design enables even application with proper 
        amount for seamless adherence without clumping.""",
        "Brand": "Romand",
        "Type": "Cushion",
        "Shade_Name": "#05 Sand 25",
        "Shade_Range": "Warm neutral beige",
        "Average_Rating": "4.6/5.0",
        "Other_Color_Options": ["#01 Porcelain 17", "#02 Pure 21", "#03 Natural 21", "#04 Beige 23"],
        "Similar_Foundations_IDs": ["4", "17", "23", "59"]
    },
    "2": {
        "Id": "2",
        "Name": "Radiant Glow Foundation",
        "Image": "https://www.sephora.com/productimages/sku/s2551398-main-zoom.jpg?imwidth=315",
        "Price": "$24.50",
        "Summary": """Achieve a radiant and natural glow with this foundation. Formulated with light-reflecting particles 
             and nourishing ingredients to enhance your skin's luminosity. Long-lasting formula for all-day wear. 
             The lightweight formula allows for comfortable wear throughout the day, and the warm neutral beige shade complements a variety of skin tones.""",
        "Brand": "Glow Beauty",
        "Type": "Liquid",
        "Shade_Name": "#02 Ivory Beige",
        "Shade_Range": "Cool pink light",
        "Average_Rating": "4.2/5.0",
        "Other_Color_Options": ["#01 Light Beige", "#03 Warm Beige", "#04 Honey", "#05 Caramel"],
        "Similar_Foundations_IDs": ["8", "31"]
    },
    "3": {
        "Id": "3",
        "Name": "Matte Finish Powder",
        "Image": "https://www.sephora.com/productimages/sku/s1787910-main-zoom.jpg?imwidth=315",
        "Price": "$15.99",
        "Summary": """A matte finish powder foundation that provides a flawless complexion. 
        Lightweight formula that controls oil and minimizes the appearance of pores. Perfect for a natural, matte look. 
        Formulated with oil-absorbing ingredients, this powder foundation effortlessly controls shine, creating a matte finish that lasts throughout the day.
        Perfect for a natural, matte look.""",
        "Brand": "Matte Maven",
        "Type": "Powder",
        "Shade_Name": "#03 Beige Buff",
        "Shade_Range": "Neutral dark brown",
        "Average_Rating": "4.8/5.0",
        "Other_Color_Options": ["#02 Light Sand", "#05 Deep Mocha"],
        "Similar_Foundations_IDs": ["7", "14", "21", "42"]
    },
    "4": {
        "Id": "4",
        "Name": "Silk Elegance Foundation",
        "Image": "https://www.sephora.com/productimages/sku/s2340917-main-zoom.jpg?imwidth=315",
        "Price": "$29.99",
        "Summary": """Experience the luxurious feel of silk on your skin with this elegant foundation. 
        Blends seamlessly for a silky smooth finish. Provides buildable coverage and a natural, luminous look.
        Provides buildable coverage and a natural, luminous look. Infused with silk proteins, this foundation offers a luxurious and smooth texture, 
        leaving your skin feeling pampered and elegant.""",
        "Brand": "Sheisedo",
        "Type": "Liquid",
        "Shade_Name": "#01 Pearl Ivory",
        "Shade_Range": "Light cool tones",
        "Average_Rating": "4.7/5.0",
        "Other_Color_Options": ["#02 Soft Beige", "#03 Rose Petal"],
        "Similar_Foundations_IDs": ["11", "37", "48", "54"]
    },
    "5": {
        "Id": "5",
        "Name": "HD Pro Finish Foundation",
        "Image": "https://www.sephora.com/productimages/sku/s2514206-main-zoom.jpg?imwidth=315",
        "Price": "$22.95",
        "Summary": """Achieve a high-definition finish with this professional-grade foundation. 
        Blurs imperfections and provides a flawless complexion. Ideal for photography and special occasions.
        The foundation's innovative blend of ingredients ensures a long-lasting and impeccable appearance, 
        allowing you to confidently showcase your radiant and picture-perfect complexion in any setting.""",
        "Brand": "Maybelliene",
        "Type": "Cream",
        "Shade_Name": "#03 Medium Beige",
        "Shade_Range": "Neutral medium",
        "Average_Rating": "4.5/5.0",
        "Other_Color_Options": ["#01 Fair Porcelain", "#02 Light Sand", "#04 Warm Tan"],
        "Similar_Foundations_IDs": ["7", "14", "21", "42", "49", "57"]
    },
    "6": {
        "Id": "6",
        "Name": "Mineral Radiance Powder",
        "Image": "https://www.sephora.com/productimages/sku/s1229038-main-zoom.jpg?imwidth=315",
        "Price": "$19.99",
        "Summary": """Enhance your natural radiance with this mineral-infused powder foundation. 
        Provides buildable coverage with a lightweight feel. Controls shine for a radiant, matte finish.
        he innovative formula goes beyond just coverage; it actively controls shine, ensuring a luminous yet 
        matte finish that lasts throughout the day. The mineral-infused properties work in harmony with your skin, 
        promoting a healthy and radiant glow that doesn't compromise on a matte effect""",
        "Brand": "Pure Radiance",
        "Type": "Powder",
        "Shade_Name": "#10 Warm Deep",
        "Shade_Range": "Warm deep brown",
        "Average_Rating": "4.4/5.0",
        "Other_Color_Options": ["#01 Light Ivory", "#03 Warm Honey", "#04 Golden Sand"],
        "Similar_Foundations_IDs": ["2", "18", "26"]
    },
    "7": {
        "Id": "7",
        "Name": "Youthful Glow Serum Foundation",
        "Image": "https://www.sephora.com/productimages/sku/s2512705-main-zoom.jpg?imwidth=315",
        "Price": "$32.50",
        "Summary": """Revitalize your skin with this serum-infused foundation. 
        Provides a youthful glow while nourishing and hydrating the skin. Lightweight formula for a natural look.
        Pamper your skin with each application, and embrace the rejuvenating effects of this foundation that effortlessly combines skincare and makeup""",
        "Brand": "Youthful Essence",
        "Type": "Serum",
        "Shade_Name": "#01 Light Porcelain",
        "Shade_Range": "Cool light ivory",
        "Average_Rating": "4.8/5.0",
        "Other_Color_Options": ["#02 Fair Beige", "#03 Rose Petal", "#05 Deep Caramel"],
        "Similar_Foundations_IDs": ["9", "28", "36", "47", "52"]
    },
    "8": {
        "Id": "8",
        "Name": "Velvet Matte Mousse",
        "Image": "https://www.sephora.com/productimages/sku/s2425254-main-zoom.jpg?imwidth=315",
        "Price": "$26.99",
        "Summary": """Experience the velvety texture of this matte mousse foundation.
        Blends easily for a smooth and matte finish. Long-lasting formula for a flawless look that lasts all day.
        Revel in the confidence that comes with knowing your look will endure, whether facing a busy day at the office or attending evening events. 
        Elevate your makeup routine with the sumptuous feel and enduring elegance of this matte mousse foundation, 
        turning every application into a moment of pure luxury.""",
        "Brand": "Velvet Touch",
        "Type": "Mousse",
        "Shade_Name": "#04 Cocoa",
        "Shade_Range": "Deep warm brown",
        "Average_Rating": "4.3/5.0",
        "Other_Color_Options": ["#01 Ivory", "#02 Beige"],
        "Similar_Foundations_IDs": ["16", "29", "33", "51", "59"]
    },
    "9": {
    "Id": "9",
    "Name": "Radiant Elegance Serum Foundation",
    "Image": "https://www.sephora.com/productimages/sku/s2708220-main-zoom.jpg?imwidth=315",
    "Price": "$34.50",
    "Summary": """Experience the radiance of this serum-infused foundation. The lightweight formula effortlessly
    blends for a natural and elegant finish. Provides a luminous glow that lasts throughout the day.  As you apply this foundation,
    witness the luminous glow it imparts to your complexion, leaving you with a radiant and youthful allure. """,
    "Brand": "Elegant Radiance",
    "Type": "Serum",
    "Shade_Name": "#02 Ivory Glow",
    "Shade_Range": "Neutral undertones",
    "Average_Rating": "4.6/5.0",
    "Other_Color_Options": ["#01 Light Beige", "#03 Warm Beige", "#04 Honey Dew"],
    "Similar_Foundations_IDs": ["18", "25", "39", "47", "56"]
    },
    "10": {
        "Id": "10",
        "Name": "Velvet Touch Liquid Silk",
        "Image": "https://www.sephora.com/productimages/sku/s2643039-main-zoom.jpg?imwidth=315",
        "Price": "$28.99",
        "Summary": """Indulge in the velvety touch of this liquid silk foundation. Delivers a smooth and
        silky finish for a luxurious makeup experience. Provides a flawless look that enhances your natural beauty.
        Unveil the allure of liquid silk and let your natural radiance shine through, creating a captivating and flawless canvas for your daily glamour.""",
        "Brand": "Silk Essence",
        "Type": "Liquid",
        "Shade_Name": "#12 Java",
        "Shade_Range": "Dark neutral deep brown",
        "Average_Rating": "4.4/5.0",
        "Other_Color_Options": ["#01 Ivory Silk", "#02 Beige Silk", "#03 Tan Silk", "#04 Mocha Silk"],
        "Similar_Foundations_IDs": ["16", "28", "33", "52", "58"]
    }
}

# ROUTES

@app.route('/')
def home():
    return render_template('home.html', Data=Data)


@app.route('/view/<id>')
def view(id):
    item = Data.get(id)
    if item:
        return render_template('view.html', item=item)
    else:
        # Handle the case where the item with the given id is not found
        return render_template('itemnotfound.html', id=id) 


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Generate a new ID for the item
        new_id = str(len(Data) + 1)
        
        # Create a new item with the form data
        new_item = {
            "Id": new_id,
            "Name": request.form.get('name'),
            "Price": request.form.get('price'),
            "Image": request.form.get('image'),
            "Summary": request.form.get('summary'),
            "Brand": request.form.get('brand'),
            "Type": request.form.get('type'),
            "Shade_Name": request.form.get('shade_name'),
            "Shade_Range": request.form.get('shade_range'),
            "Average_Rating": "{:.1f}/5.0".format(float(request.form.get('rating'))),
            "Other_Color_Options": request.form.getlist('color_option[]'),
            "Similar_Foundations_IDs": request.form.getlist('similar_id[]')
        }
        
        # Add the new item to the data dictionary
        Data[new_id] = new_item
        
        # Return a JSON response indicating success
        return jsonify({"success": True, "new_id": new_id})
    else:
        # Render the add page
        return render_template('add.html')
    

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    item = Data.get(id)
    if item:
        if request.method == 'POST':
            # Update data with form values
            item['Name'] = request.form.get('name')
            item['Price'] = request.form.get('price')
            item['Image'] = request.form.get('image')
            item['Summary'] = request.form.get('summary')
            item['Brand'] = request.form.get('brand')
            item['Type'] = request.form.get('type')
            item['Shade_Name'] = request.form.get('shade_name')
            item['Shade_Range'] = request.form.get('shade_range')
            rating_value = "{:.1f}/5.0".format(float(request.form.get('rating')))
            item['Average_Rating'] = rating_value
            
            item['Other_Color_Options'] = request.form.getlist('color_option[]')
            item['Similar_Foundations_IDs'] = request.form.getlist('similar_id[]')
            # Redirect to view page after updating
            return redirect(url_for('view', id=id))
        else:
            # Render the edit page with prepopulated values
            return render_template('edit.html', item=item)
    else:
        # Handle item not found
        return render_template('itemnotfound.html', id=id)

# search based on name, summary and shade range
@app.route('/search', methods=['POST'])
def search():
    
    search_input = request.form.get('search_input')
    
    lc_input = search_input.lower()

    matching_items = [
        item for item in Data.values() if 
        lc_input in item['Name'].lower() or  
        lc_input in item['Summary'].lower() or
        lc_input in item['Shade_Range'].lower()
        ]
    
    #get number of search results
    num_items = len(matching_items)

    return render_template('search.html',search_input=search_input, matching_items=matching_items, num_items=num_items)

if __name__ == '__main__':
    app.run(debug = True)
   



