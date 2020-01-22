from index import WasRun 
from index import TestCase 

class TestCaseTest(TestCase):
  # invoke setup first
  # invoke test
  # invoke teardown afterwards
  # log string in wasRun
  def testTemplateMethod(self):
    test = WasRun('testMethod')
    test.run()
    assert('setUp testMethod tearDown ' == test.log)
  
  # invoke teardown afterward even if the test fails
  # run multiple tests
  # report collected results
  def testResult(self):
      test = WasRun('testMethod')
      result = test.run()
      assert('1 run, 0 failed' == result.summary())


TestCaseTest('testTemplateMethod').run()
TestCaseTest('testResult').run()

