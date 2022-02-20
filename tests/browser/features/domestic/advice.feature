@domestic
@advice
@allure.suite:Domestic
Feature: Domestic - Advice articles

  Background:
    Given test authentication is done


  @allure.link:CMS-686
  @advice_1
  @articles
  Scenario: Any Exporter should see all expected sections on "Domestic - Advice landing" page
    When "Robert" goes to the "Domestic - Advice landing" page

    Then "Robert" should see following sections
      | sections                 |
      | Header                   |
      | Hero                     |
      | Breadcrumbs              |
      | Advice & Guidance tiles  |
      | Error reporting          |
#      | Footer                   |
#      | Upskill now             |


#  @allure.link:CMS-686
#  @advice_2
#  @bug_domestic
#  @articles
#  Scenario: Any Exporter should be able to get to a list of Advice articles from the home page using link in "<specific>" section
#    Given "Robert" visits the "Domestic - Advice landing" page
#
#    When "Robert" opens any article on the list
#
#    Then "Robert" should be on the "Domestic - Advice article list" page
#    And "Robert" should see following sections
#      | sections                 |
#      | Header                   |
#      | Hero                     |
#      | Breadcrumbs              |
#      | List of articles         |
#      | Error reporting          |
##      | Footer                   |
##      | Upskill now              |
##

#  @allure.link:CMS-686
#  @advice_3
#  @bug_domestic
#  @articles
#  Scenario Outline: Any Exporter should be able to get to "<advice>" Advice article
#    Given "Robert" visits the "Domestic - <advice> - Article list" page
#
#    When "Robert" opens any article on the list
#
#    Then "Robert" should be on the "Domestic - Advice article" page
#    And "Robert" should see following sections
#      | sections        |
#      | Header          |
#      | Breadcrumbs     |
#      | Share buttons   |
#      | Article         |
#      | Error reporting |
##      | Footer          |
##      | Upskill now     |
#
#    Examples:
#      | advice                                      |
#      | Find an export market                       |
#
#    @full
#    Examples:
#      | advice                                      |
#      | Create an export plan                       |
#      | Find an export market                       |
#     | Choose a route to market                    |
#      | Get export finance                          |
#      | Manage payment for export orders            |
#      | Prepare to do business in a foreign country |
#      | Prepare for export procedures and logistics  |
#      | Sell services overseas                      |
#      | Manage risk of bribery and corruption       |

#    @bug
#    @allure.issue:TT-2311
#    @fixme
#    Examples: None of "Prepare for export procedures and logistics" pages work in Dev & Staging
#      | advice                                      |
#      | Prepare for export procedures and logistics |


#  @allure.link:CMS-686
#    @advice_4
#    @bug_domestic_advice
#    @report_1
#  Scenario: Any Exporter should be able to report a problem with Advice Article page
#    Given "Robert" is on randomly selected Advice article page
#
#    When "Robert" decides to report a problem with the page
#
#    Then "Robert" should be on the "Domestic - Feedback - contact us" page
#


  @allure.issue:CMS-1698
  @allure.link:CMS-686
  @advice_5
  @bug_domestic_no_links_international
  @breadcrumbs_1
  Scenario Outline: Any Exporter should see be to use "<breadcrumb>" breadcrumb on "Advice article" page to get to "<target>" page
    Given "Robert" is on randomly selected Advice article page

    When "Robert" decides to open "<breadcrumb>"

    Then "Robert" should be on the "Domestic - <target>" page if not be redirected to "International - Landing" page

    Examples:
      | breadcrumb   | target              |
#      | great.gov.uk | Home                |
#      | Advice       | Advice Landing      |
      | Article list | Advice article list |
