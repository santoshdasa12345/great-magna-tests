@international
  @investment_atlas
  @invest
  @fas_search
@allure.link:ED-3183
@allure.link:ED-4259
@no-sso-email-verification-required
@allure.suite:International
Feature: FAS - Search

  Background:
    Given test authentication is done


  @allure.link:ED-4263
  @search
    @invest_fix_1
  Scenario Outline: Buyers should be able to find UK suppliers from "<specific> Industry"
    Given "Robert" visits the "Find a Supplier - Landing" page

    When "Robert" searches for companies using "<following>" keyword in "<specific>" sector

    Then "Robert" should be on the "Find a Supplier - search results" page
    And "Robert" should see search results filtered by "<specific>" industry
    And "Robert" should see following sections
      | Sections                    |
      | Header                      |
      | Search form                 |
      | Filters                     |
      | Results                     |
      | Subscribe for email updates |
      | Footer                      |

    Examples: Industries
      | following  | specific                               |
      | plants     | Agriculture horticulture and fisheries |
      | digital    | Creative and media                     |
      | surgery    | Healthcare and medical                 |

    @full
    Examples: Industries
      | following  | specific                               |
      | WiFi       | Security                               |
      | beer       | Food and drink                         |
      | arenas     | Global sports infrastructure           |
      | salon      | Clothing Footwear And Fashion          |


  @allure.link:ED-4263
  @search
    @invest_fix_2
  Scenario Outline: Buyers should be able to change their initial search criteria to find UK suppliers in "<other industry> Industry"
    Given "Robert" searched for companies using "<following>" keyword in "<specific>" sector

    Then "Robert" should be on the "Find a Supplier - search results" page
    And "Robert" should see search results filtered by "<specific>" industry

    When "Robert" removed previous "industries" selections
    And "Robert" fills out and submits "search form" with "captcha in dev mode" check turned "off"
      | field      | value            |
      | q          | <other keyword>  |
      | industries | <other industry> |
    Then "Robert" should be on the "Find a Supplier - search results" page
    And "Robert" should see search results filtered by "<other industry>" industry

    Examples: Industries
      | following | specific                               | other keyword | other industry                |
      | plants    | Agriculture horticulture and fisheries | food          | Food and drink                |
      | digital   | Creative and media                     | arenas        | Global sports infrastructure  |
      | surgery   | Healthcare and medical                 | salon         | Clothing Footwear And Fashion |
