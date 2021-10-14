@Great_Magna_Tests
@lessons-page
@allure.suite:Great_Magna_Lessons
Feature: GreatMagna - Lessons Page
  Background:
    Given test authentication is done


#   @allure.link:XOT-121
#   @Great-Magna-Lessons
#  Scenario:User should be able to view lesson pages for topic "Move from accidental exporting to strategic exporting" and click continue
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Learn to export"
#     And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#     And "Robert" decides to click on section "Move from accidental exporting to strategic exporting" on page "LearnToExport - Identify opportunities"
#     And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Move from accidental exporting to strategic exporting"
#
# @allure.link:XOT-122
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "Move from accidental exporting to strategic exporting" and click bottom back
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#   And "Robert" decides to click on section "Move from accidental exporting to strategic exporting" on page "LearnToExport - Identify opportunities"
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Move from accidental exporting to strategic exporting"
#   And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - Move from accidental exporting to strategic exporting"
#
#
#   @allure.link:XOT-123
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "Move from accidental exporting to strategic exporting" and click top back
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "Move from accidental exporting to strategic exporting" on page "LearnToExport - Identify opportunities"
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Move from accidental exporting to strategic exporting"
#    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Move from accidental exporting to strategic exporting"


   @allure.link:XOT-124
   @Great-Magna-Lessons-progress-bar-test
 Scenario:User should be able to view Lesson page "Move from accidental exporting to strategic exporting" and click Yes and back to check the progress bar on lessons and module and lesson categories section

Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
   And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
   Then "Robert" decides to click on "Learn to export"
   Then "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
   And "Robert" decides to click on section "Move from accidental exporting to strategic exporting" on page "LearnToExport - Identify opportunities"
    And "Robert" decides to click checkbox Yes on "LearnToExport - Move from accidental exporting to strategic exporting"
   And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - Move from accidental exporting to strategic exporting"
   And "Robert" should be able to see progress bar for section "Identify opportunities" on "LearnToExport - Identify opportunities" page
   And "Robert" decides to click on section "Top Back" on page "LearnToExport - Identify opportunities"
   And "Robert" should be able to see progress bar for section "Identify opportunities" on "LearnToExport - Learn Categories" page

#   @allure.link:XOT-124
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson page "Move from accidental exporting to strategic exporting" and click view all lessons
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "Move from accidental exporting to strategic exporting" on page "LearnToExport - Identify opportunities"
#    And "Robert" decides to click on section "view all lessons" on page "LearnToExport - Move from accidental exporting to strategic exporting"


# @allure.link:XOT-031
#  @Great-Magna-Sign-Up_les
#  Scenario Outline: New User should be able to navigate to "Learn to Export" and click on "Learn Categories" Page and enter the "Add Product" and "Add Country"
#
#  Given "Robert" visited "GreatMagna - Sign Up" page
#  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
#  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
#  Then "Robert" should be on the "GreatMagna - Dashboard" Page
#  Examples: email address and password
#     |      emailaddress                 | password    |
#     | santoshtesting10008+xxxx@gmail.com | Testing@123!|
#  And "Robert" decides to click on "Learn to export"
#  And "Robert" "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#  And "Robert" decides to enter product name "Vehicle" on page "Build An Export Plan - Travel Plan"
#  And "Robert" decides to enter country name "Germany" on the "Build An Export Plan - Travel Plan" page
#
#  And "Robert" decides to click on "Open case study"

#   @allure.link:XOT-125
#   @Great-Magna-Lessons_case
# Scenario:User should be able to open Case study
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
##    And "Robert" should be able to enter products "<products>" and country "<country>"
#        Examples: Products and Country
#         | products                 | country        |
#         | Precious stone           | United States  |
#         | Organic Chemicals        | Japan          |
#         | Crude oil                | Germany        |
#         | Land vehicle             | Ireland        |
#
#      Then "Robert" decides to "open case study" :in "<lesson>"
#
#
#    Examples:
#      | lesson                   | specific                       |
#      | Create a business profile | Find a Buyer - Home            |
#      | Find online marketplaces  | Selling online overseas - Home |
#      | Find export opportunities | Export Opportunities - Home    |
#      | UK Export Finance         | Domestic - Get Finance         |
#      | Find events and visits    | Events - Home                  |
#      | Get an EORI number        | EORI - Home                    |
#   Then "Robert" decides to click on "Learn to export"
#    And "Robert" decides to click on section "Is this opportunity right for you" on page "LearnToExport - Identify opportunities"
#     And "Robert" decides to click open "case study" in all lessons "50" times from page "LearnToExport - Is this opportunity right for you" until it reaches "managing-exchange-rates"
#    And "Robert" decides to click continue for maximum "50" times from page "LearnToExport - Is this opportunity right for you" until it reaches "managing-exchange-rates"
