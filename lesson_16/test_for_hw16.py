import pytest

from lesson_16.homework_16 import TeamLead


@pytest.mark.parametrize("attribute, expected_value", [
    ("name", "John Doe"),
    ("salary", 100000),
    ("department", "Software Development"),
    ("programming_language", "Python"),
    ("team_size", 5)
])
def test_teamlead_attributes(attribute, expected_value):
    team_lead = TeamLead("John Doe", 100000, "Software Development", "Python", 5)
    assert getattr(team_lead, attribute) == expected_value