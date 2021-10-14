@lessons-landing-page
@allure.suite:Great_Magna_Lessons_Landing
Feature: GreatMagna - Lessons Page

  Background:
    Given test authentication is done
  @learn_to_export
  @learn_categories_landing

  Scenario: Any Exporter should be able to get to a list of Advice articles from the home page using link in "<specific>" section
   Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Learn to export"

#    And "Robert" decides to click on section "Get Started" on page "LearnToExport - Learn Categories"

    And "Robert" should see following sections
      | sections                 |
      | Header                   |
      | Export academy           |
      | Learn categories         |
      | Footer                   |


  @learn_to_export
  @get_started_landing

  Scenario: Any Exporter should be able to get to a list of Advice articles from the home page using link in "<specific>" section
   Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Learn to export"

    And "Robert" decides to click on section "Get Started" on page "LearnToExport - Learn Categories"

    And "Robert" should see following sections
      | sections                 |
      | Header                   |
      | Learn to export home          |
      | Topic Title        |
      | Lessons       |
      | Footer           |


      @learn_to_export
  @identify_opportunities_landing

  Scenario: Any Exporter should be able to get to a list of Advice articles from the home page using link in "<specific>" section
   Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Learn to export"

   And "Robert" decides to click on section "Identify opportunities" on page "LearnToExport - Learn Categories"

    And "Robert" should see following sections
      | sections                 |
      | Header                   |
      | Learn to export home          |
      | Topic Title        |
      | Lessons       |
      | Footer           |


 @learn_to_export
  @prepare_to_sell_landing

  Scenario: Any Exporter should be able to get to a list of Advice articles from the home page using link in "<specific>" section
   Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Learn to export"

   And "Robert" decides to click on section "Prepare to sell" on page "LearnToExport - Learn Categories"

    And "Robert" should see following sections
      | sections                 |
      | Header                   |
      | Learn to export home          |
      | Topic Title        |
      | Lessons       |
      | Footer           |

  @learn_to_export
  @regulations_licensing_and_logistics_landing

  Scenario: Any Exporter should be able to get to a list of Advice articles from the home page using link in "<specific>" section
   Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Learn to export"

   And "Robert" decides to click on section "Regulations licensing and logistics" on page "LearnToExport - Learn Categories"

    And "Robert" should see following sections
      | sections                 |
      | Header                   |
      | Learn to export home          |
      | Topic Title        |
      | Lessons       |
      | Footer           |


    @learn_to_export
  @funding_finance_and_getting_paid_landing

  Scenario: Any Exporter should be able to get to a list of Advice articles from the home page using link in "<specific>" section
   Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Learn to export"

   And "Robert" decides to click on section "Funding finance and getting paid" on page "LearnToExport - Learn Categories"

    And "Robert" should see following sections
      | sections                 |
      | Header                   |
      | Learn to export home          |
      | Topic Title        |
      | Lessons       |
      | Footer           |


  @landing-page
  @<specific>
    @cheese_india
  Scenario Outline: Visitors should be able to find out more about "<specific topic>" and get to "<expected>" page
    Given "Robert" visited "GreatMagna - Login" page
    When "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
    Then "Robert" decides to click on "Learn to export"

    Given "Robert" visits the "Invest - landing" page

    When "Robert" decides to find out more about "<specific topic>"

    Then "Robert" should be on the "<expected>" page

    Examples:
      | specific topic          | expected                         |
      | Choose the right export opportunities                | How a dairy company adapts its cheese for the Chinese market - landing                 |
      | Move from accidental to strategic exporting | How a dairy company adapts its cheese for the Chinese market - How to set up in the UK |
      | Find a UK specialist    | ISD - Landing                    |
      | How we help             | Invest - How we help you expand  |
      | Contact us              | Invest - Contact us              |
