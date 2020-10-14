# Master Thesis

Goal of the Thesis

**"Estimation of Wealth with geospatial Data"**

(Actually, we observe the influence of geospatial data on a baseline pricing model.)

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

1. Extract building location from map **(Do we agree to extract building location from the map  to create the target variable?)**
	- Super pixels
	- Convolution

2. object (building) detection
	- Viola Jones (ensemble, of weak classifiers)
	- Convolutional Net
	- Yolo

3. Objects to detect (optional)
	- Buildings
	- Streets
	- Building sights
	- Forest
	- Lakes & Rivers
	- Change of buildings over time
	- Sun exposure?


### Benötigte Funktionen
```python
def get_address(coordinates)

def get_satellite_img(gemeinde)
```