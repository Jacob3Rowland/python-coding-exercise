from assertpy import assert_that

from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()

def test_should_return_expected_name_and_length_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)[0].length).is_equal_to(5)
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)[1].length).is_equal_to(5)
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)[0].name).is_equal_to("coconuts-00")
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)[1].name).is_equal_to("coconuts-01")
