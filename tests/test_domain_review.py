import unittest

from src.lumen_tool_render_flow.domain_review import DomainReview, review_lane, review_score


class DomainReviewTests(unittest.TestCase):
    def test_review_lane(self) -> None:
        item = DomainReview(72, 39, 8, 55)
        self.assertEqual(review_score(item), 214)
        self.assertEqual(review_lane(item), "ship")


if __name__ == "__main__":
    unittest.main()
