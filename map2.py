import folium
map = folium.Map(location=[37.42, -122.04],
                 min_zoom=12,
                 max_zoom=12,
                 tiles="cartodbpositron",
                 dragging=False)

fg = folium.FeatureGroup(name="My Map")

htmlAnantara="""
    <style type="text/css">
        .container {
            overflow: auto;
        	margin: 10px;
        	padding: 10px;
        	display: flex;
        }
        .pic{
           width: 35%;
           float: left;
           text-align: center;
           padding: 10px;
        }
        .text{
           width: 50%;
           float: left;
           text-align: left;
           padding: 20px;
        }
        img{
            width: 200px;
            height: 200px;
        }
    </style>

    <div class="container">
        <div class="pic">
            <img src="images/anantara.jpg" alt="anantara">
        </div>
        <div class="text">
            <h2>ANANTARA VILLAS</h2>
            <p>Santa Clara, CA</p>
            <hr>
            <p>Fifty-six luxury condominiums.</p>
        </div>
    </div>
    """

htmlFortuna="""
    <style type="text/css">
        .colum {
            overflow: auto;
        	margin: 10px;
        	padding: 10px;
        	display: flex;
        }
        .pic{
           width: 35%;
           float: left;
           text-align: center;
           padding: 10px;
        }
        .text{
           width: 60%;
           float: right;
           text-align: left;
           padding: 20px;
        }
        img{
            width: 200px;
            height: 200px;
        }
    </style>

    <div class="colum">
        <div class="pic">
            <img src="images/fortuna.jpg" alt="fortuna">
        </div>
        <div class="text">
            <h3>VILLA FORTUNA</h3>
            <p>Mountain View, CA</p>
            <hr>
            <p>Villa Fortuna will be offering 20 townhomes.</p>
            <p>Each townhome ranges between 1,600 to 1,900 square feet, featuring 3 to 4 bedrooms with attached 2-car garage.</p>
        </div>
    </div>
    """

fg.add_child(folium.Marker(location=[37.415531, -122.089768],
    popup=folium.Popup(htmlFortuna, max_width=630, show=False, sticky=False),
    icon=folium.Icon(color='blue', icon='home', icon_color="white", prefix='fa')))
fg.add_child(folium.Marker(location=[37.352058, -121.957700],
    popup=folium.Popup(htmlAnantara, max_width=630, show=False, sticky=False),
    icon=folium.Icon(color='blue', icon='home', icon_color="white", prefix='fa')))

map.add_child(fg)
map.save("Map2.html")
