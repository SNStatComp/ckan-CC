# http://statline.cbs.nl/Statweb/publication/?DM=SLNL&PA=83487NED&D1=a&D2=818-1396&HDR=T&STB=G1&VW=D


lines <- readLines("data_amsterdam/Kerncijfers_wijken_e_021116115000.csv", 
  encoding = "latin1")

header1 <- as.character(unlist(read.table(
  textConnection(lines[3]), sep=";", header=FALSE)))
header2 <- as.character(unlist(read.table(
  textConnection(lines[4]), sep=";", header=FALSE)))
header3 <- as.character(unlist(read.table(
  textConnection(lines[5]), sep=";", header=FALSE)))

header2 <- ifelse(header1 == header2, "", header2)
header3 <- ifelse(header2 == header3 | header1 == header3, "", header3)

simp <- function(x) {
  x <- tolower(x)
  x <- gsub("'", "", x)
  x <- gsub("[^[:alnum:]]", "_", x)
  gsub("[_]+", "_", x)
}

header1 <- simp(header1)
header2 <- simp(header2)
header3 <- simp(header3)

# header <- paste(header1, header2, header3, sep="/")
# header <- gsub("[/]*$", "", header)

header <- ifelse(header3 == "", header2, header3)
header <- ifelse(header == "", header1, header)



lines <- lines[-c(1:6, length(lines))]
dta <- read.delim(textConnection(lines), header=FALSE, sep=";", 
  dec=".", stringsAsFactors = FALSE)

for (i in 5:ncol(dta)) dta[[i]] <- as.numeric(dta[[i]])

names(dta) <- header

# Remove column with all NA
allna <- sapply(dta, function(d) all(is.na(d)))
dta <- dta[, !allna]



# =================================================
# add geo dta
library(maptools)
library(rgdal)

map_munic <- readOGR("amsterdam/gem_2016.geojson", "OGRGeoJSON")
map_distr <- readOGR("amsterdam/wijk_2016.geojson", "OGRGeoJSON")
map_neigh <- readOGR("amsterdam/buurt_2016.geojson", "OGRGeoJSON")

dta$geojson <- character(nrow(dta))
dta$lon     <- numeric(nrow(dta))
dta$lat     <- numeric(nrow(dta))

for (i in 1:nrow(dta)) {
  if (dta$soort_regio[i] == "Gemeente") {
    tmp <- map_munic[map_munic$GM_CODE == dta$codering[i], ]
  } else if (dta$soort_regio[i] == "Wijk") {
    tmp <- map_distr[map_distr$WK_CODE == dta$codering[i], ]
  } else if (dta$soort_regio[i] == "Buurt") {
    tmp <- map_neigh[map_neigh$BU_CODE == dta$codering[i], ]
  } else warning("Unsuppored region type ", dta$soort_regio[i])
  
  
  writeOGR(tmp, 'tmp.json', layer='tmp', driver='GeoJSON', check_exists = FALSE)
  dta$geojson[i] <- paste0(readLines("tmp.json"), collapse="")
  
  cors <- as.numeric(coordinates(tmp))
  dta$lon[i] <- cors[1]
  dta$lat[i] <- cors[2]
  
  cat(i, '/', nrow(dta), '\n')
}

library(dplyr)

dta <- rename(dta, 
 subject = onderwerpen,
 region_name =  gemeentenaam,
 regio_type =  soort_regio,
 region_code =  codering,
 ninhabitants =  aantal_inwoners,
 nmen =  mannen,
 nwomen =  vrouwen,
 `nage_0_to_15` =  `0_tot_15_jaar`,
 `nage_15_to_25` =  `15_tot_25_jaar`,
 `nage_25_to_45` =  `25_tot_45_jaar`,
 `nage_45_to_65` =  `45_tot_65_jaar`,
 `nage_65_older` =  `65_jaar_of_ouder`,
 nunmarried =  ongehuwd,
 nmarried =  gehuwd,
 ndivorced =  gescheiden,
 nwidowed =  verweduwd,
 nimmigrant_western =  westers_totaal,
 nimmigrant_nonwestern =  niet_westers_totaal,
 nimmigrant_marokko =  marokko,
 nimmigrant_antiles_aruba =  nederlandse_antillen_en_aruba,
 nimmigrant_surinam =  suriname,
 nimmigrant_turkey =  turkije,
 nimmigrant_other_non_western =  overig_niet_westers,
 nhouseholds =  huishoudens_totaal,
 nhh_single_person =  eenpersoonshuishoudens,
 nhh_no_children =  huishoudens_zonder_kinderen,
 nhh_with_children =  huishoudens_met_kinderen,
 ave_househ_size =  gemiddelde_huishoudensgrootte,
 populatio_density =  bevolkingsdichtheid,
 area_total =  oppervlakte_totaal,
 area_land =  oppervlakte_land,
 area_water =  oppervlakte_water,
 urbanisation_grade =  mate_van_stedelijkheid,
 address_density =  omgevingsadressendichtheid) 

dta$indelingswijziging_wijken_en_buurten <- NULL


write.csv(dta, "amsterdam/wijken_buurten.csv", row.names = FALSE,
  na = "")



