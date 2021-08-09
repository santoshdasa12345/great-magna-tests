@Great_Magna_Tests
@funding-and-credit-page
@Great_Magna_Export_Plan
@allure.suite:Great_Magna_Export_Plan_F_A_C
Feature: GreatMagna - Funding and Credit Page

   Background:
   Given test authentication is done


   @allure.link:XOT-1111
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter "How much funding you need"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to enter value in "How much funding" on page "Build An Export Plan - Funding and Credit"


   @allure.link:XOT-1112
   @Great_Magna_Export_Plan_FUNDING
  Scenario:User should be able to click on "Add a funding option" and select random option and enter value

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Funding and Credit"
#    And "Robert" decides to click on section "Choose the right funding and Credit Options" on page "Build An Export Plan - Funding and Credit"
#    And "Robert" should be on the "LearnToExport - Choose the right funding and Credit Options" page

     And "Robert" decides to select random funding options on page "Build An Export Plan - Funding and Credit"
          | Position | Amount  |
          | 1        | 5000    |
          | 2        | 1000    |
          | 3        | 12000   |
          | 4        | 25000   |
          | 5        | 35000   |

     @allure.link:XOT-1113
   @Great_Magna_Export_Plan_FUNDING
  Scenario:User should be able to delete added funding options

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
#     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Funding and Credit"
#    And "Robert" decides to click on section "Choose the right funding and Credit Options" on page "Build An Export Plan - Funding and Credit"
#    And "Robert" should be on the "LearnToExport - Choose the right funding and Credit Options" page

     And "Robert" decides to delete funding options on page "Build An Export Plan - Funding and Credit"
          | Position |
          | 10        |
          | 8        |
          | 6        |
          | 4        |
          | 2       |



  @allure.link:XOT-1114
   @Great_Magna_Export_Plan_lesson_link
  Scenario:User should be able to click lessons link "Avoid cashflow challenges when exporting"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Funding and Credit"
     And "Robert" decides to click on section "Avoid cashflow challenges when exporting" on page "Build An Export Plan - Funding and Credit"
     And "Robert" should be on the "LearnToExport - Avoid cashflow challenges when exporting" page
     And "Robert" decides to click on section "Funding and Credit" on page "LearnToExport - Avoid cashflow challenges when exporting"

  @allure.link:XOT-1115
  @Great_Magna_Export_Plan
  Scenario:User should be able to click lessons link "Choose the right funding and credit options"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Funding and Credit"
     And "Robert" decides to click on section "Choose the right funding" on page "Build An Export Plan - Funding and Credit"
     And "Robert" should be on the "LearnToExport - Choose the right funding" page
     And "Robert" decides to click on section "Funding and Credit" on page "LearnToExport - Choose the right funding"


   @allure.link:XOT-1116
   @Great_Magna_Export_Plan
  Scenario: User should be able to click on navigation bar and navigate to "Getting Paid" page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Funding and Credit"
     And "Robert" decides to click on element "Nav Getting Paid" on page "Build An Export Plan - Funding and Credit"
     And "Robert" should be on the "Build An Export Plan - Getting paid" Page


  @allure.link:XOT-1117
  @Great_Magna_Export_Plan
  Scenario:User should be able to click on page "Getting paid link" at the bottom of the page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click section complete on "Build An Export Plan - Funding and Credit"
    And "Robert" decides to click on section "Getting Paid" on page "Build An Export Plan - Funding and Credit"
    And "Robert" should be on the "Build An Export Plan - Getting Paid" page

  @allure.link:XOT-1118
  @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home and should be on Export plan Home page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Funding and Credit"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

@allure.link:XOT-1119
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Top Export plan home in Funding and Credit and should be on Export plan dashboard page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Top Export Plan Home" on page "Build An Export Plan - Funding and Credit"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

#  @allure.link:XOT-1120
#  @Great-Magna-Sign-Up
#  Scenario Outline: New User should be able to navigate to Export Plan and click on "Travel Plan" Page and enter the "Add Product"
#
#  Given "Robert" visited "GreatMagna - Sign Up" page
#  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
#  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
#  Then "Robert" should be on the "GreatMagna - Dashboard" Page
#  Examples: email address and password
#     |      emailaddress                 | password    |
#     | santoshtesting10008+xxxx@gmail.com | Testing@123!|
#  And "Robert" decides to click on "Build an export plan"
#  And "Robert" "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
#  And "Robert" decides to enter product name "oil" on page "Build An Export Plan - Funding and Credit"
#  And "Robert" decides to enter country name "Russia" on the "Build An Export Plan - Funding and Credit" page

   @allure.link:XOT-1121
   @Great_Magna_Export_Plan_12
     @failed_14
  Scenario:User should be able to click "lesson" on Funding and Credit page and click on dashboard should see "Funding and Credit" as last visited page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Funding and Credit" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" should be on the "Build An Export Plan - Funding and Credit" Page
    And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Funding and Credit"
     And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Funding and Credit"
     And "Robert" should see "Funding and Credit" text under section "Export Plan" on page "GreatMagna - Dashboard"
