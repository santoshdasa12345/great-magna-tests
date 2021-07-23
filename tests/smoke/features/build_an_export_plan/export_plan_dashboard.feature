@smoke
@export-plan-dashboard-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - Export plan Upload logo
   Background:
   Given test authentication is done

   @allure.link:XOT-1010
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "About your business" page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+889@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "About your business" on page "Build An Export Plan - Export Plan Dashboard"


