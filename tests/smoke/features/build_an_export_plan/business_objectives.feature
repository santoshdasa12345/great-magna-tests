@smoke
@business-objectives-page
@allure.suite:Great_Magna_Export_Plan
Feature: GreatMagna - Business Objectives Page
   Background:
   Given test authentication is done


#
# @allure.link:XOT-1002
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to view Business Objectives pages
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#      And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click on section "Add goal" on page "Build An Export Plan - Business Objectives"
#    And "Robert" decides to enter text at "Objectives" on page "Build An Export Plan - Business Objectives"
#   And "Robert" decides to enter text at "Owner" on page "Build An Export Plan - Business Objectives"
#   And "Robert" decides to enter text at "Planned reviews" on page "Build An Export Plan - Business Objectives"
#
#
#
#
#@allure.link:XOT-1005
#   @Great_Magna_Export_Plan
# Scenario:User should be able to click lessons "Move from accidental exporting to strategic exporting" and click back link "Business Objectives"
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on section "Move from accidental exporting to strategic exporting" on page "Build An Export Plan - Business Objectives"
#     And "Robert" should be on the "LearnToExport - Move from accidental exporting to strategic exporting" page
#     And "Robert" decides to click on section "Business Objectives" on page "LearnToExport - Move from accidental exporting to strategic exporting"


#@allure.link:XOT-1006
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to view Business Objectives pages
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on section "Target market research" on page "Build An Export Plan - Business Objectives"
#
#@allure.link:XOT-1007
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to view Business Objectives pages
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Business Objectives"
#
#
# @allure.link:XOT-1002
#   @Great_Magna_Export_Plan_B_O
#  Scenario:User should be able to click on "Add goal" and enter the objectives for exporting
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#   #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#    And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" fill business objective details on page "Build An Export Plan - Business Objectives"
#          | Position | Startdate  | Enddate    | Objectives | Owner        | PlannedReviews   |
#          | 1     | 01/02/2021 | 01/02/2028 | obj1       | obj1-owner   | obj1-plannedreviews |
#          | 2     | 01/02/2021 | 01/02/2028 | obj2       | obj2-owner   | obj2-plannedreviews |
#          | 3     | 01/02/2021 | 01/02/2028 | obj3       | obj3-owner   | obj3-plannedreviews |
#          | 4     | 01/02/2021 | 01/02/2028 | obj4       | obj4-owner   | obj4-plannedreviews |
#          | 5     | 01/02/2021 | 01/02/2028 | obj5       | obj5-owner   | obj5-plannedreviews |

      @allure.link:XOT-1021
   @Great_Magna_Export_Plan
  Scenario:User should be able to "Open DataSnapshot" and select random age group and confirm

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Data Snapshot" on page "Build An Export Plan - Target Markets Research"
     #And "Robert" decides to click on section "Open" on page "Build An Export Plan - Target Markets Research"
    And "Robert" decides to select random checkbox "Age Group" on page "Build An Export Plan - Target Markets Research"

        @allure.link:XOT-1026
   @Great_Magna_Export_Plan
 Scenario:User should be able to click lesson link "Work out customer demand" and click link back to "Target Markets Research"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to click on section "Work out customer demand" on page "Build An Export Plan - Target Markets Research"
     And "Robert" should be on the "LearnToExport - Work out customer demand" page
     And "Robert" decides to click on section "Target Markets Research" on page "LearnToExport - Work out customer demand"

#  @allure.link:XOT-1017
#   @GREAT_Magna_Export_Plan
#  Scenario:User should be able to click on "Route to market" section and select random "route" and "how will you promote product"
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "Add route to market" on page "Build An Export Plan - Marketing approach"
#     And "Robert" decides to select random item for "Route to market" on page "Build An Export Plan - Marketing approach"

#    @allure.link:XOT-1017
#   @GREAT_Magna_Export_Plan
#  Scenario:User should be able to click on "No. of units and time" section and select random units and time
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#     And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to enter value in "Number of units" on page "Build An Export Plan - Costs And Pricing"
#     And "Robert" decides to select random item for "Number of units" on page "Build An Export Plan - Costs And Pricing"
#     And "Robert" decides to enter value in "Time frame" on page "Build An Export Plan - Costs And Pricing"
#     And "Robert" decides to select random item for "Time Frame" on page "Build An Export Plan - Costs And Pricing"

#      @allure.link:XOT-1002
#   @Great_Magna_Export_Plan
#  Scenario:User should be able to "select currency" and enter invoicing currency
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#   #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Build an export plan"
#    And "Robert" decides to click on section "Costs And Pricing" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Costs And Pricing"
#    And "Robert" decides to click on section "How to Manage Exchange Rates" on page "Build An Export Plan - Costs And Pricing"
#    And "Robert" should be on the "LearnToExport - How To Manage Exchange Rates" page
#    And "Robert" decides to click on section "Costs And Pricing" on page "LearnToExport - How To Manage Exchange Rates"
#    And "Robert" decides to select random item for "Select Currency" on page "Build An Export Plan - Costs And Pricing"
#    And "Robert" decides to enter value in "Gross Price per unit" on page "Build An Export Plan - Costs And Pricing"

           @beta
   @allure.link:XOT-1021
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Travel plan" and click Back button

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on element "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Back" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page
    And "Robert" decides to click on element "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "ok Button" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" Page

              @allure.link:XOT-1017
   @GREAT_Magna_Export_Plan
  Scenario:User should be able to click on "Payment methods" section and enter Notes

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select random item for "Payment Terms" on page "Build An Export Plan - Getting Paid"
     And "Robert" decides to enter text at "Payment Terms Notes" on page "Build An Export Plan - Getting Paid"

#                 @allure.link:XOT-1008
#   @Great-Magna-Export_Plan-progress-bar-test
# Scenario:User should be able to click section complete on "Business objective" page  and back to export plan dashboard
#
#Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#   And "Robert" should be on the "GreatMagna - Dashboard" Page
#   #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Build an export plan"
#   Then "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to click section complete on "Build An Export Plan - Business Objectives"
#    And "Robert" decides to click on "Build an export plan"
#    And "Robert" should be able to see progress bar for section "Business Objectives" on "Build An Export Plan - Business Objectives" page

   @allure.link:XOT-1006
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on next "Target markets research"page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Business Objectives" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click section complete on "Build An Export Plan - Business Objectives"
     And "Robert" decides to click on section "Target markets research" on page "Build An Export Plan - Business Objectives"
     And "Robert" should be on the "Build An Export Plan - Target markets research" page
