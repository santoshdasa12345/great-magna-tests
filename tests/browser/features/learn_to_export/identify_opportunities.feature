@Great_Magna_Tests
@lessons-page
@allure.suite:Great_Magna_Lessons
Feature: GreatMagna - Lessons Page
  Background:
    Given test authentication is done

#   @allure.link:XOT-111
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "Is this opportunity right for you" and click continue 40 times
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#   And "Robert" should be on the "GreatMagna - Dashboard" Page
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#   And "Robert" decides to click on section "Is this opportunity right for you" on page "LearnToExport - Identify opportunities"
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Is this opportunity right for you"
#   And "Robert" decides to click continue for maximum "30" times from page "LearnToExport - Is this opportunity right for you" until it reaches "managing-exchange-rates"
#


   @allure.link:XOT-112
   @Great-Magna-Lessons-progress-bar-test_2
 Scenario:User should be able to view Lesson page "Choosing the right export opportunities" and click continue and back to check the progress bar on lessons and module and lesson categories section
  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
   And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
   Then "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
   And "Robert" decides to click on section "Choosing the right export opportunities" on page "LearnToExport - Identify opportunities"
    And "Robert" decides to click checkbox Yes on "LearnToExport - Choosing the right export opportunities"
   And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - Choosing the right export opportunities"
   And "Robert" should be able to see progress bar for section "Identify opportunities" on "LearnToExport - Identify opportunities" page
   And "Robert" decides to click on section "Top Back" on page "LearnToExport - Identify opportunities"
   And "Robert" should be able to see progress bar for section "Identify opportunities" on "LearnToExport - Learn Categories" page

#      @allure.link:XOT-113
#      @beta
#       @not-test
#   @Great-Magna-Placeholder-lessons-test
# Scenario:User should be able to click on Placeholder Lesson and should not be direct to content lesson page
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#   And "Robert" should be on the "GreatMagna - Dashboard" Page
#   Then "Robert" decides to click on "Learn to export"
#   Then "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#   And "Robert" decides to click on element "Placeholder lesson" on page "LearnToExport - Identify opportunities"
#   And "Robert" decides to click on element "Back" on page "LearnToExport - Identify opportunities"
#   And "Robert" should be on the "LearnToExport - Identify opportunities" Page
#    And "Robert" decides to click on element "Placeholder lesson" on page "LearnToExport - Identify opportunities"
#     And "Robert" decides to click on element "ok Button" on page "LearnToExport - Identify opportunities"
#    And "Robert" should be on the "LearnToExport - Identify opportunities" Page

