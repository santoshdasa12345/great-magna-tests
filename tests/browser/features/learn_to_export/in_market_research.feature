@Great_Magna_Tests
@lessons-page-1
@allure.suite:Great_Magna_Lessons
Feature: GreatMagna - Lessons Page
  Background:
    Given test authentication is done

#   @allure.link:XOT-131
#   @Great-Magna-Lessons
#  Scenario:User should be able to view lesson pages for topic "In market research" and click continue
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Learn to export"
#     And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#     And "Robert" decides to click on section "In market research" on page "LearnToExport - Identify opportunities"
#     And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - In market research"
#
# @allure.link:XOT-132
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "In market research" and click bottom back
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#   And "Robert" decides to click on section "In market research" on page "LearnToExport - Identify opportunities"
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - In market research"
#   And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - In market research"
#
#
#   @allure.link:XOT-133
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "In market research" and click top back
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "In market research" on page "LearnToExport - Identify opportunities"
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - In market research"
#    And "Robert" decides to click on section "Top Back" on page "LearnToExport - In market research"
#
 @allure.link:XOT-134
   @Great-Magna-Lessons-progress-bar-test
 Scenario:User should be able to view Lesson page "In market research" and click Yes lesson complete and click back to check the progress bar on Topics , module and lessons categories section.

 Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
   And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
   Then "Robert" decides to click on "Learn to export"
   Then "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
   And "Robert" decides to click on section "In market research" on page "LearnToExport - Identify opportunities"
    And "Robert" decides to click checkbox Yes on "LearnToExport - In market research"
   And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - In market research"
   And "Robert" should be able to see progress bar for section "Identify opportunities" on "LearnToExport - Identify opportunities" page
   And "Robert" decides to click on section "Top Back" on page "LearnToExport - Identify opportunities"
   And "Robert" should be able to see progress bar for section "Identify opportunities" on "LearnToExport - Learn Categories" page

#   @allure.link:XOT-135
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "In market research" and click view all lessons
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "In market research" on page "LearnToExport - Identify opportunities"
#    And "Robert" decides to click on section "view all lessons" on page "LearnToExport - In market research"
