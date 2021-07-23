@smoke
@about-your-business-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - About your Business Page
   Background:
   Given test authentication is done

#  @allure.link:XOT-1013
#   @GREAT_Magna_Export_Plan
#  Scenario:User should be able to enter Your product packaging section and enter text and validate
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "About your Business" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "Your product packaging example" on page "Build An Export Plan - About Your Business"
#     And "Robert" decides to enter text at "Your product packaging" on page "Build An Export Plan - About Your Business"
#     And "Robert" decides to validate entered text at "Your product packaging" on page "Build An Export Plan - About Your Business"
#


@allure.link:XOT-1015
   @GREAT_Magna_Export_Plan
  Scenario:User should be able to click on business objective next page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - About Your Business"

@allure.link:XOT-1016
   @GREAT_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - About Your Business"


  @allure.link:XOT-1017
   @GREAT_Magna_Export_Plan
  Scenario:User should be able to click on business performance section and select random turnover

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About Your Business" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select random item for "Your business performance dropdown" on page "Build An Export Plan - About Your business"

