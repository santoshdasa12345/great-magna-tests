#@Great_Magna_Tests
#@business-objectives-page
#@Great_Magna_Export_Plan
#@allure.suite:Great_Magna_Export_Plan_B_O
#Feature: GreatMagna - Business Objectives Page
#   Background:
#   Given test authentication is done
#
#   @allure.link:XOT-1051
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to view "Why you want to export" section and enter text and validate
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
#     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "Why you want to export example" on page "Build An Export Plan - Business Objectives"
#     And "Robert" decides to enter text at "Why you want to export" on page "Build An Export Plan - Business Objectives"
#     And "Robert" decides to validate entered text at "Why you want to export" on page "Build An Export Plan - Business Objectives"
#
## @bug
## @allure.link:XOT-1052
##   @Great_Magna_Export_Plan_B_O_123
##   @Great_Magna_Export_Plan
##  Scenario:User should be able to click on "Add goal" and enter the objectives for exporting
##
##    Given "Robert" visited "GreatMagna - Login" page
##    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
##    And "Robert" should be on the "GreatMagna - Dashboard" Page
##    Then "Robert" decides to click on "Build an export plan"
##   And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
##   And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
##    And "Robert" fill business objective details on page "Build An Export Plan - Business Objectives"
##          | Position | Objectives | Owner        | PlannedReviews      |
##          | 1        | obj1       | obj1-owner   | obj1-plannedreviews |
##          | 2        | obj2       | obj2-owner   | obj2-plannedreviews |
##          | 3        | obj3       | obj3-owner   | obj3-plannedreviews |
##          | 4        | obj4       | obj4-owner   | obj4-plannedreviews |
##          | 5        | obj5       | obj5-owner   | obj5-plannedreviews |
#
##   @allure.link:XOT-1053
##     @Great_Magna_Export_Plan
##   @Great_Magna_Export_Plan_B_O_D_123
##   Scenario:User should be able to delete objectives
##
##    Given "Robert" visited "GreatMagna - Login" page
##    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
##    And "Robert" should be on the "GreatMagna - Dashboard" Page
##     Then "Robert" decides to click on "Build an export plan"
##    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
##     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
##    And "Robert" decides to delete business objectives on page "Build An Export Plan - Business Objectives"
##          | Position |
##          | 5    |
##          | 4    |
##          | 3    |
##          | 2    |
#          | 1    |
#
#
#@allure.link:XOT-1054
#   @Great_Magna_Export_Plan_lesson_move_from
# Scenario:User should be able to click lessons "Move from accidental exporting to strategic exporting" and click back link "Business Objectives"
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Build an export plan"
#  And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
#  And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#  And "Robert" decides to click on element "move from accidental lesson" on page "Build An Export Plan - Business Objectives"
#  And "Robert" decides to click on section "Move from accidental exporting to strategic exporting" on page "Build An Export Plan - Business Objectives"
#     And "Robert" should be on the "LearnToExport - Move from accidental exporting to strategic exporting" page
#     And "Robert" decides to click on section "Business Objectives" on page "LearnToExport - Move from accidental exporting to strategic exporting"
#
#
#@allure.link:XOT-1055
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to click on section complete and "Target markets research link" at the bottom of the page
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Build an export plan"
#  And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
#  And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click section complete on "Build An Export Plan - Business Objectives"
#     And "Robert" decides to click on section "Target markets research" on page "Build An Export Plan - Business Objectives"
#     And "Robert" should be on the "Build An Export Plan - Target markets research" page
#
#@allure.link:XOT-1056
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to click on Export plan home and should be on Export plan Home page
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Build an export plan"
#  And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
#  And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Business Objectives"
#    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page
#
#
# @allure.link:XOT-1057
#   @Great_Magna_Export_Plan_123
#  Scenario:User should be able to click on Top Export plan home and should be on Export plan dashboard page
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Build an export plan"
#   And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
#   And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on section "Top Export Plan Home" on page "Build An Export Plan - Business Objectives"
#     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page
#
# @allure.link:XOT-1058
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to click on navigation bar and navigate to "Target Markets Research" page
#
#    Given "Robert" visited "GreatMagna - Login" page
#     When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#      And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Build an export plan"
#   And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
#   And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Business Objectives"
#     And "Robert" decides to click on element "Nav Target Markets Research" on page "Build An Export Plan - Business Objectives"
#     And "Robert" should be on the "Build An Export Plan - Target Markets Research" Page
#
##
## @allure.link:XOT-1059
##   @Great_Magna_Export_Plan_B_O_1
##   @Great_Magna_Export_Plan
##  Scenario:User should not be able to click on "Add goal" after 5 objectives for exporting
##
##    Given "Robert" visited "GreatMagna - Login" page
##    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
##    And "Robert" should be on the "GreatMagna - Dashboard" Page
##    Then "Robert" decides to click on "Build an export plan"
##   And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
##   And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
##    And "Robert" fill business objective details on page "Build An Export Plan - Business Objectives"
##          | Position | Objectives | Owner        | PlannedReviews      |
##          | 1        | obj1       | obj1-owner   | obj1-plannedreviews |
##          | 2        | obj2       | obj2-owner   | obj2-plannedreviews |
##          | 3        | obj3       | obj3-owner   | obj3-plannedreviews |
##          | 4        | obj4       | obj4-owner   | obj4-plannedreviews |
##          | 5        | obj5       | obj5-owner   | obj5-plannedreviews |
#
#
#   @allure.link:XOT-1060
#   @Great_Magna_Export_Plan_B_O_Last
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to click on "Add goal" and enter the objectives for exporting
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Build an export plan"
#    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
#     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" should be on the "Build An Export Plan - Business Objectives" Page
#   And "Robert" decides to click on element "Why you want to export example" on page "Build An Export Plan - Business Objectives"
#     And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Business Objectives"
#     And "Robert" should see "Business Objectives" text under section "Export Plan" on page "GreatMagna - Dashboard"
