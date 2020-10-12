# Master Thesis

Goal of the Thesis

**"Estimation of Wealth with geospatial Data"**

### Methodology

Aggregation of pictures

- Super pixels

Methods for object detection

- Viola Jones (ensemble, of weak classifiers)
- Convolutional Net
- Yolo

Objects to detect:

- Buildings
- Streets
- Building sights
- Forest
- Lakes & Rivers
- Change of buildings over time

### Data sources

- GeoVITE  
- OpenStreetMap  
- Swiss topo  
- Copernicus
- BDM Modell  
- Bevölkerungs statistik (Personen pro gebäude)  
- GWS - Gebäude und Wohn Statistik
	- Wie gross ist das Haus? Die Wohnung etc.
	- Gebäude


### Benötigte Funktionen
```python
def get_address(coordinates)

def get_satellite_img(gemeinde)
```

### Satellite Image extraction

1. Train Building detection ML Model
2. Extract Building pictures from Overall Satellite Image




# Research Papers

## Crop classification
Using satellite images to classify crops.

http://unigis.sbg.ac.at/files/Mastertheses/Full/
104866.pdf

## Difference in time buildings
Analysing where and which buildings have changed over time. from one picture to the other.

https://github.com/hbaudhuin/LamboiseNet

## LandUse & LandCover Change
Analyze the change in landuse and landcover over time.

http://unigis.sbg.ac.at/files/Mastertheses/Full/40148.pdf

# References from other papers
Remote sensing at regional and local scales has become an essential tool in wide areas. The classification of multi-spectral images has been a successful application that is used for classification of land cover maps (Lunetta and Balogh, 1999, Oettera et al. 2000, Yuan et al. 2005, ), urban growth (Yeh and Li, 1997, Zhang et al. 2002), forest change (Vogelmann and Rock, 1988, Hall et al. 1991, Coppin and Bauer, 1994), monitoring change in ecosystem condition (Lambin 1998, Weng 2002), monitoring assessing deforestation and burned forest areas (Potapov et al. 2008), agricultural expansion (Woodcock et al. 1993, Pax-Lenney et al. 1996), mapping corn (Maxwell et al. 2004), real time fire detection (Dennison and Roberts, 2009), estimating tornado damage areas (Myint et al. 2008), estimating water quality
1
characteristics of lakes (Lillesand et al. 1983, Lathrop et al. 1991, Dekker and Peters, 1993), geological mapping (Mostafa and Bishta, 2004, Bishta 2010), estimating crop acreage and production (Liu et al. 2005), monitoring of environmental pollution (Zhu and Basir, 2005), monitoring and mapping mangrove ecosystem (Kuenzer et al. 2011).

-