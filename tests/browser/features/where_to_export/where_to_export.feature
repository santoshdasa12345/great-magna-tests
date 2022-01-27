@Great_Magna_Tests
@where-to-export-page
@allure.suite:Great_Magna_Export_Plan

Feature: GreatMagna - Where To Export Page

  Background:
    Given test authentication is done

  @allure.link:XOT-1021
    @Great_Magna_Export_Plan
  @wte_1
  Scenario:User should be able to "Add product"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Where To Export"
    And "Robert" decides to enter product name "Coffee" on page "WhereToExport - Compare Countries"
    And "Robert" decides to click on select and save random product options on the "WhereToExport - Compare Countries" Page
#    Examples: product name
#      | product |
#      | Coffee  |
