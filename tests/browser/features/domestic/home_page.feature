@domestic
@home-page
@allure.suite:Domestic
Feature: Domestic - Home Page

  Background:
    Given test authentication is done


  @allure.link:ED-2366
  @home-page
  @sections
  Scenario: Any Exporter should see the "Beta bar, Hero, EU Exit enquiries banner, Advice, Services, Case Studies, Business is Great, Error Reporting" sections on the home page
    Given "Robert" visits the "Domestic - Home" page
    Then "Robert" should see following sections
      | Sections                 |
      | Header                   |
      | SSO links - logged out   |
      | Hero                     |
      | How DIT helps            |
      | Find new markets         |
      | Export goods from the UK |
#      | What's new               |
      | Error Reporting          |
      | Footer                   |
      | Sign in                  |


  @allure.link:ED-3014
  @video
  @advice
  @home-page_2
  @skip-in-firefox
  Scenario: Any Exporter should be able to play promotional video on the Home page
    Given "Robert" visits the "Domestic - Home" page

    When "Robert" decides to watch "7" seconds of the promotional video

    Then "Robert" should be able to watch at least first "3" seconds of the promotional video


  @allure.link:ED-3014
  @video
  @home-page_3
  @skip-in-firefox
  Scenario: Any Exporter should be able to close the window with promotional video on the Home page
    Given "Robert" visits the "Domestic - Home" page

    When "Robert" decides to watch "57" seconds of the promotional video
    And "Robert" closes the window with promotional video

    Then "Robert" should not see the window with promotional video


    @allure.link:XOT-1215
  @maddb
  @home-page_4
  @sections
  Scenario: Any Exporter should be able to get to the "Market Access Database" using link on the home page
    Given "Robert" visits the "Domestic - Home" page

    When "Robert" decides to find out more about "exporting goods from the UK"

    Then "Robert" should be on the "Market Access Database - Landing" page


  @allure.link:XOT-1217
    @markets
    @home-page_5
    @sections
    # re directing to different url view export market guides instead of markets ,its directing to dashboard
  Scenario Outline: Any Exporter should be able to get to the export markets listing using "<export market guides>" link on Home page
    Given "Robert" visits the "Domestic - Home" page

    When "Robert" decides to "<export market guides>"

    Then "Robert" should be on the "Domestic - markets listing" page

    Examples:
      | export market guides      |
      | view export market guides |
      | view all market guides    |


  @allure.link:XOT-1217
  @markets
  @home-page_6
  @sections
  Scenario: Exporters should be able to quickly filter export markets by one of the preselected sectors
    Given "Robert" visits the "Domestic - Home" page

    When "Robert" decides to use one of the "sector selector quick links"

    Then "Robert" should be on the "Domestic - filtered markets listing" page


  @allure.link:XOT-1217
  @markets
  @home-page_7
  @sections
  Scenario: Exporters should be able to filter export markets by the sector their business is in
    Given "Robert" visits the "Domestic - Home" page

    When "Robert" decides to find new markets for his business

    Then "Robert" should be on the "Domestic - filtered markets listing" page


  @allure.link:XOT-1218
  @markets
  @home-page_8
  @sections
  Scenario: Any Exporter should be able to learn what's new on our site
    Given "Robert" visits the "Domestic - Home" page

    When "Robert" decides to use one of the "what's new links"

    Then "Robert" should get to a working page

   @sections
   @sign_in_required_1
  Scenario: Visitor should able to login with learn to export section on the home page
    Given "Robert" visits the "Domestic - Home" page

    When "Robert" decides to click on "Learn to Export"

    Then "Robert" should be on the "GreatMagna - Sign Up" page
    And "Robert" decides to click on element "Sign in" on page "GreatMagna - Sign Up"
    And "Robert" visited "GreatMagna - Login" page
    And "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page

   @sections
   @sign_in_required_2
  Scenario: Visitor should able to login with where to export section on the home page
    Given "Robert" visits the "Domestic - Home" page

    When "Robert" decides to click on "Where to Export"

    Then "Robert" should be on the "GreatMagna - Sign Up" page
    And "Robert" decides to click on element "Sign in" on page "GreatMagna - Sign Up"
    And "Robert" visited "GreatMagna - Login" page
    And "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page

   @sections
   @sign_in_required_3
  Scenario: Visitor should able to login with make an export plan section on the home page
    Given "Robert" visits the "Domestic - Home" page

    When "Robert" decides to click on "Make An Export Plan"

    Then "Robert" should be on the "GreatMagna - Sign Up" page
    And "Robert" decides to click on element "Sign in" on page "GreatMagna - Sign Up"
    And "Robert" visited "GreatMagna - Login" page
    And "Robert" decides to enter email address "santoshtesting10008+888@gmail.com", password "Testing@123!" and click Login
    And "Robert" should be on the "GreatMagna - Dashboard" Page
