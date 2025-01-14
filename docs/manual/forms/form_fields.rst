.. _manual_form_fields:

================
Formulier velden
================

Alle velden in een formulier zijn van een bepaald type, het veld type.

Algemeen
========

Veel veld typen (ook wel componenten genoemd) hebben soortgelijke opties en 
functies. Hieronder staan de meest voorkomende genoemd, onderverdeeld in de
tabbladen binnen het component.

Basic
-----

* **Label**: Het label bij het veld dat zichtbaar is voor de eindgebruiker.
* **Property Name**: De interne naam van het veld. Deze naam wordt gebruikt om 
  eenduidig naar dit veld te verwijzen vanuit andere velden of in 
  :ref:`sjablonen <manual_templates>`.
* **Description**: Een optionele help tekst bij het veld.
* **Show in email**: Indien aangevinkt, dan wordt dit veld opgenomen in de 
  bevestigingse-mail naar de eindgebruiker.
* **Hidden**: Indien aangevinkt, dan is het veld onzichtbaar voor de 
  eindgebruiker. Dit kan bijvoorbeeld gebruikt worden om informatie voor in te 
  vullen en door te zetten naar achterliggende registratiesystemen. Beheerders
  kunnen de waarden van onzichtbare velden uiteraard wel zien.

Advanced
--------

* **This component should Display**: Selecteer ``True`` om het veld te tonen als
  onderstaande conditie geldt. Selecteer ``False`` om het veld juist te 
  verbergen als onderstaande conditie geldt.
* **When the form component**: Selecteer een ander veld dat een specifieke 
  waarde moet hebben om dit veld te tonen of te verbergen.
* **Has the value**: De waarde die het andere veld moet hebben om de conditie te
  laten slagen.

**Voorbeeld**

Stel er zijn 2 velden:

* Een *Radio* ``Stelling`` met als *Property Name* ``stelling``, en 3 waarden: 
  ``ja``, ``nee`` en ``anders``.
* Een *Text Field* ``Toelichting bij anders``. Dit veld wordt als volgt 
  ingesteld:

  * **This component should Display**: ``True``
  * **When the form component**: ``stelling``
  * **Has the value**: ``anders``

Er is nu een formulier gemaakt waarbij het tekstveld ``Toelichting bij anders``
alleen zichtbaar wordt indien als ``Stelling`` de waarde ``anders`` is gekozen.

.. image:: _assets/form_field_advanced_0.png
    :width: 49%

.. image:: _assets/form_field_advanced_1.png
    :width: 49%


Validation
----------

* **Required**: Indien aangevinkt dan is dit veld verplicht voor de 
  eindgebruiker.

* **Plugin**: U kunt gebruik maken van een externe plugin om een veld te 
  valideren. De waarde van het veld wordt naar de plugin gestuurd en 
  gevalideerd.

Registration
------------

* **Registration attribute**: Indien u de waarde van dit veld wilt doorzetten 
  naar het achterliggende registratie systeem, dan kunt u hier een attribuut 
  kiezen dat beschikbaar is in het achterliggende registratie systeem.


Text Field
==========

Het *Text Field* heeft de meest uitgebreide opties van alle veld typen.

Basic
-----

* **Show Character Count**: Indien aangevinkt, dan wordt een teller getoond aan
  de eindgebruiker met het aantal karakters dat is ingevuld.

Location
--------

* **Derive street name**: Indien aangevinkt, dan zal in dit veld automatisch de
  straatnaam worden ingevuld op basis van het ingevulde postcode en huisnummer.
* **Derive city**: Indien aangevinkt, dan zal in dit veld automatisch de
  stad worden ingevuld op basis van het ingevulde postcode en huisnummer.
* **Postcode component**: Selecteer het veld waarin de eindgebruiker de postcode
  zal invoeren. Dit wordt gebruikt voor het ophalen van de straatnaam en stad.
* **House number component**: Selecteer het veld waarin de eindgebruiker het
  huisnummer zal invoeren. Dit wordt gebruikt voor het ophalen van de straatnaam
  en stad.

**Voorbeeld**

Stel er zijn 4 velden:

* Een *Text Field* (of *Postcode Field*) ``Postcode``.
* Een *Text Field* ``Huisnummer``.
* Een *Text Field* ``Straat`` dat als volgt is ingesteld:

  * **Derive street name**: *Aangevinkt*
  * **Postcode component**: ``Postcode (postcode)``
  * **House number component**: ``Huisnummer (huisnummer)``

* Een *Text Field* ``Stad`` dat als volgt is ingesteld:

  * **Derive city**: *Aangevinkt*
  * **Postcode component**: ``Postcode (postcode)``
  * **House number component**: ``Huisnummer (huisnummer)``

  Er is nu een formulier gemaakt waarbij de straat en de stad automatisch worden
  ingevuld als de postcode en het huisnummer zijn ingevuld.
