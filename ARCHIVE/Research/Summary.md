# Master Thesis

Goal of the Thesis

**"Estimation of Wealth with geospatial Data"**

=> can be adapted

### Project Architecture

- Erstellen eines Pricing Models
 - Irgendein Supervised learning model (bsp. Linear Regression)

- Extrahieren von Features aus Satelliten Bildern
 - Gebäude Grösse
 - Flächen Grösse um Gebäude
 - Dichte der Gebäude im Umkreis (100m, 1km, 10km)

- Erstellen eines Pricing Models mit Satelliten Features
 - Gleiche Modelle wie vorher
 
- Einfluss verschiedener Variablen erklären
 - Lineare Regression
 - Additive Modelle
 - Mixed effect models?

- Vergleich Performance der beiden Pricing Modelle

### Data sources

- **GeoVITE**
- OpenStreetMap  
- Swiss topo  
- Copernicus
- BDM Modell
- Bevölkerungs statistik (Personen pro gebäude)  
- GWS - Gebäude und Wohn Statistik
	- Wie gross ist das Haus? Die Wohnung etc.
	- Gebäude

### Methodology

##### Available Data

- Map images  
- Satellite images

##### Steps
Each step has multiple possible approaches. the best one has to be found. If the approaches are suitable has to be tested.

1. Extract building location from map **(Do we agree to extract building location from the map  to create the target variable?)**
	- Super pixels
	- Convolution

2. object (building) detection
	- Viola Jones (ensemble, of weak classifiers)
	- Convolutional Net
	- Yolo

	
### Muster zu erkennen

- Bild X meter um das haus als feature (Struktur von nahem)
	- 300 meter
	- 500 meter

- Gebäude
	- Gebäude dichte
	- Gebäude grösse
	- Distanz von Gebäuden (wie frei steht mein Haus)
- Swimmingpools
- Grünflächen
	- Parks
	- Vorgarten grösse
- Strassen
	- Strassen meter pro Umkreis/Haus
	- Strassen breite pro Umkreis/Haus



### tools

python

- Geopandas
- pysal
- rasterio

postgres

- postgis (extension)