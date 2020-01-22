from index import WasRun 
from index import TestCase 
from index import TestResult

class TestCaseTest(TestCase):
  # invoke setup first
  # invoke test
  # invoke teardown afterwards
  # log string in wasRun
  def testTemplateMethod(self):
    test = WasRun('testMethod')
    test.run()
    assert 'setUp testMethod tearDown ' == test.log
  
  # invoke teardown afterward even if the test fails
  # run multiple tests
  # report collected results
  def testResult(self):
      test = WasRun('testMethod')
      result = test.run()
      assert '1 run, 0 failed' == result.summary()
  
  def testFailedResult(self):
    test = WasRun('testBrokenMethod')
    result = test.run()
    assert '1 run, 1 failed', result.summary

  # report failed test 
  def testFailedResultFormatting(self):
    result = TestResult()
    result.testStarted()
    result.testFailed()
    assert '1 run, 1 failed', result.summary
    
  # catch and report setUp errors
  
TestCaseTest('testTemplateMethod').run()
TestCaseTest('testResult').run()
TestCaseTest('testFailedResultFormatting').run()
TestCaseTest('testFailedResult').run()

