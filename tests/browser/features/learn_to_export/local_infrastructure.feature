#@lessons-page
#@allure.suite:Great_Magna_Lessons
#Feature: GreatMagna - Lessons Page
#
#  Background:
#    Given test authentication is done
#
#   @allure.link:XOT-451
#   @Great-Magna-Lessons
#  Scenario:User should be able to view lesson pages for topic "Local infrastructure" and click continue
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Learn to export"
#     And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#     And "Robert" decides to click on section "Local infrastructure" on page "LearnToExport - Identify opportunities"
##     And "Robert" decides to click on "case study" on page "LearnToExport - Local infrastructure"
##     And "Robert" decides to click on "close" on page "LearnToExport - Local infrastructure"
#     And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Local infrastructure"
###
# @allure.link:XOT-452
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "Local infrastructure" and click bottom back
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#   And "Robert" decides to click on section "Local infrastructure" on page "LearnToExport - Identify opportunities"
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Local infrastructure"
#   And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - Local infrastructure"
#
#
#   @allure.link:XOT-453
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "Local infrastructure" and click top back
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "Local infrastructure" on page "LearnToExport - Identify opportunities"
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Local infrastructure"
#    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Local infrastructure"
#
#  @allure.link:XOT-454
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson page "Local infrastructure" and click view all lessons
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "Local infrastructure" on page "LearnToExport - Identify opportunities"
#    And "Robert" decides to click on section "view all lessons" on page "LearnToExport - Local infrastructure"
