@invest
@hpo
@stage-only
@allure.suite:Invest
Feature: Invest - High Potential Opportunities

  Background:
    Given test authentication is done

@hpo_1
  @allure.link:TT-442
  Scenario Outline: Investors should be able to view "HPO - <selected>" page
    Given "Annette Geissinger" visits the "Invest - <selected> - HPO" page

#    When "Annette Geissinger" unfolds all elements in "proposition one" section
#    And "Annette Geissinger" unfolds all elements in "case studies" section

    Then "Annette Geissinger" should see following sections
      | Sections               |
      | Header                 |
      | Hero                   |
      | Contact us             |
#      | Proposition one        |
#      | Opportunity list       |
#      | Proposition two        |
#      | Competitive advantages |
#      | Testimonial            |  # this is not present on these 2 pages
#      | Case studies           |
      | Other opportunities    |
      | Investment contact     |
      | Success stories        |
      | Location               |
      | Growth prospects       |
      | Sector and market      |
#      | Error reporting        |
      | Footer                 |
      | Get in touch           |
    And "Annette Geissinger" should not see following section
      | section          |
#      | Breadcrumbs      |

    Examples: HPO pages
      | selected                   |
      | Chemicals in the humber     |
      | Lightweight                 |
      | Rail                        |
      | Carbon fibre in tees valley  |
      | Immersive technology         |

@hpo_2
  @allure.link:TT-442
  Scenario Outline: Investors should be able to view "HPO - <selected>" page
    Given "Annette Geissinger" visits the "Invest - <selected> - HPO" page

    Then "Annette Geissinger" should see following sections
      | Sections               |
      | Header                 |
      | Hero                   |
      | Contact us             |
#      | Proposition one        |
#      | Opportunity list       |
      | Other opportunities    |
      | Investment contact     |
      | Success stories        |
      | Location               |
      | Growth prospects       |
      | Sector and market      |
#      | Proposition two        |
#      | Competitive advantages |
#      | Testimonial            |
#      | Case studies           |
#      | Other opportunities    |
#      | Error reporting        |
      | Footer                 |
    And "Annette Geissinger" should not see following section
      | section          |
      | Breadcrumbs      |

    Examples: HPO pages
      | selected               |
      | Plant based protein products    |

@hpo_3
  @allure.link:TT-442
  @contact-us
  Scenario Outline: Investors should be able to reach "Contact us" page from "HPO - <selected>" page
    Given "Annette Geissinger" visits the "Invest - <selected> - HPO" page

    When "Annette Geissinger" decides to "Investment lead get in touch"

    Then "Annette Geissinger" should be on the "Invest - HPO Contact us" page
#    looks like this checkbox is not automatically selected
#    And "Annette Geissinger" should see that "<selected>" in the form is "selected"
    And "Annette Geissinger" should see following sections
      | sections         |
      | Form             |
      | Error reporting  |

    Examples: HPO pages
      | selected                          |
      | Hydrogen |

    @full
    Examples: HPO pages
      | selected                 |
      | Lightweight  |
      | Rail     |

@hpo_4
  @allure.link:TT-442
  @related-opportunities
  Scenario Outline: Investors should be able to view "Other investment opportunities" from "HPO - <selected>" page
    Given "Annette Geissinger" visits the "Invest - <selected> - HPO" page

    When "Annette Geissinger" decides to use "<specific> opportunity" link

    Then "Annette Geissinger" should be on the "Invest - <expected opportunity> - HPO" page

    Examples: HPO pages
      | selected                                 | specific | expected opportunity                |
      | Amids                                    | first    | Hydrogen                            |
      | Carbon fibre in tees valley              | second   | Plant based protein products        |
      | Chemicals in the humber                  | third    | Plant based protein products        |
      | Controlled environment agriculture       | fourth   | Rail                                |
      | Heat networks                            | fifth    | Chemicals in the humber             |
#      | Immersive technology                     | sixth    | Heat networks                       |
#      | Lightweight                              | seventh  | Controlled environment agriculture  |
#      | Plant based protein products             | eigth    | Wastefront recycling                |



    @full
#    Examples: HPO pages
#      | selected                          | specific | expected opportunity              |
#      | High productivity food production | second   | Rail infrastructure               |
#      | Lightweight structures            | first    | High productivity food production |
#      | Rail               | second   | Lightweight structures            |



  @allure.issue:TT-879
  @allure.link:TT-443
  @allure.issue:TT-1509
  @dev-only
      @hpo_5
  @captcha
  @contact-us
  Scenario Outline: Investors should be able to contact us via "<selected>" HPO page
    Given "Annette Geissinger" visits the "Invest - <selected> - Contact us" page

    When "Annette Geissinger" fills out and submits the form

#    Then "Annette Geissinger" should be on the "Invest - Thank you for your enquiry - Contact us" page
#    And "Annette Geissinger" should receive HPO enquiry confirmation email
#    And HPO Agent should receive HPO enquiry email from "Annette Geissinger"
#    And "Annette Geissinger" should see following sections
#      | Sections         |
#      | Confirmation     |
#      | Documents        |
##      | Error reporting  |
#
#    Examples: HPO pages
#      | selected                          |
#      | Heat networks |
#
#    @full
    Examples: HPO pages
      | selected                 |
#      | Lightweight  |
      | Rail    |
