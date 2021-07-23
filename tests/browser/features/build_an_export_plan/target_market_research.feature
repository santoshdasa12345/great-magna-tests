@Great_Magna_Tests
@target-markets-research-page
@allure.suite:Great_Magna_Export_Plan_T_M_R
@Great_Magna_Export_Plan
Feature: GreatMagna - Target Markets Research Page
   Background:
   Given test authentication is done

   @allure.link:XOT-1171
   @Great_Magna_Export_Plan
  Scenario:User should be able to "Open DataSnapshot" and select random age group and confirm

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Data Snapshot" on page "Build An Export Plan - Target Markets Research"
    And "Robert" decides to select random checkbox "Age Group" on page "Build An Export Plan - Target Markets Research"

@allure.link:XOT-1172
   @Great_Magna_Export_Plan
  Scenario:User should be able to select random age group and click confirm and verify the selected age group

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Data Snapshot" on page "Build An Export Plan - Target Markets Research"
    And "Robert" decides to select random checkbox "Age Group" on page "Build An Export Plan - Target Markets Research"
    And "Robert" decides to verify selected "Age Group" on page "Build An Export Plan - Target Markets Research"

   @allure.link:XOT-1173
   @Great_Magna_Export_Plan
  Scenario:User should be able to view "Describe the consumer demand" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Describe the consumer demand example" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to enter text at "Describe the consumer demand" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to validate entered text at "Describe the consumer demand" on page "Build An Export Plan - Target Markets Research"

@allure.link:XOT-1174
   @Great_Magna_Export_Plan
  Scenario:User should be able to view "Who are your competitors" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Who are your competitors example" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to enter text at "Who are your competitors" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to validate entered text at "Who are your competitors" on page "Build An Export Plan - Target Markets Research"



   @allure.link:XOT-1175
   @Great_Magna_Export_Plan
  Scenario:User should be able to view "What are the product trends" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "What are the product trends example" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to enter text at "What are the product trends" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to validate entered text at "What are the product trends" on page "Build An Export Plan - Target Markets Research"

   @allure.link:XOT-1176
   @Great_Magna_Export_Plan
  Scenario:User should be able to view "What’s your unique selling proposition" section and enter text and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "What’s your unique selling proposition example" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to enter text at "What’s your unique selling proposition" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to validate entered text at "What’s your unique selling proposition" on page "Build An Export Plan - Target Markets Research"

   @allure.link:XOT-1177
   @Great_Magna_Export_Plan
  Scenario:User should be able to enter price in  "What’s the average price for your product"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to enter value in "What’s the average price for your product" on page "Build An Export Plan - Target Markets Research"


   @allure.link:XOT-1178
   @Great_Magna_Export_Plan
 Scenario:User should be able to click lesson link "Work out customer demand" and click link back to "Target Markets Research"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "lesson" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to click on section "Work out customer demand" on page "Build An Export Plan - Target Markets Research"
     And "Robert" should be on the "LearnToExport - Work out customer demand" page
     And "Robert" decides to click on section "Target Markets Research" on page "LearnToExport - Work out customer demand"


   @allure.link:XOT-1179
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on page "Adapting Your Product link" at the bottom of the page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click section complete on "Build An Export Plan - Target Markets Research"
     And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Target Markets Research"
     And "Robert" should be on the "Build An Export Plan - Adapting Your Product" page

   @allure.link:XOT-1180
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home and should be on Export plan Home page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Target Markets Research"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page


   @allure.link:XOT-1181
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar and navigate to "Adapting Your Product" page

    Given "Robert" visited "GreatMagna - Login" page
     When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
     And "Robert" should be on the "GreatMagna - Dashboard" Page
     #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Target Markets Research"
     And "Robert" decides to click on element "Nav Adapting Your Product" on page "Build An Export Plan - Target Markets Research"
     And "Robert" should be on the "Build An Export Plan - Adapting Your Product" Page

@allure.link:XOT-1182
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Top Export plan home in Target Markets Research and should be on Export plan dashboard page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Top Export Plan Home" on page "Build An Export Plan - Target Markets Research"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

   @allure.link:XOT-1183
   @Great_Magna_Export_Plan_T_M_R_1
     @Great_Magna_Export_Plan
  Scenario:User should be able to enter price in  "What’s the average price for your product"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to enter value in "What’s the average price for your product" on page "Build An Export Plan - Target Markets Research"


@allure.link:XOT-1184
  @Great-Magna-Sign-Up
  @Great_Magna_Export_Plan
  Scenario Outline: New User should be able to navigate to Export Plan and click on "Target Markets Research" Page and enter "Add Product" and "Add Country"

  Given "Robert" visited "GreatMagna - Sign Up" page
  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
  Then "Robert" should be on the "GreatMagna - Dashboard" Page
  Examples: email address and password
     |      emailaddress                 | password    |
     | santoshtesting10008+xxxx@gmail.com | Testing@123!|
  And "Robert" decides to click on "Build an export plan"
  And "Robert" "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
  And "Robert" decides to enter product name "Coffee" on page "Build An Export Plan - Target Markets Research"
  And "Robert" decides to enter country name "India" on the "Build An Export Plan - Target Markets Research" page

  @allure.link:XOT-1185
   @Great_Magna_Export_Plan_117
    @Great_Magna_Export_Plan
  Scenario:User should be able to click on "What’s the average price for your product" on Target Markets Research" page and click on dashboard should see "Marketing approach" as last visited page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Target Markets Research" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" should be on the "Build An Export Plan - Target Markets Research" Page
    And "Robert" decides to enter value in "What’s the average price for your product" on page "Build An Export Plan - Target Markets Research"
   And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Target Markets Research"
     And "Robert" should see "Target Markets Research" text under section "Export Plan" on page "GreatMagna - Dashboard"
