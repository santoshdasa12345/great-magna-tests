@smoke
@lessons-page
@allure.suite:Great_Magna_Lessons
Feature: GreatMagna - Lessons Page

  Background:
    Given test authentication is done


    @allure.link:XOT-644
  @Great-Magna-Lessons
 Scenario:User should be able to view Lesson pages for topic "Choose the right payment method" and click view all lessons

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Funding finance and getting paid" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Choose the right payment method" on page "LearnToExport - Funding finance and getting paid"
    And "Robert" decides to click on section "view all lessons" on page "LearnToExport - Choose the right payment method"
