
@Great_Magna_Tests
@lessons-page
@allure.suite:Great_Magna_Lessons
 @Choose-the-right-funding
Feature: Users should e able to seee correct case study for the selected market and products

  Background:
    Given test authentication is done

@casestudy_1
  @allure.link:TT-442
  @related-opportunities
  Scenario Outline: Investors should be able to view "Other investment opportunities" from "HPO - <selected>" page
    Given "Annette Geissinger" visits the "Learn to Export - <selected> - HPO" page

    When "Annette Geissinger" decides to use "<specific> lesson" link

    Then "Annette Geissinger" should be on the "Learn to Export - <expected casestudy> - HPO" page

    Examples: HPO pages
      | selected                                 | specific | expected casestudy               |
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

