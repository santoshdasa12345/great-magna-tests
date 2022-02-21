#@domestic
#@markets
#@allure.suite:Domestic
#
#Feature: Domestic - Market guides
#
#  Background:
#    Given test authentication is done
#
#  @markets_1
#  Scenario: Visitors should be able to view all available markets
#    Given "Joel" visits the "Domestic - Home" page
#
#    When "Joel" decides to find out more about "Markets"
#
#    Then "Joel" should be on the "Domestic - markets listing" page
#
#
##  @pass
##  @markets_2
##  Scenario: Visitors should be able to view market guide page
##    Given "Joel" visits the "Domestic - Markets listing" page
##
##    When "Joel" selects a random market
##
##    Then "Joel" should be on the "Domestic - Markets - Guide" page
##    And "Joel" should see following sections
##      | Sections                    |
##      | Header                      |
##      | Hero                        |
##      | Breadcrumbs                 |
##      | Description                 |
##      | Opportunities for exporters |
##      | Doing business in           |
###      | Next steps                  |
##      | Error Reporting             |
##      | Footer                      |
#
#
#
#  @markets_3
#  @failed
#  Scenario: Visitors should be able to view market guide page
#    Given "Joel" visits the "Domestic - Markets listing" page
#
#    When "Joel" selects a random market
#
#    Then "Joel" should be on the "Domestic - Markets - Guide" page
#    And "Joel" should see following sections
#      | Sections                    |
#      | Header                      |
#      | Hero                        |
#      | Breadcrumbs                 |
#      | Description                 |
#      | Opportunities for exporters |
#      | Doing business in           |
##      | Next steps                  |
##      | Next steps Staging          |
#      | Error Reporting             |
#      | Footer                      |
#
#  @markets_4
#  @bug_domestic_no_link_get_in_touch
#  Scenario Outline: Visitors which decided to "<follow up>" after they read about random market should get to "<expected>" page
#    Given "Joel" is on randomly selected Market page
#
#    When "Joel" decides to "<follow up>"
#
#    Then "Joel" should be on the "Domestic - <expected>" page
#
#    Examples: next step
#      | follow up                                    | expected       |
#      | Read more advice about doing business abroad | Advice landing |
##      | Get in touch with one of our trade advisers  | New Office Finder |
#
#
#
##    @check-duties-and-customs
##    @bug_domestic_no_check_duties_link
##    @markets_5
##  Scenario Outline: Visitors which decided to "<follow up>" after they read about random market should get to Check Duties and Customs "<country>" page
##    Given "Joel" visits the "Domestic - <country> - guide" page
##
##    When "Joel" decides to "<follow up>"
##
##    Then "Joel" should be on one of the "Check duties and customs - Search product code, Check duties and customs - Access Geo Restricted" pages
##
##    Examples: next step
##      | follow up                                               | country |
##      | Check duties and customs procedures for exporting goods | Brazil  |
##      | Check duties and customs procedures for exporting goods | Germany |
##      | Check duties and customs procedures for exporting goods | Italy   |
##      | Check duties and customs procedures for exporting goods | Japan   |
#
#
##   @markets_6
##   @get_started_markets
##  Scenario: Visitor should able to login with "get started" from the market list
##    Given "Robert" visits the "Domestic - Home" page
##
##    When "Robert" decides to click on "Markets"
##    And "Robert" decides to click on element "Get started" on page "Domestic - Markets Listing"
##
##    Then "Robert" should be on the "GreatMagna - Sign Up" page
##    And "Robert" decides to click on element "Sign in" on page "GreatMagna - Sign Up"
##    And "Robert" visited "GreatMagna - Login" page
##    And "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
##    And "Robert" should be on the "GreatMagna - Dashboard" Page
##
##   @markets_7
##   @get_started_markets
##  Scenario: Visitor should able to login with "compare now" from the market guide
##     Given "Robert" visits the "Domestic - Brazil - guide" page
##
###    When "Robert" decides to click on "Markets"
##    When "Robert" decides to click on element "Compare Now" on page "Domestic - Brazil - guide"
##
##    Then "Robert" should be on the "GreatMagna - Sign Up" page
##    And "Robert" decides to click on element "Sign in" on page "GreatMagna - Sign Up"
##    And "Robert" visited "GreatMagna - Login" page
##    And "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
##    And "Robert" should be on the "GreatMagna - Dashboard" Page
