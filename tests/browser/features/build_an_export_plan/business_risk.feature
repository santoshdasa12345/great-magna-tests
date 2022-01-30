@Great_Magna_Tests
@business-risk-page
@Great_Magna_Export_Plan
@allure.suite:Great_Magna_Export_Plan_B_R

Feature: GreatMagna - Business Risk Page
   Background:
   Given test authentication is done

     @placeholder_test
     @skip
   @allure.link:XOT-1071
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Business Risk" Page and click back button

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
       And "Robert" decides to click on element "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Back" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page
    And "Robert" decides to click on element "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "ok Button" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page

@allure.link:XOT-1072
   @Great_Magna_Export_Plan

  Scenario:User should be able to click on Top Export plan home in Business Risk and should be on Export plan dashboard page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
  And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
  And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Top Export Plan Home" on page "Build An Export Plan - Business Risk"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

#@allure.link:XOT-1073
#  @Great_Magna_Export_Plan
#   @Great-Magna-Export_Plan-progress-bar-test
# Scenario:User should be able to click on "Download export plan" at the bottom of the page
#
#Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#   And "Robert" should be on the "GreatMagna - Dashboard" Page
#   Then "Robert" decides to click on "Build an export plan"
#   Then "Robert" decides to click on section "Business risk" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click section complete on "Build An Export Plan - Business risk"
#    And "Robert" decides to click on section "Download export plan" on page "Build An Export Plan - Business risk"


    @allure.link:XOT-1075
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home on "Travel plan" and should be on Export plan Home page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
      And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
       And "Robert" decides to click section complete on "Build An Export Plan - Business Risk"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Business Risk"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

# @allure.link:XOT-1076
#   @Great_Magna_Export_Plan_B_O_D_123_add
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to click on "Add A Risk" and enter the Risk details for exporting
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Build an export plan"
#   And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
#   And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" fill risk details on page "Build An Export Plan - Business Risk"
#          | Position | Risktext  | Contingencyplan |
#          | 1     | Risk-1 | Contingencyplan-1 |
#          | 2     | Risk-2 | Contingencyplan-2 |
#          | 3     | Risk-3 | Contingencyplan-3 |
#          | 4     | Risk-4 | Contingencyplan-4 |
#          | 5     | Risk-5 | Contingencyplan-5|

#      @allure.link:XOT-1077
#     @Great_Magna_Export_Plan
#   @Great_Magna_Export_Plan_B_O_D_123_del
#   Scenario:User should be able to delete "Add a Risk" details
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#     Then "Robert" decides to click on "Build an export plan"
#        And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
#    And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to delete risk details on page "Build An Export Plan - Business Risk"
#          | Position |
#          | 5    |
#          | 4    |
#          | 3    |
#          | 2    |
#          | 1    |
     @allure.link:XOT-1078
   @Great_Magna_Export_Plan
  Scenario:User should be able to click section complete on Business Risk page and click on dashboard should see "Business Risk" as last visited page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
       And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" should be on the "Build An Export Plan - Business Risk" Page
    And "Robert" decides to click section complete on "Build An Export Plan - Business Risk"
     And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Business Risk"
     And "Robert" should see "Business Risk" text under section "Export Plan" on page "GreatMagna - Dashboard"


#   @allure.link:XOT-1079
#   @Great_Magna_Export_Plan_B_R_1_111
#   @Great_Magna_Export_Plan_risk_educ
#     @failed_exp
#  Scenario:User should be able to click on "Add A Risk" and click on Examples and educational moment
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Build an export plan"
#    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
#     And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click on element "Add A Risk" on page "Build An Export Plan - Business Risk"
#    And "Robert" decides to click on element "Risk example" on page "Build An Export Plan - Business Risk"
#    And "Robert" decides to click on element "Risk educational" on page "Build An Export Plan - Business Risk"
#    And "Robert" decides to click on element "Risk likelihood educational" on page "Build An Export Plan - Business Risk"
#    And "Robert" decides to click on element "Risk impact educational" on page "Build An Export Plan - Business Risk"
#    And "Robert" decides to click on element "contingency plan educational" on page "Build An Export Plan - Business Risk"
#    And "Robert" decides to click on element "contingency plan example" on page "Build An Export Plan - Business Risk"

