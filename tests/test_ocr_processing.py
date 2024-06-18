import unittest
from src.ocr_processing import correct_ocr_errors, process_text_to_df

class TestOCRProcessing(unittest.TestCase):
    def test_correct_ocr_errors(self):
        self.assertEqual(correct_ocr_errors("Q2-06-24"), "02-06-24")
    
    def test_process_text_to_df(self):
        sample_text = """01-06-24 14:21 Cash Withdrawal 10,000.00 1,159,653.48 ATM Tesco Lotus Lamai Ref Code ATMB83823
01-06-24 15:56 Transfer Withdrawal 3,000.00 1,156,653.48 K PLUS To SCB X4084 TONGCHAI SO++"""
        df = process_text_to_df(sample_text)
        self.assertEqual(len(df), 2)
        self.assertEqual(df['Date'].iloc[0], '01-06-24')
        self.assertEqual(df['Description'].iloc[0], 'Cash Withdrawal')

if __name__ == '__main__':
    unittest.main()
