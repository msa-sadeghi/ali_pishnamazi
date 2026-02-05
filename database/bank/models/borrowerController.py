from .borrowers import Borrowers
import logging

logger = logging.getLogger(__name__)


class BorrowerController:
    def __init__(self):
        self.model = Borrowers()

    def create_borrower(self, data):
        try:
            result = self.model.create(data)
            logger.info(f"borrower with id {result} created")
            return True
        except Exception as ex:
            logger.error(f"error when creating borrower with id")
            return False

    def get_all_borrowers(self):
        try:
            result = self.model.get_all()
            logger.info("all borrowers retrieved successfully")
            return result
        except Exception as ex:
            logger.error(f"an error {ex} occured when getting all borrowers")
            return []

    def search_borrowers(self, keyword):
        pass
