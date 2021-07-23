@Great_Magna_Tests
@lessons-page-1
@allure.suite:Great_Magna_Lessons
Feature: GreatMagna - Lessons Page

  Background:
    Given test authentication is done
#
#   @allure.link:XOT-251
#   @Great-Magna-Lessons
#  Scenario:User should be able to view lesson pages for topic "Selling direct to your customer" and click continue
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#    Then "Robert" decides to click on "Learn to export"
#     And "Robert" decides to click on section "Prepare to sell" on page "LearnToExport - Learn Categories"
#     And "Robert" decides to click on section "Selling direct to your customer" on page "LearnToExport - Prepare to sell"
##     And "Robert" decides to click on "case study" on page "LearnToExport - Choose the right route to market"
##     And "Robert" decides to click on "close" on page "LearnToExport - Choose the right route to market"
#     And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Selling direct to your customer"
#
# @allure.link:XOT-252
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "Selling direct to your customer" and click bottom back
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Prepare to sell" on page "LearnToExport - Learn Categories"
#   And "Robert" decides to click on section "Selling direct to your customer" on page "LearnToExport - Prepare to sell"
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Selling direct to your customer"
#   And "Robert" decides to click on section "Bottom Back" on page "LearnToExport - Selling direct to your customer"
#
#
#   @allure.link:XOT-253
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "Selling direct to your customer" and click top back
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Prepare to sell" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "Selling direct to your customer" on page "LearnToExport - Prepare to sell"
#    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Selling direct to your customer"
#    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Selling direct to your customer"
#
      @allure.link:XOT-254
   @Great-Magna-Lessons-video
 Scenario:User should be able to view Lesson pages for topic "Selling direct to your customer" and watch video

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Prepare to sell" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Selling direct to your customer" on page "LearnToExport - Prepare to sell"
    And "Robert" should be on the "LearnToExport - Selling direct to your customer" page
    And "Robert" decides to watch "25" seconds of the promotional video
    #And "Robert" closes the window with promotional video
    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Selling direct to your customer"
    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Selling direct to your customer"

#    @allure.link:XOT-255
#   @Great-Magna-Lessons-videotranscript
#Scenario:User should be able to view Lesson pages for topic "Selling direct to your customer" and click video transcript
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Prepare to sell" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "Selling direct to your customer" on page "LearnToExport - Prepare to sell"
#   And "Robert" decides to click on element "view transcript" on page "LearnToExport - Selling direct to your customer"
#
#   @allure.link:XOT-256
#   @Great-Magna-Lessons
# Scenario:User should be able to view Lesson pages for topic "Selling direct to your customer" and click view all lessons
#
#  Given "Robert" visited "GreatMagna - Login" page
#   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#    #And "Robert" should be able to click on SkipWalkthrough
#   Then "Robert" decides to click on "Learn to export"
#   And "Robert" decides to click on section "Prepare to sell" on page "LearnToExport - Learn Categories"
#    And "Robert" decides to click on section "Selling direct to your customer" on page "LearnToExport - Prepare to sell"
#    And "Robert" decides to click on section "view all lessons" on page "LearnToExport - Selling direct to your customer"
#
