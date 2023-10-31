from pytest_mock import MockerFixture
from unittest.mock import MagicMock, patch, Mock
import unittest
import pytest
from pathlib import Path

from src.etc.paths import ROOT
from src.modes.show_mode import ShowMode
from src.modes import show_mode


@pytest.fixture
def mock_bm_data() -> dict[str, dict|str|int]:
    return {
         "children": [ {
            "children": [ {
               "date_added": "13286469372158655",
               "date_last_used": "0",
               "guid": "5cf3f4a9-f13c-4ff2-b8ee-c007b1c66212",
               "id": "6",
               "name": "uBlock Origin - Chrome Web Store",
               "type": "url",
               "url": "https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm?hl=de"
            }, {
               "date_added": "13339372445585162",
               "date_last_used": "13343130068115136",
               "guid": "d628d4d7-4f41-4184-8817-7c7f938978c4",
               "id": "262",
               "meta_info": {
                  "power_bookmark_meta": ""
               },
               "name": "Jack & Jones 5 PACK - Boxershorts - dark grey melange/dunkelgrau - Zalando.de",
               "type": "url",
               "url": "https://www.zalando.de/jack-and-jones-5-pack-boxershorts-dark-grey-melange-ja282o05n-c11.html"
            }, {
               "children": [ {
                  "date_added": "13317125211981993",
                  "date_last_used": "0",
                  "guid": "ecad546b-453e-43c9-850a-5b0565ecfa2b",
                  "id": "208",
                  "meta_info": {
                     "power_bookmark_meta": ""
                  },
                  "name": "Internet langsam: Preisminderung durch neues Gesetz - Finanztip",
                  "type": "url",
                  "url": "https://www.finanztip.de/internetanbieter/internet-langsam/"
               }, {
                  "date_added": "13343130130480940",
                  "date_last_used": "0",
                  "guid": "544b46f1-51e6-41a9-9b79-c6575dbfc5f5",
                  "id": "274",
                  "meta_info": {
                     "power_bookmark_meta": ""
                  },
                  "name": "test",
                  "type": "url",
                  "url": "https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary"
               } ],
               "date_added": "13343130119158103",
               "date_last_used": "0",
               "date_modified": "13343130130480940",
               "guid": "14224669-ea31-4003-be9d-f620b601e898",
               "id": "273",
               "name": "Internet",
               "type": "folder"
            } ],
            "date_added": "13306397684547033",
            "date_last_used": "0",
            "date_modified": "13343130119158221",
            "guid": "830b21df-18fc-41df-872d-3e73a6cf1edd",
            "id": "5",
            "name": "tmp",
            "type": "folder"
         }, {
            "date_added": "13252576791093368",
            "date_last_used": "0",
            "guid": "362f081b-d3e1-41d0-95a2-822fdc6d2d0a",
            "id": "147",
            "name": "Outlook",
            "type": "url",
            "url": "https://outlook.live.com/owa/"
         }, {
            "date_added": "13211446887514248",
            "date_last_used": "13339612946790542",
            "guid": "b3f2cda7-31a0-4117-9ca8-587658ea6cc5",
            "id": "149",
            "name": "Dropbox",
            "type": "url",
            "url": "https://www.dropbox.com/en_GB/login"
         } ],
         "date_added": "13314663694638863",
         "date_last_used": "0",
         "date_modified": "13340011838547002",
         "guid": "0bc5d13f-2cba-5d74-951f-3f233fe6c908",
         "id": "1",
         "name": "Lesezeichenleiste",
         "type": "folder"
      }


class TestShowMode(unittest.TestCase):
   def setUp(self) -> None:
      self.show_modes: ShowMode = ShowMode()

   def test_load_bookmark_file(self):
      with patch.object(show_mode, "BOOKMARKS", Path(ROOT, "test", "testdata", "231030_Bookmarks")):
         self.show_modes.load_bookmark_file()