@Great_Magna_Tests
@upload-logo-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - Export plans
   Background:
   Given test authentication is done

#   @allure.link:XOT-1010
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to upload logo
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Export Plan Dashboard - Upload Logo" on page "Build An Export Plan - Export Plan Dashboard"
#     #And "Robert" decides to click on "choose file" and save continue
#
#
  @allure.link:XOT-1113
   @Great_Magna_Export_Plan_random

  Scenario:User should be able to select random export plan from the Build an export plan

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to select random export plan on page "Build An Export Plan - Export Plan"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page

  @allure.link:XOT-1113
   @Great_Magna_Export_Plan_download

  Scenario:User should be able to select random export plan from the Build an export plan and download plan from export plan dashboard

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to select random export plan on page "Build An Export Plan - Export Plan"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page
    Then "Robert" decides to click on "Download plan"

      @allure.link:XOT-1113
   @Great_Magna_Export_Plan_delete_plan

  Scenario:User should be able to select random export plan from the Build an export plan and delete plan from export plan dashboard

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to select random export plan on page "Build An Export Plan - Export Plan"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page
    Then "Robert" decides to click on "Delete plan"

  @allure.link:XOT-1113
   @Great_Magna_Export_Plan_random_1

  Scenario:User should be able to select random export plan from the dashboard

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Build an export plan"
    Then "Robert" decides to select random export plan on page "GreatMagna - Dashboard"
    And "Robert" should be on the "Build An Export Plan - Export Plan" Page

     @allure.link:XOT-1113
   @Great_Magna_Export_Plan_delete

  Scenario:User should be able to select random export plan from the dashboard

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    Then "Robert" decides to select random export plan on page "GreatMagna - Dashboard"
    And "Robert" should be on the "Build An Export Plan - Export Plan" Page
