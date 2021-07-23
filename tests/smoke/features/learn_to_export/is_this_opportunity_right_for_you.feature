@smoke
@lessons-page
@allure.suite:Great_Magna_Lessons
Feature: GreatMagna - Lessons Page
  Background:
    Given test authentication is done


   @allure.link:XOT-121
   @Great-Magna-Lessons
  Scenario:User should be able to view lesson pages for topic "Is this opportunity right for you" and click continue

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Learn to export"
     And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"
     And "Robert" decides to click on section "Is this opportunity right for you" on page "LearnToExport - Identify opportunities"
     And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Introduction to Lessons and Learning Page"

