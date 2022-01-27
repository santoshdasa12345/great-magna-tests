@Great_Magna_Tests
@about-your-business-page
@Great_Magna_Export_Plan
@allure.suite:Great_Magna_Export_Plan_A_Y_B_P
Feature: GreatMagna - About your Business Page

  Background:
    Given test authentication is done

  @allure.link:XOT-1011
  @Great_Magna_Export_Plan_A_Y_B_P_1
  @Great_Magna_Export_Plan
  Scenario:User should be able to view "How you started" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
    And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "How you started example" on page "Build An Export Plan - About Your Business"
    And "Robert" decides to click on element "How you started educational" on page "Build An Export Plan - About Your Business"
    And "Robert" decides to enter text at "How you started" on page "Build An Export Plan - About Your Business"
    And "Robert" decides to validate entered text at "How you started" on page "Build An Export Plan - About Your Business"

