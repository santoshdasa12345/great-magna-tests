@Great_Magna_Tests
@lessons-page
@allure.suite:Great_Magna_Lessons
 @Choose-the-right-funding
Feature: GreatMagna - Lessons Page

  Background:
    Given test authentication is done

#   @allure.link:XOT-591
#   @Great-Magna-Lessons
#  Scenario:User should be able to view lesson page "Choose the right funding" and click lesson complete and click continue
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    Then "Robert" decides to click on "Learn to export"
#     And "Robert" decides to click on section "Funding finance and getting paid" on page "LearnToExport - Learn Categories"
#     And "Robert" decides to click on section "Choose the right funding" on page "LearnToExport - Funding finance and getting paid"
##     And "Robert" decides to click on "case study" on page "LearnToExport - Choose the right route to market"
##     And "Robert" decides to click on "close" on page "LearnToExport - Choose the right route to market"
#     And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Choose the right funding"
#
# @allure.link:XOT-592
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson page "Choose the right funding" and click bottom back
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#   Then "Robert" decides to click on "Learn to export"
#    And "Robert" decides to click on section "Funding finance and getting paid" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "Choose the right funding" on page "LearnToExport - Funding finance and getting paid"
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Choose the right funding"
#    And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - Choose the right funding"
#
#
#   @allure.link:XOT-593
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson page "Choose the right funding" and click top back
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#   Then "Robert" decides to click on "Learn to export"
#    And "Robert" decides to click on section "Funding finance and getting paid" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "Choose the right funding" on page "LearnToExport - Funding finance and getting paid"
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Choose the right funding"
#    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Choose the right funding"
#
#  @allure.link:XOT-594
#  @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "Choose the right funding" and click view all lessons
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#   Then "Robert" decides to click on "Learn to export"
#    And "Robert" decides to click on section "Funding finance and getting paid" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "Choose the right funding" on page "LearnToExport - Funding finance and getting paid"
#    And "Robert" decides to click on section "view all lessons" on page "LearnToExport - Choose the right funding"

  @allure.link:XOT-595
  @Great-Magna-Lessons
 Scenario:User should be able to view Lesson pages read time on  "Choose the right funding" page

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
    And "Robert" decides to click on section "Funding finance and getting paid" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Choose the right funding" on page "LearnToExport - Funding finance and getting paid"
    And "Robert" should be able to see "read time" on page "LearnToExport - Choose the right funding"
    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Choose the right funding"
   And "Robert" should be able to see "read time" on "Choose the right funding"



   @allure.link:XOT-596
  @Great-Magna-Lessons_crfaco
 Scenario: User should be able to view the Lesson page "Choose the right funding"and click Yes and back to check the progress bar on the Dashboard page.

     Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
    And "Robert" decides to click on section "Funding finance and getting paid" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Choose the right funding" on page "LearnToExport - Funding finance and getting paid"
    And "Robert" decides to click checkbox Yes on "LearnToExport - Choose the right funding"
   And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - Choose the right funding"
   And "Robert" should be able to see progress bar for section "Identify opportunities" on "LearnToExport - Identify opportunities" page
   And "Robert" decides to click on section "Top Back" on page "LearnToExport - Identify opportunities"
   And "Robert" should be able to see progress bar for section "Identify opportunities" on "LearnToExport - Learn Categories" page
