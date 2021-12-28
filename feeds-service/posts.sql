CREATE TABLE posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  image_path TEXT NOT NULL,
  caption TEXT NOT NULL,
  likes INTEGER DEFAULT 0
);

INSERT INTO
  posts (caption, image_path)
VALUES
  (
    "I naredne nedelje neposredna nastava u školama",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_2.png"
  ),
  (
    "Praznične gužve i kolone vozila širom Srbije",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_GUZVA24122021.jpg"
  ),
  (
    "Praznični darovi",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_Prikupljanje-slatkisa-za-ovogodisnje-paketice--Foto-Svetosavska-omladinska-zajednica-.jpg"
  ),
  (
    "Svedoci višeslojnih kretanja u slikarstvu",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_Miodrag-Mica-Popovic,-Gvozden-istresa-nos-na-peronu-zeleznicke-stanice-,-1970,-ulje-na-platnu-sa-aplikacijama,-175x150-cm.jpg"
  ),
  (
    "Modernizam u Galeriji SANU",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_Nadezda-Petrovic-Pompeji-1907.jpg"
  ),
  (
    "Srbija će pratiti odluku EU o kovid sertifikatima",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_tatjana-matic.jpg"
  ),
  (
    "Umrle 24 osobe, više od 1.000 novozaraženih",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_korona-virus-doktori-epidemia-f-ap-m.s.nnns.jpg"
  ),
  (
    "Broj novozaraženih u regionu na nivou prethodnih dana",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_trg-u-zagrebu.jpg"
  ),
  (
    "Slovenija zabranila doček Nove godine na otvorenom",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_ljubljana.jpgg"
  ),
  (
    "Infektolog Nožić: Pandemija će najverovatnije stati na proleće",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_setnja-knezom.jpg"
  ),
  (
    "Prosvetni zakoni otvaraju vrata državnoj maturi",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_MATURAreforma24122021.jpg"
  ),
  (
    "Američki LNG obara cenu ruskog gasa u Evropi",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_lng-2-tanker-za-prvu.jpg"
  ),
  (
    "Ruska vojska završila vežbe u blizini granice sa Ukrajinom",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_ruska-vojska-tenk-t90a-epa-efe-m.ss.-nn.jpg"
  ),
  (
    "Hiljade letova širom sveta otkazano na Božić zbog omikrona",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_w_57371620.jpg"
  ),
  (
    "Prvi let novog ruskog putničkog aviona",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_mc-21-avion-yt.jpg"
  ),(
    "Velika potražnja stambenih kredita uprkos skupim nekretninama",
    "https://www.politika.rs/thumbs//upload/Article/Image/2021_12///677z381_stanovi.jpg"
  );