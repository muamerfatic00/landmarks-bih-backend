from src.app.repositories.landmark_repository import LandmarkRepository


class LandmarkService:
    def __init__(self, repository: LandmarkRepository):
        self.repository = repository
