from django.utils.translation import gettext_lazy as _

from djchoices import ChoiceItem, DjangoChoices


class Attributes(DjangoChoices):
    """
    NOTE: this was generated by 'manage.py generate_prefill_from_spec' from a Dutch API spec so labels are Dutch
    spec: http://localhost:8021/api/schema/openapi.yaml
    path: /ingeschrevenpersonen/{burgerservicenummer}
    """

    burgerservicenummer = ChoiceItem("burgerservicenummer", _("Burgerservicenummer"))
    datumEersteInschrijvingGBA_dag = ChoiceItem(
        "_embedded.datumEersteInschrijvingGBA.dag", _("Datumingangonderzoek > Dag")
    )
    datumEersteInschrijvingGBA_datum = ChoiceItem(
        "_embedded.datumEersteInschrijvingGBA.datum", _("Datumingangonderzoek > Datum")
    )
    datumEersteInschrijvingGBA_jaar = ChoiceItem(
        "_embedded.datumEersteInschrijvingGBA.jaar", _("Datumingangonderzoek > Jaar")
    )
    datumEersteInschrijvingGBA_maand = ChoiceItem(
        "_embedded.datumEersteInschrijvingGBA.maand", _("Datumingangonderzoek > Maand")
    )
    geboorte_datum_dag = ChoiceItem(
        "_embedded.geboorte._embedded.datum.dag",
        _("Geboorte > Datumingangonderzoek > Dag"),
    )
    geboorte_datum_datum = ChoiceItem(
        "_embedded.geboorte._embedded.datum.datum",
        _("Geboorte > Datumingangonderzoek > Datum"),
    )
    geboorte_datum_jaar = ChoiceItem(
        "_embedded.geboorte._embedded.datum.jaar",
        _("Geboorte > Datumingangonderzoek > Jaar"),
    )
    geboorte_datum_maand = ChoiceItem(
        "_embedded.geboorte._embedded.datum.maand",
        _("Geboorte > Datumingangonderzoek > Maand"),
    )
    geboorte_inOnderzoek_datum = ChoiceItem(
        "_embedded.geboorte._embedded.inOnderzoek.datum",
        _("Geboorte > Inonderzoek > Datum"),
    )
    geboorte_inOnderzoek_datumIngangOnderzoek_dag = ChoiceItem(
        "_embedded.geboorte._embedded.inOnderzoek._embedded.datumIngangOnderzoek.dag",
        _("Geboorte > Inonderzoek > Datumingangonderzoek > Dag"),
    )
    geboorte_inOnderzoek_datumIngangOnderzoek_datum = ChoiceItem(
        "_embedded.geboorte._embedded.inOnderzoek._embedded.datumIngangOnderzoek.datum",
        _("Geboorte > Inonderzoek > Datumingangonderzoek > Datum"),
    )
    geboorte_inOnderzoek_datumIngangOnderzoek_jaar = ChoiceItem(
        "_embedded.geboorte._embedded.inOnderzoek._embedded.datumIngangOnderzoek.jaar",
        _("Geboorte > Inonderzoek > Datumingangonderzoek > Jaar"),
    )
    geboorte_inOnderzoek_datumIngangOnderzoek_maand = ChoiceItem(
        "_embedded.geboorte._embedded.inOnderzoek._embedded.datumIngangOnderzoek.maand",
        _("Geboorte > Inonderzoek > Datumingangonderzoek > Maand"),
    )
    geboorte_inOnderzoek_land = ChoiceItem(
        "_embedded.geboorte._embedded.inOnderzoek.land",
        _("Geboorte > Inonderzoek > Land"),
    )
    geboorte_inOnderzoek_plaats = ChoiceItem(
        "_embedded.geboorte._embedded.inOnderzoek.plaats",
        _("Geboorte > Inonderzoek > Plaats"),
    )
    geboorte_land_code = ChoiceItem(
        "_embedded.geboorte._embedded.land.code", _("Geboorte > Land > Code")
    )
    geboorte_land_omschrijving = ChoiceItem(
        "_embedded.geboorte._embedded.land.omschrijving",
        _("Geboorte > Land > Omschrijving"),
    )
    geboorte_plaats_code = ChoiceItem(
        "_embedded.geboorte._embedded.plaats.code", _("Geboorte > Land > Code")
    )
    geboorte_plaats_omschrijving = ChoiceItem(
        "_embedded.geboorte._embedded.plaats.omschrijving",
        _("Geboorte > Land > Omschrijving"),
    )
    geheimhoudingPersoonsgegevens = ChoiceItem(
        "geheimhoudingPersoonsgegevens", _("Geheimhoudingpersoonsgegevens")
    )
    geslachtsaanduiding = ChoiceItem("geslachtsaanduiding", _("Geslachtsaanduiding"))
    gezagsverhouding_inOnderzoek_datumIngangOnderzoek_dag = ChoiceItem(
        "_embedded.gezagsverhouding._embedded.inOnderzoek._embedded.datumIngangOnderzoek.dag",
        _("Gezagsverhouding > Inonderzoek > Datumingangonderzoek > Dag"),
    )
    gezagsverhouding_inOnderzoek_datumIngangOnderzoek_datum = ChoiceItem(
        "_embedded.gezagsverhouding._embedded.inOnderzoek._embedded.datumIngangOnderzoek.datum",
        _("Gezagsverhouding > Inonderzoek > Datumingangonderzoek > Datum"),
    )
    gezagsverhouding_inOnderzoek_datumIngangOnderzoek_jaar = ChoiceItem(
        "_embedded.gezagsverhouding._embedded.inOnderzoek._embedded.datumIngangOnderzoek.jaar",
        _("Gezagsverhouding > Inonderzoek > Datumingangonderzoek > Jaar"),
    )
    gezagsverhouding_inOnderzoek_datumIngangOnderzoek_maand = ChoiceItem(
        "_embedded.gezagsverhouding._embedded.inOnderzoek._embedded.datumIngangOnderzoek.maand",
        _("Gezagsverhouding > Inonderzoek > Datumingangonderzoek > Maand"),
    )
    gezagsverhouding_inOnderzoek_indicatieCurateleRegister = ChoiceItem(
        "_embedded.gezagsverhouding._embedded.inOnderzoek.indicatieCurateleRegister",
        _("Gezagsverhouding > Inonderzoek > Indicatiecurateleregister"),
    )
    gezagsverhouding_inOnderzoek_indicatieGezagMinderjarige = ChoiceItem(
        "_embedded.gezagsverhouding._embedded.inOnderzoek.indicatieGezagMinderjarige",
        _("Gezagsverhouding > Inonderzoek > Indicatiegezagminderjarige"),
    )
    gezagsverhouding_indicatieCurateleRegister = ChoiceItem(
        "_embedded.gezagsverhouding.indicatieCurateleRegister",
        _("Gezagsverhouding > Indicatiecurateleregister"),
    )
    gezagsverhouding_indicatieGezagMinderjarige = ChoiceItem(
        "_embedded.gezagsverhouding.indicatieGezagMinderjarige",
        _("Gezagsverhouding > Indicatiegezagminderjarige"),
    )
    inOnderzoek_burgerservicenummer = ChoiceItem(
        "_embedded.inOnderzoek.burgerservicenummer",
        _("Inonderzoek > Burgerservicenummer"),
    )
    inOnderzoek_datumIngangOnderzoek_dag = ChoiceItem(
        "_embedded.inOnderzoek._embedded.datumIngangOnderzoek.dag",
        _("Inonderzoek > Datumingangonderzoek > Dag"),
    )
    inOnderzoek_datumIngangOnderzoek_datum = ChoiceItem(
        "_embedded.inOnderzoek._embedded.datumIngangOnderzoek.datum",
        _("Inonderzoek > Datumingangonderzoek > Datum"),
    )
    inOnderzoek_datumIngangOnderzoek_jaar = ChoiceItem(
        "_embedded.inOnderzoek._embedded.datumIngangOnderzoek.jaar",
        _("Inonderzoek > Datumingangonderzoek > Jaar"),
    )
    inOnderzoek_datumIngangOnderzoek_maand = ChoiceItem(
        "_embedded.inOnderzoek._embedded.datumIngangOnderzoek.maand",
        _("Inonderzoek > Datumingangonderzoek > Maand"),
    )
    inOnderzoek_geslachtsaanduiding = ChoiceItem(
        "_embedded.inOnderzoek.geslachtsaanduiding",
        _("Inonderzoek > Geslachtsaanduiding"),
    )
    kiesrecht_einddatumUitsluitingEuropeesKiesrecht_dag = ChoiceItem(
        "_embedded.kiesrecht._embedded.einddatumUitsluitingEuropeesKiesrecht.dag",
        _("Kiesrecht > Datumingangonderzoek > Dag"),
    )
    kiesrecht_einddatumUitsluitingEuropeesKiesrecht_datum = ChoiceItem(
        "_embedded.kiesrecht._embedded.einddatumUitsluitingEuropeesKiesrecht.datum",
        _("Kiesrecht > Datumingangonderzoek > Datum"),
    )
    kiesrecht_einddatumUitsluitingEuropeesKiesrecht_jaar = ChoiceItem(
        "_embedded.kiesrecht._embedded.einddatumUitsluitingEuropeesKiesrecht.jaar",
        _("Kiesrecht > Datumingangonderzoek > Jaar"),
    )
    kiesrecht_einddatumUitsluitingEuropeesKiesrecht_maand = ChoiceItem(
        "_embedded.kiesrecht._embedded.einddatumUitsluitingEuropeesKiesrecht.maand",
        _("Kiesrecht > Datumingangonderzoek > Maand"),
    )
    kiesrecht_einddatumUitsluitingKiesrecht_dag = ChoiceItem(
        "_embedded.kiesrecht._embedded.einddatumUitsluitingKiesrecht.dag",
        _("Kiesrecht > Datumingangonderzoek > Dag"),
    )
    kiesrecht_einddatumUitsluitingKiesrecht_datum = ChoiceItem(
        "_embedded.kiesrecht._embedded.einddatumUitsluitingKiesrecht.datum",
        _("Kiesrecht > Datumingangonderzoek > Datum"),
    )
    kiesrecht_einddatumUitsluitingKiesrecht_jaar = ChoiceItem(
        "_embedded.kiesrecht._embedded.einddatumUitsluitingKiesrecht.jaar",
        _("Kiesrecht > Datumingangonderzoek > Jaar"),
    )
    kiesrecht_einddatumUitsluitingKiesrecht_maand = ChoiceItem(
        "_embedded.kiesrecht._embedded.einddatumUitsluitingKiesrecht.maand",
        _("Kiesrecht > Datumingangonderzoek > Maand"),
    )
    kiesrecht_europeesKiesrecht = ChoiceItem(
        "_embedded.kiesrecht.europeesKiesrecht", _("Kiesrecht > Europeeskiesrecht")
    )
    kiesrecht_uitgeslotenVanKiesrecht = ChoiceItem(
        "_embedded.kiesrecht.uitgeslotenVanKiesrecht",
        _("Kiesrecht > Uitgeslotenvankiesrecht"),
    )
    leeftijd = ChoiceItem("leeftijd", _("Leeftijd"))
    naam_aanduidingNaamgebruik = ChoiceItem(
        "_embedded.naam.aanduidingNaamgebruik", _("Naam > Aanduidingnaamgebruik")
    )
    naam_aanhef = ChoiceItem("_embedded.naam.aanhef", _("Naam > Aanhef"))
    naam_aanschrijfwijze = ChoiceItem(
        "_embedded.naam.aanschrijfwijze", _("Naam > Aanschrijfwijze")
    )
    naam_gebruikInLopendeTekst = ChoiceItem(
        "_embedded.naam.gebruikInLopendeTekst", _("Naam > Gebruikinlopendetekst")
    )
    naam_geslachtsnaam = ChoiceItem(
        "_embedded.naam.geslachtsnaam", _("Naam > Geslachtsnaam")
    )
    naam_inOnderzoek_datumIngangOnderzoek_dag = ChoiceItem(
        "_embedded.naam._embedded.inOnderzoek._embedded.datumIngangOnderzoek.dag",
        _("Naam > Inonderzoek > Datumingangonderzoek > Dag"),
    )
    naam_inOnderzoek_datumIngangOnderzoek_datum = ChoiceItem(
        "_embedded.naam._embedded.inOnderzoek._embedded.datumIngangOnderzoek.datum",
        _("Naam > Inonderzoek > Datumingangonderzoek > Datum"),
    )
    naam_inOnderzoek_datumIngangOnderzoek_jaar = ChoiceItem(
        "_embedded.naam._embedded.inOnderzoek._embedded.datumIngangOnderzoek.jaar",
        _("Naam > Inonderzoek > Datumingangonderzoek > Jaar"),
    )
    naam_inOnderzoek_datumIngangOnderzoek_maand = ChoiceItem(
        "_embedded.naam._embedded.inOnderzoek._embedded.datumIngangOnderzoek.maand",
        _("Naam > Inonderzoek > Datumingangonderzoek > Maand"),
    )
    naam_inOnderzoek_geslachtsnaam = ChoiceItem(
        "_embedded.naam._embedded.inOnderzoek.geslachtsnaam",
        _("Naam > Inonderzoek > Geslachtsnaam"),
    )
    naam_inOnderzoek_voornamen = ChoiceItem(
        "_embedded.naam._embedded.inOnderzoek.voornamen",
        _("Naam > Inonderzoek > Voornamen"),
    )
    naam_inOnderzoek_voorvoegsel = ChoiceItem(
        "_embedded.naam._embedded.inOnderzoek.voorvoegsel",
        _("Naam > Inonderzoek > Voorvoegsel"),
    )
    naam_voorletters = ChoiceItem("_embedded.naam.voorletters", _("Naam > Voorletters"))
    naam_voornamen = ChoiceItem("_embedded.naam.voornamen", _("Naam > Voornamen"))
    naam_voorvoegsel = ChoiceItem("_embedded.naam.voorvoegsel", _("Naam > Voorvoegsel"))
    opschortingBijhouding_datum_dag = ChoiceItem(
        "_embedded.opschortingBijhouding._embedded.datum.dag",
        _("Opschortingbijhouding > Datumingangonderzoek > Dag"),
    )
    opschortingBijhouding_datum_datum = ChoiceItem(
        "_embedded.opschortingBijhouding._embedded.datum.datum",
        _("Opschortingbijhouding > Datumingangonderzoek > Datum"),
    )
    opschortingBijhouding_datum_jaar = ChoiceItem(
        "_embedded.opschortingBijhouding._embedded.datum.jaar",
        _("Opschortingbijhouding > Datumingangonderzoek > Jaar"),
    )
    opschortingBijhouding_datum_maand = ChoiceItem(
        "_embedded.opschortingBijhouding._embedded.datum.maand",
        _("Opschortingbijhouding > Datumingangonderzoek > Maand"),
    )
    opschortingBijhouding_reden = ChoiceItem(
        "_embedded.opschortingBijhouding.reden", _("Opschortingbijhouding > Reden")
    )
    overlijden_datum_dag = ChoiceItem(
        "_embedded.overlijden._embedded.datum.dag",
        _("Overlijden > Datumingangonderzoek > Dag"),
    )
    overlijden_datum_datum = ChoiceItem(
        "_embedded.overlijden._embedded.datum.datum",
        _("Overlijden > Datumingangonderzoek > Datum"),
    )
    overlijden_datum_jaar = ChoiceItem(
        "_embedded.overlijden._embedded.datum.jaar",
        _("Overlijden > Datumingangonderzoek > Jaar"),
    )
    overlijden_datum_maand = ChoiceItem(
        "_embedded.overlijden._embedded.datum.maand",
        _("Overlijden > Datumingangonderzoek > Maand"),
    )
    overlijden_inOnderzoek_datum = ChoiceItem(
        "_embedded.overlijden._embedded.inOnderzoek.datum",
        _("Overlijden > Inonderzoek > Datum"),
    )
    overlijden_inOnderzoek_datumIngangOnderzoek_dag = ChoiceItem(
        "_embedded.overlijden._embedded.inOnderzoek._embedded.datumIngangOnderzoek.dag",
        _("Overlijden > Inonderzoek > Datumingangonderzoek > Dag"),
    )
    overlijden_inOnderzoek_datumIngangOnderzoek_datum = ChoiceItem(
        "_embedded.overlijden._embedded.inOnderzoek._embedded.datumIngangOnderzoek.datum",
        _("Overlijden > Inonderzoek > Datumingangonderzoek > Datum"),
    )
    overlijden_inOnderzoek_datumIngangOnderzoek_jaar = ChoiceItem(
        "_embedded.overlijden._embedded.inOnderzoek._embedded.datumIngangOnderzoek.jaar",
        _("Overlijden > Inonderzoek > Datumingangonderzoek > Jaar"),
    )
    overlijden_inOnderzoek_datumIngangOnderzoek_maand = ChoiceItem(
        "_embedded.overlijden._embedded.inOnderzoek._embedded.datumIngangOnderzoek.maand",
        _("Overlijden > Inonderzoek > Datumingangonderzoek > Maand"),
    )
    overlijden_inOnderzoek_land = ChoiceItem(
        "_embedded.overlijden._embedded.inOnderzoek.land",
        _("Overlijden > Inonderzoek > Land"),
    )
    overlijden_inOnderzoek_plaats = ChoiceItem(
        "_embedded.overlijden._embedded.inOnderzoek.plaats",
        _("Overlijden > Inonderzoek > Plaats"),
    )
    overlijden_indicatieOverleden = ChoiceItem(
        "_embedded.overlijden.indicatieOverleden", _("Overlijden > Indicatieoverleden")
    )
    overlijden_land_code = ChoiceItem(
        "_embedded.overlijden._embedded.land.code", _("Overlijden > Land > Code")
    )
    overlijden_land_omschrijving = ChoiceItem(
        "_embedded.overlijden._embedded.land.omschrijving",
        _("Overlijden > Land > Omschrijving"),
    )
    overlijden_plaats_code = ChoiceItem(
        "_embedded.overlijden._embedded.plaats.code", _("Overlijden > Land > Code")
    )
    overlijden_plaats_omschrijving = ChoiceItem(
        "_embedded.overlijden._embedded.plaats.omschrijving",
        _("Overlijden > Land > Omschrijving"),
    )
    verblijfplaats_aanduidingBijHuisnummer = ChoiceItem(
        "_embedded.verblijfplaats.aanduidingBijHuisnummer",
        _("Verblijfplaats > Aanduidingbijhuisnummer"),
    )
    verblijfplaats_datumAanvangAdreshouding_dag = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumAanvangAdreshouding.dag",
        _("Verblijfplaats > Datumingangonderzoek > Dag"),
    )
    verblijfplaats_datumAanvangAdreshouding_datum = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumAanvangAdreshouding.datum",
        _("Verblijfplaats > Datumingangonderzoek > Datum"),
    )
    verblijfplaats_datumAanvangAdreshouding_jaar = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumAanvangAdreshouding.jaar",
        _("Verblijfplaats > Datumingangonderzoek > Jaar"),
    )
    verblijfplaats_datumAanvangAdreshouding_maand = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumAanvangAdreshouding.maand",
        _("Verblijfplaats > Datumingangonderzoek > Maand"),
    )
    verblijfplaats_datumIngangGeldigheid_dag = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumIngangGeldigheid.dag",
        _("Verblijfplaats > Datumingangonderzoek > Dag"),
    )
    verblijfplaats_datumIngangGeldigheid_datum = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumIngangGeldigheid.datum",
        _("Verblijfplaats > Datumingangonderzoek > Datum"),
    )
    verblijfplaats_datumIngangGeldigheid_jaar = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumIngangGeldigheid.jaar",
        _("Verblijfplaats > Datumingangonderzoek > Jaar"),
    )
    verblijfplaats_datumIngangGeldigheid_maand = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumIngangGeldigheid.maand",
        _("Verblijfplaats > Datumingangonderzoek > Maand"),
    )
    verblijfplaats_datumInschrijvingInGemeente_dag = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumInschrijvingInGemeente.dag",
        _("Verblijfplaats > Datumingangonderzoek > Dag"),
    )
    verblijfplaats_datumInschrijvingInGemeente_datum = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumInschrijvingInGemeente.datum",
        _("Verblijfplaats > Datumingangonderzoek > Datum"),
    )
    verblijfplaats_datumInschrijvingInGemeente_jaar = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumInschrijvingInGemeente.jaar",
        _("Verblijfplaats > Datumingangonderzoek > Jaar"),
    )
    verblijfplaats_datumInschrijvingInGemeente_maand = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumInschrijvingInGemeente.maand",
        _("Verblijfplaats > Datumingangonderzoek > Maand"),
    )
    verblijfplaats_datumVestigingInNederland_dag = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumVestigingInNederland.dag",
        _("Verblijfplaats > Datumingangonderzoek > Dag"),
    )
    verblijfplaats_datumVestigingInNederland_datum = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumVestigingInNederland.datum",
        _("Verblijfplaats > Datumingangonderzoek > Datum"),
    )
    verblijfplaats_datumVestigingInNederland_jaar = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumVestigingInNederland.jaar",
        _("Verblijfplaats > Datumingangonderzoek > Jaar"),
    )
    verblijfplaats_datumVestigingInNederland_maand = ChoiceItem(
        "_embedded.verblijfplaats._embedded.datumVestigingInNederland.maand",
        _("Verblijfplaats > Datumingangonderzoek > Maand"),
    )
    verblijfplaats_functieAdres = ChoiceItem(
        "_embedded.verblijfplaats.functieAdres", _("Verblijfplaats > Functieadres")
    )
    verblijfplaats_gemeenteVanInschrijving_code = ChoiceItem(
        "_embedded.verblijfplaats._embedded.gemeenteVanInschrijving.code",
        _("Verblijfplaats > Land > Code"),
    )
    verblijfplaats_gemeenteVanInschrijving_omschrijving = ChoiceItem(
        "_embedded.verblijfplaats._embedded.gemeenteVanInschrijving.omschrijving",
        _("Verblijfplaats > Land > Omschrijving"),
    )
    verblijfplaats_huisletter = ChoiceItem(
        "_embedded.verblijfplaats.huisletter", _("Verblijfplaats > Huisletter")
    )
    verblijfplaats_huisnummer = ChoiceItem(
        "_embedded.verblijfplaats.huisnummer", _("Verblijfplaats > Huisnummer")
    )
    verblijfplaats_huisnummertoevoeging = ChoiceItem(
        "_embedded.verblijfplaats.huisnummertoevoeging",
        _("Verblijfplaats > Huisnummertoevoeging"),
    )
    verblijfplaats_identificatiecodeAdresseerbaarObject = ChoiceItem(
        "_embedded.verblijfplaats.identificatiecodeAdresseerbaarObject",
        _("Verblijfplaats > Identificatiecodeadresseerbaarobject"),
    )
    verblijfplaats_identificatiecodeNummeraanduiding = ChoiceItem(
        "_embedded.verblijfplaats.identificatiecodeNummeraanduiding",
        _("Verblijfplaats > Identificatiecodenummeraanduiding"),
    )
    verblijfplaats_inOnderzoek_aanduidingBijHuisnummer = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.aanduidingBijHuisnummer",
        _("Verblijfplaats > Inonderzoek > Aanduidingbijhuisnummer"),
    )
    verblijfplaats_inOnderzoek_datumAanvangAdreshouding = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.datumAanvangAdreshouding",
        _("Verblijfplaats > Inonderzoek > Datumaanvangadreshouding"),
    )
    verblijfplaats_inOnderzoek_datumIngangGeldigheid = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.datumIngangGeldigheid",
        _("Verblijfplaats > Inonderzoek > Datuminganggeldigheid"),
    )
    verblijfplaats_inOnderzoek_datumIngangOnderzoek_dag = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek._embedded.datumIngangOnderzoek.dag",
        _("Verblijfplaats > Inonderzoek > Datumingangonderzoek > Dag"),
    )
    verblijfplaats_inOnderzoek_datumIngangOnderzoek_datum = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek._embedded.datumIngangOnderzoek.datum",
        _("Verblijfplaats > Inonderzoek > Datumingangonderzoek > Datum"),
    )
    verblijfplaats_inOnderzoek_datumIngangOnderzoek_jaar = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek._embedded.datumIngangOnderzoek.jaar",
        _("Verblijfplaats > Inonderzoek > Datumingangonderzoek > Jaar"),
    )
    verblijfplaats_inOnderzoek_datumIngangOnderzoek_maand = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek._embedded.datumIngangOnderzoek.maand",
        _("Verblijfplaats > Inonderzoek > Datumingangonderzoek > Maand"),
    )
    verblijfplaats_inOnderzoek_datumInschrijvingInGemeente = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.datumInschrijvingInGemeente",
        _("Verblijfplaats > Inonderzoek > Datuminschrijvingingemeente"),
    )
    verblijfplaats_inOnderzoek_datumVestigingInNederland = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.datumVestigingInNederland",
        _("Verblijfplaats > Inonderzoek > Datumvestiginginnederland"),
    )
    verblijfplaats_inOnderzoek_functieAdres = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.functieAdres",
        _("Verblijfplaats > Inonderzoek > Functieadres"),
    )
    verblijfplaats_inOnderzoek_gemeenteVanInschrijving = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.gemeenteVanInschrijving",
        _("Verblijfplaats > Inonderzoek > Gemeentevaninschrijving"),
    )
    verblijfplaats_inOnderzoek_huisletter = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.huisletter",
        _("Verblijfplaats > Inonderzoek > Huisletter"),
    )
    verblijfplaats_inOnderzoek_huisnummer = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.huisnummer",
        _("Verblijfplaats > Inonderzoek > Huisnummer"),
    )
    verblijfplaats_inOnderzoek_huisnummertoevoeging = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.huisnummertoevoeging",
        _("Verblijfplaats > Inonderzoek > Huisnummertoevoeging"),
    )
    verblijfplaats_inOnderzoek_identificatiecodeAdresseerbaarObject = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.identificatiecodeAdresseerbaarObject",
        _("Verblijfplaats > Inonderzoek > Identificatiecodeadresseerbaarobject"),
    )
    verblijfplaats_inOnderzoek_identificatiecodeNummeraanduiding = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.identificatiecodeNummeraanduiding",
        _("Verblijfplaats > Inonderzoek > Identificatiecodenummeraanduiding"),
    )
    verblijfplaats_inOnderzoek_landVanwaarIngeschreven = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.landVanwaarIngeschreven",
        _("Verblijfplaats > Inonderzoek > Landvanwaaringeschreven"),
    )
    verblijfplaats_inOnderzoek_locatiebeschrijving = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.locatiebeschrijving",
        _("Verblijfplaats > Inonderzoek > Locatiebeschrijving"),
    )
    verblijfplaats_inOnderzoek_naamOpenbareRuimte = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.naamOpenbareRuimte",
        _("Verblijfplaats > Inonderzoek > Naamopenbareruimte"),
    )
    verblijfplaats_inOnderzoek_postcode = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.postcode",
        _("Verblijfplaats > Inonderzoek > Postcode"),
    )
    verblijfplaats_inOnderzoek_straatnaam = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.straatnaam",
        _("Verblijfplaats > Inonderzoek > Straatnaam"),
    )
    verblijfplaats_inOnderzoek_verblijfBuitenland = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.verblijfBuitenland",
        _("Verblijfplaats > Inonderzoek > Verblijfbuitenland"),
    )
    verblijfplaats_inOnderzoek_woonplaatsnaam = ChoiceItem(
        "_embedded.verblijfplaats._embedded.inOnderzoek.woonplaatsnaam",
        _("Verblijfplaats > Inonderzoek > Woonplaatsnaam"),
    )
    verblijfplaats_indicatieVestigingVanuitBuitenland = ChoiceItem(
        "_embedded.verblijfplaats.indicatieVestigingVanuitBuitenland",
        _("Verblijfplaats > Indicatievestigingvanuitbuitenland"),
    )
    verblijfplaats_landVanwaarIngeschreven_code = ChoiceItem(
        "_embedded.verblijfplaats._embedded.landVanwaarIngeschreven.code",
        _("Verblijfplaats > Land > Code"),
    )
    verblijfplaats_landVanwaarIngeschreven_omschrijving = ChoiceItem(
        "_embedded.verblijfplaats._embedded.landVanwaarIngeschreven.omschrijving",
        _("Verblijfplaats > Land > Omschrijving"),
    )
    verblijfplaats_locatiebeschrijving = ChoiceItem(
        "_embedded.verblijfplaats.locatiebeschrijving",
        _("Verblijfplaats > Locatiebeschrijving"),
    )
    verblijfplaats_naamOpenbareRuimte = ChoiceItem(
        "_embedded.verblijfplaats.naamOpenbareRuimte",
        _("Verblijfplaats > Naamopenbareruimte"),
    )
    verblijfplaats_postcode = ChoiceItem(
        "_embedded.verblijfplaats.postcode", _("Verblijfplaats > Postcode")
    )
    verblijfplaats_straatnaam = ChoiceItem(
        "_embedded.verblijfplaats.straatnaam", _("Verblijfplaats > Straatnaam")
    )
    verblijfplaats_vanuitVertrokkenOnbekendWaarheen = ChoiceItem(
        "_embedded.verblijfplaats.vanuitVertrokkenOnbekendWaarheen",
        _("Verblijfplaats > Vanuitvertrokkenonbekendwaarheen"),
    )
    verblijfplaats_verblijfBuitenland_adresRegel1 = ChoiceItem(
        "_embedded.verblijfplaats._embedded.verblijfBuitenland.adresRegel1",
        _("Verblijfplaats > Verblijfbuitenland > Adresregel1"),
    )
    verblijfplaats_verblijfBuitenland_adresRegel2 = ChoiceItem(
        "_embedded.verblijfplaats._embedded.verblijfBuitenland.adresRegel2",
        _("Verblijfplaats > Verblijfbuitenland > Adresregel2"),
    )
    verblijfplaats_verblijfBuitenland_adresRegel3 = ChoiceItem(
        "_embedded.verblijfplaats._embedded.verblijfBuitenland.adresRegel3",
        _("Verblijfplaats > Verblijfbuitenland > Adresregel3"),
    )
    verblijfplaats_verblijfBuitenland_land_code = ChoiceItem(
        "_embedded.verblijfplaats._embedded.verblijfBuitenland._embedded.land.code",
        _("Verblijfplaats > Verblijfbuitenland > Land > Code"),
    )
    verblijfplaats_verblijfBuitenland_land_omschrijving = ChoiceItem(
        "_embedded.verblijfplaats._embedded.verblijfBuitenland._embedded.land.omschrijving",
        _("Verblijfplaats > Verblijfbuitenland > Land > Omschrijving"),
    )
    verblijfplaats_verblijfBuitenland_vertrokkenOnbekendWaarheen = ChoiceItem(
        "_embedded.verblijfplaats._embedded.verblijfBuitenland.vertrokkenOnbekendWaarheen",
        _("Verblijfplaats > Verblijfbuitenland > Vertrokkenonbekendwaarheen"),
    )
    verblijfplaats_woonplaatsnaam = ChoiceItem(
        "_embedded.verblijfplaats.woonplaatsnaam", _("Verblijfplaats > Woonplaatsnaam")
    )
    verblijfstitel_aanduiding_code = ChoiceItem(
        "_embedded.verblijfstitel._embedded.aanduiding.code",
        _("Verblijfstitel > Land > Code"),
    )
    verblijfstitel_aanduiding_omschrijving = ChoiceItem(
        "_embedded.verblijfstitel._embedded.aanduiding.omschrijving",
        _("Verblijfstitel > Land > Omschrijving"),
    )
    verblijfstitel_datumEinde_dag = ChoiceItem(
        "_embedded.verblijfstitel._embedded.datumEinde.dag",
        _("Verblijfstitel > Datumingangonderzoek > Dag"),
    )
    verblijfstitel_datumEinde_datum = ChoiceItem(
        "_embedded.verblijfstitel._embedded.datumEinde.datum",
        _("Verblijfstitel > Datumingangonderzoek > Datum"),
    )
    verblijfstitel_datumEinde_jaar = ChoiceItem(
        "_embedded.verblijfstitel._embedded.datumEinde.jaar",
        _("Verblijfstitel > Datumingangonderzoek > Jaar"),
    )
    verblijfstitel_datumEinde_maand = ChoiceItem(
        "_embedded.verblijfstitel._embedded.datumEinde.maand",
        _("Verblijfstitel > Datumingangonderzoek > Maand"),
    )
    verblijfstitel_datumIngang_dag = ChoiceItem(
        "_embedded.verblijfstitel._embedded.datumIngang.dag",
        _("Verblijfstitel > Datumingangonderzoek > Dag"),
    )
    verblijfstitel_datumIngang_datum = ChoiceItem(
        "_embedded.verblijfstitel._embedded.datumIngang.datum",
        _("Verblijfstitel > Datumingangonderzoek > Datum"),
    )
    verblijfstitel_datumIngang_jaar = ChoiceItem(
        "_embedded.verblijfstitel._embedded.datumIngang.jaar",
        _("Verblijfstitel > Datumingangonderzoek > Jaar"),
    )
    verblijfstitel_datumIngang_maand = ChoiceItem(
        "_embedded.verblijfstitel._embedded.datumIngang.maand",
        _("Verblijfstitel > Datumingangonderzoek > Maand"),
    )
    verblijfstitel_inOnderzoek_aanduiding = ChoiceItem(
        "_embedded.verblijfstitel._embedded.inOnderzoek.aanduiding",
        _("Verblijfstitel > Inonderzoek > Aanduiding"),
    )
    verblijfstitel_inOnderzoek_datumEinde = ChoiceItem(
        "_embedded.verblijfstitel._embedded.inOnderzoek.datumEinde",
        _("Verblijfstitel > Inonderzoek > Datumeinde"),
    )
    verblijfstitel_inOnderzoek_datumIngang = ChoiceItem(
        "_embedded.verblijfstitel._embedded.inOnderzoek.datumIngang",
        _("Verblijfstitel > Inonderzoek > Datumingang"),
    )
    verblijfstitel_inOnderzoek_datumIngangOnderzoek_dag = ChoiceItem(
        "_embedded.verblijfstitel._embedded.inOnderzoek._embedded.datumIngangOnderzoek.dag",
        _("Verblijfstitel > Inonderzoek > Datumingangonderzoek > Dag"),
    )
    verblijfstitel_inOnderzoek_datumIngangOnderzoek_datum = ChoiceItem(
        "_embedded.verblijfstitel._embedded.inOnderzoek._embedded.datumIngangOnderzoek.datum",
        _("Verblijfstitel > Inonderzoek > Datumingangonderzoek > Datum"),
    )
    verblijfstitel_inOnderzoek_datumIngangOnderzoek_jaar = ChoiceItem(
        "_embedded.verblijfstitel._embedded.inOnderzoek._embedded.datumIngangOnderzoek.jaar",
        _("Verblijfstitel > Inonderzoek > Datumingangonderzoek > Jaar"),
    )
    verblijfstitel_inOnderzoek_datumIngangOnderzoek_maand = ChoiceItem(
        "_embedded.verblijfstitel._embedded.inOnderzoek._embedded.datumIngangOnderzoek.maand",
        _("Verblijfstitel > Inonderzoek > Datumingangonderzoek > Maand"),
    )
