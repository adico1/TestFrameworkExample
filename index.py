class TestCase:
  def __init__(self, name):
    self.name = name

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def run(self, result):
    result.testStarted()
    self.setUp()
    try:
      exec('self.' + self.name + '()')
    except:
      result.testFailed()
    self.tearDown()

class WasRun(TestCase):
  def __init__(self, name):
    TestCase.__init__(self, name)

  def setUp(self):
    self.log = 'setUp '

  def testMethod(self):
    self.log = self.log + 'testMethod '

  def tearDown(self):
    self.log = self.log + 'tearDown '

  def testBrokenMethod(self):
    raise Exception

class TestResult():
  def __init__(self):
    self.runCount = 0
    self.errorCount = 0

  def testFailed(self):
    self.errorCount = self.errorCount  + 1
  def testStarted(self):
    self.runCount = self.runCount + 1

  def summary(self):
    return "%d run, %d failed" %(self.runCount, self.errorCount)

class TestSuite():
  def __init__(self):
    self.tests = []
  def add(self, test):
    self.tests.append(test)
  def run(self, result):
    for test in self.tests:
      test.run(result)