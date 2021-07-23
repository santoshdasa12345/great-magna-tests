@Great_Magna_Tests
@travel-plan-page
@allure.suite:Great_Magna_Export_Plan_T_P

Feature: GreatMagna - Travel Plan Page
   Background:
   Given test authentication is done

  @allure.link:XOT-1191
  @Great_Magna_Export_Plan
  Scenario:User should be able to enter text at  "Travel Information"  and "Cultural Information"section and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "open datasnapshot" on page "Build An Export Plan - Travel Plan"
     And "Robert" decides to click on element "languages educational" on page "Build An Export Plan - Travel Plan"
     And "Robert" decides to click on element "travel information eduactional" on page "Build An Export Plan - Travel Plan"
     And "Robert" decides to enter text at "travel information" on page "Build An Export Plan - Travel Plan"
     And "Robert" decides to validate entered text at "travel information" on page "Build An Export Plan - Travel Plan"
     And "Robert" decides to enter text at "cultural information" on page "Build An Export Plan - Travel Plan"
     And "Robert" decides to validate entered text at "cultural information" on page "Build An Export Plan - Travel Plan"

   @allure.link:XOT-1192
   @Great_Magna_Export_Plan_D
  Scenario:User should be able to click on "Visa Information" and "Planned Travel" section and validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select radio button "I dont need visa" on page "Build An Export Plan - Travel Plan"
     And "Robert" decides to click on element "Planned Travel educational" on page "Build An Export Plan - Travel Plan"

   @allure.link:XOT-1193
   @Great_Magna_Export_Plan_D
  Scenario:User should be able to click on "Visa Information" and enter text adn validate

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to select radio button "I need a visa" on page "Build An Export Plan - Travel Plan"
     And "Robert" decides to enter text at "How and where" on page "Build An Export Plan - Travel Plan"
     And "Robert" decides to enter text at "How long" on page "Build An Export Plan - Travel Plan"
     And "Robert" decides to enter text at "notes" on page "Build An Export Plan - Travel Plan"

#
#
    @allure.link:XOT-1194
   @Great_Magna_Export_Plan_tp
  Scenario:User should be able to click another trip and enter trip details and delete "Trip details"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" fill trip details on page "Build An Export Plan - Travel Plan"
          | Position | TripName  |
          | 1        | Trip1- India    |
          | 3        | Trip2- Nigeria  |
          | 5        | Trip3- Ghana      |
          | 7       | Trip4- Bangladesh |
          | 9        | Trip5- Indonesia  |

  @allure.link:XOT-1195
   @Great_Magna_Export_Plan_tp
   Scenario:User should be able to delete the trip details

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
     Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to delete trip details on page "Build An Export Plan - Travel Plan"
          | Position |
          | 2     |
          | 4     |
          | 6     |
          | 8     |
          | 10     |

   @allure.link:XOT-1196
   @Great-Magna-Export_Plan-progress-bar-test
 Scenario:User should be able to click on page "Business Risk link" at the bottom of the page

Given "Robert" visited "GreatMagna - Login" page
   When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
   And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
   Then "Robert" decides to click on "Build an export plan"
   Then "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click section complete on "Build An Export Plan - Travel Plan"
    And "Robert" decides to click on section "Business Risk" on page "Build An Export Plan - Getting Paid"
    And "Robert" decides to click on "Build An Export Plan - Business Risk" page


    @allure.link:XOT-1197
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar and navigate to "Business Risk" page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Travel Plan"
     And "Robert" decides to click on element "Nav Business Risk" on page "Build An Export Plan - Travel Plan"
     And "Robert" should be on the "Build An Export Plan - Business Risk" Page


    @allure.link:XOT-1198
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home on "Travel plan" and should be on Export plan Home page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Travel plan" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Travel plan"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

@allure.link:XOT-1199
   @Great_Magna_Export_Plan_124
  Scenario:User should be able to click on Top Export plan home in Travel Plan" and should be on Export plan dashboard page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Top Export Plan Home" on page "Build An Export Plan - Travel Plan"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

@allure.link:XOT-1200
  @Great-Magna-Sign-Up
  Scenario Outline: New User should be able to navigate to Export Plan and click on "Travel Plan" Page and enter the "Add Product"

  Given "Robert" visited "GreatMagna - Sign Up" page
  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
  Then "Robert" should be on the "GreatMagna - Dashboard" Page
  Examples: email address and password
     |      emailaddress                 | password    |
     | santoshtesting10008+xxxx@gmail.com | Testing@123!|
  And "Robert" decides to click on "Build an export plan"
  And "Robert" "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
  And "Robert" decides to enter product name "Televisions" on page "Build An Export Plan - Travel Plan"
  And "Robert" decides to enter country name "Angola" on the "Build An Export Plan - Travel Plan" page


    @allure.link:XOT-1201
   @Great-Magna-Search-2
  Scenario: Visitor should be able to Enter and Save Product
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+999888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on Product and Search again for "Vehicle" on the "GreatMagna - Dashboard" Page
    And "Robert" decides to click on select and save random product options on the "GreatMagna - Dashboard" Page

 @allure.link:XOT-1202
   @Great_Magna_Export_Plan_118
  Scenario:User should be able to click on "Export Plan Home" on Travel Plan page and click on dashboard should see "Marketing approach" as last visited page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
   #And "Robert" should be able to click on SkipWalkthrough
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Travel Plan" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" should be on the "Build An Export Plan - Travel Plan" Page
    And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Travel plan"
   And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Travel Plan"
     And "Robert" should see "Travel Plan" text under section "Export Plan" on page "GreatMagna - Dashboard"
