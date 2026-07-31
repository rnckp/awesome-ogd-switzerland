# Awesome Open Government Data Switzerland

[![GitHub Stars](https://img.shields.io/github/stars/rnckp/awesome-ogd-switzerland.svg)](https://github.com/rnckp/awesome-ogd-switzerland)
[![GitHub Issues](https://img.shields.io/github/issues/rnckp/awesome-ogd-switzerland.svg)](https://github.com/rnckp/awesome-ogd-switzerland)
[![GitHub Issues](https://img.shields.io/github/issues-pr/rnckp/awesome-ogd-switzerland.svg)](https://img.shields.io/github/issues-pr/rnckp/awesome-ogd-switzerland)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
<a href="https://github.com/astral-sh/ruff"><img alt="linting - Ruff" class="off-glb" loading="lazy" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>

A manually curated list of Open Government Data (OGD) portals, websites, APIs, tools, and related resources in Switzerland. Selected international links support Swiss comparisons.

<details>
<summary><strong>Table of Contents</strong></summary>

- [Curation Policy](#curation-policy)
- [Data Sources](#data-sources)
- [Geo Data](#geo-data)
- [Linked Open Data](#linked-open-data)
- [APIs](#apis)
- [Open-source Tools](#open-source-tools)
- [Organizations](#organizations-initiatives-events-and-projects)
- [Newsletters](#newsletters)
- [Podcasts](#podcasts)
- [Miscellaneous](#miscellaneous)
- [Media](#media)
- [International](#international)
- [Contribute](#contribute)

</details>

## Curation Policy

This list follows the [Open Definition](https://opendefinition.org/): data must permit free use, modification, and redistribution, including commercial reuse. Tools must publish their source code under an [OSI-approved license](https://opensource.org/licenses). Related guides, communities, and media must be freely accessible, directly relevant, and operated by an official institution, established non-profit, research organization, or transparent community project.

Registration is acceptable when it is free and non-discriminatory, but payment, case-by-case permission, non-commercial-only terms, or unclear reuse rights are exclusion criteria for data and tools.

Repositories and catalogs that contain both open and restricted records are clearly identified. Always verify the license of an individual dataset before reuse.

## Data Sources

Portals and data sources that provide access to Swiss Open Government Data.

### National

#### Statistical and Administrative Data

- [opendata.swiss](https://opendata.swiss/de) - Central catalog of Swiss Open Government Data, operated by the Federal Statistical Office (BFS). **The most important entry point for all things OGD in Switzerland.**
- [BFS Data Portal](https://data.bfs.admin.ch/) - New data portal of the [Federal Statistical Office](https://www.bfs.admin.ch/bfs/en/home/services.html).
- [BFS Swiss Stats Explorer](https://stats.swiss/) - BFS web application designed to make it easier to find, understand and use their data.
- [BFS STAT-TAB](https://www.pxweb.bfs.admin.ch/pxweb/en/) - This interactive database of the Federal Statistical Office provides detailed statistical data and enables simple, customized data queries. The resulting tables can be exported in various formats.
- [I14Y - Metadata catalog of Switzerland](https://www.i14y.admin.ch/en/home) - The I14Y interoperability platform is Switzerland’s national data catalog. It ensures the efficient exchange of data between authorities, companies, and citizens. The platform provides a continuously expanded overview of data collections and interfaces from the Confederation, cantons, and communes, with metadata made centrally available.
- [BFS Registers](https://www.bfs.admin.ch/bfs/en/home/registers.html) - Official Swiss Enterprise Register, Population Register and Federal Register of Buildings and Dwellings.
- [Visualize](https://visualize.admin.ch) - Create and embed visualizations from any dataset provided by the LINDAS Linked Data Service.
- [Swiss official commune register](https://www.bfs.admin.ch/bfs/en/home/basics/swiss-official-commune-register.html) - Register of all Swiss commune names, numbers, and past mutations. ([App](https://www.agvchapp.bfs.admin.ch/de/home))
- [TERMDAT](https://www.bk.admin.ch/bk/de/home/dokumentation/sprachen/termdat.html) - The Federal Administration's terminology database ([direct access](https://www.termdat.ch/search)). The EU's terminology database IATE can be accessed [here](https://iate.europa.eu/home).
- [ÖREB-Kataster](https://www.cadastre.ch/de/oereb-kataster) - Extracts from the Cadastre of Public-law Restrictions on Landownership containing legally binding information about the most important public law restrictions that apply to a given plot of land.

#### Parliamentary Data

- [Schweizer Parlament](https://www.parlament.ch/de/%C3%BCber-das-parlament/fakten-und-zahlen/open-data-web-services) - Open Data and web services of the Swiss Parliament.
- [OpenParlData.ch](https://openparldata.ch/) - The [API](https://api.openparldata.ch/documentation) offers harmonized data on political actors, parliamentary proceedings, decrees, consultations, votes, and more from [78](https://admin.openparldata.ch/#/bodies) national, cantonal, and municipal parliaments.
- [Swissvotes](https://swissvotes.ch/page/dataset) - Comprehensive dataset and codebook for all Swiss federal popular votes since 1848, downloadable as CSV and XLSX under CC BY 4.0.
- [Federal Popular Votes Dashboard](https://abstimmungen.admin.ch/en/overview) - Official results with downloadable historical and election-day data, including municipal-level JSON through the API listed below.
- [SIMAP](https://www.simap.ch/) - Official public procurement platform of the Confederation, cantons, and communes. Its public JSON API permits commercial reuse.
- [Amtsblattportal](https://amtsblattportal.ch/#!/home) - Official Gazettes Portal. A publishing center for entities that publish official and commercially relevant publications in the Swiss Official Gazette of Commerce (SOGC) and in official cantonal gazettes. Data can also be imported and exported using a [REST API](https://amtsblattportal.ch/docs/api/).

#### Legal Data

- [Fedlex – Publikationsplattform des Bundesrechts](https://www.fedlex.admin.ch/de/home) - Publication platform for federal law.
- [LexFind](https://www.lexfind.ch/) - Unified search tool indexing all federal and cantonal law collections.
- [opencaselaw.ch](https://opencaselaw.ch/) - OpenCaseLaw is the largest open dataset of Swiss case law and the first LLM-ready interface to federal and cantonal legislation. Free to use, updated daily, independently funded.
- [entscheidsuche.ch](https://entscheidsuche.ch/) - This freely accessible portal offers a search of all published court decisions from Swiss courts at all levels. GitHub scraper repository of the project [here](https://github.com/entscheidsuche).
- [Onlinekommentar.ch](https://onlinekommentar.ch/) - The first non-profit and Open Access commentary platform in Switzerland. [[API](https://onlinekommentar.ch/en/apis)]
- [Center for Legal Data Science (UZH)](https://www.clds.uzh.ch/en/knowledge/databases.html) - Data-driven legal research and dataset links.

#### Financial and Economic Data

- [Swiss Federal Finance Administration FFA](https://www.efv.admin.ch/efv/en/home/finanzberichterstattung/daten/datencenter.html) - Swiss Federal budget data. Data portal [here](https://www.data.finance.admin.ch/superset/dashboard/startseite/).
- [Schweizerische Nationalbank SNB](https://data.snb.ch/de) - Swiss National Bank's data portal.

#### Federal Offices and Other National Data Sources

- [Bundesamt für Gesundheit BAG](https://www.bag.admin.ch/de/zahlen-statistiken) - Federal Office of Public Health.
- [Dashboard health insurance OKP](https://opendata.swiss/en/dataset/dashboard-krankenversicherung-okp) - Quarterly downloadable data on compulsory health insurance in Switzerland.
- [Key data on Swiss hospitals](https://opendata.swiss/en/dataset?keywords_en=health-insurance) - Machine-readable hospital statistics published by the Federal Office of Public Health.
- [Versorgungsatlas](https://www.versorgungsatlas.ch/) - Swiss Health Care Atlas provided by BAG and [Swiss Health Observatory](https://www.obsan.admin.ch/en). Public health data covering more than 100 indicators.
- [Infectious Diseases Dashboard (IDD)](https://idd.bag.admin.ch/) - Information on cases of infection and illness in Switzerland and Liechtenstein caused by various pathogens, provided by the Federal Office of Public Health FOPH / BAG.
- [Swissmedic Open Government Data](https://www.swissmedic.ch/swissmedic/en/home/services/listen_neu.html) - Monthly machine-readable data on authorized human and veterinary medicines, plus daily data on registered Swiss medical-device operators.
- [arbeit.swiss](https://www.amstat.ch/v2/amstat_de.html) - Data portal of the State Secretariat for Economic Affairs (SECO).
- [Agrarmarktdaten](https://www.agrarmarktdaten.ch/) - Comprehensive data portal provided by the Federal Office for Agriculture. The portal provides ongoing information and data on current market events in various agricultural and food markets. It includes price and quantity information along the value chain, from production to consumption.
- [Agrarbericht](https://www.blw.admin.ch/blw/de/home/agrarbericht.html) - Agricultural data provided by the Federal Office for Agriculture.
- [Schweizer Nährwertdatenbank](https://naehrwertdaten.ch/de/) - The Swiss Food Composition Database contains information on the composition of foods available in Switzerland. The database is operated by the Federal Food Safety and Veterinary Office (FSVO).
- [Bundesamt für Energie BFE](https://www.bfe.admin.ch/bfe/de/home/versorgung/statistik-und-geodaten/energiestatistiken.html) - Federal Office of Energy statistics and geodata.
- [Swiss Energy Dashboard](https://energiedashboard.admin.ch/bfe-url) - Current electricity, gas, energy-price, and supply data from the Federal Office of Energy, with a public read-only REST API.
- [Bundesamt für Sozialversicherungen BSV](https://www.bsv.admin.ch/de/statistik) - Federal Social Security Office.
- [Bundesamt für Umwelt BAFU](https://www.bafu.admin.ch/bafu/de/home/zustand.html) - Federal Office for the Environment.
- [Eidgenössische Steuerverwaltung](https://www.estv.admin.ch/estv/de/home/die-estv/steuerstatistiken-estv.html) - Federal Tax Administration.
- [Staatssekretariat für Migration SEM](https://www.sem.admin.ch/sem/de/home/publiservice/statistik.html) - State Secretariat for Migration.
- [Zentraler Firmenindex ZEFIX](https://www.zefix.admin.ch/de/search/entity/welcome) - API [here](https://www.zefix.admin.ch/ZefixPublicREST/swagger-ui/index.html).
- [Eidgenössisches Institut für Geistiges Eigentum IGE](https://www.ige.ch/de/uebersicht-dienstleistungen/digitales-angebot) - Federal Institute of Intellectual Property.
- [Konjunkturforschungsstelle ETH Zürich](https://kof.ethz.ch/daten.html)
- [Unfallversicherung UVG](https://www.unfallstatistik.ch/index.htm)

#### Real Estate and Buildings Data

- [Federal Register of Buildings and Dwellings (GWR/RegBL)](https://www.bfs.admin.ch/bfs/de/home/register/gebaeude-wohnungsregister.html) - National register of all buildings and dwellings in Switzerland, maintained by the Federal Statistical Office (BFS). Source of the EGID (building identifier) and EWID (dwelling identifier) used as reference keys across Swiss administrative data. Web application available at [housing-stat.ch](https://www.housing-stat.ch).
- [Bundesamt für Wohnungswesen BWO – Wohnungsmarkt](https://www.bwo.admin.ch/de/wohnungsmarkt) - Federal Housing Office market portal. Includes the quarterly
  [«Wohnungsmarkt auf einen Blick»](https://www.bwo.admin.ch/de/wohnungsmarkt-auf-einen-blick) and [Zahlen und Fakten zum Wohnen](https://www.bwo.admin.ch/de/zahlen-und-fakten-wohnen) with vacancy, rent and housing-market indicators.
- [BFS Bau- und Wohnungswesen](https://www.bfs.admin.ch/bfs/de/home/statistiken/bau-wohnungswesen.html) - BFS section on construction and housing: building permits, construction activity, vacancy, housing stock.
- [Schweizerischer Baupreisindex (BAP)](https://www.bfs.admin.ch/bfs/de/home/statistiken/preise/baupreise.html) - Semi-annual construction price index published by BFS, covering Hochbau and Tiefbau.
- [Wohnimmobilienpreisindex (IMPI)](https://www.bfs.admin.ch/bfs/de/home/statistiken/preise/erhebungen/impi.html) - Quarterly residential property price index for owner-occupied homes, based on transaction data from major Swiss mortgage banks.
- [Mietpreisindex (MPI)](https://www.bfs.admin.ch/bfs/de/home/statistiken/preise/erhebungen/mpi.html) - Rental price index for permanently rented dwellings; the largest single component of the Swiss CPI.
- [ARE – Daten und Analysen](https://www.are.admin.ch/de/daten) - Federal Office for Spatial Development. Spatial monitoring, Bauzonenstatistik, settlement development data, Web-GIS ARE.
- [Daten der amtlichen Vermessung (cadastre.ch)](https://www.cadastre.ch/de/daten-der-av) - Official cadastral survey (AV) data of Switzerland, operated by swisstopo. Source of parcel-level geometry; cantonal data also aggregated at [geodienste.ch](https://geodienste.ch/) (already listed).

#### Environment, Tourism and Meteorology Data

- [Swiss Tourism Data](https://www.tourismdata.ch/) - The portal is part of the National Data Infrastructure for Tourism (NaDIT) project. It serves as the catalogue of metadata of the most important data sources for Swiss tourism.
- [Bundesamt für Meteorologie und Klimatologie MeteoSchweiz](https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html) - Federal Office of Meteorology and Climatology MeteoSwiss.
- [SLF data service](https://www.slf.ch/en/services-and-products/slf-data-service/) - Data collected and produced in the context of avalanche warnings.
- [«Hydrodaten» Bundesamt für Umwelt BAFU](https://www.hydrodaten.admin.ch/de/aktuelle-lage) - Hydrological data and forecasts. Actual data [here via LINDAS](https://environment.ld.admin.ch/.well-known/void/dataset/hydro).
- [GLAMOS DOI products](https://doi.glamos.ch/) - Swiss glacier inventories, length changes, mass balances, and volume changes with persistent identifiers and CC BY 4.0 licenses.
- [Swiss National Fauna Databank](https://ipt.gbif.ch/resource?r=ifn) - Standardized species-occurrence records from InfoSpecies, downloadable as Darwin Core under CC BY 4.0.

#### Academic and Research Data

- [FORS SWISSUbase](https://www.swissubase.ch/de/) - Cross-disciplinary repository for Swiss universities; access conditions and licenses vary by record.
- [Schweizerischer Nationalfonds SNF](https://data.snf.ch/datasets) - Swiss National Science Foundation. GitHub repositories with SNF's data stories [here](https://github.com/snsf-data).
- [CERN](https://opendata.cern.ch/) - Open data portal of [CERN](https://home.web.cern.ch/), the European Laboratory for Particle Physics.
- [DaSCH Service Platform](https://dasch.swiss/about-us/platform) - Open-by-default FAIR repository for humanities research data, with Linked Data, IIIF, and REST access; verify record-level access conditions.
- [Materials Cloud Archive](https://archive.materialscloud.org/about) - Open repository for reproducible computational-materials research data.

#### Cultural Heritage Data

- [e-rara](https://www.e-rara.ch/) - Digitized Swiss printed works with public-domain or record-level open reuse terms and machine access through [OAI-PMH, IIIF, full-text, and download interfaces](https://www.e-rara.ch/wiki/apiinfo).

#### Transport Data

- [SBB Open Data](https://data.sbb.ch/pages/home/) - Swiss Federal Railways data portal.
- [Open Data Platform Mobility Switzerland](https://opentransportdata.swiss/en/) - National public-transport and real-time road-traffic data platform, including FEDRO traffic counters and alerts.
- [FEDRO open vehicle data](https://www.astra.admin.ch/en/vehicle-data) - Anonymized vehicle inventories, new registrations, and vehicle types available as unrestricted standard datasets.

### Cantonal

- [Aargau](https://www.ag.ch/de/themen/datenportal#/)
- [Basel Stadt](https://data.bs.ch/explore/)
- [Basel Land](https://data.bl.ch/explore/)
- [Basel Land Statistical Office](https://www.baselland.ch/politik-und-behorden/direktionen/finanz-und-kirchendirektion/statistisches-amt)
- [Bern](https://www.fin.be.ch/de/start/themen/OeffentlicheStatistik/statistikportal.html)
- [Fribourg / Freiburg](https://opendata.fr.ch/pages/home/)
- [Fribourg / Freiburg Statistical Office](https://www.fr.ch/de/vwbd/stata)
- [Genf](https://sitg.ge.ch/search?category=data) - Alternative portal [here](https://statistique.ge.ch/).
- [Geneva Public Transport](https://opendata.tpg.ch/pages/accueil/)
- [Glarus](https://opendata.swiss/en/organization/kanton-glarus) - Cantonal and Landsgemeinde data, including machine-readable JSON and geodata services.
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
- [Zug](https://zg.ch/de/gesundheitsdirektion/fachstelle-fuer-daten-und-statistik/open-government-data) - Open data portal shared by the canton and city of Zug.
- [Zürich](https://www.zh.ch/de/politik-staat/opendata.zhweb-noredirect.zhweb-cache.html#/)
- [Zürcher Gemeinden in Zahlen](https://zgz.statistik.zh.ch/)

### Cities and Municipalities

- [Bern](https://www.bern.ch/open-government-data-ogd/ogd-nach-themen)
- [Biel/Bienne](https://opendata.swiss/en/organization/biel-bienne) - Bilingual municipal data in open tabular and geospatial formats.
- [Lausanne](https://www.lausanne.ch/officiel/statistique.html)
- [Lugano](https://statistica.lugano.ch/site/dati-ogd/)
- [Luzern](https://www.lustat.ch/statistikportal-stadt-luzern)
- [St. Gallen](https://www.stadt.sg.ch/home/verwaltung-politik/stadt-zahlen/statistikdatenbanken.html)
- [Uster](https://www.uster.ch/opendata)
- [Winterthur](https://stadt.winterthur.ch/themen/die-stadt/winterthur/statistik) – [[GitHub](https://github.com/Stadt-Winterthur)]
- [Zürich](https://data.stadt-zuerich.ch/) – [[GitHub](https://github.com/opendatazurich)]
- [Zürich Tourismus](https://www.zuerich.com/de/business/ueber-zuerich-tourismus/open-data-portal)

### Miscellaneous

- [Historical Statistics of Switzerland](https://hsso.ch/en) - Collection of historical statistics.
- [Open Energy Data CH](https://github.com/OpenEnergyData/energy-data-ch) - List of open datasets related to energy projects in Switzerland. See also this [Open Data CH hackday contribution](https://hack.opendata.ch/project/851) for [Energy Hackday 2020](https://hack.opendata.ch/event/31).
- [Swissgrid](https://www.swissgrid.ch/de/home/customers/topics/energy-data-ch.html) - Energy data.
- [Agristat](https://www.sbv-usp.ch/de/services/agristat-statistik-der-schweizer-landwirtschaft) - Statistical data from Schweizer Bauernverband (not an official government entity).
- [Identitas Tierstatistik](https://tierstatistik.identitas.ch/en/index.html) - Various datasets on livestock and companion animals in Switzerland.
- [Jagdstatistik](https://www.jagdstatistik.ch/de/home) - Wild animal and hunting data from Bundesamt für Umwelt (BAFU).
- [Sucht Schweiz](https://www.suchtschweiz.ch/zahlen-und-fakten/) - Statistical data from Sucht Schweiz (not an official government entity).
- [Memoriav Memobase](https://memobase.ch/de/start) - Searchable audiovisual collections documenting Swiss history.
- [DODIS](https://dodis.ch/search) - Swiss diplomatic documents.
- [Schweizer Landesmuseum](https://sammlung.nationalmuseum.ch/de/maincategory)
- [Swiss Federal Archives](https://www.recherche.bar.admin.ch/recherche/) - Documents on the history of Switzerland since 1798.
- [Schweizerisches Idiotikon](https://idiotikon.ch/projekte) - Comprehensive documentation of Swiss German dialects (not an official government entity).
- [Ortsnamen.ch](https://www.ortsnamen.ch/de/) - Comprehensive catalog of Swiss place names (a project of Schweizerisches Idiotikon). A [searchable map](https://search.ortsnamen.ch/de) and [REST API](https://search.ortsnamen.ch/static/api/swagger/index.html) are also available.
- [Swiss Dwellings](https://zenodo.org/record/7788422) - Notable dataset provided by Archilyse Open Data featuring 45,176 Swiss apartments (370,000 rooms) in ~3,100 buildings, including their geometries, room typology, and visual, acoustical, topological, and daylight characteristics.
- [Christian Catholic Church Switzerland](https://christkatholisch.ch/angebote/opendata/) - Open Data offerings of Christkatholische Kirche Schweiz.

## Geo Data

### National

- [swisstopo](https://www.swisstopo.admin.ch/de/geodata.html) - National geodata portal provided by the Federal Office of Topography (Bundesamt für Landestopographie).
- [geo.admin.ch](https://www.geo.admin.ch/de/home.html) - National geodata portal (Geoportal des Bundes).
- [geo.admin.ch - Strassenverzeichnis](https://map.geo.admin.ch/#/map?lang=de&center=2660000,1190000&z=1&topic=ech&layers=ch.swisstopo.amtliches-strassenverzeichnis&bgLayer=ch.swisstopo.pixelkarte-farbe) - Official directory of all Swiss street names.
- [geocat](https://www.geocat.ch) - Geographic catalog operated by swisstopo. Provides geodata, geoservices, and models from federal offices, cantons, municipalities, research institutes, private companies, and more.
- [geobasisdaten.ch](https://geobasisdaten.ch/) - Geodata portal provided by the [«Konferenz der kantonalen Geoinformations- und Katasterstellen»](https://www.kgk-cgc.ch/). In Switzerland, the basic geodata catalog is a catalog-like listing of all geodata collected by legal authorities, linking them to the underlying legal enactments. In addition to visualizing geodata recorded under geoinformation law, it provides the dataset-specific assignment of responsible bodies and other legally relevant attributes. [More information here](https://www.kgk-cgc.ch/geobasisdaten).
- [geodienste.ch](https://geodienste.ch/) - The intercantonal portal for obtaining geodata and services. Basic geodata is aggregated and made available under the responsibility of the cantons and municipalities.
- [Geoportal.ch](https://www.geoportal.ch/) - Publication platform for Swiss geodata.
- [BFS Plattform Statatlas](https://www.atlas.bfs.admin.ch/de/index.html) - The Federal Statistical Office (BFS) offers several specialist atlases in addition to the central statistical atlas of Switzerland, providing more detailed information on specific areas of life from a statistical perspective. With numerous interactive maps, graphics, and underlying data, a wide variety of geographical processes and relationships can be easily analyzed and evaluated.
- [Datalakes](https://www.datalakes-eawag.ch/) - National geodata portal for in-situ lake measurements.
- [Alplakes](https://www.alplakes.eawag.ch/) - Operational lake models and remote sensing products.
- [Swiss Data Cube](https://www.swissdatacube.org) - 80,000 satellite images and ~30 TB of Earth observation data on Switzerland. The portal is operated by the University of Geneva and the United Nations Environment Programme/GRID-Geneva, together with the University of Zurich and the Federal Institute for Forest, Snow and Landscape Research – WSL.
- [EnviDat](https://www.envidat.ch/) - Environmental research data from Switzerland, provided by research units of the Swiss Federal Institute for Forest, Snow and Landscape WSL.

### Cantonal and city level

- [Kantonale Geoportale](https://www.kgk-cgc.ch/geodaten/kantonale_geoportale) - Overview of all cantonal geoportals.
- [Kanton Aargau](https://www.ag.ch/de/verwaltung/dfr/geoportal)
- [Kanton Appenzell Ausserrhoden](https://www.geoportal.ch/ktar)
- [Kanton Appenzell Innerrhoden](https://www.ai.ch/themen/planen-und-bauen/geodaten-und-plaene/geoportal)
- [Kanton Basel-Landschaft](https://www.baselland.ch/politik-und-behorden/direktionen/volkswirtschafts-und-gesundheitsdirektion/amt-fur-geoinformation/geoportal/geodaten)
- [Kanton Basel-Stadt](https://www.bs.ch/bvd/grundbuch-und-vermessungsamt/geo/geodaten)
- [Kanton Bern](https://www.agi.dij.be.ch/de/start.html)
- [Stadt Bern](https://map.bern.ch/geoportal/)
- [Kanton Freiburg](https://map.geo.fr.ch/)
- [Kanton Genf](https://map.sitg.ge.ch/app/)
- [Kanton Glarus](https://www.gl.ch/verwaltung/bau-und-umwelt/hochbau/raumentwicklung-und-geoinformation/geoportal-kanton-glarus.html/808)
- [Kanton Graubünden](https://geo.gr.ch/)
- [Kanton Jura](https://www.jura.ch/fr/Autorites/Administration/DEC/SDT/GeoPortail/GeoPortail-du-Canton-du-Jura.html)
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
- [OpenStreetMap CH](https://osm.ch/) - OpenStreetMap dataset limited to Switzerland and tools based on this reduced dataset (provided by [SOSM](https://sosm.ch/)). Hourly updated extracts are available [here](https://planet.osm.ch/).
- [BBBike's OSM download server](https://download.bbbike.org/osm/) - Data extracts from the OpenStreetMap project for more than 200 areas worldwide in various formats. E.g., extracts for [Zurich here](https://download.bbbike.org/osm/bbbike/Zuerich/).
- [Geofabrik's OSM download server](https://download.geofabrik.de/europe/switzerland.html) - Helpful OpenStreetMap data extracts for Switzerland (e.g., as ESRI shapefiles). Geofabrik's inspiring [portfolio of geodata projects](https://www.geofabrik.de/projects/) is definitely worth a look too.
- [Layercake](https://openstreetmap.us/our-work/layercake/) - Worldwide OSM-derived thematic layers in GeoParquet format.
- [Cadence Maps](https://cadencemaps.infs.ch/) - OSM-derived GeoParquet layers based on Geofabrik's GIS format, including POIs for Germany, Austria, and Switzerland.
- [Overture Maps](https://overturemaps.org/) - Open map data project combining OSM-derived layers with third-party "Places" POI data.

### Miscellaneous Geo Data

- [GeoHarvester](https://davidoesch.github.io/geoservice_harvester_poc/) - Portal that brings together official geodata from Swiss government entities. [[GitHub](https://github.com/davidoesch/geoservice_harvester_poc)]
- [geospatial-data-catalogs](https://github.com/giswqs/geospatial-data-catalogs) - A list of open geospatial datasets available on AWS, Earth Engine, Planetary Computer, NASA CMR, and STAC Index.
- [GeoBeer Switzerland](https://geobeer.ch/) - GeoBeerCH is an informal meeting of people interested in geography, GIS, cartography and the latest technologies.

## Linked Open Data

- [LINDAS ecosystem overview](https://lindas.admin.ch/ecosystem/) - LINDAS (Linked Data Service) allows public administrations to publish their data in the form of Knowledge Graphs and make them accessible via [lindas.admin.ch](https://lindas.admin.ch). The service is provided by the [Swiss Federal Archives](https://www.bar.admin.ch/bar/en/home.html).
- [Fedlex](https://fedlex.data.admin.ch/en-CH/home/intro) - Fedlex is the Federal Chancellery platform on which federal legislation is published. It is primarily used to publish the Official Federal Gazette, the Official Compilation of Federal Legislation, and the Classified Compilation of Federal Legislation, i.e., the consolidated version of federal legislation and international law texts.
- [Federal Geoportal Linked Data](https://geo.ld.admin.ch) - Linked Data Service of the Federal Geoportal.
- [Stadt Zürich LOD](https://www.stadt-zuerich.ch/de/politik-und-verwaltung/statistik-und-daten/linked-open-data.html)
- [Linked Data Meetup](https://www.bfh.ch/de/themen/linked-data/) - The Linked Data Meetup is a collaboration between the Swiss Federal Archives (BAR) and the BFH's Public Sector Transformation Institute. The meetup is aimed at users of linked data, especially in the LINDAS environment.

## APIs

- [opendata.swiss CKAN API](https://handbook.opendata.swiss/de/content/nutzen/api-nutzen.html) - Programmatic access to the national OGD metadata catalog.
- [Geo Admin](https://docs.geo.admin.ch/)
- [Geo Admin STAC](https://www.geo.admin.ch/de/geo-dienstleistungen/geodienste/downloadienste/stac-api.html) - API for Geo Admin's Spatial-Temporal Asset Catalog.
- [Federal Popular Votes API](https://opendata.swiss/en/dataset/echtzeitdaten-am-abstimmungstag-zu-eidgenoessischen-abstimmungsvorlagen) - Historical and continuously updated election-day JSON at municipal, district, cantonal, and federal levels.
- [SIMAP API](https://www.simap.ch/api-doc) - Public procurement publication data in JSON; the API terms permit commercial reuse.
- [Swiss Energy Dashboard API](https://energiedashboard.ch/api/swagger-ui/index.html) - Read-only REST API for energy time series, statistics, and metadata.
- [SFOE APIs](https://www.bfe.admin.ch/bfe/en/home/supply/digitalization-and-geoinformation/programming-interfaces.html) - Official overview of GeoAdmin, shared-mobility, STAC, charging-infrastructure, and OGD metadata interfaces.
- [Switzerland Tourism Open Data API](https://developer.myswitzerland.io/) - Mostly CC BY-SA 4.0 data with commercial reuse; requires a free API key and excludes linked images from the dataset licenses.
- [Overpass API (with Overpass QL)](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) - Overpass API for worldwide OpenStreetMap geospatial vector data with Overpass QL. Query example: "Italian restaurants in Switzerland" using instance [overpass-turbo.osm.ch](https://osm.li/Oqg).
- [Overpass API (with PostPASS SQL)](https://wiki.openstreetmap.org/wiki/Postpass) - Overpass API for worldwide OpenStreetMap geospatial vector data with PostGIS SQL. Query example: "Italian restaurants in Switzerland" using instance [overpass-turbo.eu](https://overpass-turbo.eu/s/2qpD).
- [CKAN API documentation](https://docs.ckan.org/en/latest/api/)
- [OpenERZ](https://github.com/metaodi/openerz) - OpenERZ is an open API for waste collection data from many different municipalities in Switzerland (e.g., Zurich, Basel, St. Gallen, Uster, Thalwil, Adliswil, and Horgen). API and Python client provided by OGD wizard [metaodi](https://github.com/metaodi), aka Stefan Oderbolz.
- [OpenPLZ API](https://www.openplzapi.org/en/) - OpenPLZ API is an open data project that makes a public street and postal code directory for Austria, Germany, Liechtenstein, and Switzerland available via an open REST API interface.
- [OpenHolidays API](https://www.openholidaysapi.org/en/) - Open Data project that collects public holiday and school holiday data and makes them available via an open REST API interface.

## Open-source Tools

- [Swiss federal OSS catalog](https://www.opensource.admin.ch/) - Official catalog of software published by federal and cantonal authorities, with repository and license information.
- [adminR Code Base](https://github.com/swiss-adminR/pkgs) - Curated list of R packages and reusable R code created by Swiss public institutions.
- [BFS](https://github.com/lgnbhl/BFS) - R package for searching and downloading data from Federal Statistical Office APIs.
- [I14Y](https://github.com/lgnbhl/I14Y) - R package for searching Switzerland's official interoperability metadata catalog.
- [swissparlpy](https://github.com/metaodi/swissparlpy) - Python client for the Swiss Parliament's open-data web services.

## Organizations, Initiatives, Events and Projects

- [Statistical Institutions in Switzerland](https://www.bfs.admin.ch/bfs/de/home/bfs/oeffentliche-statistik/system-oeffentliche-statistik/statistikinstitutionen-schweiz.html)
- [Korstat](https://confluence.swissdatacommunity.ch/plugins/viewsource/viewpagesrc.action?pageId=393257) - Conference of the regional statistical offices in Switzerland.
- [Statistiktage](https://www.statistiktage.ch/) - Annual conference organized by the [Swiss Statistical Society](https://www.stat.ch/en/) and [IMSD](https://www.imsd.ch/de/).
- [Project Rosling](https://www.projectrosling.ch) - Swiss Confederation's «Project Rosling» aims to expand dialogue on data and statistics and deepen knowledge.
- [opendata.ch](https://opendata.ch/de/) - Swiss section of the Open Knowledge Foundation.
- [opendata.ch](https://opendata.ch/events/) - List of hackathons and events.
- [GovTech Hackathons](https://digital.swiss/en/action-plan/measures/govtech-hackathon)
- [Open Data Beer](https://opendatabeer.ch/)
- [öffentlichkeitsgesetz.ch](https://www.oeffentlichkeitsgesetz.ch/deutsch/) - Forum for transparency in administration.
- [Parldigi](https://www.parldigi.ch/de/) - Parlamentarische Gruppe Digitale Nachhaltigkeit.
- [DINACON](https://dinacon.ch/) - Conference for digital sustainability.
- [Lobbywatch](https://lobbywatch.ch/lobbydatenbank/) - Lobbywatch enables citizens and media professionals to find out what interests politicians in Bern represent. They offer their data as an open database for independent evaluations.

## Newsletters

- [Bundesamt für Statistik](https://scnem.com/a.php?sid=ffnuk.16937bf,f=999)
- [Open Data CH](https://opendata.us7.list-manage.com/subscribe?u=c01c0e110415680950f8958e4&id=12200d2993)

## Podcasts

- [Statistisch gesehen](https://feeds.captivate.fm/statistisch-gesehen/) - Podcast of the Statistical Office Kanton Zürich.

## Miscellaneous

- [Swiss OGD information](https://www.bfs.admin.ch/bfs/en/home/services/ogd.html)
- [Swiss OGD Master Plan 2024–2027](https://www.bk.admin.ch/bk/en/home/digitale-transformation-ikt-lenkung/vorgaben/sn004-open_government_data_strategie_schweiz.html) - Current federal open-by-default policy, objectives, and implementation measures.
- [Geschäftsstelle OGD BFS](https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd/geschaeftsstelle.html) - This unit coordinates measures to implement the OGD strategy of the Swiss government and provides support to both data publishers and users.
- [Digitale Verwaltung Schweiz](https://www.digitale-verwaltung-schweiz.ch/)
- [National data management NaDB](https://www.bfs.admin.ch/bfs/en/home/nadb/nadb.html) - The I14Y interoperability platform is available since June 2021 to promote the multiple use of data. All of the Federal Administration’s data collections are described here. In addition, a directory of electronic interfaces (APIs) will facilitate access to the actual data.
- [Swiss DCAT Standard](https://www.ech.ch/de/ech/ech-0200/1.0) - eCH-0200 DCAT profile for Swiss data portals.
- [Forschungsstelle Digitale Nachhaltigkeit Uni Bern](https://www.digitale-nachhaltigkeit.unibe.ch/) - The Research Center for Digital Sustainability focuses on key topics such as Digital Sustainability, Open Data, Linked Data, and Open Government. The center offers studies, research, services, support, and lectures (see below) in these areas.
- [Open Data lectures Uni Bern](https://www.digitale-nachhaltigkeit.unibe.ch/studium/open_data_veranstaltung/index_ger.html) - Comprehensive lectures about Open Data in Switzerland provided by the Forschungsstelle Digitale Nachhaltigkeit at the University of Bern.
- [Swiss OSS Benchmark](https://ossbenchmark.com/institutions) - Comprehensive list of open source GitHub repositories and organizations of Swiss institutions.

## Media

Swiss data journalism teams.

- [Neue Zürcher Zeitung Visuals Team](https://github.com/nzzdev/st-methods) - Repository containing methods and code used for stories by [NZZ Visuals](https://twitter.com/nzzvisuals).
- [SRF Data](https://srfdata.github.io/) - Code and data from SRF Data, the data-driven journalism unit of Swiss Radio and TV (SRF) [[Publications and projects]](https://www.srf.ch/news/srf-data).
- [Tamedia Data Desk](https://github.com/tamedia-ddj) - GitHub account of Tamedia's data journalism team [[Projects of Ressort «Daten & Interaktiv»]](https://interaktiv.tagesanzeiger.ch/).

## International

International sources retained here are limited to cross-border datasets, neighboring jurisdictions, and resources that are directly useful for Swiss comparisons.

### Data portals and sources

- [European Union](https://data.europa.eu/en) - Official data portal of the European Commission.
- [Eurostat](https://ec.europa.eu/eurostat/web/main/data) - Data portal of the Statistical Office of the European Union [[Database]](https://ec.europa.eu/eurostat/web/main/data/database) [[Geo Data]](https://ec.europa.eu/eurostat/web/gisco/overview) [[Statistical Atlas]](https://ec.europa.eu/statistical-atlas/viewer/?config=RYB-2022.json) [[Choropleth Map Generator]](https://gisco-services.ec.europa.eu/image/screen/home) [[Experimental Statistics]](https://ec.europa.eu/eurostat/web/experimental-statistics).
- [Liechtenstein Statistics](https://www.statistikportal.li/) - Official statistics from Switzerland's closest associated neighboring state.
- [Global Biodiversity Information Facility](https://www.gbif.org)

### Curated lists

- OKFN Data Portals [[Website](https://dataportals.org/)] [[GitHub repo](https://github.com/okfn/dataportals.org)] - Very large, comprehensive list of data sources maintained by the [Open Knowledge Foundation](https://okfn.org/).
- [Awesome Public Datasets](https://github.com/awesomedata/awesome-public-datasets#government) - GitHub list with many more links to public government datasets.
- [Awesome Transit](https://github.com/CUTR-at-USF/awesome-transit) - Community list of transit APIs, apps, datasets, research, and software.

### Miscellaneous

- [Open Data Handbook](https://opendatahandbook.org/) - Guides, case studies, and resources for government and civil society on the _«what, why & how»_ of open data. Provided by the [Open Knowledge Foundation](https://okfn.org/).
- [United Nations](https://data.un.org/) - Data portal of the UN.
- [OECD](https://www.oecd.org/en/data.html) - OECD data portal.
- [Worldbank](https://data.worldbank.org/country/CH) - Data about Switzerland.
- [Our World in Data](https://ourworldindata.org/search?q=switzerland) - Data about Switzerland.
- [Open Data Watch](https://odin.opendatawatch.com/Report/) - Open data rankings and much more.

## Contribute

Contributions are welcome through issues and pull requests. A proposed resource should:

- focus on Switzerland or provide clear value for Swiss comparisons;
- identify its publisher, primary access URL, and, for data or tools, license or reuse terms;
- permit free use, modification, and redistribution, including commercial reuse, when it provides data;
- provide machine-readable data or, when it is a tool, source code under an OSI-approved license;
- be maintained by an official institution, established non-profit, research organization, or transparent community project; and
- avoid duplicating a more direct or authoritative entry already on the list.

Catalogs containing restricted records must say so explicitly. Free-to-view services, non-commercial-only APIs, proprietary applications without reusable data, and resources with unclear licensing are out of scope.
