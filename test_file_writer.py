import unittest
import os
from file_writer import write_to_file

class TestFileWriter(unittest.TestCase):
    def test_write_to_file(self):
        test_filename = 'test_output.txt'
        test_text = 'Hello, GitHub Actions!'
        
        write_to_file(test_filename, test_text)
        
        self,assertTrue(os.path.exists(test_filename))
        
        with open(test_filename, 'r') as f:
            content = f.read()
            self.assertEqual(content, test_text)
            os.remove(test_filename)

if __name__ == '__main__':
    unittest.main()
    