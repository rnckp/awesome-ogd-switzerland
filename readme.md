# Awesome Open Government Data Switzerland

[![GitHub Stars](https://img.shields.io/github/stars/rnckp/awesome-ogd-switzerland.svg)](https://github.com/rnckp/awesome-ogd-switzerland)
[![GitHub Issues](https://img.shields.io/github/issues/rnckp/awesome-ogd-switzerland.svg)](https://github.com/rnckp/awesome-ogd-switzerland)
[![GitHub Issues](https://img.shields.io/github/issues-pr/rnckp/awesome-ogd-switzerland.svg)](https://img.shields.io/github/issues-pr/rnckp/awesome-ogd-switzerland)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<a href="https://github.com/astral-sh/ruff"><img alt="linting - Ruff" class="off-glb" loading="lazy" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>

A manually curated list of Open Government Data (OGD) portals, websites, APIs, tools and other related resources in Switzerland. Relevant links to international websites are listed as well.

<details>
<summary><strong>Table of Contents</strong></summary>

- [Data Sources](#data-sources)
- [Geo Data](#geo-data)
- [Linked Open Data](#linked-open-data)
- [APIs](#apis)
- [Organizations](#organizations-initiatives-events-and-projects)
- [Newsletters](#newsletters)
- [Podcasts](#podcasts)
- [Miscellaneous](#miscellaneous)
- [Media](#media)
- [Social Media](#social-media)
- [International](#international)

</details>

## Data Sources

Portals and data sources that provide access to Swiss Open Government Data.

### National

#### Statistical and Administrative Data

- [opendata.swiss](https://opendata.swiss/de) - Central catalog of Swiss Open Government Data, operated by the Federal Statistical Office (BFS). **Most important entry point to all things OGD in Switzerland.**
- [BFS Data Portal](https://data.bfs.admin.ch/) - New data portal of the [Federal Statistical Office](https://www.bfs.admin.ch/bfs/en/home/services.html).
- [BFS STAT-TAB](https://www.pxweb.bfs.admin.ch/pxweb/en/) - This interactive database of the Federal Statistical Office provides detailed statistical data and enables simple, individual data queries. The tables produced can be exported in various formats.
- [I14Y - Metadata catalog of Switzerland.](https://www.i14y.admin.ch/en/home) - The I14Y interoperability platform is Switzerland’s national data catalogue. It ensures the efficient exchange of data between authorities, companies and citizens. In the platform, an overview of the data collections and interfaces of the Confederation, cantons and communes is continuously expanded and their metadata are made available centrally.
- [BFS Registers](https://www.bfs.admin.ch/bfs/en/home/registers.html) - Official Swiss Enterprise Register, Population Register and Federal Register of Buildings and Dwellings.
- [Visualize](https://visualize.admin.ch) - Create and embed visualizations from any dataset provided by the LINDAS Linked Data Service.
- [Swiss official commune register](https://www.bfs.admin.ch/bfs/en/home/basics/swiss-official-commune-register.html) - Register of all Swiss commune names, numbers, and past mutations. ([App](https://www.agvchapp.bfs.admin.ch/de/home))
- [TERMDAT](https://www.bk.admin.ch/bk/de/home/dokumentation/sprachen/termdat.html) - The Federal Administration's terminology database ([direct access](https://www.termdat.ch/search)). The EU's terminology database IATE can be accessed [here](https://iate.europa.eu/home).
- [ÖREB-Kataster](https://www.cadastre.ch/de/oereb-kataster) - Extracts from the Cadastre of Public-law Restrictions on Landownership containing legally binding information about the most important public law restrictions that apply to a given plot of land.

#### Parliamentary Data

- [Schweizer Parlament](https://www.parlament.ch/de/%C3%BCber-das-parlament/fakten-und-zahlen/open-data-web-services) - Open Data and web services of Swiss Parliament. Unofficial Python wrapper [here](https://github.com/metaodi/swissparlpy). R wrapper [here](https://github.com/zumbov2/swissparl).
- [OpenParlData.ch](https://openparldata.ch/) – The [API](https://api.openparldata.ch/documentation) offers harmonized data on political actors, parliamentary proceedings, decrees, consultations, votes and more from [78](https://admin.openparldata.ch/#/bodies) national, cantonal, and municipal parliaments.
- [Amtsblattportal](https://amtsblattportal.ch/#!/home) - Official Gazettes Portal. A publishing center for entities that publish official and commercially relevant publications in the Swiss Official Gazette of Commerce (SOGC) and in Official Cantonal Gazettes. Data can also be imported and exported using a [REST API](https://amtsblattportal.ch/docs/api/).

#### Legal Data

- [Fedlex – Publikationsplattform des Bundesrechts](https://www.fedlex.admin.ch/de/home) - Publication platform for federal law.
- [entscheidsuche.ch](https://entscheidsuche.ch/) - This freely accessible portal offers a search of all published court decisions from Swiss courts at all levels. GitHub scraper repository of the project [here](https://github.com/entscheidsuche).

#### Financial and Economic Data

- [Swiss Federal Finance Administration FFA](https://www.efv.admin.ch/efv/en/home/finanzberichterstattung/daten/datencenter.html) - Swiss Federal budget data. Data portal [here](https://www.data.finance.admin.ch/superset/dashboard/startseite/).
- [Schweizerische Nationalbank SNB](https://data.snb.ch/de) - Swiss National Bank data portal.

#### Federal Offices and Other National Data Sources

- [Bundesamt für Gesundheit BAG](https://www.bag.admin.ch/de/zahlen-statistiken) - Federal Office of Public Health.
- [Versorgungsatlas](https://www.versorgungsatlas.ch/) - Swiss Health Care Atlas provided by BAG and [Swiss Health Observatory](https://www.obsan.admin.ch/en). Public health data covering more than 100 indicators.
- [Infectious Diseases Dashboard (IDD)](https://idd.bag.admin.ch/) - Information on cases of infection and illness in Switzerland and Liechtenstein caused by various pathogens, provided by the Federal Office of Public Health FOPH / BAG.
- [arbeit.swiss](https://www.amstat.ch/v2/amstat_de.html) - Data portal of the State Secretariat for Economic Affairs (SECO).
- [Agrarmarktdaten](https://www.agrarmarktdaten.ch/) - Comprehensive data portal provided by the Federal Office for Agriculture. The portal provides ongoing information and data on current market events in various agricultural and food markets. You will find price and quantity information along the value chain from production to consumption.
- [Agrarbericht](https://www.blw.admin.ch/blw/de/home/agrarbericht.html) - Agricultural data provided by the Federal Office for Agriculture.
- [Schweizer Nährwertdatenbank](https://naehrwertdaten.ch/de/) - The Swiss Food Composition Database contains information on the composition of foods that are available in Switzerland. The database is operated by the Federal Food Safety and Veterinary Office FSVO.
- [Bundesamt für Energie BFE](https://www.bfe.admin.ch/bfe/de/home/versorgung/statistik-und-geodaten/energiestatistiken.html) - Federal Office of Energy.
- [Bundesamt für Sozialversicherungen BSV](https://www.bsv.admin.ch/de/statistik) - Federal Social Security Office.
- [Bundesamt für Umwelt BAFU](https://www.bafu.admin.ch/bafu/de/home/zustand.html) - Federal Office for the Environment.
- [Eidgenössische Steuerverwaltung](https://www.estv.admin.ch/estv/de/home/die-estv/steuerstatistiken-estv.html) - Federal Tax Administration.
- [Staatssekretariat für Migration SEM](https://www.sem.admin.ch/sem/de/home/publiservice/statistik.html) - State Secretariat for Migration.
- [Zentraler Firmenindex ZEFIX](https://www.zefix.admin.ch/de/search/entity/welcome) - API [here](https://www.zefix.admin.ch/ZefixPublicREST/swagger-ui/index.html).
- [Eidgenössisches Institut für Geistiges Eigentum IGE](https://www.ige.ch/de/uebersicht-dienstleistungen/digitales-angebot) - Federal Institute of Intellectual Property.
- [Konjunkturforschungsstelle ETH Zürich](https://kof.ethz.ch/daten.html)
- [Unfallversicherung UVG](https://www.unfallstatistik.ch/index.htm)

#### Environment, Tourism and Meteorology Data

- [Swiss Tourism Data](https://www.tourismdata.ch/) - The portal is part of the National Data Infrastructure for Tourism (NaDIT) project. It serves as the catalogue of metadata of the most important data sources for Swiss tourism.
- [Bundesamt für Meteorologie und Klimatologie MeteoSchweiz](https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html) - Federal Office of Meteorology and Climatology MeteoSwiss.
- [SLF data service](https://www.slf.ch/en/services-and-products/slf-data-service/) - Data collected and produced in the context of avalanche warning.

#### Academic and Research Data

- [FORS SWISSUbase](https://www.swissubase.ch/de/) - Cross-disciplinary data repository for Swiss universities.
- [Schweizerischer Nationalfonds SNF](https://data.snf.ch/datasets) - Swiss National Science Foundation. GitHub repositories with SNF's data stories [here](https://github.com/snsf-data).
- [CERN](https://opendata.cern.ch/) - Open data portal of [CERN](https://home.web.cern.ch/), the European Laboratory for Particle Physics.

#### Transport Data

- [SBB](https://data.sbb.ch/pages/home/) - Swiss Federal Railways data portal.
- [SBB](https://opentransportdata.swiss/en/) - Open transport data provided by SBB.

### Cantonal

- [Aargau](https://www.ag.ch/de/themen/datenportal#/)
- [Basel Stadt](https://data.bs.ch/explore/)
- [Basel Land](https://data.bl.ch/explore/)
- [Basel Land Statistical Office](https://www.baselland.ch/politik-und-behorden/direktionen/finanz-und-kirchendirektion/statistisches-amt)
- [Bern](https://www.fin.be.ch/de/start/themen/OeffentlicheStatistik/statistikportal.html)
- [Fribourg / Freiburg](https://opendata.fr.ch/pages/home/)
- [Fribourg / Freiburg Statistical Office](https://www.fr.ch/de/vwbd/stata)
- [Genf](https://ge.ch/sitg/donnees/demarche-open-data) - alternatively [here](https://statistique.ge.ch/).
- [Geneva Public Transport](https://opendata.tpg.ch/pages/accueil/)
- [Graubünden](https://www.gr.ch/DE/institutionen/verwaltung/dvs/awt/statistik/Seiten/home.aspx)
- [Jura](https://stat.jura.ch/)
- [Luzern](https://www.lustat.ch)
- [Neuchâtel](https://www.ne.ch/autorites/DFS/STAT/Pages/accueil.aspx)
- [Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Wirtschaft--Statistik-und-Tourismus-3874-DE.html)
- [Schwyz](https://data.sz.ch/explore/)
- [Solothurn](https://so.ch/verwaltung/finanzdepartement/amt-fuer-finanzen/statistikportal/)
- [St. Gallen](https://daten.sg.ch/explore/)
- [St. Gallen Statistical Office](https://stada2.sg.ch/)
- [Tessin](https://www4.ti.ch/index.php?id=42382)
- [Thurgau](https://data.tg.ch/explore) – Thematic atlasses [here](https://themenatlas-tg.ch/#c=home).
- [Thurgau Statistical Office](https://statistik.tg.ch/)
- [Uri](https://www.statistik-uri.ch/daten)
- [Vaud](https://www.vd.ch/themes/etat-droit-finances/statistique)
- [Wallis](https://www.vs.ch/de/web/sstp/sstp)
- [Zug](https://www.zg.ch/behoerden/gesundheitsdirektion/statistikfachstelle)
- [Zürich](https://www.zh.ch/de/politik-staat/opendata.zhweb-noredirect.zhweb-cache.html#/)
- [Zürich Gemeindeportrait](https://www.zh.ch/de/politik-staat/gemeinden/gemeindeportraet.html)
- [Zürcher Gemeinden in Zahlen](https://zgz.statistik.zh.ch/)

### Cities and Municipalities

- [Bern](https://www.bern.ch/open-government-data-ogd/ogd-nach-themen)
- [Lausanne](https://www.lausanne.ch/officiel/statistique.html)
- [Lugano](https://statistica.lugano.ch/site/dati-ogd/)
- [Luzern](https://www.lustat.ch/statistikportal-stadt-luzern)
- [St. Gallen](https://www.stadt.sg.ch/home/verwaltung-politik/stadt-zahlen/statistikdatenbanken.html)
- [Zürich](https://data.stadt-zuerich.ch/) – [[GitHub](https://github.com/opendatazurich)]
- [Zürich Tourismus](https://www.zuerich.com/de/business/ueber-zuerich-tourismus/open-data-portal)

### Miscellaneous

- [Open Energy Data CH](https://github.com/OpenEnergyData/energy-data-ch) - List of open datasets related to energy projects in Switzerland. See also this [Open Data CH hackday contribution](https://hack.opendata.ch/project/851) for the [Energy Hackday 2020](https://hack.opendata.ch/event/31).
- [Swissgrid](https://www.swissgrid.ch/de/home/customers/topics/energy-data-ch.html) - Energy data.
- [Agristat](https://www.sbv-usp.ch/de/services/agristat-statistik-der-schweizer-landwirtschaft) - Statistical data from Schweizer Bauernverband (not an official government entity).
- [Identitas Tierstatistik](https://tierstatistik.identitas.ch/en/index.html) - Various datasets on livestock and companion animals in Switzerland.
- [Jagdstatistik](https://www.jagdstatistik.ch/de/home) - Wild animal and hunting data from Bundesamt für Umwelt (BAFU).
- [Sucht Schweiz](https://zahlen-fakten.suchtschweiz.ch/de.html) - Statistical data from Sucht Schweiz (not an official government entity).
- [Memoriav Memobase](https://memobase.ch/de/start) - Searchable audiovisual collections documenting Swiss history.
- [DODIS](https://dodis.ch/search) - Swiss diplomatic documents.
- [Schweizer Landesmuseum](https://sammlung.nationalmuseum.ch/de/maincategory)
- [Swiss Federal Archives](https://www.recherche.bar.admin.ch/recherche/) - Documents on the history of Switzerland since 1798.
- [Schweizerisches Idiotikon](https://idiotikon.ch/projekte) - Comprehensive documentation of Swiss German dialects (not an official government entity).
- [Ortsnamen.ch](https://www.ortsnamen.ch/de/) - Comprehensive catalog of Swiss place names (project of Schweizerisches Idiotikon). [Searchable map](https://search.ortsnamen.ch/de) and [REST-API](https://search.ortsnamen.ch/static/api/swagger/index.html) also available.
- [Swiss Dwellings](https://zenodo.org/record/7788422) - Notable dataset provided by Archilyse Open Data featuring 45,176 Swiss apartments (370,000 rooms) in ~3,100 buildings, including their geometries, room typology, and visual, acoustical, topological, and daylight characteristics.
- [Christian Catholic Church Switzerland](https://christkatholisch.ch/angebote/opendata/) - Open Data offerings of Christkatholische Kirche Schweiz.

## Geo Data

### National

- [swisstopo](https://www.swisstopo.admin.ch/de/geodata.html) - National geodata portal provided by the Federal Office of Topography (Bundesamt für Landestopographie).
- [geo.admin.ch](https://www.geo.admin.ch/de/home.html) - National geodata portal (Geoportal des Bundes).
- [geo.admin.ch - Strassenverzeichnis](https://map.geo.admin.ch/#/map?lang=de&center=2660000,1190000&z=1&topic=ech&layers=ch.swisstopo.amtliches-strassenverzeichnis&bgLayer=ch.swisstopo.pixelkarte-farbe) - Official directory of all Swiss street names.
- [geocat](https://www.geocat.ch) - Geographic catalog operated by swisstopo. Provides geodata, geoservices, and models from federal offices, cantons, municipalities, research institutes, private companies, and more.
- [geobasisdaten.ch](https://geobasisdaten.ch/) - Geodata portal provided by the [«Konferenz der kantonalen Geoinformations- und Katasterstellen»](https://www.kgk-cgc.ch/). In Switzerland, the basic geodata catalog is a catalog-like listing of all geodata collected by legal authorities, linking them to underlying legal enactments. In addition to visualizing geodata recorded by geoinformation law, its function includes the database-specific assignment of responsible bodies and other legally relevant attributes. [More information here](https://www.kgk-cgc.ch/geobasisdaten).
- [geodienste.ch](https://geodienste.ch/) - The intercantonal portal for obtaining geodata and services. Basic geodata is aggregated and made available under the responsibility of the cantons and municipalities.
- [Geoportal.ch](https://www.geoportal.ch/) - Publication platform for Swiss geodata.
- [BFS Plattform Statatlas](https://www.atlas.bfs.admin.ch/de/index.html) - The Federal Statistical Office (BFS) offers several specialist atlases in addition to the central statistical atlas of Switzerland, providing more detailed information on specific areas of life from a statistical perspective. With numerous interactive maps, graphics, and underlying data, a wide variety of geographical processes and relationships can be easily analyzed and evaluated.
- [Datalakes](https://www.datalakes-eawag.ch/) - National geodata portal for in-situ measurements of lakes.
- [Alplakes](https://www.alplakes.eawag.ch/) - Operational lake models and remote sensing products.
- [Swiss Data Cube](https://www.swissdatacube.org) - 80,000 satellite images and ~30 TB of Earth observation data on Switzerland. The portal is operated by the University of Geneva and the United Nations Environment Programme/GRID-Geneva, together with the University of Zurich and the Federal Institute for Forest, Snow and Landscape Research – WSL.
- [EnviDat](https://www.envidat.ch/) - Environmental research data from Switzerland, provided by research units of the Swiss Federal Institute for Forest, Snow and Landscape WSL.

### Cantonal and city level

- [Kantonale Geoportale](https://www.kgk-cgc.ch/geodaten/kantonale_geoportale) - Overview of all cantonal geo portals.
- [Kanton Aargau](https://www.ag.ch/de/verwaltung/dfr/geoportal)
- [Kanton Appenzell Ausserrhoden](https://www.geoportal.ch/ktar)
- [Kanton Appenzell Innerrhoden](https://www.ai.ch/themen/planen-und-bauen/geodaten-und-plaene/geoportal)
- [Kanton Basel-Landschaft](https://www.baselland.ch/politik-und-behorden/direktionen/volkswirtschafts-und-gesundheitsdirektion/amt-fur-geoinformation/geoportal)
- [Kanton Basel-Stadt](https://www.bs.ch/bvd/grundbuch-und-vermessungsamt/geo/geodaten)
- [Kanton Bern](https://www.agi.dij.be.ch/de/start.html)
- [Stadt Bern](https://map.bern.ch/geoportal/)
- [Kanton Freiburg](https://map.geo.fr.ch/)
- [Kanton Genf](https://map.sitg.ge.ch/app/)
- [Kanton Glarus](https://www.gl.ch/verwaltung/bau-und-umwelt/hochbau/raumentwicklung-und-geoinformation/geoportal-kanton-glarus.html/808)
- [Kanton Graubünden](https://geo.gr.ch/)
- [Kanton Jura](https://www.jura.ch/DEN/SDT/GeoPortail/GeoPortail-du-Canton-du-Jura.html)
- [Kanton Luzern](https://geoportal.lu.ch/karten)
- [Kanton Neuenburg](https://www.ne.ch/autorites/DDTE/SGRF/SITN/geoportail/Pages/accueil.aspx)
- [Kantone Nidwalden Obwalden](https://www.gis-daten.ch/geodaten/geodatenkatalog/)
- [Kanton Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-1262910-DE.html)
- [Kanton Schwyz](https://www.sz.ch/behoerden/verwaltung/umweltdepartement/amt-fuer-geoinformation/geoportal-webgis.html/8756-8758-8802-9447-9448-9462)
- [Kanton Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/geoportal/)
- [Kanton St. Gallen](https://www.sg.ch/bauen/geoinformation/gi/geodaten.html)
- [Kanton Tessin](https://map.geo.ti.ch/)
- [Kanton Thurgau](https://map.geo.tg.ch) – Separate geo data shop [here](https://shop.geo.tg.ch/) (requires registration).
- [Kanton Uri](https://www.ur.ch/geoinformationen) - Geo portal with download option [here](https://geo.ur.ch).
- [Kanton Waadt](https://www.geo.vd.ch/)
- [Kanton Wallis](https://www.vs.ch/de/web/egeo)
- [Kanton Zug](https://zg.ch/de/planen-bauen/geoinformation/geoinformationen-nutzen)
- [Kanton Zürich](https://geo.zh.ch/data)
- [Stadt Zürich](https://www.stadt-zuerich.ch/geodaten/)

### OpenStreetMap

- [Swiss OpenStreetMap Association (SOSM)](https://sosm.ch/) - Association that supports projects, people, companies, and organizations in Switzerland that collect, use, process, and distribute open and free geodata.
- [OpenStreetMap CH](https://osm.ch/) - OpenStreetMap dataset limited to Switzerland and tools based on this reduced dataset (provided by [SOSM](https://sosm.ch/)). Hourly updated [extracts here](https://planet.osm.ch/).
- [BBBike's OSM download server](https://download.bbbike.org/osm/) - Data extracts from the OpenStreetMap project for more than 200 areas worldwide in various formats. E.g., extracts for [Zurich here](https://download.bbbike.org/osm/bbbike/Zuerich/).
- [Geofabrik's OSM download server](https://download.geofabrik.de/europe/switzerland.html) - Helpful OpenStreetMap data extracts for Switzerland (e.g., as ESRI shapefiles). Geofabrik's inspiring [portfolio of geodata projects](https://www.geofabrik.de/projects/) is definitely worth a look too.

### Miscellaneous Geo Data

- [GeoHarvester](https://davidoesch.github.io/geoservice_harvester_poc/) - Portal that brings together official geodata from Swiss government entities. [[GitHub](https://github.com/davidoesch/geoservice_harvester_poc)]
- [geospatial-data-catalogs](https://github.com/giswqs/geospatial-data-catalogs) - A list of open geospatial datasets available on AWS, Earth Engine, Planetary Computer, NASA CMR, and STAC Index.
- [GeoBeer Switzerland](https://geobeer.ch/) - GeoBeerCH is an informal meeting of people interested in geography, GIS, cartography and the latest technologies.
- [mapplus.ch](https://www.mapplus.ch/) - Various Geo Data portals, viewers and links.

## Linked Open Data

- [LINDAS ecosystem overview](https://lindas.admin.ch/ecosystem/) - LINDAS (Linked Data Service) allows public administrations to publish their data in the form of Knowledge Graphs and make them accessible via <https://lindas.admin.ch>. The service is offered by the [Swiss Federal Archives](https://www.bar.admin.ch/bar/en/home.html).
- [Fedlex](https://fedlex.data.admin.ch/en-CH/home/intro) - Fedlex is the Federal Chancellery platform on which federal legislation is published. It is primarily used to publish the Official Federal Gazette, the Official Compilation of Federal Legislation, and the Classified Compilation of Federal Legislation, i.e., the consolidated version of federal legislation and international law texts.
- [Federal Geoportal Linked Data](https://geo.ld.admin.ch) - Linked Data Service of the Federal Geoportal.
- [Stadt Zürich LOD](https://www.stadt-zuerich.ch/prd/de/index/statistik/publikationen-angebote/linked-open-data.html)
- [Linked Data Meetup](https://www.bfh.ch/de/themen/linked-data/) - The Linked Data Meetup is a collaboration between the Swiss Federal Archives (BAR) and the BFH's Public Sector Transformation Institute. The meetup is aimed at users of linked data, especially in the LINDAS environment.

## APIs

- [opendata.swiss](https://handbook.opendata.swiss/de/content/nutzen/api-nutzen.html)
- [Geo Admin](https://docs.geo.admin.ch/)
- [Geo Admin STAC](https://www.geo.admin.ch/de/geo-dienstleistungen/geodienste/downloadienste/stac-api.html) - API for Geo Admin's Spatial-Temporal Asset Catalog.
- [Shared mobility](https://www.admin.ch/gov/de/start/dokumentation/medienmitteilungen.msg-id-82109.html)
- [Additional API documentation](https://nrohrbach.github.io/ApiDocumentation/) - More information for APIs provided by opendata.swiss, Geo Admin, and Shared mobility.
- [Schweiz Tourismus](https://developer.myswitzerland.io/)
- [SRGSSR](https://developer.srgssr.ch/) - APIs of the publicly funded broadcaster in Switzerland.
- [CKAN API documentation](https://docs.ckan.org/en/latest/api/)
- [OpenERZ](https://github.com/metaodi/openerz) - OpenERZ is an open API for waste collection data from many different municipalities in Switzerland (e.g., Zurich, Basel, St. Gallen, Uster, Thalwil, Adliswil, Horgen, etc.). API and Python client provided by OGD wizard [metaodi](https://github.com/metaodi) aka Stefan Oderbolz.
- [OpenPLZ API](https://www.openplzapi.org/en/) - OpenPLZ API is an open data project that makes a public street and postal code directory for Austria, Germany, Liechtenstein, and Switzerland available via an open REST API interface.
- [OpenHolidays API](https://www.openholidaysapi.org/en/) - Open Data project that collects public holiday and school holiday data and makes it available via an open REST API interface.

## Organizations, Initiatives, Events and Projects

- [Statistical Institutions in Switzerland](https://www.bfs.admin.ch/bfs/de/home/bfs/oeffentliche-statistik/system-oeffentliche-statistik/statistikinstitutionen-schweiz.html)
- [Korstat](http://www.corstat.ch/de/) - Conference of the regional statistical offices in Switzerland.
- [Statistiktage](https://www.statistiktage.ch/) - Annual conference organized by [Swiss Statistical Society](https://www.stat.ch/en/) and [IMSD](https://www.imsd.ch/de/).
- [Project Rosling](https://www.projectrosling.ch) - Swiss Confederation's «Project Rosling» aims to expand dialogue on data and statistics and deepen knowledge.
- [opendata.ch](https://opendata.ch/de/) - Swiss section of the Open Knowledge Foundation.
- [opendata.ch](https://opendata.ch/events/) - List of hackathons and events.
- [Open Data Beer](https://opendatabeer.ch/)
- [Prototype Fund](https://prototypefund.de/en/) - A funding program of the Federal Ministry of Education and Research (BMBF) that is managed and evaluated by the Open Knowledge Foundation Germany. Individuals and small teams (of coders, hackers, designers, and more) can receive funding to test their ideas and develop open source applications in the areas of Civic Tech, Data Literacy, IT Security, and Software Infrastructure.
- [öffentlichkeitsgesetz.ch](https://www.oeffentlichkeitsgesetz.ch/deutsch/) - Forum for transparency in administration.
- [Parldigi](https://www.parldigi.ch/de/) - Parlamentarische Gruppe Digitale Nachhaltigkeit.
- [DINACON](https://dinacon.ch/) - Conference for digital sustainability.
- [Lobbywatch](https://lobbywatch.ch/de/seite/datenexport) - Lobbywatch enables citizens and media professionals to find out what interests politicians in Bern represent. They offer their data as an open database for independent evaluations.

## Newsletters

- [Bundesamt für Statistik](https://scnem.com/a.php?sid=ffnuk.16937bf,f=999)
- [Open Data CH](https://opendata.us7.list-manage.com/subscribe?u=c01c0e110415680950f8958e4&id=12200d2993)

## Podcasts

- [Statistisch gesehen](https://feeds.captivate.fm/statistisch-gesehen/) - Podcast of the Statistical Office Kanton Zürich.
- [StatGespräch](https://www.destatis.de/DE/Mediathek/Podcasts/_inhalt.html) - Podcast of the Statistical Office Germany.

## Miscellaneous

- [Swiss OGD information](https://www.bfs.admin.ch/bfs/en/home/services/ogd.html)
- [Swiss OGD strategy](https://www.bfs.admin.ch/bfs/en/home/services/ogd/documentation.assetdetail.16164831.html)
- [Geschäftsstelle OGD BFS](https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd/geschaeftsstelle.html) - This unit coordinates measures to implement the OGD strategy of the Swiss government and provides support to both data publishers and users.
- [Digitale Verwaltung Schweiz](https://www.digitale-verwaltung-schweiz.ch/)
- [National data management NaDB](https://www.bfs.admin.ch/bfs/en/home/nadb/nadb.html) - The I14Y interoperability platform is available since June 2021 to promote the multiple use of data. All of the Federal Administration’s data collections are described here. In addition, a directory of electronic interfaces (APIs) will facilitate access to the actual data.
- [Swiss DCAT Standard](https://www.ech.ch/de/ech/ech-0200/1.0) - eCH-0200 DCAT-Profile for Swiss data portals.
- [adminR Code Base](https://github.com/swiss-adminR/pkgs) - A curated list of R packages and R code created and used by Swiss public institutions.
- [Forschungsstelle Digitale Nachhaltigkeit Uni Bern](https://www.digitale-nachhaltigkeit.unibe.ch/) - The Research Center for Digital Sustainability focuses on key topics such as Digital Sustainability, Open Data, Linked Data, and Open Government. The center offers studies, research, services, support, and lectures (see below) in these areas.
- [Open Data lectures Uni Bern](https://www.digitale-nachhaltigkeit.unibe.ch/studium/open_data_veranstaltung/index_ger.html) - Comprehensive lectures about Open Data in Switzerland provided by Forschungsstelle Digitale Nachhaltigkeit of the University of Bern.
- [Swiss OSS Benchmark](https://ossbenchmark.com/institutions) - Comprehensive list of open source GitHub repos/orgs of Swiss institutions.

## Media

Swiss data journalism teams.

- [Neue Zürcher Zeitung Visuals Team](https://github.com/nzzdev/st-methods) - Repository containing methods and code used for stories by [NZZ Visuals](https://twitter.com/nzzvisuals).
- [SRF Data](https://srfdata.github.io/) - Code and data from SRF Data, the data-driven journalism unit of Swiss Radio and TV (SRF) [[Publications and projects]](https://www.srf.ch/news/srf-data).
- [Tamedia Data Desk](https://github.com/tamedia-ddj) - GitHub account of Tamedia's data journalism team [[Projects of Ressort «Daten & Interaktiv»]](https://interaktiv.tagesanzeiger.ch/).

## Social Media

- [Twitter lists by Open Data CH](https://twitter.com/OpendataCH/lists)

## International

Interesting international data portals and websites.

### Data portals and sources

- [List of European Statistical Offices](https://www.destatis.de/EN/Service/Address-Book/europe.html) - List provided by [Destatis](https://www.destatis.de).
- [European Union](https://data.europa.eu/en) - Official data portal of the European Commission.
- [Eurostat](https://ec.europa.eu/eurostat/web/main/data) - Data portal of the Statistical Office of the European Union [[Database]](https://ec.europa.eu/eurostat/web/main/data/database) [[Geo Data]](https://ec.europa.eu/eurostat/web/gisco/overview) [[Statistical Atlas]](https://ec.europa.eu/statistical-atlas/viewer/?config=RYB-2022.json) [[Choropleth Map Generator]](https://gisco-services.ec.europa.eu/image/screen/home) [[Experimental Statistics]](https://ec.europa.eu/eurostat/web/experimental-statistics).
- [IATE](https://iate.europa.eu/home) - Terminology database of the EU.
- [Germany](https://www.govdata.de/) - Germany's main OGD data portal.
- [Germany](https://www-genesis.destatis.de/genesis/online) - Database of the Federal Statistical Office of Germany [[Experimental Statistics]](https://www.destatis.de/EN/Service/EXDAT/_node.html).
- [Germany](https://gdz.bkg.bund.de/) - Geodata shop of Germany's Federal Agency for Cartography and Geodesy (BKG).
- [Germany](https://www.geoportal.de/) - BKG's interactive geodata offering «geoportal.de».
- [Germany](https://basemap.de/) - basemap.de is a collection of cartographic products developed by the federal and state governments.
- [Albania](https://www.instat.gov.al/) - Statistical office.
- [Andorra](https://www.estadistica.ad/portal/apps/sites/#/estadistica-en) - Statistical Office.
- [Austria](https://www.statistik.at/en) - Statistical Office.
- [Austria](https://www.data.gv.at/)
- [Belarus](http://www.belstat.gov.by/en/) - Statistical Office.
- [Belgium](https://statbel.fgov.be/en) - Statistical Office.
- [Belgium](https://data.gov.be/en)
- [Bosnia and Herzegovina](https://bhas.gov.ba/) - Statistical Office.
- [Bulgaria](https://www.nsi.bg/en) - Statistical Office.
- [Croatia](http://www.dzs.hr/default_e.htm) - Statistical Office.
- [Cyprus](https://www.cystat.gov.cy/en/default) - Statistical Office.
- [Czechia](http://www.czso.cz/csu/czso/home) - Statistical Office.
- [Denmark](http://www.dst.dk/en) - Statistical Office.
- [Estonia](http://www.stat.ee/) - Statistical Office.
- [Estonia](https://avaandmed.eesti.ee/)
- [Finland](https://www.opendata.fi/en)
- [Finland](https://stat.fi/index_en.html)
- [France](http://www.insee.fr/en) - Statistical Office.
- [France](https://www.data.gouv.fr/en/datasets/)
- [Greece](http://www.statistics.gr/en/home) - Statistical Office.
- [Greece](https://www.data.gov.gr/)
- [Hungary](http://www.ksh.hu/) - Statistical Office.
- [Iceland](http://www.statice.is/) - Statistical Office.
- [Ireland](http://www.cso.ie/) - Statistical Office.
- [Ireland](https://data.gov.ie/)
- [Italy](http://www.istat.it/en/) - Statistical Office.
- [Italy](https://www.dati.gov.it/)
- [Kosovo](https://ask.rks-gov.net/) - Statistical Office.
- [Latvia](https://stat.gov.lv/en)
- [Liechtenstein](https://www.statistikportal.li/) - Statistical Office.
- [Lithuania](https://www.stat.gov.lt/en) - Statistical Office.
- [Luxembourg](https://statistiques.public.lu/en.html) - Statistical Office.
- [Luxembourg](https://data.public.lu/en/#)
- [Malta](https://nso.gov.mt/) - Statistical Office.
- [Moldova](http://statistica.gov.md/index.php) - Statistical Office.
- [Monaco](http://www.monacostatistics.mc/) - Statistical Office.
- [Montenegro](http://monstat.org/eng/index.php) - Statistical Office.
- [Netherlands](http://www.cbs.nl/en-GB/default.htm) - Statistical Office.
- [Netherlands](https://data.overheid.nl/en)
- [North Macedonia](http://www.stat.gov.mk/Default_en.aspx) - Statistical Office.
- [Norway](http://www.ssb.no/english/) - Statistical Office.
- [Poland](http://stat.gov.pl/en/) - Statistical Office.
- [Portugal](https://www.ine.pt/) - Statistical Office.
- [Portugal](https://www.pordata.pt/en/Home) - Dataportal «Pordata»
- [Romania](http://www.insse.ro/cms/en) - Statistical Office.
- [Romania](https://data.gov.ro/en/)
- [San Marino](https://www.statistica.sm/pub1/StatisticaSM/en/) - Statistical Office.
- [Serbia](https://www.stat.gov.rs/en-us/) - Statistical Office.
- [Slovakia](https://slovak.statistics.sk) - Statistical Office.
- [Slovenia](http://www.stat.si/StatWeb/en/home) - Statistical Office.
- [Spain](http://www.ine.es/en/welcome.shtml) - Statistical Office.
- [Sweden](http://www.scb.se/en/) - Statistical Office.
- [Türkiye](https://www.tuik.gov.tr/Home/Index) - Statistical Office.
- [Ukraine](http://www.ukrstat.gov.ua/) - Statistical Office.
- [Ukraine](https://data.gov.ua/en/)
- [United Kingdom:](http://www.ons.gov.uk/ons/index.html) - Statistical Office.
- [United Kingdom](https://www.data.gov.uk/)
- [Russian Federation](https://eng.rosstat.gov.ru/) - Statistical Office.
- [Australia](https://data.gov.au/)
- [New Zealand](https://www.stats.govt.nz/all-topics/)
- [Singapore](https://beta.data.gov.sg/)
- [Hongkong](https://data.gov.hk/en/)
- [India](https://data.gov.in/)
- [Canada](https://www.statcan.gc.ca/en/start)
- [United States](https://data.gov/)
- [Socrata's Open Data Network](https://www.opendatanetwork.com/) - Broad offering of US-American OGD datasets. API docs [here](https://dev.socrata.com/consumers/getting-started.html).
- [FRED Economic Data](https://fred.stlouisfed.org/) - Online database with hundreds of thousands of economic data time series from American, international, public, and private sources.
- [NASDAQ Data Portal](https://data.nasdaq.com/)
- [Global Biodiversity Information Facility](https://www.gbif.org)

### Curated lists

- OKFN Data Portals [[Website](https://dataportals.org/)] [[GitHub repo](https://github.com/okfn/dataportals.org)] - Very large and comprehensive list of data sources maintained by the [Open Knowledge Foundation](https://okfn.org/).
- Open Data Inception [[Database](https://data.opendatasoft.com/explore/dataset/open-data-sources%40public/table/?sort=code_en)] [[Data Map](https://opendatainception.io/)] - Very large and comprehensive list of data sources maintained by the data portal vendor [Opendatasoft](https://www.opendatasoft.com/). See [this article for background information](https://www.opendatasoft.com/en/blog/how-we-put-together-a-list-of-1600-open-data-portals-around-the-world-to-help-open-data-community/).
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets#government) - GitHub list with many more links to public government datasets.
- [Awesome Transit](https://github.com/CUTR-at-USF/awesome-transit) - Community list of transit APIs, apps, datasets, research, and software.
- [Awesome Hackathon](https://github.com/dribdat/awesome-hackathon) - Recommendations of tools for crowdsourcing primarily from the open data community.

### Miscellaneous

- [Open Data Handbook](https://opendatahandbook.org/) – Guides, case studies, and resources for government and civil society on the _«what, why & how»_ of open data. Provided by the [Open Knowledge Foundation](https://okfn.org/).
- [bund.dev](https://bund.dev/) - «Bundesstelle für Open Data». Very active and influential non-governmental open data initiative [[GitHub](https://github.com/bundesAPI)].
- [Greenpeace Open Data Portal](https://daten.greenpeace.de/dataset/)
- [Code for Germany](https://www.codefor.de/) - A network of open government experts who work as volunteer civic developers for sustainable digital change in politics and administration. Strong focus on Open Data; list of [inspiring projects here](https://www.codefor.de/projekte/).
- [United Nations](https://data.un.org/) - Data portal of the UN.
- [OECD](https://data.oecd.org/) - OECD data portal.
- [OECD OGD information](https://www.oecd.org/gov/digital-government/open-government-data.htm) - OGD ranking of OECD.
- [Worldbank](https://data.worldbank.org/country/CH) - Data about Switzerland.
- [Our World in Data](https://ourworldindata.org/search?q=switzerland) - Data about Switzerland.
- [Open Data Watch](https://odin.opendatawatch.com/Report/) - Open data rankings and much more.
- [Open Data Monitor](https://opendatamonitor.eu/frontend/web/index.php?r=datacatalogue%2Flist)

## Contribute

Contributions are always welcome. Just open an issue or a pull request with your suggestions.
