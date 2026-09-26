# Awesome Open Government Data Switzerland

[![GitHub Stars](https://img.shields.io/github/stars/rnckp/awesome-ogd-switzerland.svg)](https://github.com/rnckp/awesome-ogd-switzerland)
[![GitHub Issues](https://img.shields.io/github/issues/rnckp/awesome-ogd-switzerland.svg)](https://github.com/rnckp/awesome-ogd-switzerland/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/rnckp/awesome-ogd-switzerland.svg)](https://github.com/rnckp/awesome-ogd-switzerland/pulls)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated directory of Swiss Open Government Data (OGD), complemented by Swiss research, community and privately published open data, tools and learning resources. A small selection of European sources supports comparisons with Switzerland.

OGD is data published by public authorities. General open data can come from any publisher: inclusion depends on relevance, provenance and reuse rights, not the publisher’s legal form. Non-government sources are identified in their descriptions or grouped under research and community headings.

<details>
<summary><strong>Table of Contents</strong></summary>

- [Start here](#start-here)
- [Data sources](#data-sources): [National catalogs and thematic sources](#national-catalogs-and-thematic-sources), [Cantonal portals](#cantonal-portals), [Municipal portals](#municipal-portals)
- [Geospatial data](#geospatial-data)
- [APIs and linked data](#apis-and-linked-data)
- [Tools and libraries](#tools-and-libraries)
- [Guides, standards and policy](#guides-standards-and-policy)
- [Community and publications](#community-and-publications)
- [European comparisons](#european-comparisons)
- [Curation and contributions](#curation-and-contributions)

</details>

## Start here

For a broad dataset search, begin with [opendata.swiss](https://opendata.swiss/de). For official statistics, use the [BFS data overview](https://data.bfs.admin.ch/). For maps and spatial data, see [Geospatial data](#geospatial-data). For programmatic access, follow API links beside each source or use the [selected interfaces](#selected-interfaces).

The primary link names the resource’s landing page unless the description identifies a direct download, API reference or repository. **Catalog** means a discovery index, **viewer/dashboard** means browser-based exploration, **download** means data files, and **API** means programmatic access. A catalog or viewer does not by itself guarantee open access to its underlying data.

Coverage is selective. A missing canton, municipality or topic does not imply that no open data exists. Check each dataset’s license, formats and access requirements before reuse.

## Data sources

Federal and regional OGD alongside complementary Swiss open data. “National” groups catalogs and thematic sources relevant to Switzerland; it does not imply that every publisher is a federal authority or every dataset covers the whole country.

### National catalogs and thematic sources

#### Catalogs and official statistics

- [opendata.swiss](https://opendata.swiss/de) — National OGD metadata catalog operated by the Federal Statistical Office (BFS/FSO). Find datasets from federal, cantonal and municipal publishers; follow each record to its downloads or services. [Catalog API](https://handbook.opendata.swiss/de/content/nutzen/api-nutzen.html).
- [BFS Data Portal](https://data.bfs.admin.ch/) — Overview of BFS datasets by statistical topic and access type. Use it to find spreadsheet tables, machine-readable files and API-accessible data.
- [BFS Swiss Stats Explorer](https://stats.swiss/) — Interactive explorer for BFS statistics, succeeding STAT-TAB. Use it to browse statistical data and select the dimensions needed for an analysis.
- [BFS STAT-TAB](https://www.pxweb.bfs.admin.ch/pxweb/en/) — Interactive BFS tables built from selectable data cubes, with exports in several formats. Some cubes are moving to [Swiss Stats Explorer](https://stats.swiss/); check there if a table is missing.
- [I14Y metadata catalog](https://www.i14y.admin.ch/en/home) — Metadata catalog describing Swiss data collections and interfaces. Use it to discover what exists and who is responsible; a catalog record does not mean the underlying data is open or downloadable.
- [BFS Registers](https://www.bfs.admin.ch/bfs/en/home/registers.html) — BFS overview of enterprise, population, and building and dwelling registers. Documentation and access routes vary by register; inclusion here does not imply access to individual administrative records.
- [Swiss official commune register](https://www.bfs.admin.ch/bfs/en/home/basics/swiss-official-commune-register.html) — BFS reference list of commune names, numbers and historical changes. Access: register information and [lookup application](https://www.agvchapp.bfs.admin.ch/de/home).

#### Administrative data, procurement and official notices

- [SIMAP](https://www.simap.ch/) — Official Swiss public procurement publications. Access: search portal and [JSON API documentation](https://www.simap.ch/api-doc).
- [Amtsblattportal](https://amtsblattportal.ch/#!/home) — Swiss Official Gazette of Commerce and cantonal gazette publications. Access: search portal and [REST API documentation](https://amtsblattportal.ch/docs/api/).
- [Zentraler Firmenindex ZEFIX](https://www.zefix.admin.ch/de/search/entity/welcome) — Central index of Swiss registered companies. Access: search and [REST API documentation](https://www.zefix.admin.ch/ZefixPublicREST/swagger-ui/index.html).
- [Eidgenössisches Institut für Geistiges Eigentum IGE](https://www.ige.ch/de/uebersicht-dienstleistungen/digitales-angebot) — Federal Institute of Intellectual Property digital services. Access: service directory; verify the access and reuse terms of the selected service.
- [TERMDAT](https://www.bk.admin.ch/bk/de/home/dokumentation/sprachen/termdat.html) — Federal Administration terminology database. Access: [term search](https://www.termdat.ch/search). For EU terminology, see IATE under [European comparisons](#european-comparisons).

#### Politics, elections and votes

- [Schweizer Parlament](https://www.parlament.ch/de/%C3%BCber-das-parlament/fakten-und-zahlen/open-data-web-services) — Swiss Parliament open-data services. Access: official web-service documentation.
- [OpenParlData.ch](https://openparldata.ch/) — Community project harmonizing parliamentary proceedings, actors, votes and related records across Swiss levels of government. Access: [API documentation](https://api.openparldata.ch/documentation) and [coverage directory](https://admin.openparldata.ch/#/bodies).
- [Swissvotes](https://swissvotes.ch/page/dataset) — Research dataset on Swiss federal popular votes since 1848. Access: CSV/XLSX downloads and a codebook under CC BY 4.0.
- [Federal Popular Votes Dashboard](https://abstimmungen.admin.ch/en/overview) — Official federal popular-vote results, including historical and voting-day data. Access: dashboard and [JSON dataset/API information](https://opendata.swiss/en/dataset/echtzeitdaten-am-abstimmungstag-zu-eidgenoessischen-abstimmungsvorlagen).
- [Lobbywatch](https://lobbywatch.ch/lobbydatenbank/) — Non-profit project documenting interests represented in the Swiss Parliament. Access: lobbying database and information on data reuse.

#### Legal data

- [Fedlex – Publikationsplattform des Bundesrechts](https://www.fedlex.admin.ch/de/home) — Federal legislation and official legal publications. Access: reading/search portal and [linked-data documentation](https://fedlex.data.admin.ch/en-CH/home/intro).
- [LexFind](https://www.lexfind.ch/) — Federal and cantonal legislation index. Access: unified search linking to law collections.
- [opencaselaw.ch](https://opencaselaw.ch/) — Independent project providing Swiss case-law data and access to federal and cantonal legislation. Access: project portal.
- [entscheidsuche.ch](https://entscheidsuche.ch/) — Community search portal for published Swiss court decisions. Access: search and [scraper repositories](https://github.com/entscheidsuche).
- [Onlinekommentar.ch](https://onlinekommentar.ch/) — Non-profit platform for open-access legal commentaries. Access: articles and [API documentation](https://onlinekommentar.ch/en/apis).
- [Center for Legal Data Science (UZH)](https://www.clds.uzh.ch/en/knowledge/databases.html) — University of Zürich legal research and dataset directory. Access: source links.

#### Finance, economy and employment

- [Swiss Federal Finance Administration FFA](https://www.efv.admin.ch/efv/en/home/finanzberichterstattung/daten/datencenter.html) — Federal Finance Administration budget and financial reporting data. Access: [data dashboard](https://www.data.finance.admin.ch/superset/dashboard/startseite/).
- [Schweizerische Nationalbank SNB](https://data.snb.ch/de) — Swiss National Bank statistics. Access: data portal.
- [arbeit.swiss](https://www.amstat.ch/v2/amstat_de.html) — SECO labor-market statistics. Access: AMSTAT data portal.
- [Eidgenössische Steuerverwaltung](https://www.estv.admin.ch/estv/de/home/die-estv/steuerstatistiken-estv.html) — Federal Tax Administration tax statistics. Access: statistical tables and publications.
- [KOF Data Service](https://data.kof.ethz.ch/) — ETH Zürich KOF economic time series and metadata. Access: API guide for CSV, XLSX and JSON downloads; the service includes restricted series, so select public indicators and verify their reuse terms.
- [Historical Statistics of Switzerland](https://hsso.ch/en) — Historical Swiss statistics compiled by a research project. Access: topic-based tables.

#### Health and social insurance

- [Bundesamt für Gesundheit BAG](https://www.bag.admin.ch/de/zahlen-statistiken) — Federal Office of Public Health statistics directory. Use the topic pages to find reports, tables and related dashboards.
- [Dashboard health insurance OKP](https://opendata.swiss/en/dataset/dashboard-krankenversicherung-okp) — BAG indicators on compulsory health insurance in Switzerland. Access: dataset record with quarterly downloads.
- [Key data on Swiss hospitals](https://opendata.swiss/de/dataset/kennzahlen-der-schweizer-spitaler-2024) — BAG hospital indicators for 2024 and a historical series starting in 2008. Access: downloadable spreadsheets and documentation.
- [Versorgungsatlas](https://www.versorgungsatlas.ch/) — Health-care indicators from BAG and the [Swiss Health Observatory](https://www.obsan.admin.ch/en). Access: interactive atlas.
- [Infectious Diseases Dashboard (IDD)](https://idd.bag.admin.ch/) — Federal Office of Public Health dashboard on reported infectious diseases in Switzerland and Liechtenstein. Access: interactive charts and supporting information.
- [Swissmedic Open Government Data](https://www.swissmedic.ch/swissmedic/en/home/services/listen_neu.html) — Swissmedic data on authorized medicines and registered medical-device operators. Access: machine-readable lists.
- [Bundesamt für Sozialversicherungen BSV](https://www.bsv.admin.ch/de/statistik) — Federal Social Security Office statistics on social insurance. Access: topic pages and statistical publications.
- [Unfallversicherung UVG](https://www.unfallstatistik.ch/index.htm) — Swiss accident-insurance statistics. Access: statistical tables and publications.
- [Sucht Schweiz](https://www.suchtschweiz.ch/zahlen-und-fakten/) — Addiction statistics from the non-profit Addiction Switzerland. Access: indicators and publications; verify reuse terms for the selected material.

#### Population, migration and religion

- [Staatssekretariat für Migration SEM](https://www.sem.admin.ch/sem/de/home/publiservice/statistik.html) — State Secretariat for Migration statistics. Access: topic pages and statistical publications.
- [Christian Catholic Church Switzerland](https://christkatholisch.ch/angebote/opendata/) — Data published by the Christian Catholic Church of Switzerland, a non-government source. Access: open-data directory.

#### Agriculture and food

- [Agrarmarktdaten](https://www.agrarmarktdaten.ch/) — Federal Office for Agriculture price and quantity data across agricultural and food markets. Access: data portal.
- [Agrarbericht](https://www.blw.admin.ch/blw/de/home/agrarbericht.html) — Federal Office for Agriculture reporting on Swiss agriculture. Access: report and supporting data.
- [Schweizer Nährwertdatenbank](https://naehrwertdaten.ch/de/) — Federal Food Safety and Veterinary Office data on the composition of foods available in Switzerland. Access: searchable database.
- [Agristat](https://www.sbv-usp.ch/de/services/agristat-statistik-der-schweizer-landwirtschaft) — Agricultural statistics from the Swiss Farmers’ Union, a non-government publisher. Access: statistics and publications; verify reuse terms for individual products.
- [Identitas Tierstatistik](https://tierstatistik.identitas.ch/en/index.html) — Livestock and companion-animal statistics from Identitas. Access: statistics portal.

#### Energy

- [Bundesamt für Energie BFE](https://www.bfe.admin.ch/de/energiestatistik) — Federal Office of Energy statistics and geodata. Access: topic directory and [API overview](https://www.bfe.admin.ch/de/api).
- [Swiss Energy Dashboard](https://energiedashboard.admin.ch/bfe-url) — Federal Office of Energy electricity, gas, price and supply indicators. Access: dashboard and [read-only REST API](https://energiedashboard.ch/api/swagger-ui/index.html).
- [Swissgrid](https://www.swissgrid.ch/de/home/customers/topics/energy-data-ch.html) — Swiss transmission-grid operator energy data. Access: data page.
- [Open Energy Data CH](https://github.com/OpenEnergyData/energy-data-ch) — Community-maintained directory of open Swiss energy datasets. Access: source links in a GitHub repository.

#### Buildings, housing and land

- [Federal Register of Buildings and Dwellings (GWR/RegBL)](https://www.bfs.admin.ch/bfs/de/home/register/gebaeude-wohnungsregister.html) — BFS building and dwelling register, including reference identifiers EGID and EWID. Access: register documentation and [housing-stat.ch](https://www.housing-stat.ch); public data and administrative access have different scopes.
- [Bundesamt für Wohnungswesen BWO – Wohnungsmarkt](https://www.bwo.admin.ch/de/wohnungsmarkt) — Federal Housing Office housing-market indicators. Access: [market overview](https://www.bwo.admin.ch/de/wohnungsmarkt-auf-einen-blick) and [housing statistics](https://www.bwo.admin.ch/de/zahlen-und-fakten-wohnen).
- [BFS Bau- und Wohnungswesen](https://www.bfs.admin.ch/bfs/de/home/statistiken/bau-wohnungswesen.html) — BFS construction and housing statistics, including activity, vacancies and housing stock. Access: topic pages and statistical tables.
- [Schweizerischer Baupreisindex (BAP)](https://www.bfs.admin.ch/bfs/de/home/statistiken/preise/baupreise.html) — BFS construction price index for building construction and civil engineering. Access: statistical tables and methodology.
- [Wohnimmobilienpreisindex (IMPI)](https://www.bfs.admin.ch/bfs/de/home/statistiken/preise/erhebungen/impi.html) — BFS quarterly residential property price index for owner-occupied homes. Access: statistical tables and methodology.
- [Mietpreisindex (MPI)](https://www.bfs.admin.ch/bfs/de/home/statistiken/preise/erhebungen/mpi.html) — BFS rental price index for permanently rented dwellings. Access: statistical tables and methodology.
- [ARE – Daten und Analysen](https://www.are.admin.ch/de/daten) — Federal Office for Spatial Development spatial monitoring, building-zone and settlement data. Access: data directory and mapping resources.
- [ÖREB-Kataster](https://www.cadastre.ch/de/oereb-kataster) — Cadastre of public-law restrictions on landownership. Access: information on obtaining parcel-level extracts; consult the relevant canton for data services.
- [Daten der amtlichen Vermessung (cadastre.ch)](https://www.cadastre.ch/de/daten-der-av) — Official cadastral survey data coordinated by swisstopo. Access: information on parcel geometry and data supply; see [geodienste.ch](https://geodienste.ch/) for aggregated cantonal services.
- [Swiss Dwellings](https://zenodo.org/records/7788422) — Apartment geometry and derived building-analysis data published by Archilyse, a private company. Access: versioned dataset download on Zenodo; see the record for its license.

#### Environment, climate and biodiversity

- [Bundesamt für Umwelt BAFU](https://www.bafu.admin.ch/bafu/de/home/zustand.html) — Federal Office for the Environment indicators and environmental reporting. Access: topic directory.
- [Bundesamt für Meteorologie und Klimatologie MeteoSchweiz](https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html) — Federal weather and climate observations and products. Access: MeteoSwiss open-data service information.
- [SLF data service](https://www.slf.ch/en/services-and-products/slf-data-service/) — WSL Institute for Snow and Avalanche Research observations used in avalanche warnings. Access: data-service information.
- [«Hydrodaten» Bundesamt für Umwelt BAFU](https://www.hydrodaten.admin.ch/de/aktuelle-lage) — Federal Office for the Environment hydrological observations and forecasts. Access: dashboard and [LINDAS dataset metadata](https://environment.ld.admin.ch/.well-known/void/dataset/hydro).
- [GLAMOS DOI products](https://doi.glamos.ch/) — Swiss glacier inventories and change measurements from the GLAMOS monitoring program. Access: versioned downloads with persistent identifiers and CC BY 4.0 licenses.
- [Swiss National Fauna Databank](https://ipt.gbif.ch/resource?r=ifn) — InfoSpecies species-occurrence records for Switzerland. Access: Darwin Core download under CC BY 4.0.
- [Jagdstatistik](https://www.jagdstatistik.ch/de/home) — Federal Office for the Environment hunting and wildlife statistics. Access: statistics portal.

#### Tourism

- [Swiss Tourism Data](https://www.tourismdata.ch/) — Tourism data-source metadata catalog from the National Data Infrastructure for Tourism project. Access: source discovery; access and reuse conditions depend on the linked provider.
- [Zürich Tourismus](https://www.zuerich.com/de/business/ueber-zuerich-tourismus/open-data-portal) — Tourism organization data for Zürich. Access: open-data portal information.
- [Switzerland Tourism Open Data API](https://developer.myswitzerland.io/) — Swiss tourism data from Switzerland Tourism. Access: API with a free key; most data is CC BY-SA 4.0, but linked images are excluded from dataset licenses.

#### Transport

- [SBB Open Data](https://data.sbb.ch/pages/home/) — Swiss Federal Railways datasets. Access: data portal.
- [Open Data Platform Mobility Switzerland](https://opentransportdata.swiss/en/) — Swiss public-transport and road-traffic data, including FEDRO counters and alerts. Access: datasets and service documentation.
- [FEDRO open vehicle data](https://www.astra.admin.ch/en/vehicle-data) — Federal vehicle inventories, registrations and vehicle-type data. Access: anonymized standard dataset downloads.
- [Geneva Public Transport](https://opendata.tpg.ch/pages/accueil/) — Geneva public-transport operator data. Access: data portal.

#### Research repositories

Research data from Swiss institutions and collaborations. These are complementary to OGD; repository records can have different licenses or access restrictions.

- [FORS SWISSUbase](https://www.swissubase.ch/de/) — Cross-disciplinary repository for Swiss research. Access: dataset records; access conditions and licenses vary by record.
- [Schweizerischer Nationalfonds SNF](https://data.snf.ch/datasets) — Swiss National Science Foundation research-funding data. Access: datasets and [data-story repositories](https://github.com/snsf-data).
- [CERN](https://opendata.cern.ch/) — Particle-physics research data from CERN experiments. Access: open-data catalog and downloads.
- [DaSCH Service Platform](https://dasch.swiss/about-us/platform) — Humanities research-data repository. Access: records, Linked Data, IIIF and REST services; verify record-level access and reuse conditions.
- [Materials Cloud Archive](https://archive.materialscloud.org/about) — Computational-materials research repository. Access: versioned dataset records and downloads.

#### Cultural heritage and archives

Discovery resources for cultural and historical material. Open catalog metadata and reusable digitized content are different things: images, recordings and documents may have separate rights, and some collections include restricted records. Use item-level rights statements and access information; inclusion is not a blanket open license for the collection.

- [e-rara](https://www.e-rara.ch/) — Digitized Swiss printed works. Access: collection search and [OAI-PMH, IIIF, full-text and download interfaces](https://www.e-rara.ch/wiki/apiinfo). Check the rights statement for each digitized work.
- [Memoriav Memobase](https://memobase.ch/de/start) — Swiss audiovisual heritage discovery portal. Access: catalog records and linked media; recording and image rights vary by item.
- [DODIS](https://dodis.ch/search) — Swiss diplomatic-history research database. Access: document search; consult item-level rights before reusing document images.
- [Schweizer Landesmuseum](https://sammlung.nationalmuseum.ch/de/maincategory) — Swiss National Museum collection catalog. Access: object search; catalog descriptions and object photographs may have different reuse conditions.
- [Swiss Federal Archives](https://www.recherche.bar.admin.ch/recherche/) — Federal archival discovery catalog for Swiss history. Access: finding aids and available digital documents; some records require an order or access permission.
- [Schweizerisches Idiotikon](https://idiotikon.ch/projekte) — Research resources documenting Swiss German dialects. Access: dictionaries and project resources; consult the terms of each resource.
- [Ortsnamen.ch](https://www.ortsnamen.ch/de/) — Research catalog of Swiss place names. Access: [map search](https://search.ortsnamen.ch/de) and [REST API documentation](https://search.ortsnamen.ch/static/api/swagger/index.html).

### Cantonal portals

Selected cantonal catalogs and statistics portals. General data portals and statistical-office sites may provide different coverage; geodata portals are listed separately below.

- [Aargau](https://www.ag.ch/de/themen/datenportal#/) — Cantonal open-data catalog. Access: dataset search.
- [Basel-Stadt](https://data.bs.ch/explore/) — Cantonal open-data catalog. Access: dataset search.
- [Basel-Landschaft](https://data.bl.ch/explore/) — Cantonal open-data catalog. Access: dataset search.
- [Basel-Landschaft Statistical Office](https://www.baselland.ch/politik-und-behorden/direktionen/finanz-und-kirchendirektion/daten-statistik) — Cantonal official statistics. Access: statistical portal and publications.
- [Bern](https://www.fin.be.ch/de/start/themen/OeffentlicheStatistik/statistikportal.html) — Cantonal official statistics. Access: statistical portal and publications.
- [Fribourg / Freiburg](https://opendata.fr.ch/pages/home/) — Cantonal open-data catalog. Access: dataset search.
- [Fribourg / Freiburg Statistical Office](https://www.fr.ch/de/vwbd/stata) — Cantonal official statistics. Access: statistical portal and publications.
- [Geneva](https://sitg.ge.ch/search?category=data) — Geneva geodata catalog (SITG). Access: dataset search; the [cantonal statistics portal](https://statistique.ge.ch/) covers statistical topics.
- [Glarus](https://opendata.swiss/en/organization/kanton-glarus) — Cantonal and Landsgemeinde datasets. Access: opendata.swiss publisher catalog with tabular and geospatial resources.
- [Graubünden](https://www.gr.ch/DE/institutionen/verwaltung/dvs/awt/statistik/Seiten/home.aspx) — Cantonal official statistics. Access: statistical portal and publications.
- [Jura](https://stat.jura.ch/) — Cantonal official statistics. Access: statistical portal and publications.
- [Luzern](https://www.lustat.ch) — Cantonal official statistics. Access: statistical portal and publications.
- [Neuchâtel](https://www.ne.ch/autorites/DFS/STAT/Pages/accueil.aspx) — Cantonal official statistics. Access: statistical portal and publications.
- [Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Wirtschaft--Statistik-und-Tourismus-3874-DE.html) — Cantonal official statistics. Access: statistical portal and publications.
- [Schwyz](https://data.sz.ch/explore/) — Cantonal open-data catalog. Access: dataset search.
- [Solothurn](https://so.ch/verwaltung/finanzdepartement/amt-fuer-finanzen/statistikportal/) — Cantonal official statistics. Access: statistical portal and publications.
- [St. Gallen](https://daten.sg.ch/explore/) — Cantonal open-data catalog. Access: dataset search.
- [St. Gallen Statistical Office](https://stada2.sg.ch/) — Cantonal official statistics. Access: statistical portal and publications.
- [Ticino](https://www4.ti.ch/index.php?id=42382) — Cantonal official statistics. Access: statistical portal and publications.
- [Thurgau](https://data.tg.ch/explore) — Cantonal open-data catalog. Access: dataset search and [thematic atlases](https://themenatlas-tg.ch/#c=home).
- [Thurgau Statistical Office](https://statistik.tg.ch/) — Cantonal official statistics. Access: statistical portal and publications.
- [Uri](https://www.statistik-uri.ch/daten) — Cantonal official statistics. Access: statistical portal and publications.
- [Vaud](https://www.vd.ch/themes/etat-droit-finances/statistique) — Cantonal official statistics. Access: statistical portal and publications.
- [Valais](https://www.vs.ch/de/web/sstp/sstp) — Cantonal official statistics. Access: statistical portal and publications.
- [Zug](https://zg.ch/de/gesundheitsdirektion/fachstelle-fuer-daten-und-statistik/open-government-data) — Open data shared by the canton and city of Zug. Access: official OGD entry page.
- [Zürich](https://www.zh.ch/de/politik-staat/opendata.zhweb-noredirect.zhweb-cache.html#/) — Cantonal open-data catalog. Access: dataset search.
- [Zürcher Gemeinden in Zahlen](https://zgz.statistik.zh.ch/) — Municipal statistics published by the Canton of Zürich. Access: comparison portal.

### Municipal portals

Selected municipal catalogs and statistics portals. Check the linked canton for additional local data.

- [Bern](https://www.bern.ch/open-government-data-ogd/ogd-nach-themen) — Municipal open-data resources. Access: official OGD entry page.
- [Biel/Bienne](https://opendata.swiss/en/organization/biel-bienne) — Municipal datasets from Biel/Bienne. Access: opendata.swiss publisher catalog.
- [Lausanne](https://www.lausanne.ch/officiel/statistique.html) — Municipal official statistics. Access: statistical portal and tables.
- [Lugano](https://statistica.lugano.ch/site/dati-ogd/) — Municipal open-data resources. Access: official OGD entry page.
- [Luzern](https://www.lustat.ch/statistikportal-stadt-luzern) — Municipal official statistics. Access: statistical portal and tables.
- [St. Gallen](https://www.stadt.sg.ch/home/verwaltung-politik/stadt-zahlen/statistikdatenbanken.html) — Municipal official statistics. Access: statistical portal and tables.
- [Uster](https://www.uster.ch/opendata) — Municipal open-data resources. Access: official OGD entry page.
- [Winterthur](https://stadt.winterthur.ch/themen/arbeit-steuern-wirtschaft/daten-statistik) — Municipal statistics. Access: data pages and [source repositories](https://github.com/Stadt-Winterthur).
- [Zürich](https://data.stadt-zuerich.ch/) — Municipal data catalog. Access: datasets, [source repositories](https://github.com/opendatazurich) and [linked-data services](https://www.stadt-zuerich.ch/de/politik-und-verwaltung/statistik-und-daten/linked-open-data.html).

## Geospatial data

### Official sources and catalogs

Federal and shared regional discovery services. Metadata and maps can include layers whose download and reuse conditions differ.

- [swisstopo](https://www.swisstopo.admin.ch/de/geodata.html) — Federal Office of Topography geodata products. Access: product descriptions and download routes.
- [geo.admin.ch](https://www.geo.admin.ch/de/home.html) — Federal geodata services and map information. Access: portal, [service documentation](https://docs.geo.admin.ch/), [STAC download API information](https://www.geo.admin.ch/de/geo-dienstleistungen/geodienste/downloadienste/stac-api.html) and [linked data](https://geo.ld.admin.ch).
- [geo.admin.ch — Strassenverzeichnis](https://map.geo.admin.ch/#/map?lang=de&center=2660000,1190000&z=1&topic=ech&layers=ch.swisstopo.amtliches-strassenverzeichnis&bgLayer=ch.swisstopo.pixelkarte-farbe) — Official Swiss street-name directory. Access: map layer in the federal viewer.
- [geocat](https://www.geocat.ch) — Swiss geodata metadata catalog operated by swisstopo. Access: descriptions and links to data/services; access conditions vary by record.
- [geobasisdaten.ch](https://geobasisdaten.ch/) — Inventory of legally mandated Swiss geodata from the cantonal geoinformation conference (KGK/CGC). Access: dataset responsibilities and legal references; [background information](https://www.kgk-cgc.ch/geobasisdaten).
- [geodienste.ch](https://geodienste.ch/) — Intercantonal service aggregating basic geodata from cantons and municipalities. Access: geodata services and data-supply information.
- [Geoportal.ch](https://www.geoportal.ch/) — Regional geodata publication platform. Access: maps and services; coverage and reuse conditions vary by participating authority and layer.
- [BFS Plattform Statatlas](https://www.atlas.bfs.admin.ch/de/index.html) — BFS thematic statistical atlases. Use these for map-based exploration of regional indicators; consult the linked tables for underlying data.

### Research and environmental geodata

- [Datalakes](https://www.datalakes-eawag.ch/) — Eawag lake-measurement data. Access: interactive portal.
- [Alplakes](https://www.alplakes.eawag.ch/) — Eawag lake models and remote-sensing products. Access: interactive portal.
- [Swiss Data Cube](https://www.swissdatacube.org) — Earth-observation data infrastructure for Switzerland, operated by Swiss research institutions and UNEP/GRID-Geneva. Access: project portal and data resources.
- [EnviDat](https://www.envidat.ch/) — WSL environmental research-data repository. Access: dataset records; access conditions and licenses vary by record.

### Cantonal and municipal geoportals

Official map and catalog entry points. Consult each layer’s metadata for download services, license and registration requirements.

- [Cantonal geoportal directory](https://www.kgk-cgc.ch/geodaten/kantonale_geoportale) — KGK/CGC directory of cantonal geodata entry points. Access: links to official portals.
- [Canton of Aargau](https://www.ag.ch/de/verwaltung/dfr/geoportal) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Appenzell Ausserrhoden](https://www.geoportal.ch/ktar) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Appenzell Innerrhoden](https://www.ai.ch/themen/planen-und-bauen/geodaten-und-plaene/geoportal) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Basel-Landschaft](https://www.baselland.ch/politik-und-behorden/direktionen/volkswirtschafts-und-gesundheitsdirektion/amt-fur-geoinformation/geoportal/geodaten) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Basel-Stadt](https://www.bs.ch/bvd/grundbuch-und-vermessungsamt/geo/geodaten) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Bern](https://www.agi.dij.be.ch/de/start.html) — Official regional geodata. Access: map and catalog entry point.
- [City of Bern](https://map.bern.ch/geoportal/) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Fribourg / Freiburg](https://map.geo.fr.ch/) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Geneva](https://map.sitg.ge.ch/app/) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Glarus](https://www.gl.ch/verwaltung/bau-und-umwelt/hochbau/raumentwicklung-und-geoinformation/geoportal-kanton-glarus.html/808) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Graubünden](https://geo.gr.ch/) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Jura](https://www.jura.ch/fr/Autorites/Administration/DEC/SDT/GeoPortail/GeoPortail-du-Canton-du-Jura.html) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Luzern](https://geoportal.lu.ch/karten) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Neuchâtel](https://www.ne.ch/autorites/DDTE/SGRF/SITN/geoportail/Pages/accueil.aspx) — Official regional geodata. Access: map and catalog entry point.
- [Nidwalden and Obwalden](https://www.gis-daten.ch/geodaten/geodatenkatalog/) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-1262910-DE.html) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Schwyz](https://www.sz.ch/behoerden/verwaltung/umweltdepartement/amt-fuer-geoinformation/geoportal-webgis.html/8756-8758-8802-9447-9448-9462) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/geoportal/) — Official regional geodata. Access: map and catalog entry point.
- [Canton of St. Gallen](https://www.sg.ch/bauen/geoinformation/gi/geodaten.html) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Ticino](https://map.geo.ti.ch/) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Thurgau](https://map.geo.tg.ch) — Cantonal geodata. Access: map viewer and [geodata shop](https://shop.geo.tg.ch/) requiring registration.
- [Canton of Uri](https://www.ur.ch/geoinformationen) — Cantonal geodata information. Access: service overview and [map/download portal](https://geo.ur.ch).
- [Canton of Vaud](https://www.geo.vd.ch/) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Valais](https://www.vs.ch/de/web/egeo) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Zug](https://zg.ch/de/planen-bauen/geoinformation/geoinformationen-nutzen) — Official regional geodata. Access: map and catalog entry point.
- [Canton of Zürich](https://geo.zh.ch/data) — Official regional geodata. Access: map and catalog entry point.
- [City of Zürich](https://www.stadt-zuerich.ch/geodaten/) — Official regional geodata. Access: map and catalog entry point.

### Community and global geodata

Non-government open geodata with Swiss coverage. OSM-derived and other global products complement official Swiss sources.

- [OpenStreetMap CH](https://osm.ch/) — Community-maintained Swiss OpenStreetMap resources from SOSM. Access: tools and [data extracts](https://planet.osm.ch/); query data with [Overpass QL](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) or [Postpass SQL](https://wiki.openstreetmap.org/wiki/Postpass).
- [BBBike's OSM download server](https://download.bbbike.org/osm/) — OpenStreetMap extracts in several formats. Access: download directory, including [Zürich extracts](https://download.bbbike.org/osm/bbbike/Zuerich/).
- [Geofabrik's OSM download server](https://download.geofabrik.de/europe/switzerland.html) — OpenStreetMap extracts for Switzerland. Access: downloadable geospatial files, including shapefiles.
- [Layercake](https://openstreetmap.us/our-work/layercake/) — Worldwide OSM-derived thematic layers from OpenStreetMap US. Access: GeoParquet data resources.
- [Cadence Maps](https://cadencemaps.infs.ch/) — OSM-derived layers, including points of interest for Germany, Austria and Switzerland. Access: GeoParquet data resources.
- [Overture Maps](https://overturemaps.org/) — Global community map project combining OSM-derived layers and other sources. Access: data releases; check each layer’s license and attribution requirements.

### Geodata discovery tools

- [GeoHarvester](https://davidoesch.github.io/geoservice_harvester_poc/) — Community discovery portal for official Swiss geodata services. Access: service search and [source code](https://github.com/davidoesch/geoservice_harvester_poc).
- [geospatial-data-catalogs](https://github.com/giswqs/geospatial-data-catalogs) — Community directory of geospatial datasets across cloud and catalog services. Access: source links; check each dataset’s license and Swiss coverage.

## APIs and linked data

API links stay beside their source entries. This section highlights selected interfaces for common workflows; it is not a complete inventory of every API in the directory. Catalog APIs return metadata, while data APIs return records or observations.

### Selected interfaces

- [opendata.swiss CKAN API](https://handbook.opendata.swiss/de/content/nutzen/api-nutzen.html) — National OGD metadata catalog interface. Access: API guide; dataset records link onward to the actual data.
- [Geo Admin](https://docs.geo.admin.ch/) — Federal geodata service documentation. Access: interface guides linked from the GeoAdmin source entry.
- [Geo Admin STAC](https://www.geo.admin.ch/de/geo-dienstleistungen/geodienste/downloadienste/stac-api.html) — Federal Spatial Temporal Asset Catalog (STAC) interface for discovering and downloading geospatial assets. Access: API information.
- [Federal Popular Votes API](https://opendata.swiss/en/dataset/echtzeitdaten-am-abstimmungstag-zu-eidgenoessischen-abstimmungsvorlagen) — Official federal popular-vote results in JSON, with municipal, district, cantonal and national coverage. Access: dataset record and interface information.
- [SIMAP API](https://www.simap.ch/api-doc) — Swiss public procurement publications in JSON. Access: API documentation; the source portal is listed under administrative data.
- [Swiss Energy Dashboard API](https://energiedashboard.ch/api/swagger-ui/index.html) — Federal energy time series, statistics and metadata. Access: read-only REST API reference.
- [SFOE APIs](https://www.bfe.admin.ch/de/api) — Federal Office of Energy interface directory covering energy and mobility services. Access: documentation links.
- [Overpass API (with Overpass QL)](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) — Query OpenStreetMap data using Overpass QL. Access: API documentation and a [Swiss restaurant query example](https://osm.li/Oqg).
- [Postpass](https://wiki.openstreetmap.org/wiki/Postpass) — Query OpenStreetMap data using SQL over PostGIS. Access: Postpass documentation and a [restaurant query example](https://overpass-turbo.eu/s/2qpD).
- [OpenERZ](https://github.com/metaodi/openerz) — Community API for municipal waste-collection schedules in Switzerland. Access: API project and Python client source code.
- [OpenPLZ API](https://www.openplzapi.org/en/) — Community street and postal-code directory for Switzerland, Liechtenstein, Austria and Germany. Access: REST API documentation.
- [OpenHolidays API](https://www.openholidaysapi.org/en/) — Community public-holiday and school-holiday data. Access: REST API documentation and supported-country coverage.

### Linked data services

Services for accessing structured, linked datasets. Follow the service documentation for query endpoints, supported datasets and examples.

- [LINDAS ecosystem overview](https://lindas.admin.ch/ecosystem/) — Swiss Federal Archives service for publishing and querying linked datasets. Access: ecosystem guide and [service documentation](https://lindas.admin.ch).
- [Fedlex](https://fedlex.data.admin.ch/en-CH/home/intro) — Linked-data access to federal legislation and official legal publications. Access: data-service documentation; the [reading portal](https://www.fedlex.admin.ch/de/home) is listed under legal data.
- [Federal Geoportal Linked Data](https://geo.ld.admin.ch) — Linked-data interface to federal geodata. Access: service entry point.
- [City of Zürich LOD](https://www.stadt-zuerich.ch/de/politik-und-verwaltung/statistik-und-daten/linked-open-data.html) — City of Zürich linked open data. Access: service overview and documentation; see also the municipal data catalog.

## Tools and libraries

### Visualization and data clients

- [Visualize](https://visualize.admin.ch) — Web tool for creating and embedding charts from compatible LINDAS datasets. Access: browser application and [BSD-3-Clause source code](https://github.com/visualize-admin/visualization-tool).
- [BFS](https://github.com/lgnbhl/BFS) — Community R client for Federal Statistical Office APIs. Access: package source and documentation.
- [I14Y](https://github.com/lgnbhl/I14Y) — Community R client for the Swiss interoperability metadata catalog. Access: package source and documentation.
- [swissparlpy](https://github.com/metaodi/swissparlpy) — Community Python client for Swiss Parliament web services. Access: package source and documentation.

### Source-code directories

Indexes of software and repositories. Check the license of each project; a directory listing alone does not establish an open-source license.

- [Federal Open Source GitHub Index](https://github.com/swiss/index) — Directory of Swiss Confederation GitHub organizations. Access: repository index.
- [Swiss federal OSS catalog](https://www.opensource.admin.ch/) — Software published by federal and cantonal authorities. Access: catalog with repository and license information.
- [adminR Code Base](https://github.com/swiss-adminR/pkgs) — R packages and reusable code created by Swiss public institutions. Access: curated repository links.
- [Swiss OSS Benchmark](https://ossbenchmark.com/institutions) — Directory of source-code repositories and organizations from Swiss institutions. Access: searchable index.

## Guides, standards and policy

- [Swiss OGD information](https://www.bfs.admin.ch/bfs/en/home/services/ogd.html) — Federal guidance on Open Government Data. Access: policy and publishing information.
- [Swiss OGD Master Plan 2024–2027](https://www.bk.admin.ch/bk/en/home/digitale-transformation-ikt-lenkung/vorgaben/sn004-open_government_data_strategie_schweiz.html) — Federal open-by-default objectives and implementation measures for 2024–2027. Access: policy documents.
- [Geschäftsstelle OGD BFS](https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd/geschaeftsstelle.html) — Federal OGD coordination and support for publishers and users. Access: office information and guidance.
- [Digitale Verwaltung Schweiz](https://www.digitale-verwaltung-schweiz.ch/) — Digital Public Services Switzerland. Access: public-sector digital transformation programs and guidance.
- [National data management NaDB](https://www.bfs.admin.ch/bfs/en/home/nadb/nadb.html) — Federal program for reusing administrative data. Access: program information; discover collections and interfaces through I14Y in the data-source catalog section.
- [Swiss DCAT Standard](https://www.ech.ch/de/ech/ech-0200/1.0) — eCH-0200 metadata profile for Swiss data portals. Access: linked version 1.0 of the standard; check the publisher for subsequent versions.
- [Forschungsstelle Digitale Nachhaltigkeit Uni Bern](https://www.digitale-nachhaltigkeit.unibe.ch/) — University of Bern research on digital sustainability and open data. Access: research and teaching resources.
- [Open Data lectures Uni Bern](https://www.digitale-nachhaltigkeit.unibe.ch/studium/open_data_veranstaltung/index_ger.html) — University of Bern open-data teaching material. Access: course information and resources.
- [CKAN API documentation](https://docs.ckan.org/en/latest/api/) — Generic documentation for accessing CKAN catalogs, including opendata.swiss. Access: API reference.
- [Open Data Handbook](https://opendatahandbook.org/) — Open Knowledge Foundation introduction to open data, reuse and publishing. Access: online handbook.

## Community and publications

### Organizations and initiatives

- [Statistical Institutions in Switzerland](https://www.bfs.admin.ch/bfs/de/home/bfs/oeffentliche-statistik/system-oeffentliche-statistik/statistikinstitutionen-schweiz.html) — BFS directory of Swiss statistical institutions. Access: publisher directory.
- [Korstat](https://confluence.swissdatacommunity.ch/plugins/viewsource/viewpagesrc.action?pageId=393257) — Conference of regional statistical offices in Switzerland. Access: organization information.
- [Project Rosling](https://www.projectrosling.ch) — Federal initiative supporting dialogue and knowledge about data and statistics. Access: project information.
- [opendata.ch](https://opendata.ch/de/) — Swiss open-data association. Access: community information and [events](https://opendata.ch/events/).
- [öffentlichkeitsgesetz.ch](https://www.oeffentlichkeitsgesetz.ch/deutsch/) — Non-profit forum for transparency in public administration. Access: guidance and information on access to official documents.
- [Parldigi](https://www.parldigi.ch/de/) — Parliamentary group for digital sustainability. Access: activities and policy information.
- [Swiss OpenStreetMap Association (SOSM)](https://sosm.ch/) — Community association supporting open geodata in Switzerland. Access: projects and participation information.

### Events and meetups

- [Statistiktage](https://www.statistiktage.ch/) — Swiss statistics conference organized by the [Swiss Statistical Society](https://www.stat.ch/en/) and [IMSD](https://www.imsd.ch/de/). Access: event program.
- [GovTech Hackathons](https://digital.swiss/en/action-plan/measures/govtech-hackathon) — Federal GovTech hackathon initiative. Access: event and program information.
- [Open Data Beer](https://opendatabeer.ch/) — Swiss open-data community gatherings. Access: event information.
- [DINACON](https://dinacon.ch/) — Swiss conference on digital sustainability. Access: event information.
- [GeoBeer Switzerland](https://geobeer.ch/) — Swiss community meetings on geography, GIS and cartography. Access: event information.
- [Linked Data Meetup](https://www.bfh.ch/de/themen/linked-data/) — Meetup organized by the Swiss Federal Archives and BFH for users of linked data, including LINDAS. Access: event information.

### Newsletters

- [Bundesamt für Statistik](https://scnem.com/a.php?sid=ffnuk.16937bf,f=999) — Federal Statistical Office newsletter. Access: subscription page.
- [Open Data CH](https://opendata.us7.list-manage.com/subscribe?u=c01c0e110415680950f8958e4&id=12200d2993) — Opendata.ch newsletter. Access: subscription form.

### Podcasts

- [Statistisch gesehen](https://feeds.captivate.fm/statistisch-gesehen/) — Podcast from the Canton of Zürich’s Office for Statistics and Data. Access: RSS feed.

### Data journalism

Reusable code and data accompanying Swiss journalism. Access to linked articles and rights to article text or images are separate from repository and dataset licenses.

- [Neue Zürcher Zeitung Visuals Team](https://github.com/nzzdev/st-methods) — Methods and code accompanying NZZ Visuals journalism. Access: GitHub repository.
- [SRF Data](https://srfdata.github.io/) — Code and data accompanying SRF data journalism. Access: project site and [published stories](https://www.srf.ch/news/srf-data).
- [Tamedia Data Desk](https://github.com/tamedia-ddj) — Tamedia data-journalism repositories. Access: GitHub organization and [interactive stories](https://interaktiv.tagesanzeiger.ch/).

## European comparisons

Core European catalogs and official statistics from Switzerland’s neighboring countries. Use these for cross-border discovery and comparisons; check definitions, periods, territorial units and Swiss coverage before combining data.

### European catalogs and statistics

- [European Union](https://data.europa.eu/en) — European data catalog for cross-border source discovery. Access: dataset search; licenses and access conditions vary by record.
- [Eurostat](https://ec.europa.eu/eurostat/web/main/data) — European statistical data for comparisons involving Switzerland. Access: [database](https://ec.europa.eu/eurostat/web/main/data/database) and [GISCO geodata](https://ec.europa.eu/eurostat/web/gisco/overview); check Swiss coverage for each series.
- [List of European Statistical Offices](https://www.destatis.de/EN/Service/Address-Book/europe.html) — Destatis directory of European statistical offices. Access: source directory for comparisons beyond the neighboring countries listed below.
- [IATE](https://iate.europa.eu/home) — EU multilingual terminology database for interpreting European administrative concepts. Access: term search.

### Neighboring countries

- [Germany — GovData](https://www.govdata.de/) — German government open-data catalog. Access: dataset search; useful for neighboring-country comparisons.
- [Germany — Destatis GENESIS](https://www-genesis.destatis.de/genesis/online) — German Federal Statistical Office tables. Access: GENESIS database for statistical comparisons with Switzerland.
- [Austria — Statistics Austria](https://www.statistik.at/en) — Austrian official statistics. Access: statistical topics and tables for neighboring-country comparisons.
- [Austria — data.gv.at](https://www.data.gv.at/) — Austrian government open-data catalog. Access: dataset search.
- [France — INSEE](https://www.insee.fr/en/accueil) — French official statistics from INSEE. Access: statistical topics and tables for neighboring-country comparisons.
- [France — data.gouv.fr](https://www.data.gouv.fr/en/datasets/) — French government open-data catalog. Access: dataset search.
- [Italy — Istat](https://www.istat.it/en/) — Italian official statistics from Istat. Access: statistical topics and tables for neighboring-country comparisons.
- [Italy — dati.gov.it](https://www.dati.gov.it/) — Italian public-sector data catalog. Access: dataset search.
- [Liechtenstein — Statistics Portal](https://www.statistikportal.li/) — Liechtenstein official statistics. Access: topic-based tables for neighboring-country comparisons.

## Curation and contributions

### Curation policy

Data must permit free use, modification and redistribution, including commercial reuse, following the [Open Definition](https://opendefinition.org/). Software must provide source code under an [OSI-approved license](https://opensource.org/licenses). Free, non-discriminatory registration is acceptable; payment, case-by-case permission, non-commercial-only terms and unclear reuse rights do not qualify a dataset or tool for inclusion.

Evaluate publishers by identifiable provenance, relevance and documented reuse rights. Public authorities, research institutions, communities, individuals, non-profits and companies can all publish qualifying resources. Government publication alone does not establish openness.

Discovery catalogs and repositories may include restricted records if the entry clearly explains this limitation and helps users find reusable material. Their inclusion does not endorse every record. Guides, standards, communities and journalism resources must offer freely accessible material relevant to using or understanding open data; linked articles and cultural objects may carry separate rights.

### Contribute

Contributions are welcome through [issues](https://github.com/rnckp/awesome-ogd-switzerland/issues) and [pull requests](https://github.com/rnckp/awesome-ogd-switzerland/pulls). Please:

- Explain the resource’s relevance to Switzerland or to the core European comparison sources.
- Identify the publisher, geographic or thematic coverage, and primary access URL.
- For data, link to machine-readable files or an access interface and documented open reuse terms; for software, link to source code and its open-source license.
- Identify mixed-access catalogs, registration requirements and item-level rights where applicable.
- Use the pattern `Resource name — contents and coverage. Access: catalog, viewer, download, API or source code.` Keep descriptions to one or two sentences and use descriptive secondary link labels.
- Keep API links beside the source. Add an entry to selected interfaces only when it offers a useful additional navigation route.
- Prefer one canonical entry and concise cross-references over repeated descriptions. Avoid promotional claims and undated counts.

Free-to-view data services without reusable data, non-commercial-only datasets and proprietary applications without qualifying open data or source code are out of scope. Report suspected broken links separately from access blocks or temporary connection failures.
