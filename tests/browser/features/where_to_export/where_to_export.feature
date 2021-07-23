@Great_Magna_Tests
@where-to-export-page
@allure.suite:Great_Magna_Export_Plan

Feature: GreatMagna - Where To Export Page
   Background:
   Given test authentication is done

   @allure.link:XOT-1021
   @Great_Magna_Export_Plan
  Scenario Outline:User should be able to "Add place" and " Add Country"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Where To Export"
     And "Robert" decides to enter product name "Coffee" on page "WhereToExport - Compare Countries"
     And "Robert" decides to click on select and save random product options on the "WhereToExport - Compare Countries" Page
    Examples: product name
      | product |
      | Coffee |

   @allure.link:XOT-1022
   @Great_Magna_Export_Plan
  Scenario:User should be able to "Add a place"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Where To Export"
     And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | India       | 1 |
      | Nigeria     | 2 |
      | Indonesia   | 3 |
      | Israel      | 4 |
      | Bangladesh  | 5 |
      | Spain       | 6 |
      | Argentina   | 7 |
      | Venezuela   | 8 |
      | Germany     | 9 |
      | Italy       | 10 |

  @allure.link:XOT-1023
   @Great_Magna_Export_Plan_WTE_Default_Tab
  Scenario:User should be able to see the country and data in the table on default tab
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Kosovo       | 1 |
      | Latvia     | 2 |
      | Liechtenstein   | 3 |
      | Lithuania      | 4 |
      | Luxembourg  | 5 |
      | Malta       | 6 |
      | Monaco   | 7 |
      | Montenegro   | 8 |
      | Netherlands     | 9 |
      | North Macedonia       | 10 |
    And "Robert" should see country details on page "WhereToExport - Compare Countries"

  @allure.link:XOT-1024
   @Great_Magna_Export_Plan_WTE_Europe_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Norway       | 1 |
      | Poland     | 2 |
      | Portugal   | 3 |
      | Romania      | 4 |
      | San Marino  | 5 |
      | Serbia       | 6 |
      | Slovakia   | 7 |
      | Slovenia   | 8 |
      | Spain     | 9 |
      | Sweden       | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

      @allure.link:XOT-1025
   @Great_Magna_Export_Plan_WTE_Europe_Asiapacific_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Switzerland       | 1 |
      | Vatican City     | 2 |
      | Australia   | 3 |
      | Brunei      | 4 |
      | Cambodia  | 5 |
      | East Timor       | 6 |
      | Fiji   | 7 |
      | Indonesia   | 8 |
      | Japan     | 9 |
      | Kiribati       | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

   @allure.link:XOT-1026
   @Great_Magna_Export_Plan_WTE_Asiapacific_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Laos       | 1 |
      | Malaysia     | 2 |
      | Marshall Islands   | 3 |
      | Micronesia      | 4 |
      | Myanmar  | 5 |
      | Nauru       | 6 |
      | New Zealand   | 7 |
      | North Korea   | 8 |
      | Palau     | 9 |
      | Papua New Guinea       | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

      @allure.link:XOT-1027
   @Great_Magna_Export_Plan_WTE_Asiapacific_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Philippines       | 1 |
      | Samoa     | 2 |
      | Singapore   | 3 |
      | Solomon Islands      | 4 |
      | South korea  | 5 |
      | Thailand       | 6 |
      | Tonga   | 7 |
      | Tuvalu   | 8 |
      | Vanuatu     | 9 |
      | Vietnam      | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

   @allure.link:XOT-1028
   @Great_Magna_Export_Plan_WTE_Africa_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Algeria       | 1 |
      | Angola     | 2 |
      | Benin   | 3 |
      | Botswana      | 4 |
      | Burkina Faso  | 5 |
      | Burundi       | 6 |
      | Cameroon   | 7 |
      | Cape Verde   | 8 |
      | Central African Republic     | 9 |
      | Chad      | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

      @allure.link:XOT-1029
   @Great_Magna_Export_Plan_WTE_Africa_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Comros       | 1 |
      | Congo     | 2 |
      | Congo(Democratic Republic)   | 3 |
      | Dijibouti      | 4 |
      | Egypt  | 5 |
      | Equatorial Guinea       | 6 |
      | Eritrea   | 7 |
      | Eswatini   | 8 |
      | Ethiopia    | 9 |
      | Gabon      | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

    @allure.link:XOT-1030
   @Great_Magna_Export_Plan_WTE_Africa_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Ghana       | 1 |
      | Guinea     | 2 |
      | Guinea-Bissau   | 3 |
      | Ivory Coast      | 4 |
      | Kenya  | 5 |
      | Lesotho      | 6 |
      | Liberia   | 7 |
      | Libya   | 8 |
      | Madagascar    | 9 |
      | Malawi      | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

                  @allure.link:XOT-1031
   @Great_Magna_Export_Plan_WTE_Africa_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Mali       | 1 |
      | Mauritania     | 2 |
      | Mauritius   | 3 |
      | Morocco      | 4 |
      | Mozambique  | 5 |
      | Namibia      | 6 |
      | Niger   | 7 |
      | NIgeria   | 8 |
      | Rwanda    | 9 |
      | Sao Tome and Prinicipe      | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

    @allure.link:XOT-1032
   @Great_Magna_Export_Plan_WTE_Africa_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Senegal       | 1 |
      | Seychelles     | 2 |
      | Sierra Leone   | 3 |
      | Somalia      | 4 |
      | South Africa  | 5 |
      | South Sudan      | 6 |
      | Sudan   | 7 |
      | Tanzania   | 8 |
      | The Gambia    | 9 |
      | Togo      | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

        @allure.link:XOT-1033
   @Great_Magna_Export_Plan_WTE_Africafinal_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Tunisia       | 1 |
      | Uganda     | 2 |
      | Zambia   | 3 |
      | Zimbabwe      | 4 |
      | South Africa  | 5 |
      | South Sudan      | 6 |
      | Sudan   | 7 |
      | Tanzania   | 8 |
      | The Gambia    | 9 |
      | Togo      | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

    @allure.link:XOT-1034
   @Great_Magna_Export_Plan_WTE_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Estonia       | 1 |
      | Finland     | 2 |
      | France   | 3 |
      | Germany      | 4 |
      | Greece  | 5 |
      | Hungary       | 6 |
      | Iceland   | 7 |
      | Ireland   | 8 |
      | Israel     | 9 |
      | Italy       | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

  @allure.link:XOT-1035
   @Great_Magna_Export_Plan_WTE_D_1
  Scenario:User should be able to delete entered country details

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Albania       | 1 |
      | Andorra     | 2 |
      | Austria   | 3 |
      | Belgium      | 4 |
      | Bosnia and herzegovina  | 5 |
      | Bulgaria       | 6 |
      | Croatia   | 7 |
      | Cyprus   | 8 |
      | Czechia     | 9 |
      | Denmark       | 10 |
    And "Robert" decides to delete country details on page "WhereToExport - Compare Countries"
      | Position |
      | 10 |
      | 9 |
      | 8 |
      | 7 |
      | 6 |
      | 5 |
      | 4 |
      | 3 |
      | 2 |
      | 1 |

 @allure.link:XOT-1036
   @Great_Magna_Export_Plan_WTE_ASIA_NorthAmerica_UAE_Yemen_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Bangladesh           | 1 |
      | Bhutan               | 2 |
      | India                | 3 |
      | Maldives             | 4 |
      | Nepal                | 5 |
      | Sri Lanka            | 6 |
      | Canada               | 7 |
      | United States        | 8 |
      | United Arab Emirates | 9 |
      | Yemen                | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

   @allure.link:XOT-1037
   @Great_Magna_Export_Plan_WTE_Midlleeast_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Afghanistan          | 1 |
      | Bahrain               | 2 |
      | Iran                | 3 |
      | Iraq             | 4 |
      | Jordan                | 5 |
      | Kuwait            | 6 |
      | Lebanon              | 7 |
      | Oman        | 8 |
      | Pakistan | 9 |
      | Qatar                | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

  @allure.link:XOT-1038
   @Great_Magna_Export_Plan_WTE_Midlleeast_Latinamerica_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Saudi Arabia         | 1 |
      | Syria              | 2 |
      | Argentina                | 3 |
      | Barbados             | 4 |
      | Belize                | 5 |
      | Bolivia            | 6 |
      | Brazil              | 7 |
      | Chile        | 8 |
      | Colombia | 9 |
      | Antigua and Barbuda               | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

 @allure.link:XOT-1039
   @Great_Magna_Export_Plan_WTE_Latinamerica_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Costa rica         | 1 |
      | Cuba              | 2 |
      | Dominica                | 3 |
      | Dominican Republic             | 4 |
      | ECUADOR                | 5 |
      | El salvador            | 6 |
      | Grenada              | 7 |
      | Guatemala        | 8 |
      | Guyana | 9 |
      | Haiti              | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

    @allure.link:XOT-1040
   @Great_Magna_Export_Plan_WTE_Latinamerica_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Honduras         | 1 |
      | Jamaica              | 2 |
      | Mexico                | 3 |
      | Nicaragua             | 4 |
      | Panama                | 5 |
      | Paraguay            | 6 |
      | Peru              | 7 |
      | St kitts and Nevis        | 8 |
      | St Lucia | 9 |
      | St Vincent             | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

   @allure.link:XOT-1041
   @Great_Magna_Export_Plan_WTE_Latinamerica_easterneurope_china_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Suriname         | 1 |
      | The Bahamas              | 2 |
      | Trinidad and Tobago                | 3 |
      | Uruguay             | 4 |
      | Venezuela                | 5 |
      | Uzbekistan            | 6 |
      | Ukraine              | 7 |
      | Turkmenistan        | 8 |
      | Turkey| 9 |
      | China             | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

      @allure.link:XOT-1042
   @Great_Magna_Export_Plan_WTE_Latinamerica_easterneurope_china_ALL_Tabs
  Scenario:User should be able to see the country and data in the table in all tabs
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Armenia         | 1 |
      | Azerbaijan              | 2 |
      | Belarus                | 3 |
      | Georgia             | 4 |
      | Kazakhstan                | 5 |
      | Krygyzstan            | 6 |
      | Moldova              | 7 |
      | Mongolia        | 8 |
      | Russia| 9 |
      | Tajikistan             | 10 |
    And "Robert" should see country details on all tabs on page "WhereToExport - Compare Countries"

 @allure.link:XOT-1035
   @Great_Magna_Export_Plan_WTE_D_V
  Scenario:User should be able to validate entered country details

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Albania       | 1 |
      | Andorra     | 2 |
      | Austria   | 3 |
      | Belgium      | 4 |
      | Bosnia and herzegovina  | 5 |
      | Bulgaria       | 6 |
      | Croatia   | 7 |
      | Cyprus   | 8 |
      | Czechia     | 9 |
      | Denmark       | 10 |
    And "Robert" decides to validate entered country details and change from the list "WhereToExport - Compare Countries"

  @allure.link:XOT-1035
   @Great_Magna_Export_Plan_WTE_D_112
  Scenario:User should be not able to enter more than 10 countries

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Albania       | 1 |
      | Andorra     | 2 |
      | Austria   | 3 |
      | Belgium      | 4 |
      | Bosnia and herzegovina  | 5 |
      | Bulgaria       | 6 |
      | Croatia   | 7 |
      | Cyprus   | 8 |
      | Czechia     | 9 |
      | Denmark       | 10 |
      | Czechia       | 11 |

   @allure.link:XOT-1035
   @Great_Magna_Export_Plan_WTE_D_115
  Scenario:User should not be able to enter country name which already entered

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Albania       | 1 |
      | Albania     | 2 |
      | Italy     | 2 |
      | Austria   | 3 |
      | Germany      | 4 |
      | Germany      | 5 |
      | Bosnia and herzegovina  | 5 |
      | Bulgaria       | 6 |
      | Croatia   | 7 |
      | Cyprus   | 8 |
      | Cyprus   | 9 |
      | Czechia     | 9 |
      | Denmark       | 10 |

     @allure.link:XOT-1035
   @Great_Magna_Export_Plan_WTE_D
  Scenario:User should be able to change country name which already entered in the personalisation bar with ready to choose country list

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "5" tabs on page "WhereToExport - Compare Countries"
      | CountryName | CountryPlaceNumber |
      | Albania       | 1 |
      | Andorra     | 2 |
      | Austria   | 3 |
      | Albania      | 4 |
      | India      | 4 |
      | Bosnia and herzegovina  | 5 |
      | Bulgaria       | 6 |
      | Croatia   | 7 |
      | Cyprus   | 8 |
      | Czechia     | 9 |
      | Czechia       | 10 |
      | Denmark       | 10 |

 @allure.link:XOT-1035
   @Great_Magna_Export_Plan_WTE_Link
  Scenario:User should be able to click on Learn to export button and View your export plan button
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
    | CountryName | CountryPlaceNumber |
      | Senegal       | 1 |
      | Seychelles     | 2 |
      | Sierra Leone   | 3 |
      | Somalia      | 4 |
      | South Africa  | 5 |
      | South Sudan      | 6 |
      | Sudan   | 7 |
      | Tanzania   | 8 |
      | The Gambia    | 9 |
      | Togo      | 10 |
   And "Robert" decides to click on "Learn to Export"
   And "Robert" should be on the "LearnToExport - Learn Categories" Page
   And "Robert" should be on the "GreatMagna - Dashboard" Page
   And "Robert" decides to click on "Where To Export"
   And "Robert" decides to click on "View Your Export Plan"

    @allure.link:XOT-1035
   @Great_Magna_Export_Plan_WTE_Link_1
  Scenario:User should be able to click on Learn to export button and View your export plan button
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+9878@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter maximum "10" country names with display "3" tabs on page "WhereToExport - Compare Countries"
    | CountryName | CountryPlaceNumber |
      | Senegal       | 1 |
    And "Robert" decides to click on element "UN Comtrade" on page "WhereToExport - Compare Countries"
    And "Robert" decides to click on element "World Bank" on page "WhereToExport - Compare Countries"
    And "Robert" decides to click on element "Transparency International" on page "WhereToExport - Compare Countries"
    And "Robert" decides to click on element "World Bank" on page "WhereToExport - Compare Countries"
