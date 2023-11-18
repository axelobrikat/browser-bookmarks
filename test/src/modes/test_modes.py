import unittest
from pytest_mock import MockerFixture
from unittest.mock import MagicMock, patch
import pytest
from pathlib import Path

from src.etc.paths import ROOT
from src.modes.mode import Mode
from src.modes import mode
from src.etc.exceptions import Exc


def get_exp_bm_data_roots() -> dict[str, dict]:
   """returns expected data of BOOKMARKS file -> roots after json.load

   Returns:
       dict[str, dict]: expected data as dict
   """
   return {
      "roots": {
         "bookmark_bar": {
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
         },
         "other": {
            "children": [  ],
            "date_added": "13314663694638864",
            "date_last_used": "0",
            "date_modified": "13339612917749873",
            "guid": "82b081ec-3dd3-529c-8475-ab6c344590dd",
            "id": "2",
            "name": "Weitere Lesezeichen",
            "type": "folder"
         },
         "synced": {
            "children": [ {
               "date_added": "13251073445185664",
               "date_last_used": "0",
               "guid": "5577687b-3464-48b0-bbc9-a4160717be20",
               "id": "198",
               "name": "Teekanne Ländertee Collection Box, 1er Pack (1 x 383.25 g): Amazon.de: Grocery",
               "type": "url",
               "url": "https://www.amazon.de/Teekanne-L%C3%A4ndertee-Collection-Pack-383-25/dp/B074FZCBRC/ref=mp_s_a_1_3?dchild=1&keywords=teekanne+teebox&qid=1606569148&sprefix=teekanne+teebox&sr=8-3"
            }, {
               "date_added": "13287138712190645",
               "date_last_used": "0",
               "guid": "72191e4e-808f-4ee5-98aa-117f53a1070c",
               "id": "199",
               "name": "8 Lösungen zur Behebung „PC fährt hoch, Bildschirm schwarz/leer“",
               "type": "url",
               "url": "https://de.minitool.com/datenwiederherstellung/pc-faehrt-hoch-aber-kein-bild-geloest.html"
            }, {
               "date_added": "13287423186595292",
               "date_last_used": "0",
               "guid": "4dc8f9d0-660d-497f-a8c8-823865db11c0",
               "id": "200",
               "name": "Wildromantische Badestellen in Deutschland| MERIAN",
               "type": "url",
               "url": "https://www.merian.de/deutschland/sechs-wilde-badestellen-zum-alleinsein"
            } ],
            "date_added": "13314663694638866",
            "date_last_used": "0",
            "date_modified": "13287423186595292",
            "guid": "4cf2e351-0e85-532b-bb37-df045d8f8d0f",
            "id": "3",
            "name": "Mobile Lesezeichen",
            "type": "folder"
         }
      }
   }


class TestModeLoadFileSuccess(unittest.TestCase):
   """test mode.py with a patched BOOKMARKS file in ./test/testdata
   """
   @patch.multiple(Mode, __abstractmethods__=set())
   def setUp(self) -> None:
      self.mode: Mode = Mode()

   @pytest.fixture(autouse=True)
   def mock_bookmarks(self, mocker: MockerFixture):
      self.mocked_bookmarks: MagicMock = mocker.patch.object(
         mode,
         "BOOKMARKS",
         Path(ROOT, "test", "testdata", "231030_Bookmarks")
      )

   def test_load_bookmark_file_success(self):
      """check successful reading of BOOKMARKS file content
      - use BOOKMARKS file stored in ./test/testdata/
      """
      with self.mocked_bookmarks:
         self.mode.load_bookmark_file()

      # assert dict keys #
      assert list(self.mode.bm_data.keys()) == [
         "checksum",
         "roots",
         "sync_metadata",
         "version",
      ]

      # assert dict values #
      assert self.mode.bm_data[
         "checksum"] == "81a729c7af18b037e563bda45193eb13"
      assert self.mode.bm_data[
         "roots"] == get_exp_bm_data_roots()["roots"]
      assert self.mode.bm_data[
         "sync_metadata"].startswith("Cu8BCs")
      assert self.mode.bm_data[
         "version"] == 1



class TestModeLoadFileFail(unittest.TestCase):
   """test mode.py with a not existing BOOKMARKS file leading to an error
   - Note, this class, covering the fail state, could also be united with the ...
     ... class, covering the success state, using patch.multiple (?)
   """
   @patch.multiple(Mode, __abstractmethods__=set())
   def setUp(self) -> None:
      self.mode: Mode = Mode()

   @patch.object(Exc, "exit")
   def test_load_bookmark_file_load_fail(self, mock_exit: MagicMock):
      """check failed reading of BOOKMARKS file content
      - use not existing BOOKMARKS file

      Args:
          mock_exit (MagicMock): mocked exit function
      """
      with patch.object(
         mode,
         "BOOKMARKS",
         Path(ROOT, "test", "testdata", "not_existing_file")
      ):
         self.mode.load_bookmark_file()

      mock_exit.assert_called_once()
      assert str(mock_exit.call_args[0][0]).startswith(
         f"Cannot load bookmarks file "
      )

   @patch.object(Exc, "exit")
   def test_load_bookmark_file_typecheck_fail(self, mock_exit: MagicMock):
      """test exiting program when content of BOOKMARKS file is no json

      Args:
          mock_exit (MagicMock): mocked exit function
      """
      with patch.object(
         mode,
         "BOOKMARKS",
         Path(ROOT, "test", "testdata", "231030_Bookmarks")
      ):
         with patch.object(
            Mode,
            "check_bm_data_for_json",
            return_value=False
         ):
            self.mode.load_bookmark_file()
            mock_exit.assert_called_once_with(
                f"Data specified in BOOKMARKS file has not the correct format."
                f"Check that is has JSON format."
            )