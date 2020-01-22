from index import WasRun 
from index import TestCase 
from index import TestResult
from index import TestSuite

class TestCaseTest(TestCase):
  # invoke setup first
  # invoke test
  # invoke teardown afterwards
  # log string in wasRun
  def testTemplateMethod(self):
    test = WasRun('testMethod')
    result = TestResult()
    test.run(result)
    assert("setUp testMethod tearDown " == test.log)
  
  # invoke teardown afterward even if the test fails
  # run multiple tests
  def testSuite(self):
    suite = TestSuite()
    suite.add(WasRun('testMethod'))
    suite.add(WasRun('testBrokenMethod'))
    result = TestResult()
    suite.run(result)
    assert('2 run, 1 failed' == result.summary())

  # report collected results
  def testResult(self):
    test = WasRun('testMethod')
    result = TestResult()
    test.run(result)
    assert("1 run, 0 failed" == result.summary())
  
  def testFailedResult(self):
    test = WasRun('testBrokenMethod')
    result = TestResult()
    test.run(result)
    assert("1 run, 1 failed" == result.summary())

  # report failed test 
  def testFailedResultFormatting(self):
    result = TestResult()
    result.testStarted()
    result.testFailed()
    assert("1 run, 1 failed" == result.summary())
    
  # catch and report setUp errors

suite = TestSuite()
suite.add(TestCaseTest('testTemplateMethod'))
suite.add(TestCaseTest('testResult'))
suite.add(TestCaseTest('testFailedResultFormatting'))
suite.add(TestCaseTest('testFailedResult'))
suite.add(TestCaseTest('testSuite'))
result = TestResult()
suite.run(result)
print(result.summary())
