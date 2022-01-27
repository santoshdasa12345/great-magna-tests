@Great_Magna_Tests
@lessons-page
@allure.suite:Great_Magna_Lessons
 @Choose-the-right-funding
Feature: GreatMagna - Lessons Page

  Background:
    Given test authentication is done

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
