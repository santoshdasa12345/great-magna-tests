@smoke
@search-page
@allure.suite:Great_Magna_Search
Feature: Search product & country in personalisation

  Background:
    Given Test authentication is done

  @allure.link:XOT-081
  @Great-Magna-Search-1
 Scenario Outline: User should be able to search I want to export products in country

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" should be able to enter products "<products>" and country "<country>"
        Examples: Products and Country
         | products                 | country      |
         | Vehicle                  | India      |



