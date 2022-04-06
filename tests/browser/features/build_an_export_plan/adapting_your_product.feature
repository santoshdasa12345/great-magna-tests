@Great_Magna_Tests
@adapting-your-product-page
@Great_Magna_Export_Plan
@allure.suite:Great_Magna_Export_Plan_A_F_Y_T_M
Feature: GreatMagna - Adapting Your Product Page
   Background:
   Given test authentication is done

   @allure.link:XOT-1031
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on "Open DataSnapshot" and check whether atleast one language is present

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Open Data Snapshot" on page "Build An Export Plan - Adapting Your Product"
     #And "Robert" decides to click on element "Hide Data Snapshot" on page "Build An Export Plan - Adapting Your Product"

   @allure.link:XOT-1032
   @Great_Magna_Export_Plan_adapt
  Scenario:User should be able to click lesson link "Adapting your product or service" and click link back to "Adapting your product"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Adapting lesson" on page "Build An Export Plan - Adapting Your Product"
     And "Robert" decides to click on section "Adapting your product or service" on page "Build An Export Plan - Adapting Your Product"
     And "Robert" should be on the "LearnToExport - Adapting your product or service" page
     And "Robert" decides to click on section "Adapting Your Product" on page "LearnToExport - Adapting your product or service"


   @allure.link:XOT-1033
   @Great_Magna_Export_Plan_changing
  Scenario:User should be able to view tool tip and enter relevant text in "Changing your product to adapt to your target market"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Labelling educational" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to enter text at "Labelling" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to validate entered text at "Labelling" on page "Build An Export Plan - Adapting Your Product"

    And "Robert" decides to click on element "Packaging educational" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to enter text at "Packaging" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to validate entered text at "Packaging" on page "Build An Export Plan - Adapting Your Product"

    And "Robert" decides to click on element "Size educational" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to enter text at "Size" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to validate entered text at "Size" on page "Build An Export Plan - Adapting Your Product"

#    And "Robert" decides to click on element "Product changes to comply educational" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to enter text at "Product changes to comply" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to validate entered text at "Product changes to comply" on page "Build An Export Plan - Adapting Your Product"

    And "Robert" decides to click on element "Translations educational" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to enter text at "Translations" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to validate entered text at "Translations" on page "Build An Export Plan - Adapting Your Product"

    And "Robert" decides to enter text at "Other changes" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to validate entered text at "Other changes" on page "Build An Export Plan - Adapting Your Product"


   @allure.link:XOT-1034
   @Great_Magna_Export_Plan_comm
  Scenario:User should be able to view educational tool tip and enter relevant text in "Documents you need to provide to meet the requirements for your target market"

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on element "Certificate of origin educational" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to enter text at "Certificate of origin" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to validate entered text at "Certificate of origin" on page "Build An Export Plan - Adapting Your Product"

    And "Robert" decides to click on element "Insurance certificate educational" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to enter text at "Insurance certificate" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to validate entered text at "Insurance certificate" on page "Build An Export Plan - Adapting Your Product"

