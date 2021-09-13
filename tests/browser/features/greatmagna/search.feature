@Great_Magna_Tests
@search-page
@allure.suite:Great_Magna_Search
Feature: Search product & country in personalisation

  Background:
    Given Test authentication is done

    @allure.link:XOT-081
   @Great-Magna-Search-1
  Scenario: New Visitor should be able to go to Dashboard page on click "Search again"
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+999888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" should be able to enter products "Vehicle"
    And "Robert" decides to click on Search again on the "GreatMagna - Dashboard" Page
    And "Robert" should be on the "GreatMagna - Dashboard" page

  @allure.link:XOT-082
   @Great-Magna-Search-2
  Scenario: Visitor should be able to Enter and Save Product
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+999888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on Product and Search again for "Vehicle" on the "GreatMagna - Dashboard" Page
    And "Robert" decides to click on select and save random product options on the "GreatMagna - Dashboard" Page


    @allure.link:XOT-083
   @Great-Magna-Search-2
  Scenario: Visitor should be able to Enter and Save Country
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+999888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to enter country name "Germany" on the "GreatMagna - Dashboard" Page


  @allure.link:XOT-084
  @Great-Magna-Search_5
 Scenario Outline: User should be able to search I want to export products in country

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+999888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" should be able to enter products "<products>" and country "<country>"
        Examples: Products and Country
         | products                 | country      |
         | Vehicle                  | India      |
#         | Leather                  | Poland       |
#         | Red Roses                | Netherlands  |
#         | Steel                    | India        |
#         | Shirt                    | South Korea  |




  @allure.link:XOT-085
  @Great-Magna-Search
  Scenario Outline: Visitor should be able to see error message on failure to enter product
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" should be able to enter products "<products>"
#    And "Robert" should be able to see error message "No results found for" on the "GreatMagna - Dashboard" Page
#    And "Robert" decides to click on "Search again"
#    Examples: Products and Country
#         | products                 | country       |
#         | @@@@@@                   | !!!!!!!       |
#         | ILoveLondonIwanttotest   | ££££££££      |
#         | 123456789                | %%%%%%%%      |
#         |           .,//           | ±±±__<>:"{}_  |
