@pixels
@invest_pixels
@allure.suite:Invest
Feature: Invest - Pixels

  Background:
    Given test authentication is done


  Scenario Outline: Pixels should be present on "Invest - <selected>" page
    Given "Robert" visits the "Invest - <selected>" page

    Then "Robert" should be on the "Invest - <selected>" page
    And following web statistics analysis or tracking elements should be present
      | Google Tag Manager             |
      | Google Tag Manager - no script |
      | UTM Cookie Domain              |
    And following web statistics analysis or tracking elements should NOT be present
      | LinkedIn tracking pixel |
      | Facebook tracking pixel |

    Examples: Various pages
      | selected                |
      | Landing                 |
      | Contact Us              |
      | How to set up in the UK |

    @stage-only
    Examples: HPO pages
      | selected                               |
#      | High productivity food production - HPO|
      | Lightweight - HPO           |
      | Rail - HPO              |

    @dev-only
    Examples: UK Setup Guides
      | selected                                                  |
      | Establish a UK business base -guide                       |
      | Get support to move your tech business to the UK - guide  |
      | Register a company in the UK - guide                     |
      | Open a UK business bank account - guide                   |
      | Access finance in the UK - guide                          |
      | Research and development support in the UK - guide        |
      | UK visas and migration - guide                            |
      | Hire skilled workers for your UK operations - guide       |
      | UK tax and incentives - guide                             |
