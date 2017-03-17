import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'lib')))

import unittest
from dispatcher import Dispatcher

class TestDispatcher(unittest.TestCase):
  """Tests for Dispatcher"""

  def setUp(self):
    """Get data from file to test"""
    try:
      with open("test_inputs.txt") as f:
        self._inputs = f.readlines()
    except Exception:
      self._inputs = None


  def test_is_test_file_present(self):
    """Check if test file is present in folder"""
    self.assertNotEqual(self._inputs, None)


  def test_parse_input_dispatch(self):
    """Check initialization dispatcher with inputs / dispatchering / output"""
    d = None
    try:
      d = Dispatcher(self._inputs)
    except Exception:
      self.fail("Error in input data")

    try:
      d.dispatch()
    except Exception:
      self.fail("Error in dispatchering")

    expectedRes = ["1 3 N", "5 5 E"]
    res = d.getPositions()

    self.assertNotEqual(res, None)
    self.assertEqual(len(expectedRes), len(res))
    for r, er in zip(res, expectedRes):
      self.assertEqual(r, er)


if __name__ == '__main__':
    unittest.main()