from met_icon_search import met_icon_search
import pytest
s = met_icon_search.SearchMET()
def test_MET():
    assert s!= None

def test_MET_images():
    assert len(s.cropped_images()) <= 10
