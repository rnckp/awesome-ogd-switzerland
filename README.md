# Awesome Open Government Data Switzerland

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Suggestions welcome](https://img.shields.io/badge/suggestions-welcome-brightgreen)](https://github.com/rnckp/awesome-ogd-switzerland/issues/new)
[![License: CC0](https://img.shields.io/badge/license-CC0-blue)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/rnckp/awesome-ogd-switzerland.svg)](https://github.com/rnckp/awesome-ogd-switzerland)
[![Last commit](https://img.shields.io/github/last-commit/rnckp/awesome-ogd-switzerland)](https://github.com/rnckp/awesome-ogd-switzerland/commits/main/)

A curated directory of Swiss Open Government Data (OGD), research, community and privately published open data, tools and learning resources. Selected European sources support comparisons with Switzerland.

OGD comes from public authorities; open data can come from any publisher. Inclusion depends on relevance, provenance and reuse rights. Non-government sources are identified in descriptions or grouped under research and community headings.

Know a useful resource? [Share a link](https://github.com/rnckp/awesome-ogd-switzerland/issues/new)—suggestions and corrections are always welcome.

<details>
<summary><strong>Table of Contents</strong></summary>

<ul>
  <li><a href="#start-here">Start here</a></li>
  <li><a href="#data-sources">Data sources</a>
    <ul>
      <li><a href="#national-catalogs-and-thematic-sources">National catalogs and thematic sources</a></li>
      <li><a href="#cantonal-portals">Cantonal portals</a></li>
      <li><a href="#municipal-portals">Municipal portals</a></li>
    </ul>
  </li>
  <li><a href="#geospatial-data">Geospatial data</a></li>
  <li><a href="#apis-and-linked-data">APIs and linked data</a></li>
  <li><a href="#tools-and-libraries">Tools and libraries</a></li>
  <li><a href="#guides-standards-and-policy">Guides, standards and policy</a></li>
  <li><a href="#community-and-publications">Community and publications</a></li>
  <li><a href="#european-comparisons">European comparisons</a></li>
  <li><a href="#curation-and-contributions">Curation and contributions</a></li>
</ul>

</details>

## Start here

- **Find datasets:** Search [opendata.swiss](https://opendata.swiss/de).
- **Explore statistics:** Start with the [BFS data overview](https://data.bfs.admin.ch/).
- **Find maps and geodata:** Browse [Geospatial data](#geospatial-data).
- **Access APIs:** Follow API links beside each source or browse the [selected interfaces](#selected-interfaces).

Check each dataset’s license, formats and access requirements before reuse. The directory itself is published under [CC0](LICENSE); linked resources have their own terms.

**Browse by topic:** [Politics and votes](#politics-elections-and-votes) · [Legal data](#legal-data) · [Economy and employment](#finance-economy-and-employment) · [Health](#health-and-social-insurance) · [Population](#population-migration-and-religion) · [Agriculture](#agriculture-and-food) · [Energy](#energy) · [Housing and land](#buildings-housing-and-land) · [Environment and climate](#environment-climate-and-biodiversity) · [Tourism](#tourism) · [Transport](#transport) · [Research](#research-repositories) · [Culture and archives](#cultural-heritage-and-archives) · [Procurement and official notices](#administrative-data-procurement-and-official-notices).

## Data sources

Federal and regional OGD alongside other Swiss open data. “National” groups catalogs and thematic sources relevant to Switzerland, without implying federal publishers or nationwide coverage.

### National catalogs and thematic sources

#### Catalogs and official statistics

- [opendata.swiss](https://opendata.swiss/de) — National OGD metadata catalog operated by the Federal Statistical Office (BFS/FSO). Find datasets from federal, cantonal and municipal publishers; follow each record to its downloads or services. [Catalog API](https://handbook.opendata.swiss/de/content/nutzen/api-nutzen.html).
- [BFS Data Portal](https://data.bfs.admin.ch/) — Overview of BFS datasets by statistical topic and access type. Use it to find spreadsheet tables, machine-readable files and API-accessible data.
- [BFS Swiss Stats Explorer](https://stats.swiss/) — Interactive explorer for BFS statistics, succeeding STAT-TAB. Use it to browse statistical data and select the dimensions needed for an analysis.
- [BFS STAT-TAB](https://www.pxweb.bfs.admin.ch/pxweb/en/) — Interactive BFS tables built from selectable data cubes, with exports in several formats. Some cubes are moving to [Swiss Stats Explorer](https://stats.swiss/); check there if a table is missing.
- [I14Y metadata catalog](https://www.i14y.admin.ch/en/home) — Metadata catalog describing Swiss data collections and interfaces. Use it to discover what exists and who is responsible; a catalog record does not mean the underlying data is open or downloadable.
- [BFS Registers](https://www.bfs.admin.ch/bfs/en/home/registers.html) — BFS overview of enterprise, population, and building and dwelling registers. Documentation and access routes vary by register; inclusion here does not imply access to individual administrative records.
- [Swiss official commune register](https://www.bfs.admin.ch/bfs/en/home/basics/swiss-official-commune-register.html) — BFS reference list of commune names, numbers and historical changes. [Lookup application](https://www.agvchapp.bfs.admin.ch/de/home).

#### Administrative data, procurement and official notices

- [SIMAP](https://www.simap.ch/) — Official Swiss public procurement publications. [JSON API documentation](https://www.simap.ch/api-doc).
- [Amtsblattportal](https://amtsblattportal.ch/#!/home) — Swiss Official Gazette of Commerce and cantonal gazette publications. [REST API documentation](https://amtsblattportal.ch/docs/api/).
- [Zentraler Firmenindex ZEFIX](https://www.zefix.admin.ch/de/search/entity/welcome) — Central index of Swiss registered companies. [REST API documentation](https://www.zefix.admin.ch/ZefixPublicREST/swagger-ui/index.html).
- [Eidgenössisches Institut für Geistiges Eigentum IGE](https://www.ige.ch/de/uebersicht-dienstleistungen/digitales-angebot) — Federal Institute of Intellectual Property digital services. Verify the access and reuse terms of the selected service.
- [TERMDAT](https://www.bk.admin.ch/bk/de/home/dokumentation/sprachen/termdat.html) — Federal Administration terminology database. [Term search](https://www.termdat.ch/search) · [EU terminology (IATE)](#european-comparisons).

#### Politics, elections and votes

- [Schweizer Parlament](https://www.parlament.ch/de/%C3%BCber-das-parlament/fakten-und-zahlen/open-data-web-services) — Swiss Parliament open-data services.
- [OpenParlData.ch](https://openparldata.ch/) — Community project harmonizing parliamentary proceedings, actors, votes and related records across Swiss levels of government. [API documentation](https://api.openparldata.ch/documentation) · [Coverage directory](https://admin.openparldata.ch/#/bodies).
- [Swissvotes](https://swissvotes.ch/page/dataset) — Research dataset on Swiss federal popular votes since 1848, with CSV/XLSX downloads and a codebook under CC BY 4.0.
- [Federal Popular Votes Dashboard](https://abstimmungen.admin.ch/en/overview) — Official federal popular-vote results, including historical and voting-day data. [JSON dataset/API information](https://opendata.swiss/en/dataset/echtzeitdaten-am-abstimmungstag-zu-eidgenoessischen-abstimmungsvorlagen).
- [Lobbywatch](https://lobbywatch.ch/lobbydatenbank/) — Non-profit project documenting interests represented in the Swiss Parliament.

#### Legal data

- [Fedlex – Publikationsplattform des Bundesrechts](https://www.fedlex.admin.ch/de/home) — Federal legislation and official legal publications. [Linked-data documentation](https://fedlex.data.admin.ch/en-CH/home/intro).
- [LexFind](https://www.lexfind.ch/) — Federal and cantonal legislation index.
- [opencaselaw.ch](https://opencaselaw.ch/) — Independent project providing Swiss case-law data and access to federal and cantonal legislation.
- [entscheidsuche.ch](https://entscheidsuche.ch/) — Community search portal for published Swiss court decisions. [Scraper repositories](https://github.com/entscheidsuche).
- [Onlinekommentar.ch](https://onlinekommentar.ch/) — Non-profit platform for open-access legal commentaries. [API documentation](https://onlinekommentar.ch/en/apis).
- [Center for Legal Data Science (UZH)](https://www.clds.uzh.ch/en/knowledge/databases.html) — University of Zürich legal research and dataset directory.

#### Finance, economy and employment

- [Swiss Federal Finance Administration FFA](https://www.efv.admin.ch/efv/en/home/finanzberichterstattung/daten/datencenter.html) — Federal Finance Administration budget and financial reporting data. [Data dashboard](https://www.data.finance.admin.ch/superset/dashboard/startseite/).
- [Schweizerische Nationalbank SNB](https://data.snb.ch/de) — Swiss National Bank statistics.
- [arbeit.swiss](https://www.amstat.ch/v2/amstat_de.html) — SECO labor-market statistics.
- [Eidgenössische Steuerverwaltung](https://www.estv.admin.ch/estv/de/home/die-estv/steuerstatistiken-estv.html) — Federal Tax Administration tax statistics.
- [KOF Data Service](https://data.kof.ethz.ch/) — ETH Zürich KOF economic time series and metadata. API guide for CSV, XLSX and JSON downloads; includes restricted series, so select public indicators and verify reuse terms.
- [Historical Statistics of Switzerland](https://hsso.ch/en) — Historical Swiss statistics compiled by a research project.

#### Health and social insurance

- [Bundesamt für Gesundheit BAG](https://www.bag.admin.ch/de/zahlen-statistiken) — Federal Office of Public Health statistics directory. Use the topic pages to find reports, tables and related dashboards.
- [Dashboard health insurance OKP](https://opendata.swiss/en/dataset/dashboard-krankenversicherung-okp) — BAG indicators on compulsory health insurance in Switzerland, with quarterly downloads.
- [Key data on Swiss hospitals](https://opendata.swiss/de/dataset/kennzahlen-der-schweizer-spitaler-2024) — BAG hospital indicators for 2024 and a historical series starting in 2008, with downloadable spreadsheets and documentation.
- [Versorgungsatlas](https://www.versorgungsatlas.ch/) — Health-care indicators from BAG and the [Swiss Health Observatory](https://www.obsan.admin.ch/en).
- [Infectious Diseases Dashboard (IDD)](https://idd.bag.admin.ch/) — Federal Office of Public Health dashboard on reported infectious diseases in Switzerland and Liechtenstein.
- [Swissmedic Open Government Data](https://www.swissmedic.ch/swissmedic/en/home/services/listen_neu.html) — Machine-readable Swissmedic lists of authorized medicines and registered medical-device operators.
- [Bundesamt für Sozialversicherungen BSV](https://www.bsv.admin.ch/de/statistik) — Federal Social Security Office statistics on social insurance.
- [Unfallversicherung UVG](https://www.unfallstatistik.ch/index.htm) — Swiss accident-insurance statistics.
- [Sucht Schweiz](https://www.suchtschweiz.ch/zahlen-und-fakten/) — Addiction statistics from the non-profit Addiction Switzerland. Verify reuse terms for the selected material.

#### Population, migration and religion

- [Staatssekretariat für Migration SEM](https://www.sem.admin.ch/sem/de/home/publiservice/statistik.html) — State Secretariat for Migration statistics.
- [Christian Catholic Church Switzerland](https://christkatholisch.ch/angebote/opendata/) — Data published by the Christian Catholic Church of Switzerland, a non-government source.

#### Agriculture and food

- [Agrarmarktdaten](https://www.agrarmarktdaten.ch/) — Federal Office for Agriculture price and quantity data across agricultural and food markets.
- [Agrarbericht](https://www.blw.admin.ch/blw/de/home/agrarbericht.html) — Federal Office for Agriculture reporting on Swiss agriculture.
- [Schweizer Nährwertdatenbank](https://naehrwertdaten.ch/de/) — Federal Food Safety and Veterinary Office data on the composition of foods available in Switzerland.
- [Agristat](https://www.sbv-usp.ch/de/services/agristat-statistik-der-schweizer-landwirtschaft) — Agricultural statistics from the Swiss Farmers’ Union, a non-government publisher. Verify reuse terms for individual products.
- [Identitas Tierstatistik](https://tierstatistik.identitas.ch/en/index.html) — Livestock and companion-animal statistics from Identitas.

#### Energy

- [Bundesamt für Energie BFE](https://www.bfe.admin.ch/de/energiestatistik) — Federal Office of Energy statistics and geodata. [API overview](https://www.bfe.admin.ch/de/api).
- [Swiss Energy Dashboard](https://energiedashboard.admin.ch/bfe-url) — Federal Office of Energy electricity, gas, price and supply indicators. [Read-only REST API](https://energiedashboard.ch/api/swagger-ui/index.html).
- [Swissgrid](https://www.swissgrid.ch/de/home/customers/topics/energy-data-ch.html) — Swiss transmission-grid operator energy data.
- [Open Energy Data CH](https://github.com/OpenEnergyData/energy-data-ch) — Community-maintained directory of open Swiss energy datasets.

#### Buildings, housing and land

- [Federal Register of Buildings and Dwellings (GWR/RegBL)](https://www.bfs.admin.ch/bfs/de/home/register/gebaeude-wohnungsregister.html) — BFS building and dwelling register, including reference identifiers EGID and EWID. Public data and administrative access have different scopes. [Register information](https://www.housing-stat.ch).
- [Bundesamt für Wohnungswesen BWO – Wohnungsmarkt](https://www.bwo.admin.ch/de/wohnungsmarkt) — Federal Housing Office housing-market indicators. [Market overview](https://www.bwo.admin.ch/de/wohnungsmarkt-auf-einen-blick) · [Housing statistics](https://www.bwo.admin.ch/de/zahlen-und-fakten-wohnen).
- [BFS Bau- und Wohnungswesen](https://www.bfs.admin.ch/bfs/de/home/statistiken/bau-wohnungswesen.html) — BFS construction and housing statistics, including activity, vacancies and housing stock.
- [Schweizerischer Baupreisindex (BAP)](https://www.bfs.admin.ch/bfs/de/home/statistiken/preise/baupreise.html) — BFS construction price index for building construction and civil engineering.
- [Wohnimmobilienpreisindex (IMPI)](https://www.bfs.admin.ch/bfs/de/home/statistiken/preise/erhebungen/impi.html) — BFS quarterly residential property price index for owner-occupied homes.
- [Mietpreisindex (MPI)](https://www.bfs.admin.ch/bfs/de/home/statistiken/preise/erhebungen/mpi.html) — BFS rental price index for permanently rented dwellings.
- [ARE – Daten und Analysen](https://www.are.admin.ch/de/daten) — Federal Office for Spatial Development spatial monitoring, building-zone and settlement data.
- [ÖREB-Kataster](https://www.cadastre.ch/de/oereb-kataster) — Cadastre of public-law restrictions on landownership. Information on obtaining parcel-level extracts; consult the relevant canton for data services.
- [Daten der amtlichen Vermessung (cadastre.ch)](https://www.cadastre.ch/de/daten-der-av) — Official cadastral survey data coordinated by swisstopo. See [Geodienste.ch](https://geodienste.ch/) for aggregated cantonal services.
- [Swiss Dwellings](https://zenodo.org/records/7788422) — Apartment geometry and derived building-analysis data published by Archilyse, a private company. Versioned download on Zenodo; see the record for its license.

#### Environment, climate and biodiversity

- [Bundesamt für Umwelt BAFU](https://www.bafu.admin.ch/bafu/de/home/zustand.html) — Federal Office for the Environment indicators and environmental reporting.
- [Bundesamt für Meteorologie und Klimatologie MeteoSchweiz](https://www.meteoswiss.admin.ch/services-and-publications/service/open-data.html) — Federal weather and climate observations and products.
- [SLF data service](https://www.slf.ch/en/services-and-products/slf-data-service/) — WSL Institute for Snow and Avalanche Research observations used in avalanche warnings.
- [«Hydrodaten» Bundesamt für Umwelt BAFU](https://www.hydrodaten.admin.ch/de/aktuelle-lage) — Federal Office for the Environment hydrological observations and forecasts. [LINDAS dataset metadata](https://environment.ld.admin.ch/.well-known/void/dataset/hydro).
- [GLAMOS DOI products](https://doi.glamos.ch/) — Swiss glacier inventories and change measurements from the GLAMOS monitoring program. Versioned downloads with persistent identifiers and CC BY 4.0 licenses.
- [Swiss National Fauna Databank](https://ipt.gbif.ch/resource?r=ifn) — InfoSpecies species-occurrence records for Switzerland, downloadable as Darwin Core under CC BY 4.0.
- [Jagdstatistik](https://www.jagdstatistik.ch/de/home) — Federal Office for the Environment hunting and wildlife statistics.

#### Tourism

- [Swiss Tourism Data](https://www.tourismdata.ch/) — Tourism data-source metadata catalog from the National Data Infrastructure for Tourism project. Access and reuse conditions depend on the linked provider.
- [Zürich Tourismus](https://www.zuerich.com/de/business/ueber-zuerich-tourismus/open-data-portal) — Tourism organization data for Zürich.
- [Switzerland Tourism Open Data API](https://developer.myswitzerland.io/) — Swiss tourism data from Switzerland Tourism. Requires a free API key; most data is CC BY-SA 4.0, but linked images are excluded from dataset licenses.

#### Transport

- [SBB Open Data](https://data.sbb.ch/pages/home/) — Swiss Federal Railways datasets.
- [Open Data Platform Mobility Switzerland](https://opentransportdata.swiss/en/) — Swiss public-transport and road-traffic data, including FEDRO counters and alerts.
- [FEDRO open vehicle data](https://www.astra.admin.ch/en/vehicle-data) — Anonymized federal vehicle inventories, registrations and vehicle-type data available for download.
- [Geneva Public Transport](https://opendata.tpg.ch/pages/accueil/) — Geneva public-transport operator data.

#### Research repositories

Research data from Swiss institutions and collaborations complements OGD. Licenses and access restrictions vary by record.

- [FORS SWISSUbase](https://www.swissubase.ch/de/) — Cross-disciplinary repository for Swiss research. Access conditions and licenses vary by record.
- [Schweizerischer Nationalfonds SNF](https://data.snf.ch/datasets) — Swiss National Science Foundation research-funding data. [Data-story repositories](https://github.com/snsf-data).
- [CERN](https://opendata.cern.ch/) — Particle-physics research data from CERN experiments.
- [DaSCH Service Platform](https://dasch.swiss/about-us/platform) — Humanities research-data repository. Linked Data, IIIF and REST services; verify record-level access and reuse conditions.
- [Materials Cloud Archive](https://archive.materialscloud.org/about) — Computational-materials research repository with versioned dataset downloads.

#### Cultural heritage and archives

Discovery resources for cultural and historical material. Open metadata does not establish reuse rights for images, recordings or documents. Collections may include restricted records; check each item’s rights and access information.

- [e-rara](https://www.e-rara.ch/) — Digitized Swiss printed works. Check the rights statement for each digitized work. [OAI-PMH, IIIF, full-text and download interfaces](https://www.e-rara.ch/wiki/apiinfo).
- [Memoriav Memobase](https://memobase.ch/de/start) — Swiss audiovisual heritage discovery portal. Recording and image rights vary by item.
- [DODIS](https://dodis.ch/search) — Swiss diplomatic-history research database. Consult item-level rights before reusing document images.
- [Schweizer Landesmuseum](https://sammlung.nationalmuseum.ch/de/maincategory) — Swiss National Museum collection catalog. Catalog descriptions and object photographs may have different reuse conditions.
- [Swiss Federal Archives](https://www.recherche.bar.admin.ch/recherche/) — Federal archival discovery catalog for Swiss history. Finding aids and available digital documents; some records require an order or access permission.
- [Schweizerisches Idiotikon](https://idiotikon.ch/projekte) — Research resources documenting Swiss German dialects. Consult the terms of each resource.
- [Ortsnamen.ch](https://www.ortsnamen.ch/de/) — Research catalog of Swiss place names. [Map search](https://search.ortsnamen.ch/de) · [REST API documentation](https://search.ortsnamen.ch/static/api/swagger/index.html).

### Cantonal portals

Selected cantonal catalogs and statistics portals; coverage varies by portal type. Geodata portals are listed separately below.

- [Aargau](https://www.ag.ch/de/themen/datenportal#/) — Cantonal open-data catalog.
- [Basel-Stadt](https://data.bs.ch/explore/) — Cantonal open-data catalog.
- [Basel-Landschaft](https://data.bl.ch/explore/) — Cantonal open-data catalog.
- [Basel-Landschaft Statistical Office](https://www.baselland.ch/politik-und-behorden/direktionen/finanz-und-kirchendirektion/daten-statistik) — Cantonal official statistics.
- [Bern](https://www.fin.be.ch/de/start/themen/OeffentlicheStatistik/statistikportal.html) — Cantonal official statistics.
- [Fribourg / Freiburg](https://opendata.fr.ch/pages/home/) — Cantonal open-data catalog.
- [Fribourg / Freiburg Statistical Office](https://www.fr.ch/de/vwbd/stata) — Cantonal official statistics.
- [Geneva](https://sitg.ge.ch/search?category=data) — Geneva geodata catalog (SITG). See also the [Cantonal statistics portal](https://statistique.ge.ch/).
- [Glarus](https://opendata.swiss/en/organization/kanton-glarus) — Cantonal and Landsgemeinde datasets. Tabular and geospatial resources on opendata.swiss.
- [Graubünden](https://www.gr.ch/DE/institutionen/verwaltung/dvs/awt/statistik/Seiten/home.aspx) — Cantonal official statistics.
- [Jura](https://stat.jura.ch/) — Cantonal official statistics.
- [Luzern](https://www.lustat.ch) — Cantonal official statistics.
- [Neuchâtel](https://www.ne.ch/autorites/DFS/STAT/Pages/accueil.aspx) — Cantonal official statistics.
- [Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Wirtschaft--Statistik-und-Tourismus-3874-DE.html) — Cantonal official statistics.
- [Schwyz](https://data.sz.ch/explore/) — Cantonal open-data catalog.
- [Solothurn](https://so.ch/verwaltung/finanzdepartement/amt-fuer-finanzen/statistikportal/) — Cantonal official statistics.
- [St. Gallen](https://daten.sg.ch/explore/) — Cantonal open-data catalog.
- [St. Gallen Statistical Office](https://stada2.sg.ch/) — Cantonal official statistics.
- [Ticino](https://www4.ti.ch/index.php?id=42382) — Cantonal official statistics.
- [Thurgau](https://data.tg.ch/explore) — Cantonal open-data catalog. [Thematic atlases](https://themenatlas-tg.ch/#c=home).
- [Thurgau Statistical Office](https://statistik.tg.ch/) — Cantonal official statistics.
- [Uri](https://www.statistik-uri.ch/daten) — Cantonal official statistics.
- [Vaud](https://www.vd.ch/themes/etat-droit-finances/statistique) — Cantonal official statistics.
- [Valais](https://www.vs.ch/de/web/sstp/sstp) — Cantonal official statistics.
- [Zug](https://zg.ch/de/gesundheitsdirektion/fachstelle-fuer-daten-und-statistik/open-government-data) — Open data shared by the canton and city of Zug.
- [Zürich](https://www.zh.ch/de/politik-staat/opendata.zhweb-noredirect.zhweb-cache.html#/) — Cantonal open-data catalog.
- [Zürcher Gemeinden in Zahlen](https://zgz.statistik.zh.ch/) — Municipal statistics published by the Canton of Zürich.

### Municipal portals

Selected municipal catalogs and statistics portals. Check the linked canton for additional local data.

- [Bern](https://www.bern.ch/open-government-data-ogd/ogd-nach-themen) — Municipal open-data resources.
- [Biel/Bienne](https://opendata.swiss/en/organization/biel-bienne) — Municipal datasets from Biel/Bienne. Publisher catalog on opendata.swiss.
- [Lausanne](https://www.lausanne.ch/officiel/statistique.html) — Municipal official statistics.
- [Lugano](https://statistica.lugano.ch/site/dati-ogd/) — Municipal open-data resources.
- [Luzern](https://www.lustat.ch/statistikportal-stadt-luzern) — Municipal official statistics.
- [St. Gallen](https://www.stadt.sg.ch/home/verwaltung-politik/stadt-zahlen/statistikdatenbanken.html) — Municipal official statistics.
- [Uster](https://www.uster.ch/opendata) — Municipal open-data resources.
- [Winterthur](https://stadt.winterthur.ch/themen/arbeit-steuern-wirtschaft/daten-statistik) — Municipal statistics. [Source repositories](https://github.com/Stadt-Winterthur).
- [Zürich](https://data.stadt-zuerich.ch/) — Municipal data catalog. [Source repositories](https://github.com/opendatazurich) · [Linked-data services](https://www.stadt-zuerich.ch/de/politik-und-verwaltung/statistik-und-daten/linked-open-data.html).

## Geospatial data

### Official sources and catalogs

Federal and shared regional discovery services. Metadata and maps can include layers whose download and reuse conditions differ.

- [swisstopo](https://www.swisstopo.admin.ch/de/geodata.html) — Federal Office of Topography geodata products.
- [geo.admin.ch](https://www.geo.admin.ch/de/home.html) — Federal geodata services and map information. [Service documentation](https://docs.geo.admin.ch/) · [STAC download API information](https://www.geo.admin.ch/de/geo-dienstleistungen/geodienste/downloadienste/stac-api.html) · [Linked data](https://geo.ld.admin.ch).
- [geo.admin.ch — Strassenverzeichnis](https://map.geo.admin.ch/#/map?lang=de&center=2660000,1190000&z=1&topic=ech&layers=ch.swisstopo.amtliches-strassenverzeichnis&bgLayer=ch.swisstopo.pixelkarte-farbe) — Official Swiss street-name directory. Map layer in the federal viewer.
- [geocat](https://www.geocat.ch) — Swiss geodata metadata catalog operated by swisstopo. Access conditions vary by record.
- [geobasisdaten.ch](https://geobasisdaten.ch/) — Inventory of legally mandated Swiss geodata from the cantonal geoinformation conference (KGK/CGC). Includes dataset responsibilities and legal references. [Background information](https://www.kgk-cgc.ch/geobasisdaten).
- [geodienste.ch](https://geodienste.ch/) — Intercantonal service aggregating basic geodata from cantons and municipalities.
- [Geoportal.ch](https://www.geoportal.ch/) — Regional geodata publication platform. Coverage and reuse conditions vary by participating authority and layer.
- [BFS Plattform Statatlas](https://www.atlas.bfs.admin.ch/de/index.html) — BFS thematic statistical atlases. Use these for map-based exploration of regional indicators; consult the linked tables for underlying data.

### Research and environmental geodata

- [Datalakes](https://www.datalakes-eawag.ch/) — Eawag lake-measurement data.
- [Alplakes](https://www.alplakes.eawag.ch/) — Eawag lake models and remote-sensing products.
- [Swiss Data Cube](https://www.swissdatacube.org) — Earth-observation data infrastructure for Switzerland, operated by Swiss research institutions and UNEP/GRID-Geneva.
- [EnviDat](https://www.envidat.ch/) — WSL environmental research-data repository. Access conditions and licenses vary by record.

### Cantonal and municipal geoportals

Official map and catalog entry points. Consult each layer’s metadata for download services, license and registration requirements.

- [Cantonal geoportal directory](https://www.kgk-cgc.ch/geodaten/kantonale_geoportale) — KGK/CGC directory of cantonal geodata entry points.
- [Canton of Aargau](https://www.ag.ch/de/verwaltung/dfr/geoportal) — Official regional geodata.
- [Canton of Appenzell Ausserrhoden](https://www.geoportal.ch/ktar) — Official regional geodata.
- [Canton of Appenzell Innerrhoden](https://www.ai.ch/themen/planen-und-bauen/geodaten-und-plaene/geoportal) — Official regional geodata.
- [Canton of Basel-Landschaft](https://www.baselland.ch/politik-und-behorden/direktionen/volkswirtschafts-und-gesundheitsdirektion/amt-fur-geoinformation/geoportal/geodaten) — Official regional geodata.
- [Canton of Basel-Stadt](https://www.bs.ch/bvd/grundbuch-und-vermessungsamt/geo/geodaten) — Official regional geodata.
- [Canton of Bern](https://www.agi.dij.be.ch/de/start.html) — Official regional geodata.
- [City of Bern](https://map.bern.ch/geoportal/) — Official regional geodata.
- [Canton of Fribourg / Freiburg](https://map.geo.fr.ch/) — Official regional geodata.
- [Canton of Geneva](https://map.sitg.ge.ch/app/) — Official regional geodata.
- [Canton of Glarus](https://www.gl.ch/verwaltung/bau-und-umwelt/hochbau/raumentwicklung-und-geoinformation/geoportal-kanton-glarus.html/808) — Official regional geodata.
- [Canton of Graubünden](https://geo.gr.ch/) — Official regional geodata.
- [Canton of Jura](https://www.jura.ch/fr/Autorites/Administration/DEC/SDT/GeoPortail/GeoPortail-du-Canton-du-Jura.html) — Official regional geodata.
- [Canton of Luzern](https://geoportal.lu.ch/karten) — Official regional geodata.
- [Canton of Neuchâtel](https://www.ne.ch/autorites/DDTE/SGRF/SITN/geoportail/Pages/accueil.aspx) — Official regional geodata.
- [Nidwalden and Obwalden](https://www.gis-daten.ch/geodaten/geodatenkatalog/) — Official regional geodata.
- [Canton of Schaffhausen](https://sh.ch/CMS/Webseite/Kanton-Schaffhausen/Beh-rde/Verwaltung/Volkswirtschaftsdepartement/Amt-f-r-Geoinformation-1262910-DE.html) — Official regional geodata.
- [Canton of Schwyz](https://www.sz.ch/behoerden/verwaltung/umweltdepartement/amt-fuer-geoinformation/geoportal-webgis.html/8756-8758-8802-9447-9448-9462) — Official regional geodata.
- [Canton of Solothurn](https://so.ch/verwaltung/bau-und-justizdepartement/amt-fuer-geoinformation/geoportal/) — Official regional geodata.
- [Canton of St. Gallen](https://www.sg.ch/bauen/geoinformation/gi/geodaten.html) — Official regional geodata.
- [Canton of Ticino](https://map.geo.ti.ch/) — Official regional geodata.
- [Canton of Thurgau](https://map.geo.tg.ch) — Cantonal geodata. [Geodata shop](https://shop.geo.tg.ch/) requires registration.
- [Canton of Uri](https://www.ur.ch/geoinformationen) — Cantonal geodata information. [Map/download portal](https://geo.ur.ch).
- [Canton of Vaud](https://www.geo.vd.ch/) — Official regional geodata.
- [Canton of Valais](https://www.vs.ch/de/web/egeo) — Official regional geodata.
- [Canton of Zug](https://zg.ch/de/planen-bauen/geoinformation/geoinformationen-nutzen) — Official regional geodata.
- [Canton of Zürich](https://geo.zh.ch/data) — Official regional geodata.
- [City of Zürich](https://www.stadt-zuerich.ch/geodaten/) — Official regional geodata.

### Community and global geodata

Non-government open geodata with Swiss coverage. OSM-derived and other global products complement official Swiss sources.

- [OpenStreetMap CH](https://osm.ch/) — Community-maintained Swiss OpenStreetMap resources from SOSM. [Data extracts](https://planet.osm.ch/) · [Overpass QL](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) · [Postpass SQL](https://wiki.openstreetmap.org/wiki/Postpass).
- [BBBike's OSM download server](https://download.bbbike.org/osm/) — OpenStreetMap extracts in several formats. [Zürich extracts](https://download.bbbike.org/osm/bbbike/Zuerich/).
- [Geofabrik's OSM download server](https://download.geofabrik.de/europe/switzerland.html) — OpenStreetMap extracts for Switzerland in formats including shapefiles.
- [Layercake](https://openstreetmap.us/our-work/layercake/) — Worldwide OSM-derived thematic layers from OpenStreetMap US in GeoParquet format.
- [Cadence Maps](https://cadencemaps.infs.ch/) — OSM-derived GeoParquet layers, including points of interest for Germany, Austria and Switzerland.
- [Overture Maps](https://overturemaps.org/) — Global community map project combining OSM-derived layers and other sources. Check each layer’s license and attribution requirements.

### Geodata discovery tools

- [GeoHarvester](https://davidoesch.github.io/geoservice_harvester_poc/) — Community discovery portal for official Swiss geodata services. [Source code](https://github.com/davidoesch/geoservice_harvester_poc).
- [geospatial-data-catalogs](https://github.com/giswqs/geospatial-data-catalogs) — Community directory of geospatial datasets across cloud and catalog services. Check each dataset’s license and Swiss coverage.

## APIs and linked data

API links appear beside source entries; selected interfaces for common workflows are highlighted here. Catalog APIs return metadata; data APIs return records or observations.

### Selected interfaces

- [opendata.swiss CKAN API](https://handbook.opendata.swiss/de/content/nutzen/api-nutzen.html) — National OGD metadata catalog interface. Returns metadata; dataset records link onward to the actual data.
- [Geo Admin](https://docs.geo.admin.ch/) — Federal geodata service documentation.
- [Geo Admin STAC](https://www.geo.admin.ch/de/geo-dienstleistungen/geodienste/downloadienste/stac-api.html) — Federal Spatial Temporal Asset Catalog (STAC) interface for discovering and downloading geospatial assets.
- [Federal Popular Votes API](https://opendata.swiss/en/dataset/echtzeitdaten-am-abstimmungstag-zu-eidgenoessischen-abstimmungsvorlagen) — Official federal popular-vote results in JSON, with municipal, district, cantonal and national coverage.
- [SIMAP API](https://www.simap.ch/api-doc) — Swiss public procurement publications in JSON.
- [Swiss Energy Dashboard API](https://energiedashboard.ch/api/swagger-ui/index.html) — Read-only REST API for federal energy time series, statistics and metadata.
- [SFOE APIs](https://www.bfe.admin.ch/de/api) — Federal Office of Energy interface directory covering energy and mobility services.
- [Overpass API (with Overpass QL)](https://wiki.openstreetmap.org/wiki/Overpass_API/Overpass_QL) — Query OpenStreetMap data using Overpass QL. [Swiss restaurant query example](https://osm.li/Oqg).
- [Postpass](https://wiki.openstreetmap.org/wiki/Postpass) — Query OpenStreetMap data using SQL over PostGIS. [Restaurant query example](https://overpass-turbo.eu/s/2qpD).
- [OpenERZ](https://github.com/metaodi/openerz) — Community API for municipal waste-collection schedules in Switzerland. Includes Python client source code.
- [OpenPLZ API](https://www.openplzapi.org/en/) — Community street and postal-code directory for Switzerland, Liechtenstein, Austria and Germany.
- [OpenHolidays API](https://www.openholidaysapi.org/en/) — Community public-holiday and school-holiday data. REST API documentation lists supported countries.

### Linked data services

Access structured, linked datasets; see service documentation for query endpoints, supported datasets and examples.

- [LINDAS ecosystem overview](https://lindas.admin.ch/ecosystem/) — Swiss Federal Archives service for publishing and querying linked datasets. [Service documentation](https://lindas.admin.ch).
- [Fedlex](https://fedlex.data.admin.ch/en-CH/home/intro) — Linked-data access to federal legislation and official legal publications. [Reading portal](https://www.fedlex.admin.ch/de/home).
- [Federal Geoportal Linked Data](https://geo.ld.admin.ch) — Linked-data interface to federal geodata.
- [City of Zürich LOD](https://www.stadt-zuerich.ch/de/politik-und-verwaltung/statistik-und-daten/linked-open-data.html) — City of Zürich linked open data.

## Tools and libraries

### Visualization and data clients

- [Visualize](https://visualize.admin.ch) — Web tool for creating and embedding charts from compatible LINDAS datasets. [BSD-3-Clause source code](https://github.com/visualize-admin/visualization-tool).
- [BFS](https://github.com/lgnbhl/BFS) — Community R client for Federal Statistical Office APIs.
- [I14Y](https://github.com/lgnbhl/I14Y) — Community R client for the Swiss interoperability metadata catalog.
- [swissparlpy](https://github.com/metaodi/swissparlpy) — Community Python client for Swiss Parliament web services.

### Source-code directories

Software and repository indexes. Check each project’s license; listing does not establish open-source status.

- [Federal Open Source GitHub Index](https://github.com/swiss/index) — Directory of Swiss Confederation GitHub organizations.
- [Swiss federal OSS catalog](https://www.opensource.admin.ch/) — Software published by federal and cantonal authorities. Includes repository and license information.
- [adminR Code Base](https://github.com/swiss-adminR/pkgs) — R packages and reusable code created by Swiss public institutions.
- [Swiss OSS Benchmark](https://ossbenchmark.com/institutions) — Directory of source-code repositories and organizations from Swiss institutions.

## Guides, standards and policy

- [Swiss OGD information](https://www.bfs.admin.ch/bfs/en/home/services/ogd.html) — Federal guidance on Open Government Data.
- [Swiss OGD Master Plan 2024–2027](https://www.bk.admin.ch/bk/en/home/digitale-transformation-ikt-lenkung/vorgaben/sn004-open_government_data_strategie_schweiz.html) — Federal open-by-default objectives and implementation measures for 2024–2027.
- [Geschäftsstelle OGD BFS](https://www.bfs.admin.ch/bfs/de/home/dienstleistungen/ogd/geschaeftsstelle.html) — Federal OGD coordination and support for publishers and users.
- [Digitale Verwaltung Schweiz](https://www.digitale-verwaltung-schweiz.ch/) — Public-sector digital transformation programs and guidance from Digital Public Services Switzerland.
- [National data management NaDB](https://www.bfs.admin.ch/bfs/en/home/nadb/nadb.html) — Federal program for reusing administrative data. Discover collections and interfaces through I14Y in the data-source catalog section.
- [Swiss DCAT Standard](https://www.ech.ch/de/ech/ech-0200/1.0) — eCH-0200 metadata profile for Swiss data portals. Links to version 1.0; check the publisher for subsequent versions.
- [Forschungsstelle Digitale Nachhaltigkeit Uni Bern](https://www.digitale-nachhaltigkeit.unibe.ch/) — University of Bern research on digital sustainability and open data.
- [Open Data lectures Uni Bern](https://www.digitale-nachhaltigkeit.unibe.ch/studium/open_data_veranstaltung/index_ger.html) — University of Bern open-data teaching material.
- [CKAN API documentation](https://docs.ckan.org/en/latest/api/) — Generic documentation for accessing CKAN catalogs, including opendata.swiss.
- [Open Data Handbook](https://opendatahandbook.org/) — Open Knowledge Foundation introduction to open data, reuse and publishing.

## Community and publications

### Organizations and initiatives

- [Statistical Institutions in Switzerland](https://www.bfs.admin.ch/bfs/de/home/bfs/oeffentliche-statistik/system-oeffentliche-statistik/statistikinstitutionen-schweiz.html) — BFS directory of Swiss statistical institutions.
- [Korstat](https://confluence.swissdatacommunity.ch/plugins/viewsource/viewpagesrc.action?pageId=393257) — Conference of regional statistical offices in Switzerland.
- [Project Rosling](https://www.projectrosling.ch) — Federal initiative supporting dialogue and knowledge about data and statistics.
- [opendata.ch](https://opendata.ch/de/) — Swiss open-data association. [Events](https://opendata.ch/events/).
- [öffentlichkeitsgesetz.ch](https://www.oeffentlichkeitsgesetz.ch/deutsch/) — Non-profit forum for transparency in public administration. Guidance on access to official documents.
- [Parldigi](https://www.parldigi.ch/de/) — Parliamentary group for digital sustainability.
- [Swiss OpenStreetMap Association (SOSM)](https://sosm.ch/) — Community association supporting open geodata in Switzerland.

### Events and meetups

- [Statistiktage](https://www.statistiktage.ch/) — Swiss statistics conference organized by the [Swiss Statistical Society](https://www.stat.ch/en/) and [IMSD](https://www.imsd.ch/de/).
- [GovTech Hackathons](https://digital.swiss/en/action-plan/measures/govtech-hackathon) — Federal GovTech hackathon initiative.
- [Open Data Beer](https://opendatabeer.ch/) — Swiss open-data community gatherings.
- [DINACON](https://dinacon.ch/) — Swiss conference on digital sustainability.
- [GeoBeer Switzerland](https://geobeer.ch/) — Swiss community meetings on geography, GIS and cartography.
- [Linked Data Meetup](https://www.bfh.ch/de/themen/linked-data/) — Meetup organized by the Swiss Federal Archives and BFH for users of linked data, including LINDAS.

### Newsletters

Links lead to subscription pages.

- [Bundesamt für Statistik](https://scnem.com/a.php?sid=ffnuk.16937bf,f=999) — Federal Statistical Office newsletter.
- [Open Data CH](https://opendata.us7.list-manage.com/subscribe?u=c01c0e110415680950f8958e4&id=12200d2993) — Opendata.ch newsletter.

### Podcasts

- [Statistisch gesehen](https://feeds.captivate.fm/statistisch-gesehen/) — RSS feed for the podcast from the Canton of Zürich’s Office for Statistics and Data.

### Data journalism

Reusable code and data from Swiss journalism. Linked articles have separate access conditions and rights for text and images.

- [Neue Zürcher Zeitung Visuals Team](https://github.com/nzzdev/st-methods) — Methods and code accompanying NZZ Visuals journalism.
- [SRF Data](https://srfdata.github.io/) — Code and data accompanying SRF data journalism. [Published stories](https://www.srf.ch/news/srf-data).
- [Tamedia Data Desk](https://github.com/tamedia-ddj) — Tamedia data-journalism repositories. [Interactive stories](https://interaktiv.tagesanzeiger.ch/).

## European comparisons

European catalogs and neighboring countries’ official statistics for cross-border discovery and comparisons. Check definitions, periods, territorial units and Swiss coverage before combining data.

### European catalogs and statistics

- [European Union](https://data.europa.eu/en) — European data catalog for cross-border source discovery. Licenses and access conditions vary by record.
- [Eurostat](https://ec.europa.eu/eurostat/web/main/data) — European statistical data for comparisons involving Switzerland. Check Swiss coverage for each series. [Database](https://ec.europa.eu/eurostat/web/main/data/database) · [GISCO geodata](https://ec.europa.eu/eurostat/web/gisco/overview).
- [List of European Statistical Offices](https://www.destatis.de/EN/Service/Address-Book/europe.html) — Destatis directory of European statistical offices.
- [IATE](https://iate.europa.eu/home) — EU multilingual terminology database for interpreting European administrative concepts.

### Neighboring countries

- [Germany — GovData](https://www.govdata.de/) — German government open-data catalog.
- [Germany — Destatis GENESIS](https://www-genesis.destatis.de/genesis/online) — German Federal Statistical Office tables.
- [Austria — Statistics Austria](https://www.statistik.at/en) — Austrian official statistics.
- [Austria — data.gv.at](https://www.data.gv.at/) — Austrian government open-data catalog.
- [France — INSEE](https://www.insee.fr/en/accueil) — French official statistics from INSEE.
- [France — data.gouv.fr](https://www.data.gouv.fr/en/datasets/) — French government open-data catalog.
- [Italy — Istat](https://www.istat.it/en/) — Italian official statistics from Istat.
- [Italy — dati.gov.it](https://www.dati.gov.it/) — Italian public-sector data catalog.
- [Liechtenstein — Statistics Portal](https://www.statistikportal.li/) — Liechtenstein official statistics.

## Curation and contributions

### Contribute

Found a useful resource, a broken link or something unclear? [Issues](https://github.com/rnckp/awesome-ogd-switzerland/issues) and [pull requests](https://github.com/rnckp/awesome-ogd-switzerland/pulls) are welcome—a link and a few words are enough. I review every suggestion, and we can work out where it fits together.

When reviewing a resource, I look for:

- Relevance to Swiss open data or the core European comparison sources.
- An identifiable publisher, clear geographic or thematic coverage and a direct link to the resource.
- For data, machine-readable files or an access interface, with documented terms allowing open reuse. For software, source code with an open-source license.
- For guides, communities and other supporting resources, freely accessible material that helps people use or understand open data.

See the [curation policy](#curation-policy) for details. No need to check everything before suggesting a resource—if you’re unsure about fit or reuse terms, we can look together.

To edit directly, use `Resource name — contents and coverage.` in one or two sentences, with API links beside the source. Prefer one main entry with cross-references; avoid promotional claims and undated counts. I’m happy to help with wording, placement and formatting.

For broken links, please mention what happened: a missing page, an access block or a connection error.

For maintenance scripts, development commands and the agent skill, see the [helper documentation](src/README.md).

### Curation policy

Data must permit free use, modification and redistribution, including commercial reuse, following the [Open Definition](https://opendefinition.org/). Software must provide source code under an [OSI-approved license](https://opensource.org/licenses). Free, non-discriminatory registration is acceptable. Payment, case-by-case permission, non-commercial-only terms and unclear reuse rights do not qualify a dataset or tool for inclusion.

Resources from public authorities, researchers, communities, individuals, non-profits and companies qualify on the same criteria: identifiable provenance, relevance and documented reuse rights. Government publication alone does not establish openness.

Catalogs and repositories may include restricted records if the entry explains this and helps users find reusable material; inclusion does not endorse every record. Guides, standards, communities and journalism must offer freely accessible material that helps people use or understand open data. Linked articles and cultural objects may carry separate rights.

## Licence

This list is released under [CC0 1.0](LICENSE). Linked resources retain their own licences and terms.