#    And "Robert" decides to click on element "Commercial invoice educational" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to enter text at "Commercial invoice" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to validate entered text at "Commercial invoice" on page "Build An Export Plan - Adapting Your Product"

    And "Robert" decides to click on element "UK customs declaration educational" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to enter text at "UK customs declaration" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to validate entered text at "UK customs declaration" on page "Build An Export Plan - Adapting Your Product"

    @allure.link:XOT-1035
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on navigation bar and navigate to "Marketing Approach" page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
     And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
      And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on element "Open Navigation" on page "Build An Export Plan - Adapting Your Product"
     And "Robert" decides to click on element "Nav Marketing Approach" on page "Build An Export Plan - Adapting Your Product"
     And "Robert" should be on the "Build An Export Plan - Marketing Approach" Page

  @allure.link:XOT-1036
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on page "Marketing approach link" at the bottom of the page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
    And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click section complete on "Build An Export Plan - Adapting Your Product"
     And "Robert" decides to click on section "Marketing approach" on page "Build An Export Plan - Adapting Your Product"
     And "Robert" should be on the "Build An Export Plan - Marketing approach" page

   @allure.link:XOT-1037
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Export plan home and should be on Export plan Home page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
     And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" decides to click on section "Export Plan Home" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page


 @allure.link:XOT-1038
   @Great_Magna_Export_Plan_add_document
  Scenario:User should be able to click on "Add another document" and enter the Document name and Notes

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
   And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
   And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" fill document details on page "Build An Export Plan - Adapting Your Product"
          | Position | DocumentName  |   Notes         |
          | 1        | Vat certif    | Vat certificate |
          | 2        | Reg Document  | Reg Document    |
          | 3        | Id Proof      | Id Proof        |
          | 4        | Address Proof | Address Proof   |
          | 5        | Packing List  | Packing List    |

#    @allure.link:XOT-1039
#   @Great_Magna_Export_Plan_del_doc
#   Scenario:User should be able to click on "Add another document" and delete the document and notes
#
#    Given "Robert" visited "GreatMagna - Login" page
#    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
#    And "Robert" should be on the "GreatMagna - Dashboard" Page
#     Then "Robert" decides to click on "Build an export plan"
#    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
#      And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
#    And "Robert" decides to delete document details on page "Build An Export Plan - Adapting Your Product"
#          | Position |
#          | 5     |
#          | 4     |
#          | 3     |
#          | 2     |
#          | 1     |

  @allure.link:XOT-1040
   @Great_Magna_Export_Plan
  Scenario:User should be able to click on Top Export plan home and should be on Export plan dashboard page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
    And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
     And "Robert" decides to click on section "Top Export Plan Home" on page "Build An Export Plan - Adapting Your Product"
     And "Robert" should be on the "Build An Export Plan - Export Plan Dashboard" page

#@allure.link:XOT-1041
#  @Great-Magna-Sign-Up
#  Scenario Outline: New User should be able to navigate to Export Plan and click on "Adapting your product" Page and enter the "Add Product" and "Add Country"
#
#  Given "Robert" visited "GreatMagna - Sign Up" page
#  When "Robert" decides to enter email address "<emailaddress>", password "<password>" and click Sign up
#  Then "Robert" should be able to see confirmation code page from email "santoshtesting10008@gmail.com", password "Testing@123!" and enter code
#  Then "Robert" should be on the "GreatMagna - Dashboard" Page
#  Examples: email address and password
#     |      emailaddress                 | password    |
#     | santoshtesting10008+xxxx@gmail.com | Testing@123!|
#  And "Robert" decides to click on "Build an export plan"
#  And "Robert" "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
#  And "Robert" decides to enter product name "Coffee" on page "Build An Export Plan - Adapting Your Product"
#  And "Robert" decides to enter country name "India" on the "Build An Export Plan - Adapting Your Product" page

     @allure.link:XOT-1042
   @Great_Magna_Export_Plan_last
  Scenario:User should be able to click on "Open DataSnapshot" on Adapting Your Product page and click on dashboard should see "Adapting Your Product" as last visited page

    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Build an export plan"
    And "Robert" decides to click on section "Exporting Plan 1" on page "Build An Export Plan - Export Plan"
    And "Robert" decides to click on section "Adapting Your Product" on page "Build An Export Plan - Export Plan Dashboard"
    And "Robert" should be on the "Build An Export Plan - Adapting Your Product" Page
    And "Robert" decides to click on element "Open Data Snapshot" on page "Build An Export Plan - Adapting Your Product"
    And "Robert" decides to click on element "Dashboard" on page "Build An Export Plan - Adapting Your Product"
#    And "Robert" should see "Adapting Your Product" text under section "Export Plan" on page "GreatMagna - Dashboard"
