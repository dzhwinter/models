import unittest

def ndcg(y_pred, y, k):
  """
  evaluate the ndcg metric, ndcg@10 means k = 10
  """
  

class NDCGTest(unittest.TestCase):
  def sample_test(self):
    y = [1,2,3,4,5,6]
    y_pred = [3,2,3,0,1,2]
    self.assertEqual(ndcg(y_pred, y, len(y)), 0.961)

if __name__ == '__main__':
  unittest.main()
