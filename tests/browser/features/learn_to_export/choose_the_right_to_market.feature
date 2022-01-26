@Great_Magna_Tests
@lessons-page
@allure.suite:Great_Magna_Lessons
Feature: GreatMagna - Lessons Page

 Background:
    Given test authentication is done

   @allure.link:XOT-244
   @Great-Magna-Lessons-video
 Scenario:User should be able to view Lesson page "Choose the right route to market" and watch video

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
    And "Robert" decides to click on section "Prepare to sell" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Choose the right route to market" on page "LearnToExport - Prepare to sell"
    And "Robert" should be on the "LearnToExport - Choose the right route to market" page
    And "Robert" decides to watch "32" seconds of the promotional video
    #And "Robert" closes the window with promotional video
    And "Robert" decides to click checkbox Yes and click continue on "LearnToExport - Choose the right route to market"
    And "Robert" decides to click on section "Top Back" on page "LearnToExport - Choose the right route to market"

    @allure.link:XOT-245
   @Great-Magna-Lessons-videotranscript
Scenario:User should be able to view Lesson page "Choose the right route to market" and click video transcript

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
    And "Robert" decides to click on section "Prepare to sell" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Choose the right route to market" on page "LearnToExport - Prepare to sell"
    And "Robert" decides to click on element "view transcript" on page "LearnToExport - Choose the right route to market"


    @allure.link:XOT-246
   @Great-Magna-Lessons
 Scenario:User should be able to view Lesson pages for topic "Choose the right route to market" and click view all lessons

  Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   Then "Robert" decides to click on "Learn to export"
   And "Robert" decides to click on section "Prepare to sell" on page "LearnToExport - Learn Categories"
    And "Robert" decides to click on section "Choose the right route to market" on page "LearnToExport - Prepare to sell"
#    And "Robert" decides to click on section "view all lessons" on page "LearnToExport - Choose the right route to market"

